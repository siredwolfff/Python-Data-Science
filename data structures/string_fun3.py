from data import story

print(f"total char in the story: {len(story)}")
words= story.split()
print(f"total words in the story: {len(words)}")


print(f'total unique words in the story: {len(set(words))}')
print(words)

sentences= story.split('.')
print(f'total sentences in the story: {len(sentences)}')
print(sentences)

lines= story.split('/n')
print(f'total lines in the story: {len(lines)}')
print(lines)

poem_list= [
    'Twinkle, twinkle, little star,',
    'How I wonder what you are,',
    'Up above the words so high,',
    'Like a diamomnd in the sky,',
    
]
poem= "\n". join(poem_list)
print(poem)
