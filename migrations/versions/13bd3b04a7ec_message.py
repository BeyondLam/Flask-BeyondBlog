"""message

Revision ID: 13bd3b04a7ec
Revises: 
Create Date: 2020-03-02 03:42:12.130925

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '13bd3b04a7ec'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('admin',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=128), nullable=True),
    sa.Column('password', sa.String(length=128), nullable=True),
    sa.Column('avatar', sa.String(length=256), nullable=True),
    sa.Column('power', sa.Enum('超级管理员', '管理员'), nullable=True),
    sa.Column('status', sa.Enum('正常', '删除'), nullable=True),
    sa.Column('create_time', sa.DateTime(), nullable=True),
    sa.Column('update_time', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('username')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=128), nullable=True),
    sa.Column('password', sa.String(length=128), nullable=True),
    sa.Column('avatar', sa.String(length=256), nullable=True),
    sa.Column('phone', sa.String(length=11), nullable=True),
    sa.Column('status', sa.Enum('正常', '删除'), nullable=True),
    sa.Column('create_time', sa.DateTime(), nullable=True),
    sa.Column('update_time', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('username')
    )
    op.create_table('admin_login_log',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('admin_id', sa.Integer(), nullable=True),
    sa.Column('ip', sa.String(length=128), nullable=True),
    sa.Column('create_time', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['admin_id'], ['admin.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_admin_login_log_create_time'), 'admin_login_log', ['create_time'], unique=False)
    op.create_table('admin_operate_log',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('admin_id', sa.Integer(), nullable=True),
    sa.Column('ip', sa.String(length=128), nullable=True),
    sa.Column('detail', sa.String(length=256), nullable=True),
    sa.Column('create_time', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['admin_id'], ['admin.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_admin_operate_log_create_time'), 'admin_operate_log', ['create_time'], unique=False)
    op.create_table('blog',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.TEXT(), nullable=True),
    sa.Column('content', sa.TEXT(), nullable=True),
    sa.Column('summary', sa.TEXT(), nullable=True),
    sa.Column('logo', sa.String(length=256), nullable=True),
    sa.Column('status', sa.Integer(), nullable=True),
    sa.Column('author_id', sa.Integer(), nullable=True),
    sa.Column('page_views', sa.Integer(), nullable=True),
    sa.Column('like_numbers', sa.Integer(), nullable=True),
    sa.Column('comment_numbers', sa.Integer(), nullable=True),
    sa.Column('create_time', sa.DateTime(), nullable=True),
    sa.Column('update_time', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['author_id'], ['admin.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('board',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.Text(), nullable=True),
    sa.Column('content', sa.Text(), nullable=True),
    sa.Column('status', sa.Enum('正常', '删除'), nullable=True),
    sa.Column('create_time', sa.DateTime(), nullable=True),
    sa.Column('admin_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['admin_id'], ['admin.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_board_create_time'), 'board', ['create_time'], unique=False)
    op.create_table('message',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('sender_id', sa.Integer(), nullable=True),
    sa.Column('recipient_id', sa.Integer(), nullable=True),
    sa.Column('content', sa.Text(), nullable=True),
    sa.Column('create_time', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['recipient_id'], ['admin.id'], ),
    sa.ForeignKeyConstraint(['sender_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_message_create_time'), 'message', ['create_time'], unique=False)
    op.create_table('search_history',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('keyword', sa.TEXT(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('create_time', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user_login_log',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('ip', sa.String(length=128), nullable=True),
    sa.Column('create_time', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_user_login_log_create_time'), 'user_login_log', ['create_time'], unique=False)
    op.create_table('user_operate_log',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('ip', sa.String(length=128), nullable=True),
    sa.Column('detail', sa.String(length=256), nullable=True),
    sa.Column('create_time', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_user_operate_log_create_time'), 'user_operate_log', ['create_time'], unique=False)
    op.create_table('collect_blog_article',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('blog_id', sa.Integer(), nullable=True),
    sa.Column('create_time', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['blog_id'], ['blog.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('comment',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('sender_id', sa.Integer(), nullable=True),
    sa.Column('content', sa.Text(), nullable=True),
    sa.Column('blog_id', sa.Integer(), nullable=True),
    sa.Column('create_time', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['blog_id'], ['blog.id'], ),
    sa.ForeignKeyConstraint(['sender_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_comment_create_time'), 'comment', ['create_time'], unique=False)
    op.create_table('tag',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('blog_id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=32), nullable=True),
    sa.Column('create_time', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['blog_id'], ['blog.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_tag_create_time'), 'tag', ['create_time'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_tag_create_time'), table_name='tag')
    op.drop_table('tag')
    op.drop_index(op.f('ix_comment_create_time'), table_name='comment')
    op.drop_table('comment')
    op.drop_table('collect_blog_article')
    op.drop_index(op.f('ix_user_operate_log_create_time'), table_name='user_operate_log')
    op.drop_table('user_operate_log')
    op.drop_index(op.f('ix_user_login_log_create_time'), table_name='user_login_log')
    op.drop_table('user_login_log')
    op.drop_table('search_history')
    op.drop_index(op.f('ix_message_create_time'), table_name='message')
    op.drop_table('message')
    op.drop_index(op.f('ix_board_create_time'), table_name='board')
    op.drop_table('board')
    op.drop_table('blog')
    op.drop_index(op.f('ix_admin_operate_log_create_time'), table_name='admin_operate_log')
    op.drop_table('admin_operate_log')
    op.drop_index(op.f('ix_admin_login_log_create_time'), table_name='admin_login_log')
    op.drop_table('admin_login_log')
    op.drop_table('user')
    op.drop_table('admin')
    # ### end Alembic commands ###