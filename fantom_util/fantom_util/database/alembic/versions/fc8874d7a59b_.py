"""empty message

Revision ID: fc8874d7a59b
Revises: aa5cd0308e05
Create Date: 2018-06-19 23:34:43.441423

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fc8874d7a59b'
down_revision = 'aa5cd0308e05'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('incoherent_node_utterance_worker_job',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('NOW()'), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('worker_id', sa.Integer(), nullable=True),
    sa.Column('job_id', sa.Integer(), nullable=True),
    sa.Column('node_utterance_id', sa.Integer(), nullable=True),
    sa.Column('assignment_id', sa.String(), nullable=True),
    sa.Column('hit_id', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['job_id'], ['job.id'], ),
    sa.ForeignKeyConstraint(['node_utterance_id'], ['node_utterance.id'], ),
    sa.ForeignKeyConstraint(['worker_id'], ['worker.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('incoherent_node_utterance_worker_job')
    # ### end Alembic commands ###
