"""empty message

Revision ID: 74ff7335b807
Revises: e2f994d7d500
Create Date: 2018-05-17 08:59:45.031626

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '74ff7335b807'
down_revision = 'e2f994d7d500'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('conversation',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('NOW()'), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('session_id', sa.String(), nullable=True),
    sa.Column('user_utterance', sa.String(), nullable=True),
    sa.Column('system_utterance', sa.String(), nullable=True),
    sa.Column('topic', sa.String(), nullable=True),
    sa.Column('candidates', sa.String(), nullable=True),
    sa.Column('interaction_timestamp', sa.DateTime(), nullable=True),
    sa.Column('intent', sa.String(), nullable=True),
    sa.Column('sentiment', sa.String(), nullable=True),
    sa.Column('user_id', sa.String(), nullable=True),
    sa.Column('graphsearch_score', sa.Float(), nullable=True),
    sa.Column('history', sa.String(), nullable=True),
    sa.Column('asr_json', sa.String(), nullable=True),
    sa.Column('asr_score', sa.Float(), nullable=True),
    sa.Column('conversation_id', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('conversation')
    # ### end Alembic commands ###
