# Dictionary of Dictionaries
europe = {'spain':{'capital':'madrid','population':46.77},
          'france':{'capital':'paris','population':66.03},
          'germany':{'capital':'berlin','population':80.62},
          'norway':{'capital':'oslo','population':5.084}
          }

# Print out capital of france
print(europe['france']['capital'])
print("\n")

# Create sub-dictionary data
data = {'capital':'rome','population':59.03}

# Add data to europe under key 'italy'
europe['italy'] = data

# Print Europe
print(europe)
