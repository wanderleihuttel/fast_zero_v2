from dataclasses import asdict

import pytest
from sqlalchemy import select

from fastapi_zero.models import User


@pytest.mark.asyncio
async def test_create_user(session, mock_db_time):
    with mock_db_time(model=User) as time:
        new_user = User(
            username='alice', password='secret', email='teste@test'
        )
        session.add(new_user)
        await session.commit()
        user = await session.scalar(
            select(User).where(User.username == 'alice')
        )

    assert asdict(user) == {
        'id': 1,
        'username': 'alice',
        'email': 'teste@test',
        'password': 'secret',
        'created_at': time,
        'updated_at': time,
    }


# async def test_update_user(session, mock_db_time):
#     with mock_db_time(model=User) as time:
#         new_user = User(
#             username='alice', password='secret', email='teste@test'
#         )
#         session.add(new_user)
#         await session.commit()

#         new_user.password = 'newsecret'
#         new_user.updated_at = time

#         await session.commit()
#         await session.refresh(new_user)

#         user = await session.scalar(
#             select(User).where(User.username == 'alice')
#         )

#     assert asdict(user) == {
#         'id': 1,
#         'username': 'alice',
#         'email': 'teste@test',
#         'password': 'newsecret',
#         'created_at': time,
#         'updated_at': time,
#     }
