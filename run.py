import yaml
import os
import sys

joinpdf_cmd="/System/Library/Automator/Combine\ PDF\ Pages.action/Contents/Resources/join.py"

stream = open("sample.yaml", 'r')
dictionary = list(yaml.load_all(stream))[0]

print('*'*50)
print(dictionary)
print('*'*50)

OUTDIR = dictionary['OUTPUT_DIR']
if not os.path.exists(OUTDIR):
	print(f'Creating OUTPUT Directory: {OUTDIR}')
	os.makedirs(OUTDIR)

for DICT in dictionary['OUTPUTS']:
	out_file = os.path.join(OUTDIR, DICT['OUT_FILE'])
	in_files = DICT['INPUTS']
	for f in in_files:
		if not os.path.exists(f):
			print(f"{f} file is missing. Please check")
			sys.exit()

	cmd_args = [joinpdf_cmd, '--output', out_file, ' '.join(in_files)]
	cmd = ' '.join(cmd_args)
	print(cmd)
	os.system(cmd)