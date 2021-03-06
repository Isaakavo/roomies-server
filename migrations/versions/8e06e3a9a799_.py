"""empty message

Revision ID: 8e06e3a9a799
Revises: 
Create Date: 2022-01-07 10:17:40.123420

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8e06e3a9a799'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('tasks', sa.Column('is_completed', sa.Boolean(), nullable=False, server_default='false'))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('tasks', 'is_completed')
    # ### end Alembic commands ###
