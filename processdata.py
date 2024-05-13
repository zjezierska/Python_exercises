def process_data(s):
  new_list = []
  
  for dict in s:
    new_dict = {}
    new_dict["name"] = dict["name"]
    new_dict["average_score"] = Average(dict["scores"])
    new_dict["is_adult"] = dict["age"] >= 18

    new_list.append(new_dict)

return new_list
  

def Average(lst): 
    return sum(lst) / len(lst) 
  
