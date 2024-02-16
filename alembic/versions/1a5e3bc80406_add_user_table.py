"""add user table

Revision ID: 1a5e3bc80406
Revises: 027a4b88ba63
Create Date: 2024-02-13 10:37:44.917968

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1a5e3bc80406'
down_revision: Union[str, None] = '027a4b88ba63'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.create_table(
        "user",
        sa.Column("id", sa.Integer),
        sa.Column("username", sa.String, nullable=False),
        sa.Column("email", sa.String, nullable=False),
        sa.Column("password", sa.String, nullable=False),
        sa.Column("created_at", sa.TIMESTAMP(timezone=True), 
                  nullable=False, server_default=sa.text("NOW()")),
        sa.Column("is_active", sa.Boolean),
 
        sa.UniqueConstraint("email"),
        sa.PrimaryKeyConstraint("id")
    )
    pass


def downgrade():
    op.drop_table("user")
    pass
