import sys
import decode

message = "sunboT219x10y20z1t1000A10.880V12s33"
if len(sys.argv)>1:
    message = sys.argv[1]

results = decode.word_by_word(message)
print(f"Decode result of '{message}'")
decode.print_results(results)
