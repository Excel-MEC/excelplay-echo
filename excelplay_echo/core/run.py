import judge
import sys

if __name__ == "__main__":
    pid = sys.argv[1]
    fid = "media/"+ sys.argv[2]
    print(judge.run(pid,fid))