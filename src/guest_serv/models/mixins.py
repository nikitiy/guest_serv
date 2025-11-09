from datetime import datetime, timezone
from typing import Annotated

from sqlalchemy import DateTime, Integer
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.sql import func
from sqlalchemy.types import DateTime as DateTimeType


class IdMixin:
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)


UTCDateTime = Annotated[datetime, DateTimeType(timezone=True)]


class CreatedUpdatedMixin:
    created_at: Mapped[UTCDateTime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
        server_default=func.now(),
        nullable=False,
        index=True,
        doc="When the record was created (UTC)",
    )
    updated_at: Mapped[UTCDateTime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
        server_default=func.now(),
        onupdate=lambda: datetime.now(timezone.utc),
        server_onupdate=func.now(),
        nullable=False,
        index=True,
        doc="When the entry was last updated (UTC)",
    )


__all__ = ("IdMixin", "CreatedUpdatedMixin")
