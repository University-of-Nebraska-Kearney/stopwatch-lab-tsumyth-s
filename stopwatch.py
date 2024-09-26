
# Importing Libraries
import datetime
SECONDS_PER_HOUR=3600
SECONDS_PER_MINUTE=60

#Sets timer to start
input("Press Enter to start.")
start_time = str(datetime.datetime.now().time()).split(":")
start_hour = start_time[0]
start_minute = start_time[1]
start_second = start_time[2]

#Stops timer by user
input("Press Enter again to stop.")
stop_time = str(datetime.datetime.now().time()).split(":")
stop_hour = stop_time[0]
stop_minute = stop_time[1]
stop_second = stop_time[2]
 
 
#Conversion of hours to seconds
act_stop_hour = int (stop_hour) * SECONDS_PER_HOUR
act_start_hour = int (start_hour) * SECONDS_PER_HOUR

#Conversion of minutes to seconds
act_stop_minute = int(stop_minute) * SECONDS_PER_MINUTE
act_start_minute = int(start_minute) * SECONDS_PER_MINUTE

# Calculating the total seconds
start_time_in_seconds = int(act_start_hour) + int(act_start_minute) + float(start_second)
stop_time_in_seconds = int(act_stop_hour) + int(act_stop_minute) + float(stop_second)
total_seconds = float(stop_time_in_seconds) - float(start_time_in_seconds)

# Turn seconds back to times
end_hour = int(total_seconds) // SECONDS_PER_HOUR
end_hour_in_minutes = end_hour * SECONDS_PER_MINUTE
end_hour_in_seconds = end_hour_in_minutes * SECONDS_PER_MINUTE
end_minute = (int (total_seconds) // SECONDS_PER_MINUTE) - int (end_hour_in_minutes)
end_minute_in_seconds = end_minute * SECONDS_PER_MINUTE
end_second = (float (total_seconds) - float (end_hour_in_seconds) - float (end_minute_in_seconds))

# Get time for end
end_time = (f"{end_hour}:{end_minute}:{end_second: 2f}")

#Displays the final result
print (f"{end_time}")




