import sys

message = "sunboT219x10y20z1t1000A10.880V12s33"
if len(sys.argv)>1:
    message = sys.argv[1]



def decode(x, message, case_sensitive = False):
    if case_sensitive:
        term = message.split(x)
    else:
        term = message.lower().split(x.lower())
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
    
def decode_all(message):
    results = []
    key = ''
    value = ''
    for c in message:
        if c not in '1234567890.':
            if value != '' and key !='':
                type = 'integer'
                if '.' in value:
                    value = float(value) 
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
            value = float(value)
            type = 'float'
        else:
            value = int(value)
        results.append({ "key":key, "value":value, "type": type})
    return results

results = decode_all(message)

print(f"Decode result of '{message}'")

print('─'*80)
print(f'{"KEY":20}{"VALUE":20}TYPE')
print('─'*80)


for result in results:
    print(f'{result["key"]:20}{str(result["value"]):20}{result["type"]}')





