"""empty message

Revision ID: 7107a7f39d39
Revises: 41901edd6a9e
Create Date: 2018-06-20 20:34:46.596560

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7107a7f39d39'
down_revision = '41901edd6a9e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('conversation', sa.Column('graphsearch_matched_node', sa.Integer(), nullable=True))
    op.add_column('conversation', sa.Column('graphsearch_matched_utt', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('conversation', 'graphsearch_matched_utt')
    op.drop_column('conversation', 'graphsearch_matched_node')
    # ### end Alembic commands ###
