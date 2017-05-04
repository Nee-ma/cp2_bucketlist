"""empty message

Revision ID: 483cf5c95dfa
Revises: 5fb08479b7e4
Create Date: 2017-05-04 11:55:16.582801

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '483cf5c95dfa'
down_revision = '5fb08479b7e4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('bucketitem', 'done',
               existing_type=sa.BOOLEAN(),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('bucketitem', 'done',
               existing_type=sa.BOOLEAN(),
               nullable=True)
    # ### end Alembic commands ###
