"""empty message

Revision ID: 9c6d26e4d549
Revises: 6589c8319269
Create Date: 2024-05-10 15:47:34.929368

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9c6d26e4d549'
down_revision = '6589c8319269'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('solicitud', schema=None) as batch_op:
        batch_op.add_column(sa.Column('responsable', sa.String(length=50), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('solicitud', schema=None) as batch_op:
        batch_op.drop_column('responsable')

    # ### end Alembic commands ###