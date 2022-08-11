"""add content column to posts table

Revision ID: 47a71f60d943
Revises: ace0f33a3ec3
Create Date: 2022-08-11 13:41:31.828729

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '47a71f60d943'
down_revision = 'ace0f33a3ec3'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
