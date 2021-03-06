"""Added User Model

Revision ID: 093a8809c8a2
Revises: dedf2d8f47d7
Create Date: 2021-11-23 22:07:05.892676

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '093a8809c8a2'
down_revision = 'dedf2d8f47d7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(), nullable=True),
    sa.Column('last_name', sa.String(), nullable=True),
    sa.Column('email', sa.String(), nullable=True),
    sa.Column('password', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    # ### end Alembic commands ###
