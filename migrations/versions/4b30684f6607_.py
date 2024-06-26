"""empty message

Revision ID: 4b30684f6607
Revises: 1e41fc7990c9
Create Date: 2024-05-03 15:25:21.226661

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4b30684f6607'
down_revision = '1e41fc7990c9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('empleado',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombre', sa.String(length=250), nullable=True),
    sa.Column('apellido', sa.String(length=250), nullable=True),
    sa.Column('ci', sa.String(length=250), nullable=True),
    sa.Column('cargo', sa.String(length=250), nullable=True),
    sa.Column('departamento', sa.String(length=250), nullable=True),
    sa.Column('solicitud', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('empleado')
    # ### end Alembic commands ###
