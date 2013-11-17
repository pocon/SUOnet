# Run Each of these functions to specify settings made for the timeslot

from Exercise.models import *
import random, string

letters = 'ABCDEFGHJKMNPQRSTWXYZ'
numbers = '23456789'

def random_checkpoint_code():
    code = ''.join(random.choice(letters + numbers) for x in range(5))
    if Checkpoint_Code.objects.filter(code=code):
        return random_checkpoint_code()
    
    return code

def random_ambush_code():
    code = ''.join(random.choice(letters + numbers) for x in range(3))
    if Section.objects.filter(ambush_code=code):
        return random_ambush_code()
    
    return code


# Initial Setup: Run before deployment #
def init():
    # Ambush Codes
    for section in Section.objects.all():
        section.ambush_code = random_ambush_code()
        section.save()

    
    # Checkpoint Codes
    for checkpoint in Checkpoint.objects.all():
        for section in Section.objects.all():
            Checkpoint_Code.objects.create(
                checkpoint=checkpoint,
                section=section,
                code=random_checkpoint_code(),
                )

    # Settings and Setup
    s = Setting.objects.get_or_create(key="ambush_award", defaults={'value':"0"})
    s[0].value = "150"
    s[0].save()
    
    s = Setting.objects.get_or_create(key="ambush_demerit", defaults={'value':0})
    s[0].value = "-150"
    s[0].save()
