"""Creating a post table

Revision ID: b42dd2eeeb99
Revises: 
Create Date: 2024-02-13 09:19:24.543959

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b42dd2eeeb99'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.create_table(
        "post",
        sa.Column("id", sa.Integer, primary_key=True, index=True),
        sa.Column("title", sa.String),
        sa.Column("content", sa.String),
        sa.Column("published", sa.Boolean),
    )
    pass


def downgrade():
    op.drop_table("post")
    pass
