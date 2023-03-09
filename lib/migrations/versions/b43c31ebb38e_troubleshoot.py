"""troubleshoot

Revision ID: b43c31ebb38e
Revises: 54c6413c2e0e
Create Date: 2023-03-09 10:05:13.811069

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b43c31ebb38e'
down_revision = '54c6413c2e0e'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('students', sa.Column('email', sa.String(), nullable=True))
    op.drop_column('students', 'grade')
    op.drop_column('students', 'subject')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('students', sa.Column('subject', sa.VARCHAR(), nullable=True))
    op.add_column('students', sa.Column('grade', sa.INTEGER(), nullable=True))
    op.drop_column('students', 'email')
    # ### end Alembic commands ###