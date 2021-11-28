def filter(filter_list, filter_output, filter_string, output='off'):
  
  filtered = filter_output

  for junk in filter_list:
    
    if output == 'on':
      print(f'Checking for {junk} !')
    
    if junk in filter_output:
      filtered = filtered.replace(junk, filter_string)
      print(f'Result : Finded  "{junk}" , replacing to  "{filter_string}"  !\n')
      continue
      
    else:
      print(f'Result : Not found  "{junk}"  !\n')
      continue
  
  if output == 'on':
    print(filtered)
