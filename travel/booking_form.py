from papi_sdk import APIv3
from papi_sdk.models.order_booking_form import (
    B2BHotelOrderBookingFormResponse,
    OrderBookingFormRequest,
)


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


if __name__ == "__main__":
    papi = APIv3(key="your_key")
    result = make_booking_form(
        client=papi,
        order_id="your_order_id",
        rate_hash="rate_hash_from_hotel_page",
        language="ru",
        ip_address="your_ip_address",
    )
    print(
        "we need payment type data from 'result.data.payment_types' for creating a new booking in booking finish"
    )
