# __  __    ___    _______
#/  `/  \|\ || /\ /  `|/__`
#\__,\__/| \||/~~\\__,|.__/
#
"""
Contact Cards
~~~~~~~~~~~~~~~~~~~~~
Contacts let's you create Contact Cards in Python that just work, so you can worry about having meaningful conversations
with people who know who you are.

Here's how it works:
   >>> from contacts import ContactCard
   >>> card = ContactCard()
   >>> card.name = 'David Heimann'
   >>> card.first_name = 'David'
   >>> card.last_name = 'Heimann'
   >>> card.photo = image_file
   >>> card.phone_number = '+1XXXXXXX'
   >>> card.twitter = '@david_heimann'
   >>> card.build()
   Card built.
   >>> print(card)
   Contact Card (vobject)
   Name: David Heimann
   First Name: David
   Last Name: Heimann
   Phone Number: +1XXXXXXXX
   Photo: JPEG (2 MB)
   Twitter: @david_heimann

   Card built at: <timestamp>
:copyright: (c) 2017 by David Heimann.
:license: MIT, see LICENSE for more details.
"""