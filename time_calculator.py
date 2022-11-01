
def add_time(start_time, duration, weekday ="none"):

    # first step is to split the strings and save the items to a list to be able to iterate them
    time_list = start_time.split(' ')
    s_time = time_list[0].split(':')
    meridian = time_list[1]
    duration_list = duration.split(':')

    ## print('start time is {}, duration is {} and meridian {}'.format(s_time, duration_list, meridian))

    # second step is to sum the total time as integers
    total_time = [int(x)+int(y) for x, y in zip(s_time, duration_list)]
    ## print('total time is {}'.format(total_time))

    # third step is to format the minutes to transfrom into hours after crossing 60

    if total_time[1] > 60:
        add_hours = (total_time[1] // 60)
        total_time[1] = total_time[1] - ((total_time[1]//60) * 60)
        ## print('hours to add {}'.format(add_hours))
        total_time[0] = total_time[0] + add_hours # adding hours to total time

    # fourth step is calculate the hours
    total_hours = total_time[0]
    if total_time[0] > 12:
        total_time[0] = total_time[0] - ((total_time[0]//12) * 12)

    if total_time[0] == 0:
        total_time[0] = 12

    # fifth step is to format all list items to a string to add a 0 in front of ints from 1 to 9

    if total_time[1] < 10:
        total_time[1] = str('0{}'.format(total_time[1]))
    else:
        total_time[1] = str(total_time[1])

    total_time[0] = str(total_time[0])

    ##print('meridian time is {}'.format(total_time))



    # defining the right meridian

    half_days = total_hours // 12
    half_day_modulus = half_days % 2


    if half_days == 0:
        total_time.append(meridian)
    elif half_days > 0 and half_day_modulus == 1 and meridian == "AM":
        final_meridian = "PM"
        total_time.append(final_meridian)
    elif half_days > 0 and half_day_modulus == 0 and meridian == "AM":
        final_meridian = "AM"
        total_time.append(final_meridian)
    elif half_days > 0 and half_day_modulus == 1 and meridian == "PM":
        final_meridian = "AM"
        total_time.append(final_meridian)
    elif half_days > 0 and half_day_modulus == 0 and meridian == "PM":
        final_meridian = "PM"
        total_time.append(final_meridian)

    # calculating days later

    total_days = total_hours // 24  # calculating total days to check modulus
    ## print('total hours {} and total days {}'.format(total_hours, total_days))

    if meridian == 'PM' and 12 < total_hours < 25:
        total_time.append('next day')
    elif meridian == 'PM' and total_hours > 24:
        total_time.append('({} days later)'.format(total_days + 1))
    elif meridian == 'AM' and 24 < total_hours < 48:
        total_time.append('next day')
    elif meridian == 'AM' and total_hours > 48:
        total_time.append('({} days later)'.format(total_days))

    # dealing with weekday

    if meridian == "PM" and half_days > 0:
        total_days = total_days + 1

    day_definition = 0

    if weekday == 'Monday':
        day_definition = (total_days + 1) % 8
    elif weekday == 'Tuesday':
        day_definition = (total_days + 2) % 8
    elif weekday == 'Wednesday':
        day_definition = (total_days + 3) % 8
    elif weekday == 'Thursday':
        day_definition = (total_days + 4) % 8
    elif weekday == 'Friday':
        day_definition = (total_days + 5) % 8
    elif weekday == 'Saturday':
        day_definition = (total_days + 6) % 8
    elif weekday == 'Sunday':
        day_definition = (total_days + 7) % 8

    if day_definition == 1:
        total_time.append('Monday')
    elif day_definition == 2:
        total_time.append('Tuesday')
    elif day_definition == 3:
        total_time.append('Wednesday')
    elif day_definition == 4:
        total_time.append('Thursday')
    elif day_definition == 5:
        total_time.append('Friday')
    elif day_definition == 6:
        total_time.append('Saturday')
    elif day_definition == 7:
        total_time.append('Sunday')


    ## print('{} \n'.format(total_time))

    new_time = ''
    if len(total_time) == 3:
        new_time = "{}:{} {}".format(total_time[0], total_time[1], total_time[2])
    elif len(total_time) == 4:
        new_time = "{}:{} {} {}".format(total_time[0], total_time[1], total_time[2], total_time[3])

    return new_time


add_time("3:00 PM", "3:10")
# Returns: 6:10 PM

add_time("11:30 AM", "2:32", "Monday")
# Returns: 2:02 PM, Monday

add_time("11:43 AM", "00:20")
# Returns: 12:03 PM

add_time("10:10 PM", "3:30")
# Returns: 1:40 AM (next day)

add_time("11:43 PM", "24:20", "Tuesday")
# Returns: 12:03 AM, Thursday (2 days later)

add_time("6:30 PM", "205:12")
# Returns: 7:42 AM (9 days later)
