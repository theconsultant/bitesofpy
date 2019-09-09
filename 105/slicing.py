#from string import ascii_lowercase
import string

text = """
One really nice feature of Python is polymorphism: using the same operation
on different types of objects.
Let's talk about an elegant feature: slicing.
You can use this on a string as well as a list for example
'pybites'[0:2] gives 'py'.
The first value is inclusive and the last one is exclusive so
here we grab indexes 0 and 1, the letter p and y.
When you have a 0 index you can leave it out so can write this as 'pybites'[:2]
but here is the kicker: you can use this on a list too!
['pybites', 'teaches', 'you', 'Python'][-2:] would gives ['you', 'Python']
and now you know about slicing from the end as well :)
keep enjoying our bites!
"""

another_text = """
Take the block of text provided and strip() off the whitespace at the ends.
Split the whole block up by newline (\n).
 if the first character is lowercase, split it into words and add the last word
of that line to the results list.
Strip the trailing dot (.) and exclamation mark (!) from the word first.
finally return the results list!
"""

def slice_and_dice(text=text):
    """Strip the whitespace (newlines) off text at both ends,
       split the text string on newline (\n).
       Next check if the first char of each (stripped) line is lowercase,
       if so split the line into words and append the last word to
       the results list. Make sure that you strip off any trailing
       exclamation marks (!) and dots (.), Return the results list."""
    results = []
    
    text = text.strip()
    text_clean = text.splitlines()

    for line in text_clean:
        line = line.strip()
        chars = list(line)
        letter = str(chars[0])
        if letter in string.ascii_lowercase:
            line = line.strip('!.')
            words = line.split()
            results.extend(words[-1:])
    return(results)

slice_and_dice(text=text)