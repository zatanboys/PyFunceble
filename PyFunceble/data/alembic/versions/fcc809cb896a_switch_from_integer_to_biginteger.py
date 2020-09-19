"""Switch from Integer to BigInteger

Revision ID: fcc809cb896a
Revises: d8893cd406db
Create Date: 2020-09-19 13:53:27.138994

"""
import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects import mysql
from sqlalchemy.exc import OperationalError

# pylint: skip-file

# revision identifiers, used by Alembic.
revision = "fcc809cb896a"
down_revision = "d8893cd406db"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(
        "pyfunceble_mined_ibfk_1", "pyfunceble_mined", type_="foreignkey"
    )
    op.drop_constraint(
        "pyfunceble_mined_ibfk_2", "pyfunceble_mined", type_="foreignkey"
    )
    op.drop_constraint(
        "pyfunceble_status_ibfk_1", "pyfunceble_status", type_="foreignkey"
    )

    op.alter_column(
        "pyfunceble_file",
        "id",
        existing_type=mysql.INTEGER(display_width=11),
        type_=sa.BigInteger(),
        autoincrement=True,
    )
    op.alter_column(
        "pyfunceble_mined",
        "file_id",
        existing_type=mysql.INTEGER(display_width=11),
        type_=sa.BigInteger(),
        existing_nullable=False,
    )
    op.alter_column(
        "pyfunceble_status",
        "file_id",
        existing_type=mysql.INTEGER(display_width=11),
        type_=sa.BigInteger(),
        existing_nullable=False,
    )
    op.alter_column(
        "pyfunceble_mined",
        "id",
        existing_type=mysql.INTEGER(display_width=11),
        type_=sa.BigInteger(),
        autoincrement=True,
    )
    op.alter_column(
        "pyfunceble_mined",
        "subject_id",
        existing_type=mysql.INTEGER(display_width=11),
        type_=sa.BigInteger(),
        existing_nullable=False,
    )
    op.alter_column(
        "pyfunceble_status",
        "id",
        existing_type=mysql.INTEGER(display_width=11),
        type_=sa.BigInteger(),
        autoincrement=True,
    )
    op.alter_column(
        "pyfunceble_whois_record",
        "epoch",
        existing_type=mysql.INTEGER(display_width=11),
        type_=sa.BigInteger(),
        existing_nullable=False,
    )
    op.alter_column(
        "pyfunceble_whois_record",
        "id",
        existing_type=mysql.INTEGER(display_width=11),
        type_=sa.BigInteger(),
        autoincrement=True,
    )

    with op.batch_alter_table("pyfunceble_mined") as batch_op:
        batch_op.create_foreign_key(
            "pyfunceble_mined_ibfk_1",
            "pyfunceble_file",
            ["file_id"],
            ["id"],
            onupdate="CASCADE",
            ondelete="CASCADE",
        )
        batch_op.create_foreign_key(
            "pyfunceble_mined_ibfk_2",
            "pyfunceble_status",
            ["subject_id"],
            ["id"],
            onupdate="CASCADE",
            ondelete="CASCADE",
        )
    with op.batch_alter_table("pyfunceble_status") as batch_op:
        batch_op.create_foreign_key(
            "pyfunceble_status_ibfk_1",
            "pyfunceble_file",
            ["file_id"],
            ["id"],
            onupdate="CASCADE",
            ondelete="CASCADE",
        )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(
        "pyfunceble_mined_ibfk_1", "pyfunceble_mined", type_="foreignkey"
    )
    op.drop_constraint(
        "pyfunceble_mined_ibfk_2", "pyfunceble_mined", type_="foreignkey"
    )
    op.drop_constraint(
        "pyfunceble_status_ibfk_1", "pyfunceble_status", type_="foreignkey"
    )

    op.alter_column(
        "pyfunceble_whois_record",
        "id",
        existing_type=sa.BigInteger(),
        type_=mysql.INTEGER(display_width=11),
        autoincrement=True,
    )
    op.alter_column(
        "pyfunceble_whois_record",
        "epoch",
        existing_type=sa.BigInteger(),
        type_=mysql.INTEGER(display_width=11),
        existing_nullable=False,
    )
    op.alter_column(
        "pyfunceble_status",
        "id",
        existing_type=sa.BigInteger(),
        type_=mysql.INTEGER(display_width=11),
        autoincrement=True,
    )
    op.alter_column(
        "pyfunceble_status",
        "file_id",
        existing_type=sa.BigInteger(),
        type_=mysql.INTEGER(display_width=11),
        existing_nullable=False,
    )
    op.alter_column(
        "pyfunceble_mined",
        "subject_id",
        existing_type=sa.BigInteger(),
        type_=mysql.INTEGER(display_width=11),
        existing_nullable=False,
    )
    op.alter_column(
        "pyfunceble_mined",
        "id",
        existing_type=sa.BigInteger(),
        type_=mysql.INTEGER(display_width=11),
        autoincrement=True,
    )
    op.alter_column(
        "pyfunceble_mined",
        "file_id",
        existing_type=sa.BigInteger(),
        type_=mysql.INTEGER(display_width=11),
        existing_nullable=False,
    )
    op.alter_column(
        "pyfunceble_file",
        "id",
        existing_type=sa.BigInteger(),
        type_=mysql.INTEGER(display_width=11),
        autoincrement=True,
    )

    with op.batch_alter_table("pyfunceble_mined") as batch_op:
        batch_op.create_foreign_key(
            "pyfunceble_mined_ibfk_1",
            "pyfunceble_file",
            ["file_id"],
            ["id"],
            onupdate="CASCADE",
            ondelete="CASCADE",
        )
        batch_op.create_foreign_key(
            "pyfunceble_mined_ibfk_2",
            "pyfunceble_status",
            ["subject_id"],
            ["id"],
            onupdate="CASCADE",
            ondelete="CASCADE",
        )
    with op.batch_alter_table("pyfunceble_status") as batch_op:
        batch_op.create_foreign_key(
            "pyfunceble_status_ibfk_1",
            "pyfunceble_file",
            ["file_id"],
            ["id"],
            onupdate="CASCADE",
            ondelete="CASCADE",
        )
    # ### end Alembic commands ###
