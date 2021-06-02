"""empty message

Revision ID: 193c272745bc
Revises: 3cc1db160bae
Create Date: 2021-06-02 14:42:39.111271

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '193c272745bc'
down_revision = '3cc1db160bae'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('trip', sa.Column('gender', sa.String(), nullable=True))
    op.add_column('trip', sa.Column('birthday', sa.DateTime(), nullable=True))
    op.create_index(op.f('ix_trip_birthday'), 'trip', ['birthday'], unique=False)
    op.create_index(op.f('ix_trip_gender'), 'trip', ['gender'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_trip_gender'), table_name='trip')
    op.drop_index(op.f('ix_trip_birthday'), table_name='trip')
    op.drop_column('trip', 'birthday')
    op.drop_column('trip', 'gender')
    # ### end Alembic commands ###
