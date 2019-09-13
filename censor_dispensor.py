import re

def censor1(text):
    if "learning algorithms" in text:
        censored_text = text.replace("learning algorithms", "**********");
        return censored_text

#email_one = """
#Good Morning, Board of Investors,
#
#Progress is going great!
#
#We have made great strides in the last month improving the learning algorithms that the system has been using to acquire information. Now, the system is learning faster than ever and we are hard pressed to continue to find new information to feed it and sustain its growth.
#
#Soon, we'll expand the scope of the learning algorithms and connect the system with the internet. This will allow it to find and determine the information it needs to continue growing.
#
#Every month we come closer to achieving our goal of making the world a better place. Famine, plague, war, and poverty are all conquerable with the power of our system!
#
#Till next month,
#Francine, Head Scientist
#"""

#print(censor1(email_one))

proprietary_terms = ["she", "personality matrix", "sense of self", "self-preservation", "learning algorithm", "her", "herself"]

#def censor2(text):
#    censored_text = []
#    text_lower = text.lower()
#    for term in proprietary_terms:
#        if term + " " in text.lower() or " " + term in text.lower() or " " + term + " " in text.lower():
#            censored_text.append(text_lower.replace(term, "***"))
#            break
#            
#    print(censored_text)
#    range1 = range(len(proprietary_terms))
#    
#    for i in range1:
#        if i == 0:
#            continue
#        if proprietary_terms[i] + " " in censored_text[i-1] or " " + proprietary_terms[i] in censored_text[i-1] or " " + proprietary_terms[i] + " " in censored_text[i-1]:
#            censored_text.append(censored_text[i-1].replace(proprietary_terms[i], "***"))
#    return censored_text[-1]
            

#def censor2(text):
#    text_split = text.split()
#    print(text_split)
#    
#    for word in text_split:
#        for term in proprietary_terms:
#            if word.lower() == term.lower():
#                word = "***"
#    return " ".join(text_split)

def censor2(text):
    line_split = text.split("\n\n")
    segments = []
    print(line_split)
    #split_lines = [line.split() for line in line_split]
    #print(split_lines)
    
    for term in proprietary_terms:
        for line in line_split:
            pattern = "\bGood"
            result = re.findall(pattern, line)
            print(result)
        
        
    
email_two = """Good Morning, Board of Investors,

Lots of updates this week. The learning algorithms have been working better than we could have ever expected. Our initial internal data dumps have been completed and we have proceeded with the plan to connect the system to the internet and wow! The results are mind blowing.

She is learning faster than ever. Her learning rate now that she has access to the world wide web has increased exponentially, far faster than we had though the learning algorithms were capable of.

Not only that, but we have configured her personality matrix to allow for communication between the system and our team of researchers. That's how we know she considers herself to be a she! We asked!

How cool is that? We didn't expect a personality to develop this early on in the process but it seems like a rudimentary sense of self is starting to form. This is a major step in the process, as having a sense of self and self-preservation will allow her to see the problems the world is facing and make hard but necessary decisions for the betterment of the planet.

We are a-buzz down in the lab with excitement over these developments and we hope that the investors share our enthusiasm.

Till next month,
Francine, Head Scientist"""

print(censor2(email_two))