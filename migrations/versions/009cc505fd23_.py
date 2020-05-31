"""empty message

Revision ID: 009cc505fd23
Revises: 
Create Date: 2020-05-31 12:12:24.773633

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '009cc505fd23'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.Column('nus_net_id', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_users_name'), 'users', ['name'], unique=False)
    op.create_index(op.f('ix_users_nus_net_id'), 'users', ['nus_net_id'], unique=True)
    op.create_table('user_mods',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('code', sa.String(length=8), nullable=True),
    sa.Column('mod_id', sa.String(length=64), nullable=True),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('class_grp', sa.JSON(), nullable=True),
    sa.Column('term', sa.String(length=6), nullable=True),
    sa.Column('student', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['student'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_user_mods_code'), 'user_mods', ['code'], unique=False)
    op.create_index(op.f('ix_user_mods_id'), 'user_mods', ['id'], unique=False)
    op.create_index(op.f('ix_user_mods_mod_id'), 'user_mods', ['mod_id'], unique=False)
    op.create_index(op.f('ix_user_mods_term'), 'user_mods', ['term'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_user_mods_term'), table_name='user_mods')
    op.drop_index(op.f('ix_user_mods_mod_id'), table_name='user_mods')
    op.drop_index(op.f('ix_user_mods_id'), table_name='user_mods')
    op.drop_index(op.f('ix_user_mods_code'), table_name='user_mods')
    op.drop_table('user_mods')
    op.drop_index(op.f('ix_users_nus_net_id'), table_name='users')
    op.drop_index(op.f('ix_users_name'), table_name='users')
    op.drop_table('users')
    # ### end Alembic commands ###
