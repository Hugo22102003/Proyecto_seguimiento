"""empty message

Revision ID: d25c054928eb
Revises: 67286c184d5a
Create Date: 2024-06-28 11:48:33.041082

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd25c054928eb'
down_revision = '67286c184d5a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('asginar_departamento', schema=None) as batch_op:
        batch_op.create_unique_constraint(None, ['id'])

    with op.batch_alter_table('asignar', schema=None) as batch_op:
        batch_op.create_unique_constraint(None, ['id'])

    with op.batch_alter_table('departamento', schema=None) as batch_op:
        batch_op.create_unique_constraint(None, ['id'])

    with op.batch_alter_table('usuario', schema=None) as batch_op:
        batch_op.add_column(sa.Column('rango', sa.String(length=50), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('usuario', schema=None) as batch_op:
        batch_op.drop_column('rango')

    with op.batch_alter_table('departamento', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='unique')

    with op.batch_alter_table('asignar', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='unique')

    with op.batch_alter_table('asginar_departamento', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='unique')

    # ### end Alembic commands ###