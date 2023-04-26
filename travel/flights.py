from datetime import datetime, timedelta, date
from typing import List

from papi_sdk import APIv3
from papi_sdk.models.order_booking_finish.b2b import B2BHotelOrderBookingFinishRequest, \
    B2BHotelOrderBookingFinishPartner
from papi_sdk.models.order_booking_finish.base import HotelOrderBookingFinishUser, HotelOrderBookingFinishRoom, \
    HotelOrderBookingFinishGuest, HotelOrderBookingFinishPaymentType
from papi_sdk.models.order_booking_form import OrderBookingFormRequest
from papi_sdk.models.search.base_request import GuestsGroup
from papi_sdk.models.search.hotelpage.b2b import B2BHotelPageResponse, B2BHotelPageRequest


# from .search_hotelpage import get_hotel_page
# from .booking_finish import make_booking_finish
# from .booking_form import make_booking_form


def make_booking_form(
        client,
        order_id,
        rate_hash,
        language,
        ip_address,
):
    return client.b2b_order_booking_form(
        OrderBookingFormRequest(
            partner_order_id=order_id,
            book_hash=rate_hash,
            language=language,
            user_ip=ip_address,
        )
    )


def make_booking_finish(
        client,
        email,
        phone,
        order_id,
        language,
        guest_first_name,
        guest_last_name,
        pt_type,
        pt_amount,
        pt_currency_code,
):
    user = HotelOrderBookingFinishUser(
        email=email,
        phone=phone,
    )
    rooms = [
        HotelOrderBookingFinishRoom(
            guests=[
                HotelOrderBookingFinishGuest(
                    first_name=guest_first_name,
                    last_name=guest_last_name,
                )
            ]
        )
    ]
    payment_type = HotelOrderBookingFinishPaymentType(
        type=pt_type,
        amount=pt_amount,
        currency_code=pt_currency_code,
    )
    return client.b2b_order_booking_finish(
        data=B2BHotelOrderBookingFinishRequest(
            user=user,
            partner=B2BHotelOrderBookingFinishPartner(partner_order_id=order_id),
            language=language,
            rooms=rooms,
            payment_type=payment_type,
        )
    )


def get_hotel_page(
        client,
        hotel_id,
        checkin,
        checkout,
        residency,
        language,
        adults,
        children):
    return client.b2b_search_hotel_page(
        data=B2BHotelPageRequest(
            id=hotel_id,
            checkin=checkin,
            checkout=checkout,
            residency=residency,
            language=language,
            guests=[GuestsGroup(adults=adults, children=children)],
        )
    )


if __name__ == "__main__":
    papi = APIv3(key="4930:43a33a2a-ca60-4d32-9394-03e7ed413572")
    hp = get_hotel_page(
        client=papi,
        hotel_id="test_hotel",
        checkin=datetime.now(),
        checkout=datetime.now() + timedelta(days=2),
        residency="ru",
        language="ru",
        adults=2,
        children=[],
    )
    if hp.error:
        raise (Exception(hp.error))
    print(f"we have caught {len([h for h in hp.data.hotels[0].rates])} booking hashes")
    print(hp.data.hotels[0].rates[0].book_hash)

    # Next, we are going to the booking form with a rate hash from the hotel page result
    order_id = "12"
    booking_form = make_booking_form(
        client=papi,
        order_id=order_id,
        rate_hash=hp.data.hotels[0].rates[0].book_hash,
        language="ru",
        ip_address="192.185.131.36",
    )
    if booking_form.error:
        raise (Exception(booking_form.error))
    print("we have gotten the booking form!")

    # When we have the booking form data, we can go to the booking finish endpoint with payment type data
    result = make_booking_finish(
        client=papi,
        email="mahkamkasimov94@gmail.com",
        phone="+998977165434",
        order_id=order_id,
        language="ru",
        guest_first_name="Test",
        guest_last_name="Test",
        pt_type=booking_form.data.payment_types[0].type,
        pt_amount=str(booking_form.data.payment_types[0].amount),
        pt_currency_code=booking_form.data.payment_types[0].currency_code,
    )
    if result.error:
        raise (Exception(result.error))
    if result.status == "ok":
        print("congratulates! the booking is done!")
