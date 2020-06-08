#!/bin/python3
import os, glob
from latex import build_pdf, LatexBuildError
import watcher


def build_resume(file_name_glob='*.tex'):
  for file_name in glob.glob(file_name_glob):
    print('compiling {}'.format(file_name))
    compile_tex(file_name);


def compile_tex(tex_filename):
  base_filename = tex_filename.split('.tex')[0]
  pdf_filename = '{}{}'.format(base_filename, '.pdf')

  current_dir = os.path.abspath(os.path.dirname(__file__))

  with open(tex_filename) as tex_file:
    try:
      pdf = build_pdf(tex_file, texinputs=[current_dir, ''])
      pdf.save_to(pdf_filename)

    except LatexBuildError as e:
      for err in e.get_errors():
        print(u'Error in {0[filename]}, line {0[line]}: {0[error]}'.format(err))
        # also print one line of context
        print(u'    {}\n'.format(err['context'][1]))


def compile_resume_watcher_callback(event_type, file_path):
  if '.tex' in file_path:
    build_resume(file_path)


if __name__ == '__main__':
  watcher_instance = watcher.Watcher(compile_resume_watcher_callback)
  watcher_instance.run()
