"""add feeds colum to post table

Revision ID: 027a4b88ba63
Revises: b42dd2eeeb99
Create Date: 2024-02-13 10:09:01.002800

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '027a4b88ba63'
down_revision: Union[str, None] = 'b42dd2eeeb99'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.add_column("post", sa.Column("feeds", sa.String))

    pass


def downgrade():
    op.drop_column("post", "feeds")
    pass
