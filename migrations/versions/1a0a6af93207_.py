"""empty message

Revision ID: 1a0a6af93207
Revises: 01b0f59e868a
Create Date: 2024-05-14 09:48:44.517766

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1a0a6af93207'
down_revision = '01b0f59e868a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('asignar', schema=None) as batch_op:
        batch_op.add_column(sa.Column('usuario_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key(None, 'usuario', ['usuario_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('asignar', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('usuario_id')

    # ### end Alembic commands ###
