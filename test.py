import argparse

if __name__ == '__main__':
    args=argparse.ArgumentParser()
    args.add_argument("--name", "-n", default='kunal', type=str)
    args.add_argument("--age","-a",default=21.0, type=float)
    parse_args=args.parse_args()

    print(parse_args.name,parse_args.age)
