"""empty message

Revision ID: d8802c8bb913
Revises: 85fb7494e552
Create Date: 2018-07-31 04:16:41.181448

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd8802c8bb913'
down_revision = '85fb7494e552'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('rating_utterance_row', sa.Column('turn_error', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('rating_utterance_row', 'turn_error')
    # ### end Alembic commands ###
