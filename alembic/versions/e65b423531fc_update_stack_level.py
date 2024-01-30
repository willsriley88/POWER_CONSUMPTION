"""update stack level

Revision ID: e65b423531fc
Revises: f5bb2bec6189
Create Date: 2024-01-30 11:40:19.469843

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e65b423531fc'
down_revision: Union[str, None] = 'f5bb2bec6189'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("VOLTAGE", sa.Column("STACK", sa.Integer(), nullable=False))


def downgrade() -> None:
    op.drop_column("VOLTAGE", "STACK")
