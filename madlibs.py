def madlib():
    body = input("title : ")

    verb = input("verb: ")
    adj1 = input("adjective1 : ")
    adj2 = input("adjective: ")
    adj3 = input("adjective: ")
    adj4 = input("adjective: ")
    adj5 = input("adjective: ")
    adj6 = input("adjective: ")
    adj7 = input("adjective: ")
    adj8 = input("adjective: ")

    noun1 = input("noun :")
    noun2 = input("noun:")

    noun_plural_1 = input ("noun (plural): ")
    noun_plural_2= input ("noun (plural): ")
    madlib_story = f" They call him {body}, the one who {verb}s with {adj1} precision\
    In a {adj2} world where justice is {adj3}, he walks alone—armed with a {noun1} and haunted by a {noun2}\
    His reputation is {adj4}; even the {noun_plural_1} whisper his name before they fall\
    The night was {adj5}, his resolve {adj6}, his movements {adj7}, and his vengeance {adj8}\
    He doesn`t start wars... but he ends them. One by one, the {noun_plural_2} fade—just like everything else he once cared about\
    "
    print(madlib_story)



madlib()