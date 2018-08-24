import os,subprocess,filecmp

# logger added
import logging
logging.basicConfig(filename='example.log',level=logging.DEBUG)


class Judge:

	def __init__(self,cwd):
		self.cwd=cwd
		# change directory
		os.chdir(self.cwd)
		self.timelimit = 1

	def compile(self,pid,fid,cwd):
		"""
		bash ./filename.sh
		if possible change file permissions
		add #!/bin/bash at beginning
		AC = accept compilation
		FC = failed compilation
		"""
		with open(self.cwd+"/tmp/err.txt",'w') as err:
			# cmd = self.cwd.replace("[filename]",fid)
			t = subprocess.run(["chmod 700 (fid).sh"],shell=True)
			logging.error(t)
			t.communicate()
			response = t.returncode
			t.kill()
			if (response==0):
				return "AC"
			else:
				return "FC"


	def execute(self,pid,fid):
		"""
		Functionaliy : execute shell script and
		delivery and execute script
		"""

		with open(self	.cwd + "/env/testcases/"+str(pid)+".txt","r") as input:
			with open(self.cwd+"/tmp/temp.txt",'w') as output :
				process=subprocess.Popen(['./(fid).sh'],preexec_fn=os.setsid,cwd=os.getcwd(),stdin=input,stdout=output)
				try:
					process.communicate(timeout=self.timelimit)
				except subprocess.TimeoutExpired:
					t = 125
				if t==125:
					return "ES"



	def validate(self,pid):
		#"test input and out"
		if filecmp.cmp(self.cwd+"/tmp/output.txt",self.cwd+"/env/key/key"+str(pid)+".txt"==True):
			return "AC"
		else:
			return "WA"

def run(pid,filename):
	cwd = os.getcwd()
	logging.info(cwd)

	fid = os.path.splitext(filename)[0]
	logging.info(fid)
	ext = os.path.splitext(filename)[1]
	obj = Judge(cwd)
	ccf = obj.compile(pid,fid,cwd)
	# if ccf != "CS":
	# 	return ccf
	# ex = obj.execute(pid,fid)
	# if ex != "ES":
	# 	return ex
	# response = obj.validate(pid)
	# return(response)

if __name__ == "__main__":
	run(1,'rshell.sh')
