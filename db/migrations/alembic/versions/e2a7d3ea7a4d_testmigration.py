"""testmigration

Revision ID: e2a7d3ea7a4d
Revises: 52d449a57517
Create Date: 2025-04-01 12:02:26.938746

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e2a7d3ea7a4d'
down_revision: Union[str, None] = '52d449a57517'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
