# Contacts
Contacts lets humans create contact cards, so that they can talk to other humans without being confused. 

![Phone Gif](https://media.giphy.com/media/yPhqlJccIOaru/giphy.gif)

So, someone needs your digits? No problem, couldn't be easier. Observe:

```python
from contacts import ContactCard

card = ContactCard(
    first_name='David',
    last_name='Heimann',
    phone_number='+1XXXXXXX',
    email='email@address.com',
    twitter='@david_heimann',
    website='https://about.me/dheimann'
)

# Build the card to generate a file that can be saved locally or to a server of your choosing.
card.build()
```