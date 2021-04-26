"""empty message

Revision ID: ba6766e8c50f
Revises: 
Create Date: 2021-04-26 13:56:47.749048

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ba6766e8c50f'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('actor_rel')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('actor_rel',
    sa.Column('movie_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('actor_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['actor_id'], ['actors.id'], name='actor_rel_actor_id_fkey'),
    sa.ForeignKeyConstraint(['movie_id'], ['movies.id'], name='actor_rel_movie_id_fkey'),
    sa.PrimaryKeyConstraint('movie_id', 'actor_id', name='actor_rel_pkey')
    )
    # ### end Alembic commands ###
