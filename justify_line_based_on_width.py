def justify_line_based_on_width(para, maxWidth):
    """
    accept a paragraph string and page width as parameters and return an array of left AND right justified strings.
    :param para: The paragraph which needs to be justified.
    :param maxWidth: Maximum page width.
    :return: List with justified lines.
    """
    word_list = para.split()
    result_list, current_line, num_of_letters = [], [], 0
    for word in word_list:
        if num_of_letters + len(word) + len(current_line) > maxWidth:
            for i in range(maxWidth - num_of_letters):
                current_line[i % (len(current_line) - 1 or 1)] += ' '
            result_list.append(''.join(current_line))
            current_line, num_of_letters = [], 0
        current_line += [word]
        num_of_letters += len(word)
    return result_list + [' '.join(current_line).ljust(maxWidth)]


if __name__ == '__main__':
    par = "This is a sample text but a complicated problem to be solved, so we are adding more text to see that it actually works."
    result = justify_line_based_on_width(par, 20)
    print(result)
