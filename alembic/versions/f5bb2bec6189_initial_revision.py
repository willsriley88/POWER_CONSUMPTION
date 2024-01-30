"""initial revision

Revision ID: f5bb2bec6189
Revises: 
Create Date: 2024-01-30 11:17:06.754868

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '748d658f2a19'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table("VOLTAGE", sa.Column("DEVICE", sa.String(), nullable=False))
    op.add_column("VOLTAGE", sa.Column("VALUE", sa.Float(), nullable=False))
    op.add_column("VOLTAGE", sa.Column("ID", sa.Integer(), nullable=False, autoincrement=True, primary_key=True))
    op.add_column("VOLTAGE", sa.Column("TIME_STAMP", sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text("now()")))


def downgrade() -> None:
    op.drop_table("VOLTAGE")
