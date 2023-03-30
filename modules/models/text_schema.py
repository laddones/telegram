from modules.models.schema import Person
from modules.models.text_enum import Texts


class TextModul:
    @staticmethod
    def checker(item: str) -> str:
        if item is None:
            return '???'
        return item

    @staticmethod
    def show_search_person(person: Person) -> str:
        if person.images:
            print(person.images)
            image = person.images[0].image
            print(image)
        else:
            image = 'https://sabilaw.org/wp-content/uploads/2020/11/img_2263-1024x777.jpg'
        return Texts.SHOW_PERSON.format(
            first_name=TextModul.checker(person.first_name),
            last_name=TextModul.checker(person.last_name),
            middle_name=TextModul.checker(person.middle_name if person.middle_name else None),
            birthday=TextModul.checker(person.birthday if person.birthday else None),
            citizenship=TextModul.checker(person.citizenship if person.citizenship else None),
            passport=TextModul.checker(person.passport if person.passport else None),
            individual_identification_number=TextModul.checker(person.individual_identification_number if person.individual_identification_number else None),
            place_of_birthday=TextModul.checker(person.place_of_birthday if person.place_of_birthday else None),
            place_of_living=TextModul.checker(person.place_of_living if person.place_of_living else None),
            type_of_army=TextModul.checker(person.type_of_army if person.type_of_army else None),
            type_of_army_choice=TextModul.checker(person.type_of_army_choice if person.type_of_army_choice else None),
            rank=TextModul.checker(person.rank if person.rank else None),
            rank_choice=TextModul.checker(person.rank_choice if person.rank_choice else None),
            job_title=TextModul.checker(person.job_title if person.job_title else None),
            military_unit=TextModul.checker(person.military_unit if person.military_unit else None),
            military_from=TextModul.checker(person.military_from if person.military_from else None),
            commander=TextModul.checker(person.commander if person.commander else None),
            place_where_accident=TextModul.checker(person.place_where_accident if person.place_where_accident else None),
            data_when_accident=TextModul.checker(person.data_when_accident if person.data_when_accident else None),
            source=TextModul.checker(person.source if person.source else None),
            additional_info=TextModul.checker(person.additional_info if person.additional_info else None),
            image=TextModul.checker(image)
        )

#     @staticmethod
#     def show_add_person(person: PersonCreateSchema) -> str:
#         return Texts.SHOW_ADD_PERSON.format(
#             first_name=TextModul.checker(person.first_name),
#             last_name=TextModul.checker(person.last_name),
#             middle_name=TextModul.checker(person.middle_name),
#             birthday=TextModul.checker(person.birthday),
#             military_unit=TextModul.checker(person.military_unit),
#             phone_number=TextModul.checker(person.phone_number),
#             status_person=TextModul.checker(person.status_person),
#             text=TextModul.checker(person.text).replace('<p>', '').replace('</p>', ''),
#             image='https://sabilaw.org/wp-content/uploads/2020/11/img_2263-1024x777.jpg'
#         )
#
#
