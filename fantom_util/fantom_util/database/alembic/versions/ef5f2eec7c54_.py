"""empty message

Revision ID: ef5f2eec7c54
Revises: d61ac139ee25
Create Date: 2018-06-16 00:24:53.475365

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = 'ef5f2eec7c54'
down_revision = 'd61ac139ee25'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('conversation_node_utterance_id_fkey', 'conversation', type_='foreignkey')
    op.drop_column('conversation', 'node_utterance_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('conversation', sa.Column('node_utterance_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.create_foreign_key('conversation_node_utterance_id_fkey', 'conversation', 'node_utterance',
                          ['node_utterance_id'], ['id'])
    # ### end Alembic commands ###
