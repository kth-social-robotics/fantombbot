"""empty message

Revision ID: 09cdb6c0041b
Revises: 74ff7335b807
Create Date: 2018-05-29 15:27:34.226616

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '09cdb6c0041b'
down_revision = '74ff7335b807'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('conversation', sa.Column('processed', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('conversation', 'processed')
    # ### end Alembic commands ###
