"""add hotels

Revision ID: 8e737f17ce66
Revises: 0ae618b1495e
Create Date: 2023-09-16 01:39:13.748840

"""
from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

from hotels.models import Hotels
from rooms.models import Rooms

# revision identifiers, used by Alembic.
revision: str = '8e737f17ce66'
down_revision: Union[str, None] = '0ae618b1495e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

hotels = Hotels.__table__
rooms = Rooms.__table__


def upgrade() -> None:
    op.bulk_insert(
        hotels,
        [
            {
                "id": 1,
                "name": "Frederic Koklen Boutique Hotel",
                "location": "Odesa",
                "services": ["TV", "Wifi", "Parking"],
                "rooms_quantity": 3,
                "image_id": 1
            },
            {
                "id": 2,
                "name": "Ribas Rooms Odesa",
                "location": "Odesa",
                "services": ["Wifi", "Parking", "Internet"],
                "rooms_quantity": 1,
                "image_id": 2
            },
            {
                "id": 3,
                "name": "GRAND OTRADA Hotel Resort & SPA",
                "location": "Odesa",
                "services": ["Wifi", "Parking", "Internet", "Restaurant"],
                "rooms_quantity": 3,
                "image_id": 3
            },
            {
                "id": 4,
                "name": "Design-hotel Rooms and Rumors",
                "location": "Odesa",
                "services": ["Wifi", "Parking", "Internet"],
                "rooms_quantity": 3,
                "image_id": 4
            },
            {
                "id": 5,
                "name": "Hotel Sorrento",
                "location": "Odesa",
                "services": ["Wifi", "Internet", "Restaurant"],
                "rooms_quantity": 1,
                "image_id": 5
            },
            {
                "id": 6,
                "name": "Sunday Rooms",
                "location": "Odesa",
                "services": ["Wifi", "Internet"],
                "rooms_quantity": 2,
                "image_id": 6
            }
        ],
    )

    op.bulk_insert(
        rooms,
        [
            {
                "id": 1,
                "hotel_id": 1,
                "name": "Standard Twin Room",
                "description": "Spacious, elegant suite decorated in English style with bedroom, living room and relaxation room with armchairs and a sofa. Features a balcony, antique artwork and bathroom with a spa bath and sauna. This spacious suite overlooks a quiet street of the historic center and features wooden panels on walls",
                "price": 3122,
                "services": ["Wifi", "Telephone"],
                "quantity": 5,
                "image_id": 11
            },
            {
                "id": 2,
                "hotel_id": 1,
                "name": "Standard Double Room",
                "description": "This room features a wooden furniture, coffee and tea making facilities and a selection of pillows",
                "price": 3122,
                "services": ["Wifi", "Telephone", "Air conditioning"],
                "quantity": 5,
                "image_id": 12
            },
            {
                "id": 3,
                "hotel_id": 1,
                "name": "Junior Suite with Fireplace",
                "description": "This bright junior suite is decorated in Spanish style. It features a seating area with armchairs and a sofa. The bathroom is private, equipped with a spa bath, a tropical shower and toiletries",
                "price": 4289,
                "services": ["Wifi", "Telephone", "Air conditioning", "Spa tub"],
                "quantity": 4,
                "image_id": 13
            },
            {
                "id": 4,
                "hotel_id": 2,
                "name": "Deluxe Double Room",
                "description": "The air-conditioned double room offers a flat-screen TV with cable channels, a private entrance, a wardrobe, a safe deposit box as well as city views. The unit offers 1 bed",
                "price": 1100,
                "services": ["Wifi", "Air conditioning", "Flat-screen TV"],
                "quantity": 10,
                "image_id": None
            },
            {
                "id": 5,
                "hotel_id": 3,
                "name": "Standard Double Room",
                "description": "This double room's standout feature is the private pool. The spacious air-conditioned double room offers a flat-screen TV with satellite channels, a private entrance, soundproof walls, a mini-bar as well as city views",
                "price": 3075,
                "services": ["Wifi", "Air conditioning", "Flat-screen TV", "Private pool"],
                "quantity": 6,
                "image_id": 31
            },
            {
                "id": 6,
                "hotel_id": 3,
                "name": "Twin Room - Disability Access",
                "description": "Providing free toiletries and bathrobes, this twin room includes a private bathroom with a walk-in shower, a hairdryer and slippers. The spacious air-conditioned twin room provides a flat-screen TV with satellite channels, a private entrance, soundproof walls, a mini-bar as well as city views. The unit offers 2 beds",
                "price": 3113,
                "services": ["Wifi", "Air conditioning", "Private Bathroom", "Soundproof"],
                "quantity": 10,
                "image_id": 32
            },
            {
                "id": 7,
                "hotel_id": 3,
                "name": "Superior Double Room",
                "description": "This double room's special feature is the private pool. Providing free toiletries and bathrobes, this double room includes a private bathroom with a bath, a hairdryer and slippers. The spacious air-conditioned double room provides a flat-screen TV with satellite channels, a private entrance, soundproof walls, a mini-bar as well as city views. The unit offers 1 bed",
                "price": 3810,
                "services": ["Wifi", "Air conditioning", "Private Bathroom", "Soundproof", "Private pool", "Balcony"],
                "quantity": 5,
                "image_id": 33
            },
            {
                "id": 8,
                "hotel_id": 4,
                "name": "Standard King Room without Window - Elvis Presley room",
                "description": "This air-conditioned and soundproofed room offers a private bathroom fitted with a shower cabin. Bathrobes are provided. A flat-screen TV and record player are featured",
                "price": 1100,
                "services": ["Wifi", "Air conditioning", "Private Bathroom"],
                "quantity": 6,
                "image_id": 41
            },
            {
                "id": 9,
                "hotel_id": 4,
                "name": "Standard Double or Twin Room without Window - Jim Morrison room",
                "description": "Providing free toiletries and bathrobes, this twin/double room includes a private bathroom with a walk-in shower, a hairdryer and slippers. This twin/double room is air-conditioned and features a flat-screen TV with cable channels, a wardrobe, a safe deposit box and heating",
                "price": 1100,
                "services": ["Wifi", "Air conditioning", "Private Bathroom"],
                "quantity": 6,
                "image_id": 42
            },
            {
                "id": 10,
                "hotel_id": 4,
                "name": "Superior King Room - John Lennon room",
                "description": "This air-conditioned room has a private bathroom fitted with a shower cabin. Bathrobes are provided. A flat-screen TV and record player are featured",
                "price": 1300,
                "services": ["Wifi", "Air conditioning", "Private Bathroom"],
                "quantity": 3,
                "image_id": 43
            },
            {
                "id": 11,
                "hotel_id": 5,
                "name": "Apartment",
                "description": "This apartment features a flat-screen TV with cable channels, a mini-bar, a fridge and a safety deposit box. There is also a wardrobe, a chair and air-conditioning. There is a kitchen equipped with a stove and a microwave",
                "price": 1100,
                "services": ["Wifi", "Air conditioning", "Attached bathroom", "Private kitchenette", "Minibar"],
                "quantity": 23,
                "image_id": 51
            },
            {
                "id": 12,
                "hotel_id": 6,
                "name": "Standard Double Room",
                "description": "This air-conditioned double room includes a flat-screen TV with cable channels and a private bathroom. The unit offers 1 bed",
                "price": 1300,
                "services": ["Wifi", "Air conditioning", "Attached bathroom", "Flat-screen TV"],
                "quantity": 10,
                "image_id": 61
            },
            {
                "id": 13,
                "hotel_id": 6,
                "name": "Standard Twin Room",
                "description": "This air-conditioned twin room is consisted of of a flat-screen TV with cable channels and a private bathroom. The unit has 2 beds",
                "price": 1300,
                "services": ["Wifi", "Air conditioning", "Attached bathroom", "Flat-screen TV"],
                "quantity": 15,
                "image_id": 62
            },
        ],
    )


def downgrade() -> None:
    op.execute(
        rooms.delete().where(
            sa.and_(rooms.c.id <= 13)
        )
    )

    op.execute(
        hotels.delete().where(
            sa.and_(hotels.c.id <= 6)
        )
    )
