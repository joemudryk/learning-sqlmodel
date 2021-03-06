"""Add hero power to hero model

Revision ID: a1723e69971e
Revises: 1c2b4baaf73e
Create Date: 2021-09-10 12:28:11.172461

"""
from alembic import op
import sqlalchemy as sa
import sqlmodel


# revision identifiers, used by Alembic.
revision = 'a1723e69971e'
down_revision = '1c2b4baaf73e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('hero', sa.Column('power', sa.Integer(), nullable=True))
    op.create_index(op.f('ix_hero_power'), 'hero', ['power'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_hero_power'), table_name='hero')
    op.drop_column('hero', 'power')
    # ### end Alembic commands ###
