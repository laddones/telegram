from enum import Enum
from typing import Optional

from pydantic import BaseModel


class PersonPostStatus(str, Enum):
    PUBLISHED = 'PUBLISHED'
    UNPUBLISHED = 'UNPUBLISHED'


class Image(BaseModel):
    id: int
    image: str


class SearchSchema(BaseModel):
    last_name: str
    first_name: str
    middle_name: Optional[str] = None
    birthday: Optional[str] = None


class Person(BaseModel):
    images: Optional[list[Image]] = None
    last_name: str
    first_name: str
    middle_name: Optional[str] = None
    birthday: Optional[str] = None
    citizenship: Optional[str] = None
    passport: Optional[str] = None
    individual_identification_number: Optional[str] = None
    place_of_birthday: Optional[str] = None
    place_of_living: Optional[str] = None
    additional_info: Optional[str] = None
    source: Optional[str] = None
    job_title: Optional[str] = None
    rank: Optional[str] = None
    rank_choice: Optional[str] = None
    military_unit: Optional[str] = None
    type_of_army: Optional[str] = None
    type_of_army_choice: Optional[str] = None
    military_from: Optional[str] = None
    commander: Optional[str] = None
    status_person: Optional[str] = None
    place_where_accident: Optional[str] = None
    data_when_accident: Optional[str] = None


