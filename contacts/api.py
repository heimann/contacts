"""
contacts.api
~~~~~~~~~~~~
This module implements the Contacts 📕 API.
:copyright: (c) 2017 by David Heimann.
:license: MIT, see LICENSE for more details.
"""

import vobject


class ContactCard(object):
    """
    A :class:`Contact Card <ContactCard>` object.

    :param name: Full Name (required).
    :param first_name: First Name.
    :param last_name: Last Name.
    :param photo: fileobject of photo.
    :param email: E-Mail address.
    :param website: URL.
    :param twitter: Twitter Username (ex: @david_heimann)
    """

    _card = None

    def __init__(self):
        self._card = vobject.vCard()
