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

from .rules import ALLOWED_FIELDS

class ContactCard(object):
    """A :class: `Contact Card <ContactCard>` object that describes a person or entity for use with Phones.

    Attributes:
        card: The built contact card.
    """

    _allowed_fields = ALLOWED_FIELDS + ['_card', '_card_field']
    card = None

    def __init__(
            self,
            name,
            phone_number,
            first_name=False,
            last_name=False,
            photo=False,
            email=False,
            website=False,
            twitter=False
        ):
        """Initializes a ContactCard.

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

        # all those keys will be initialized as class attributes
        allowed_keys = set(ALLOWED_FIELDS)
        # initialize all allowed keys to false
        self.__dict__.update((key, False) for key in allowed_keys)
        # and update the given keys by their given values
        self.__dict__.update((key, value) for key, value in kwargs.items() if key in allowed_keys)


    def __setattr__(self, attribute, value):
        if not attribute in set(self._allowed_fields):
            print("{0} is not a valid attribute of a Contact Card.\nValid attributes are: {1}".format(
                attribute,
                ALLOWED_FIELDS
            ))
        else:
            self.__dict__[attribute] = value
