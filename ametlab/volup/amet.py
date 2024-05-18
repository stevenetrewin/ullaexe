def process_checking(driver):
  # This function checks if the driver process is running and returns True or False
  import psutil # A module for process and system utilities
  for process in psutil.process_iter(): # Iterate over all running processes
    if process.name() == driver: # Check if the process name matches the driver
      return True # Return True if found
  return False # Return False if not found
