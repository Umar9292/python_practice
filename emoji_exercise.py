# message = input('> ')
# words = message.split(' ')
# emoticons = {
#     ':)': '😀',
#     ':(': '🙁'
# }
#
# output = ''
# for word in words:
#     output += emoticons.get(word, word) + ' '
#
# print(output)

# Doing the same thing with a function


def emoji_converter(message):
    words = message.split(' ')
    emoticons = {
        ':)': '😀',
        ':(': '🙁'
    }

    output = ''
    for word in words:
        output += emoticons.get(word, word) + ' '
    return output


message = input('> ')
print(emoji_converter(message))