"""empty message

Revision ID: 01b0f59e868a
Revises: c2be68429dba
Create Date: 2024-05-14 09:44:18.529748

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '01b0f59e868a'
down_revision = 'c2be68429dba'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('asignar', schema=None) as batch_op:
        batch_op.add_column(sa.Column('estado', sa.String(length=50), nullable=True))

    with op.batch_alter_table('usuario', schema=None) as batch_op:
        batch_op.add_column(sa.Column('departamento_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key(None, 'departamento', ['departamento_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('usuario', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('departamento_id')

    with op.batch_alter_table('asignar', schema=None) as batch_op:
        batch_op.drop_column('estado')

    # ### end Alembic commands ###