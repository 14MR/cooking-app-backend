from djchoices import ChoiceItem, DjangoChoices


class RecipeBlockType(DjangoChoices):
    image = ChoiceItem('image')
    text = ChoiceItem('text')
    timer = ChoiceItem('timer')

