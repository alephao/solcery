import sys
import common
import errors

def main(args):
  if len(args) < 3:
    print("Usage: solcery errgen <output_path> [<path_to_file_containing_error>]")
    return

  output_path = args[1]
  
  all_errors = set([])
  for path in args[2:]:
    errs = common.errors_on_file(path)
    all_errors = all_errors.union(set(errs))

  all_errors = list(map(common.error_sig_to_obj, all_errors))
  
  contents = errors.gen_file_contents(all_errors)

  file = open(output_path, mode='w')
  file.write(contents)  
  file.close()

if __name__=="__main__":
  main(sys.argv)
