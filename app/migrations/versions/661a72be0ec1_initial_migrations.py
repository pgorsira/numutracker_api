"""initial migrations

Revision ID: 661a72be0ec1
Revises: 
Create Date: 2018-08-26 07:19:46.867933

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '661a72be0ec1'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('artist',
    sa.Column('mbid', sa.String(length=36), nullable=False),
    sa.Column('name', sa.String(length=512), nullable=False),
    sa.Column('active', sa.Boolean(), server_default=sa.text('true'), nullable=True),
    sa.Column('sort_name', sa.String(length=512), nullable=False),
    sa.Column('disambiguation', sa.String(length=512), nullable=False),
    sa.Column('art', sa.String(length=100), server_default=sa.text('NULL'), nullable=True),
    sa.Column('date_added', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.Column('date_art_check', sa.DateTime(timezone=True), server_default=sa.text('NULL'), nullable=True),
    sa.Column('date_checked', sa.DateTime(timezone=True), server_default=sa.text('NULL'), nullable=True),
    sa.Column('date_updated', sa.DateTime(timezone=True), server_default=sa.text('NULL'), nullable=True),
    sa.Column('apple_music_link', sa.String(), nullable=True),
    sa.Column('spotify_link', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('mbid')
    )
    op.create_table('release',
    sa.Column('mbid', sa.String(length=36), nullable=False),
    sa.Column('title', sa.String(length=512), nullable=False),
    sa.Column('artists_string', sa.String(length=512), nullable=False),
    sa.Column('active', sa.Boolean(), server_default=sa.text('true'), nullable=True),
    sa.Column('type', sa.Enum('ALBUM', 'AUDIOBOOK', 'BROADCAST', 'COMPILATION', 'DEMO', 'DJ_MIX', 'EP', 'INTERVIEW', 'LIVE', 'MIX_TAPE', 'OTHER', 'REMIX', 'SINGLE', 'SOUNDTRACK', 'SPOKENWORD', 'UNKNOWN', name='releasetype'), nullable=True),
    sa.Column('date_release', sa.Date(), server_default=sa.text('NULL'), nullable=False),
    sa.Column('art', sa.String(length=100), server_default=sa.text('NULL'), nullable=True),
    sa.Column('date_added', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.Column('date_art_check', sa.DateTime(timezone=True), server_default=sa.text('NULL'), nullable=True),
    sa.Column('date_updated', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.Column('date_checked', sa.DateTime(timezone=True), server_default=sa.text('NULL'), nullable=True),
    sa.Column('apple_music_link', sa.String(), nullable=True),
    sa.Column('spotify_link', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('mbid')
    )
    op.create_index(op.f('ix_release_date_release'), 'release', ['date_release'], unique=False)
    op.create_index(op.f('ix_release_type'), 'release', ['type'], unique=False)
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=True),
    sa.Column('password_hash', sa.String(length=128), nullable=True),
    sa.Column('username', sa.String(length=12), nullable=True),
    sa.Column('date_joined', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.Column('album', sa.Boolean(), server_default=sa.text('true'), nullable=True),
    sa.Column('single', sa.Boolean(), server_default=sa.text('true'), nullable=True),
    sa.Column('ep', sa.Boolean(), server_default=sa.text('true'), nullable=True),
    sa.Column('live', sa.Boolean(), server_default=sa.text('false'), nullable=True),
    sa.Column('soundtrack', sa.Boolean(), server_default=sa.text('false'), nullable=True),
    sa.Column('remix', sa.Boolean(), server_default=sa.text('false'), nullable=True),
    sa.Column('other', sa.Boolean(), server_default=sa.text('false'), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('username')
    )
    op.create_index(op.f('ix_user_email'), 'user', ['email'], unique=True)
    op.create_table('artist_aka',
    sa.Column('artist_mbid', sa.String(length=36), nullable=False),
    sa.Column('name', sa.String(length=512), nullable=False),
    sa.ForeignKeyConstraint(['artist_mbid'], ['artist.mbid'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('artist_mbid', 'name')
    )
    op.create_index(op.f('ix_artist_aka_artist_mbid'), 'artist_aka', ['artist_mbid'], unique=False)
    op.create_table('artist_import',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('import_name', sa.String(length=100), nullable=False),
    sa.Column('import_mbid', sa.String(length=36), nullable=True),
    sa.Column('import_method', sa.Enum('APPLE', 'SPOTIFY', 'LASTFM', name='importmethod'), nullable=True),
    sa.Column('found_mbid', sa.String(length=36), nullable=True),
    sa.Column('date_added', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.Column('date_checked', sa.DateTime(timezone=True), server_default=sa.text('NULL'), nullable=True),
    sa.ForeignKeyConstraint(['found_mbid'], ['artist.mbid'], onupdate='CASCADE', ondelete='SET NULL', initially='DEFERRED', deferrable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], onupdate='CASCADE', ondelete='CASCADE', initially='DEFERRED', deferrable=True),
    sa.PrimaryKeyConstraint('user_id', 'import_name')
    )
    op.create_index(op.f('ix_artist_import_user_id'), 'artist_import', ['user_id'], unique=False)
    op.create_table('artist_release',
    sa.Column('artist_mbid', sa.String(length=36), nullable=False),
    sa.Column('release_mbid', sa.String(length=36), nullable=False),
    sa.ForeignKeyConstraint(['artist_mbid'], ['artist.mbid'], onupdate='CASCADE', ondelete='CASCADE', initially='DEFERRED', deferrable=True),
    sa.ForeignKeyConstraint(['release_mbid'], ['release.mbid'], onupdate='CASCADE', ondelete='CASCADE', initially='DEFERRED', deferrable=True),
    sa.PrimaryKeyConstraint('artist_mbid', 'release_mbid')
    )
    op.create_table('user_activity',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('date', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.Column('release_mbid', sa.String(length=36), nullable=True),
    sa.Column('artist_mbid', sa.String(length=36), nullable=True),
    sa.Column('activity', sa.Enum('LISTENED', 'UNLISTENED', 'FOLLOW_ARTIST', 'FOLLOW_RELEASE', 'UNFOLLOW_ARTIST', 'UNFOLLOW_RELEASE', 'APPLE_IMPORT', 'SPOTIFY_IMPORT', 'LASTFM_IMPORT', 'COMMENT_ARTIST', 'COMMENT_RELEASE', 'RATED_RELEASE', name='activitytypes'), nullable=True),
    sa.Column('data', sa.JSON(), nullable=True),
    sa.ForeignKeyConstraint(['artist_mbid'], ['artist.mbid'], onupdate='CASCADE', ondelete='CASCADE', initially='DEFERRED', deferrable=True),
    sa.ForeignKeyConstraint(['release_mbid'], ['release.mbid'], onupdate='CASCADE', ondelete='CASCADE', initially='DEFERRED', deferrable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user_artist',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('mbid', sa.String(length=36), nullable=False),
    sa.Column('name', sa.String(length=512), nullable=False),
    sa.Column('sort_name', sa.String(length=512), nullable=False),
    sa.Column('disambiguation', sa.String(length=512), nullable=False),
    sa.Column('art', sa.String(length=100), server_default=sa.text('NULL'), nullable=True),
    sa.Column('date_updated', sa.DateTime(timezone=True), server_default=sa.text('NULL'), nullable=True),
    sa.Column('apple_music_link', sa.String(), nullable=True),
    sa.Column('spotify_link', sa.String(), nullable=True),
    sa.Column('date_followed', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.Column('follow_method', sa.Enum('APPLE', 'SPOTIFY', 'LASTFM', name='importmethod'), nullable=True),
    sa.Column('following', sa.Boolean(), server_default=sa.text('false'), nullable=True),
    sa.ForeignKeyConstraint(['mbid'], ['artist.mbid'], onupdate='CASCADE', ondelete='CASCADE', initially='DEFERRED', deferrable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('user_id', 'mbid')
    )
    op.create_index(op.f('ix_user_artist_following'), 'user_artist', ['following'], unique=False)
    op.create_table('user_notifications',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('date_created', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.Column('type', sa.Enum('PAST', 'UPCOMING', 'RECENT', 'RELEASED', name='notificationtype'), nullable=True),
    sa.Column('release_mbid', sa.String(length=36), nullable=False),
    sa.Column('date_sent', sa.DateTime(timezone=True), server_default=sa.text('NULL'), nullable=True),
    sa.ForeignKeyConstraint(['release_mbid'], ['release.mbid'], onupdate='CASCADE', ondelete='CASCADE', initially='DEFERRED', deferrable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('user_id', 'release_mbid')
    )
    op.create_index(op.f('ix_user_notifications_date_created'), 'user_notifications', ['date_created'], unique=False)
    op.create_index(op.f('ix_user_notifications_type'), 'user_notifications', ['type'], unique=False)
    op.create_table('user_release',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('mbid', sa.String(length=36), nullable=False),
    sa.Column('title', sa.String(length=512), nullable=False),
    sa.Column('artists_string', sa.String(length=512), nullable=False),
    sa.Column('type', sa.Enum('ALBUM', 'AUDIOBOOK', 'BROADCAST', 'COMPILATION', 'DEMO', 'DJ_MIX', 'EP', 'INTERVIEW', 'LIVE', 'MIX_TAPE', 'OTHER', 'REMIX', 'SINGLE', 'SOUNDTRACK', 'SPOKENWORD', 'UNKNOWN', name='releasetype'), nullable=True),
    sa.Column('date_release', sa.Date(), server_default=sa.text('NULL'), nullable=False),
    sa.Column('art', sa.String(length=100), server_default=sa.text('NULL'), nullable=True),
    sa.Column('date_updated', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.Column('apple_music_link', sa.String(), nullable=True),
    sa.Column('spotify_link', sa.String(), nullable=True),
    sa.Column('date_added', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.Column('add_method', sa.Enum('AUTOMATIC', 'MANUAL', 'LISTENED', name='addmethod'), nullable=True),
    sa.Column('listened', sa.Boolean(), server_default=sa.text('false'), nullable=True),
    sa.Column('date_listened', sa.DateTime(timezone=True), nullable=True),
    sa.ForeignKeyConstraint(['mbid'], ['release.mbid'], onupdate='CASCADE', ondelete='CASCADE', initially='DEFERRED', deferrable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], onupdate='CASCADE', ondelete='CASCADE', initially='DEFERRED', deferrable=True),
    sa.PrimaryKeyConstraint('user_id', 'mbid')
    )
    op.create_index(op.f('ix_user_release_date_listened'), 'user_release', ['date_listened'], unique=False)
    op.create_index(op.f('ix_user_release_date_release'), 'user_release', ['date_release'], unique=False)
    op.create_index(op.f('ix_user_release_type'), 'user_release', ['type'], unique=False)
    op.create_index(op.f('ix_user_release_user_id'), 'user_release', ['user_id'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_user_release_user_id'), table_name='user_release')
    op.drop_index(op.f('ix_user_release_type'), table_name='user_release')
    op.drop_index(op.f('ix_user_release_date_release'), table_name='user_release')
    op.drop_index(op.f('ix_user_release_date_listened'), table_name='user_release')
    op.drop_table('user_release')
    op.drop_index(op.f('ix_user_notifications_type'), table_name='user_notifications')
    op.drop_index(op.f('ix_user_notifications_date_created'), table_name='user_notifications')
    op.drop_table('user_notifications')
    op.drop_index(op.f('ix_user_artist_following'), table_name='user_artist')
    op.drop_table('user_artist')
    op.drop_table('user_activity')
    op.drop_table('artist_release')
    op.drop_index(op.f('ix_artist_import_user_id'), table_name='artist_import')
    op.drop_table('artist_import')
    op.drop_index(op.f('ix_artist_aka_artist_mbid'), table_name='artist_aka')
    op.drop_table('artist_aka')
    op.drop_index(op.f('ix_user_email'), table_name='user')
    op.drop_table('user')
    op.drop_index(op.f('ix_release_type'), table_name='release')
    op.drop_index(op.f('ix_release_date_release'), table_name='release')
    op.drop_table('release')
    op.drop_table('artist')
    # ### end Alembic commands ###
