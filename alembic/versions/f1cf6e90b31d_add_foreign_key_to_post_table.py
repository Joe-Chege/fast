"""add foreign_key to post table

Revision ID: f1cf6e90b31d
Revises: 1a5e3bc80406
Create Date: 2024-02-13 10:51:54.584759

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f1cf6e90b31d'
down_revision: Union[str, None] = '1a5e3bc80406'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
