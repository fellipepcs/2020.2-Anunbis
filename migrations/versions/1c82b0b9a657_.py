"""empty message

Revision ID: 1c82b0b9a657
Revises: f4e4a306cdcd
Create Date: 2021-05-16 00:23:42.977664

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1c82b0b9a657'
down_revision = 'f4e4a306cdcd'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('professor', sa.Column('email_verified', sa.Boolean(), nullable=False))
    op.add_column('student', sa.Column('email_verified', sa.Boolean(), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('student', 'email_verified')
    op.drop_column('professor', 'email_verified')
    # ### end Alembic commands ###
