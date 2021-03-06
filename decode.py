def given_word(x, word, case_sensitive = False):
    if case_sensitive:
        term = word.split(x)
    else:
        term = word.lower().split(x.lower())
    result = ''
    valid = ''
    if len(term)<2:
        return 0

    valid = term[1]
    if len(term)>2:
        for t in term:
            if t != '' and t[-1] in '1234567890':
                valid = t

    for c in valid:
        if c in '1234567890.':
            result = result + c
        else:
            break
    if len(result) == 0:
        return 0
    if '.' in result:
        return float(result)
    return int(result)
    

def word_by_word(message):
    results = []
    key = ''
    value = ''
    for c in message:
        if c not in '1234567890.':
            if value != '' and key !='':
                type = 'integer'
                if '.' in value:
                    try:
                        value = float(value)
                    except:
                        value = 0.0
                    type = 'float'
                else:
                    value = int(value)
                results.append({ "key":key, "value":value, "type": type})
                value = ''
                key = ''
            key = key + c
        else:
            if key == '':
                value = c
            else:
                value += c
    if key !='':
        type = 'integer'
        if value =='':
            value = 0
        elif '.' in value:
            try:
                value = float(value)
            except:
                value = 0.0
            type = 'float'
        else:
            value = int(value)
        results.append({ "key":key, "value":value, "type": type})
    return results


def print_results(results):
    print('─'*80)
    print(f'{"KEY":20}{"VALUE":20}TYPE')
    print('─'*80)

    for result in results:
        print(f'{result["key"]:20}{str(result["value"]):20}{result["type"]}')


if __name__ == "__main__":
    message = input("Input a string to decode:")
    decoded = word_by_word(message)
    print_results(decoded)


