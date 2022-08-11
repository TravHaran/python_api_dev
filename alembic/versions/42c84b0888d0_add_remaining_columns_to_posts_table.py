"""add remaining columns to posts table

Revision ID: 42c84b0888d0
Revises: 4c8458eb2b92
Create Date: 2022-08-11 16:24:00.152067

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '42c84b0888d0'
down_revision = '4c8458eb2b92'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('published', sa.Boolean(), nullable=False, server_default='TRUE'))
    op.add_column('posts', sa.Column('created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('now()')))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'created_at')
    pass
