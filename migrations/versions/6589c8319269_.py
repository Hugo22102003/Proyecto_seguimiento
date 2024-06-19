"""empty message

Revision ID: 6589c8319269
Revises: 8cbf60668260
Create Date: 2024-05-10 12:03:58.513677

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6589c8319269'
down_revision = '8cbf60668260'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('asignar', schema=None) as batch_op:
        batch_op.add_column(sa.Column('solicitud_id', sa.Integer(), nullable=True))
        batch_op.drop_constraint('asignar_empleado_id_fkey', type_='foreignkey')
        batch_op.create_foreign_key(None, 'solicitud', ['solicitud_id'], ['id'])
        batch_op.create_foreign_key(None, 'empleado', ['empleado_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('asignar', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.create_foreign_key('asignar_empleado_id_fkey', 'solicitud', ['empleado_id'], ['id'])
        batch_op.drop_column('solicitud_id')

    # ### end Alembic commands ###