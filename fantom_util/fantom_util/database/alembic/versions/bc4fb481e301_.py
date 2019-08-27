"""empty message

Revision ID: bc4fb481e301
Revises: 44fb705503d8
Create Date: 2018-08-08 13:18:17.744012

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bc4fb481e301'
down_revision = '44fb705503d8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('utterance', sa.Column('has_more_than_20_qualifaction', sa.Boolean(), server_default=sa.text('false'), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('utterance', 'has_more_than_20_qualifaction')
    # ### end Alembic commands ###
