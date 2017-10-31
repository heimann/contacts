import phonenumbers

from ..exceptions import ContactCardException

def convert_to_e164(raw_phone):
    """
    Converts a raw input to a phone number, verified based on the e164 standard.

    For e164 see: <https://www.itu.int/rec/dologin_pub.asp?lang=e&id=T-REC-E.164-201011-I!!PDF-E&type=items>
    From: <http://twilio-python.readthedocs.io/en/latest/faq.html>

    :param raw_phone: (str) Phone Number.
    :return: Verified, formatted e164 number.
    """
    try:
        if not raw_phone:
            return

        # TODO: Handle international phone numbers.
        if raw_phone[0] == '+':
            # Phone number may already be in E.164 format.
            parse_type = None
        else:
            # If no country code information present, assume it's a US number
            parse_type = "US"

        phone_representation = phonenumbers.parse(raw_phone, parse_type)
        return phonenumbers.format_number(phone_representation,
            phonenumbers.PhoneNumberFormat.E164)
    except phonenumbers.NumberParseException:
        raise ContactCardException(
            "The phone number supplied doesn't look like a valid phone number."
        )
    except Exception as e:
        raise ContactCardException(
            "Exception when converting phone number to e164."
        )

