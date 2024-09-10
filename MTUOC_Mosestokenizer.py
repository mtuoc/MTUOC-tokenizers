from sacremoses import MosesTokenizer, MosesDetokenizer
import sys

def print_help():
    print("MTUOC_Mosestokenizer.py A tokenizer for using Moses, usage:")
    print("Tokenization:")
    print("   python3 MTUOC_Mosestokenizer.py en < text.txt")
    print("   cat text.txt | python3 MTUOC_Mosestokenizer.py en")
    print("Deokenization:")
    print("   python3 MTUOC_Mosestokenizer.py en detokenize < text.txt")
    print("   cat text.txt | python3 MTUOC_Mosestokenizer.py en detokenize")
    
        

if __name__ == "__main__":
    if len(sys.argv)<2:
        print_help()
        sys.exit()
    elif sys.argv[1]=="-h" or sys.argv[1]=="--help":
            print_help()
            sys.exit()
        
    else:
        lang=sys.argv[1]
        if len(sys.argv)==2: action="tokenize"
        elif sys.argv[2]=="tokenize": action="tokenize"
        elif sys.argv[2]=="detokenize": action="detokenize"
        if action=="tokenize":
            tokenizer= MosesTokenizer(lang=lang)
            for line in sys.stdin:
                line=line.rstrip()
                print(line)
                outsegment=" ".join(tokenizer.tokenize(line))
                print(outsegment)
        if action=="tokenize":
            tokenizer= MosesTokenizer(lang=lang)
            for line in sys.stdin:
                line=line.rstrip()
                outsegment=" ".join(tokenizer.tokenize(line))
                print(outsegment)
        elif action=="detokenize":
            detokenizer= MosesDetokenizer(lang=lang)
            for line in sys.stdin:
                line=line.rstrip()
                outsegment=detokenizer.detokenize(line.split())
                print(outsegment)

