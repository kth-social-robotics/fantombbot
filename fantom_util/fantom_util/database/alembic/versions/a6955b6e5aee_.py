"""empty message

Revision ID: a6955b6e5aee
Revises: b824c68fa114
Create Date: 2018-08-07 11:51:12.041308

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a6955b6e5aee'
down_revision = 'b824c68fa114'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('linked_nodes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('NOW()'), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('linked_to_node_id', sa.Integer(), nullable=True),
    sa.Column('linked_from_node_id', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_linked_nodes_linked_from_node_id'), 'linked_nodes', ['linked_from_node_id'], unique=False)
    op.create_index(op.f('ix_linked_nodes_linked_to_node_id'), 'linked_nodes', ['linked_to_node_id'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_linked_nodes_linked_to_node_id'), table_name='linked_nodes')
    op.drop_index(op.f('ix_linked_nodes_linked_from_node_id'), table_name='linked_nodes')
    op.drop_table('linked_nodes')
    # ### end Alembic commands ###
