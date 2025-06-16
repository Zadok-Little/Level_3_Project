first_group_questions = 'When going into combat are you (Answer with A or B):\n    A: Charging into melee?\n    B: Staying at range?'
second_group_questions = 'In a fantasy setting, which would you use? (Answer with A or B):\n    A: Physical Weapons\n    B: Magical Prowess'

physical_melee_questions = [
    {
        'question': 'How do you prep for a fight?', 
        'options': {
            'A': 'I love to practice my techniques! Sparring is a passion!',
            'B': 'Honestly? Anger guides me. I do what I feel!',
            'C': 'Victory lies in the element of surprise. I will not be caught unprepared. They WILL.',
            'D': 'Working on inner peace is more important than a fight.'
        },
        'class_map': {
            'A': 'Fighter',
            'B': 'Barbarian',
            'C': 'Rogue',
            'D': 'Monk'
        }

    }, 

    {
        'question': 'What weapons do you prefer?', 
        'options': {
            'A': 'Anything I am trained in would be ideal!',
            'B': 'Anything that around me! Or anyone!',
            'C': 'Something easy to use to get inside someones guard.',
            'D': 'My body is already a vessel for violence.'
        },
        'class_map': {
            'A': 'Fighter',
            'B': 'Barbarian',
            'C': 'Rogue',
            'D': 'Monk'
        }

    }, 

    {
        'question': 'Whats the best kind of pet?', 
        'options': {
            'A': 'A loyal pet that I can count on in battle!',
            'B': 'Something HUGE I can ride into battle!!! VICTORY OR DEATH!!!',
            'C': 'Something small and quiet...',
            'D': 'Something that can exist with me, as we both enjoy each others company.'
        },
        'class_map': {
            'A': 'Fighter',
            'B': 'Barbarian',
            'C': 'Rogue',
            'D': 'Monk'
        }

    }, 

    {
        'question': 'In highschool, what social group were you part of?...', 
        'options': {
            'A': 'The jocks!',
            'B': 'School? Who needs it?',
            'C': 'I was an outcast.',
            'D': 'The weebs and nerds!'
        },
        'class_map': {
            'A': 'Fighter',
            'B': 'Barbarian',
            'C': 'Rogue',
            'D': 'Monk'
        }

    }, 

    {
        'question': 'You are in a glimmering treasure room... What catches your eye best?', 
        'options': {
            'A': 'Two gleaming crossed swords, bearing a sigil of an ancient and powerful house. They call to you.',
            'B': 'A beer mug that never seems to empty!',
            'C': 'A floating carpet that never quite touches the floor.',
            'D': 'Glasses that seem to see beyond this plane.'
        },
        'class_map': {
            'A': 'Fighter',
            'B': 'Barbarian',
            'C': 'Rogue',
            'D': 'Monk'
        }

    }
]
physical_range_questions = [
    {
        'question': 'How do you prep for a fight?', 
        'options': {
            'A': 'I love to practice my techniques! Sparring is a passion!',
            'B': 'Victory lies in the element of surprise. I will not be caught unprepared. They WILL.',
            'C': 'I take a survey of my surroundings. I like getting the upper hand before a battle.'
        },
        'class_map': {
            'A': 'Fighter',
            'B': 'Rogue',
            'C': 'Ranger'
        }

    }, 

    {
        'question': 'What weapons do you prefer?', 
        'options': {
            'A': 'Crossbows! Anything easy to find, as I feel comfortable with any ranged weapon',
            'B': 'Short bows or a hand crassbow! Something small to hide easily.',
            'C': 'A Long Bow. Something reliable that keeps me far away from the combat'
        },
        'class_map': {
            'A': 'Fighter',
            'B': 'Rogue',
            'C': 'Ranger'
        }

    }, 

    {
        'question': 'Whats the best kind of pet?', 
        'options': {
            'A': 'A loyal pet that I can count on in battle!',
            'B': 'Something small and quiet...',
            'C': 'One I can ride!'
        },
        'class_map': {
            'A': 'Fighter',
            'B': 'Rogue',
            'C': 'Ranger'
        }

    }, 

    {
        'question': 'In highschool, what social group were you part of?', 
        'options': {
            'A': 'The jocks!',
            'B': '... the outcasts',
            'C': 'The adventurers...? We liked to go outside a lot.'
        },
        'class_map': {
            'A': 'Fighter',
            'B': 'Rogue',
            'C': 'Ranger'
        }

    }, 

    {
        'question': 'You are in a glimmering treasure room... What catches your eye best?', 
        'options': {
            'A': 'Two gleaming crossed swords, bearing a sigil of an ancient and powerful house. They call to you.',
            'B': 'A floating carpet that never quite touches the floor.',
            'C': 'An bronze statue of a wolf.. its eyes watch you as you walk around the room...'
        },
        'class_map': {
            'A': 'Fighter',
            'B': 'Rogue',
            'C': 'Ranger'
        }

    }
]
magical_melee_questions = [
    {
        'question': 'How do you prep for a fight?', 
        'options': {
            'A': 'Focusing my will and reminding myself why I\'m fighting.',
            'B': 'Praying to my God for guidance and reassurance.',
            'C': 'I really prefer to find my bearings with nature. A clear mind is powerful.',
            'D': 'Maybe a ritual? Can I hex my enemies...?',
            'E': '"Me? Flossing my teeth! You can\'t seduce the enemy without a dazzling smile!'
        },
        'class_map': {
            'A': 'Paladin',
            'B': 'Cleric',
            'C': 'Druid',
            'D': 'Warlock',
            'E': 'Bard'
        }

    }, 

    {
        'question': 'What weapons do you prefer?', 
        'options': {
            'A': 'A weapon and a shield! I protect everyone I can.',
            'B': 'Something blunt out of respect to my God.',
            'C': 'This cool stick I found in the woods is good.',
            'D': 'A weapon I summon myself!',
            'E': 'Maybe an instrument and my sheer good looks and charm... Who could resist this face?'
        },
        'class_map': {
            'A': 'Paladin',
            'B': 'Cleric',
            'C': 'Druid',
            'D': 'Warlock',
            'E': 'Bard'
        }

    }, 

    {
        'question': 'Whats the best kind of pet?', 
        'options': {
            'A': 'Something strong and reliable!',
            'B': 'Something I can devote all my time to!',
            'C': 'Does anything I find in the wilderness count...?',
            'D': 'Something rare!',
            'E': 'Something cute and cuddly!'
        },
        'class_map': {
            'A': 'Paladin',
            'B': 'Cleric',
            'C': 'Druid',
            'D': 'Warlock',
            'E': 'Bard'
        }

    }, 

    {
        'question': 'In highschool, what social group were you part of?', 
        'options': {
            'A': 'The jocks!',
            'B': 'I was actually part of this really awesome bible group!',
            'C': 'The adventurers...? We liked to go outside a lot.',
            'D': 'The goth and emo kids...',
            'E': 'I fit in anywhere. ;)'
        },
        'class_map': {
            'A': 'Paladin',
            'B': 'Cleric',
            'C': 'Druid',
            'D': 'Warlock',
            'E': 'Bard'
        }

    }, 

    {
        'question': 'You are in a glimmering treasure room... What catches your eye best?', 
        'options': {
            'A': 'A glowing shield with a golden lion insignia emblazed on it.',
            'B': 'A bubbling clear blue pool whos depths are unfathomable.',
            'C': 'A sealed box, that seems to have some sort of small living animal inside...?',
            'D': 'A scroll that seems to possess infinite knowledge... and knowledge means power.',
            'E': 'A magically self playing flute that hovers mid air...'
        },
        'class_map': {
            'A': 'Paladin',
            'B': 'Cleric',
            'C': 'Druid',
            'D': 'Warlock',
            'E': 'Bard'
        }

    }
]
magical_range_questions = [
    {
        'question': 'How do you prep for a fight?', 
        'options': {
            'A': 'Praying to my God for guidance and reassurance.',
            'B': 'Me? Flossing my teeth! You can\'t seduce the enemy without a dazzling smile!',
            'C': 'I read up. Gather as much knowledge as I can. Knowledge is power.',
            'D': 'I have no need to prepare! The power within me will conquer all.',
            'E': 'Maybe a ritual? Can I hex my enemies...?'
        },
        'class_map': {
            'A': 'Cleric',
            'B': 'Bard',
            'C': 'Wizard',
            'D': 'Sorcerer',
            'E': 'Warlock'
        }

    }, 

    {
        'question': 'Whats the best kind of pet?', 
        'options': {
            'A': 'Something I can devote all my time to!',
            'B': 'Something cute and cuddly!',
            'C': 'Something that can curl up on my lap as I read.',
            'D': 'Something that has a long lifespan. I\'d prefer a lifelong friend.',
            'E': 'Something rare!'
        },
        'class_map': {
            'A': 'Cleric',
            'B': 'Bard',
            'C': 'Wizard',
            'D': 'Sorcerer',
            'E': 'Warlock'
        }

    }, 

    {
        'question': 'What weapons do you prefer?', 
        'options': {
            'A': 'Something blunt out of respect to my God.',
            'B': 'Maybe an instrument and my sheer good looks and charm... Who could resist this face?',
            'C': 'Spell books are always great to have on hand.',
            'D': 'Something to focus my innate power, like a wand or a staff.',
            'E': 'A weapon I summon myself!'
        },
        'class_map': {
            'A': 'Cleric',
            'B': 'Bard',
            'C': 'Wizard',
            'D': 'Sorcerer',
            'E': 'Warlock'
        }

    }, 

    {
        'question': 'In highschool, what social group were you part of?', 
        'options': {
            'A': 'I was actually part of this awesome bible group!',
            'B': 'I fit in anywhere. ;)',
            'C': 'The intellectuals.',
            'D': 'I fit best with the popular kids.',
            'E': 'The goth and emo kids...'
        },
        'class_map': {
            'A': 'Cleric',
            'B': 'Bard',
            'C': 'Wizard',
            'D': 'Sorcerer',
            'E': 'Warlock'
        }

    }, 

    {
        'question': 'You are in a glimmering treasure room... What catches your eye best?', 
        'options': {
            'A': 'A bubbling clear blue pool whos depths are unfathomable.',
            'B': 'A magically self playing flute that hovers in mid air...',
            'C': 'A staff of a great mage that has long been passed.',
            'D': 'A multi-colored patchy robe, where each patch symbolizes a spell...',
            'E': 'A scroll that seems to possess infinite knowledge... and knowledge means power.'
        },
        'class_map': {
            'A': 'Cleric',
            'B': 'Bard',
            'C': 'Wizard',
            'D': 'Sorcerer',
            'E': 'Warlock'
        }

    }
]

