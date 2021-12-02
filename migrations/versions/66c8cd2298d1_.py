"""empty message

Revision ID: 66c8cd2298d1
Revises: 73be758b4bf7
Create Date: 2021-12-01 23:27:43.040449

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '66c8cd2298d1'
down_revision = '73be758b4bf7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('cart', sa.Column('product_key', sa.String(), nullable=True))
    op.drop_column('cart', 'product_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('cart', sa.Column('product_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_column('cart', 'product_key')
    # ### end Alembic commands ###
