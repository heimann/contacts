"""
contacts.api
~~~~~~~~~~~~
This module implements the Contacts 📕 API.
:copyright: (c) 2017 by David Heimann.
:license: MIT, see LICENSE for more details.
"""

import vobject

from .exceptions import (
    ContactCardException,
)

from .fields.phone_number import convert_to_e164
from .rules import ALLOWED_FIELDS


class ContactCard(object):
    """A :class: `Contact Card <ContactCard>` object that describes a person or entity for use with Phones.

    Attributes:
        card: The built contact card.
    """

    _modifiable_fields = ALLOWED_FIELDS + ['_card', '_card_field']
    card = None

    def __init__(self, **kwargs):
        """Initializes a ContactCard.

        (See ALLOWED_FIELDS)
        :param name: Full Name (required).
        :param phone_number: Phone Number (required).
        :param first_name: First Name.
        :param last_name: Last Name.
        :param photo: fileobject of photo.
        :param email: E-Mail address.
        :param website: URL.
        :param twitter: Twitter Username (ex: @david_heimann)
        """
        self._card = vobject.vCard()

        self.__dict__.update((key, False) for key in self._modifiable_fields)
        self.__dict__.update((key, value) for key, value in kwargs.items() if key in self._modifiable_fields)

    def __repr__(self):
        return f"ContactCard(name={self.name}, phone_number={self.phone_number})"

    def __setattr__(self, attribute, value):
        if not attribute in set(self._modifiable_fields):
            print("{0} is not a valid attribute of a Contact Card.\nValid attributes are: {1}".format(
                attribute,
                ALLOWED_FIELDS
            ))
        else:
            self.__dict__[attribute] = value

    def _clean_fields(self):
        for field in ALLOWED_FIELDS:
            getattr(self, f"_clean_{field}")()

    def _clean_phone_number(self):
        if not self.phone_number:
            raise ContactCardException(
                "A Contact Card must have a :phone_number: to pass validation."
            )

        print("Cleaning phone number")
        self.phone_number = convert_to_e164(self.phone_number)

    def _clean_name(self):
        pass

    def _clean_email(self):
        pass

    def _clean_first_name(self):
        pass

    def _clean_last_name(self):
        pass

    def _clean_photo(self):
        pass

    def _clean_twitter(self):
        pass

    def _clean_website(self):
        pass

    def build(self):
        """
        Builds a ContactCard (.vcf) file and returns it given the instances parameters.

        :return: Card (file - .vcf).
        """
        # Clean all fields.
        self._clean_fields()

        # Build