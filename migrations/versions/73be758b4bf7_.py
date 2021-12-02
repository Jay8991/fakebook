"""empty message

Revision ID: 73be758b4bf7
Revises: dbb6e4309158
Create Date: 2021-12-01 23:25:41.649536

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '73be758b4bf7'
down_revision = 'dbb6e4309158'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('cart_product_id_fkey', 'cart', type_='foreignkey')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_foreign_key('cart_product_id_fkey', 'cart', 'product', ['product_id'], ['id'])
    # ### end Alembic commands ###
