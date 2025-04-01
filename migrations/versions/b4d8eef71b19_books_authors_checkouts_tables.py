"""books, authors & checkouts tables

Revision ID: b4d8eef71b19
Revises: 
Create Date: 2025-04-01 17:38:43.506679

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b4d8eef71b19'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('author',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=True),
    sa.Column('surname', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('author', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_author_name'), ['name'], unique=False)
        batch_op.create_index(batch_op.f('ix_author_surname'), ['surname'], unique=False)

    op.create_table('book',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=100), nullable=True),
    sa.Column('author', sa.String(length=200), nullable=True),
    sa.Column('genre', sa.String(length=200), nullable=True),
    sa.Column('publish_date', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('book', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_book_author'), ['author'], unique=True)
        batch_op.create_index(batch_op.f('ix_book_genre'), ['genre'], unique=False)
        batch_op.create_index(batch_op.f('ix_book_publish_date'), ['publish_date'], unique=False)
        batch_op.create_index(batch_op.f('ix_book_title'), ['title'], unique=False)

    op.create_table('checkout_record',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=100), nullable=True),
    sa.Column('author', sa.String(length=200), nullable=True),
    sa.Column('borrow_date', sa.DateTime(), nullable=True),
    sa.Column('return_date', sa.DateTime(), nullable=True),
    sa.Column('is_borrowed', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('checkout_record', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_checkout_record_author'), ['author'], unique=False)
        batch_op.create_index(batch_op.f('ix_checkout_record_borrow_date'), ['borrow_date'], unique=False)
        batch_op.create_index(batch_op.f('ix_checkout_record_return_date'), ['return_date'], unique=False)
        batch_op.create_index(batch_op.f('ix_checkout_record_title'), ['title'], unique=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('checkout_record', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_checkout_record_title'))
        batch_op.drop_index(batch_op.f('ix_checkout_record_return_date'))
        batch_op.drop_index(batch_op.f('ix_checkout_record_borrow_date'))
        batch_op.drop_index(batch_op.f('ix_checkout_record_author'))

    op.drop_table('checkout_record')
    with op.batch_alter_table('book', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_book_title'))
        batch_op.drop_index(batch_op.f('ix_book_publish_date'))
        batch_op.drop_index(batch_op.f('ix_book_genre'))
        batch_op.drop_index(batch_op.f('ix_book_author'))

    op.drop_table('book')
    with op.batch_alter_table('author', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_author_surname'))
        batch_op.drop_index(batch_op.f('ix_author_name'))

    op.drop_table('author')
    # ### end Alembic commands ###
