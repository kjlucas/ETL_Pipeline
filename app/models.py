import datetime

from sqlalchemy import Date, DateTime, Float, String, func, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase


class Base(DeclarativeBase):
    pass


class DataSeries(Base):
    __tablename__ = "data_series"

    __table_args__ = (UniqueConstraint("date", "series_id", name="unique_series_date"),)
    id: Mapped[int] = mapped_column(primary_key=True)
    date: Mapped[Date] = mapped_column(Date, nullable=False)
    series_id: Mapped[str] = mapped_column(String(50), nullable=False)
    value: Mapped[float] = mapped_column(Float, nullable=False)
    created_at: Mapped[datetime.datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())