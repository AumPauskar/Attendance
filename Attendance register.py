#Attendance register


from tkinter import *
import time
import psutil
#importing modules


size='640x480'
label_time_font=('Calibri', 20)
label_date_font=('Calibri', 14)
multiplicate=75
button_width=15
button_height=2
button_borderwidth=2


#active or inactive
confirm_status='active'
save_status='active'


colour_white='#ffffff'
colour_black='#000000'
colour_red='#ff0000'
colour_blue='#1500ff'
colour_green='#00ff08'
colour_yellow='#ffff00'
colour_pale_pink='#ffa6cb'
colour_pale_blue='#a4f5eb'
colour_pale_yellow='#feffa8'
colour_blood_red='#bd190d'
colour_pale_violet='#805fa1'
colour_pale_green='#98ff8c'
colour_deep_blue='#2a3596'
colour_pale_silver='#f0f0f0'
colour_mango_green='#10913b'
colour_orange='#cf6311'
colour_=''
colour_=''
colour_=''
colour_=''
colour_=''
colour_=''
colour_=''
colour_=''
colour_=''
colour_=''


candidate1_status='idk'
candidate2_status='idk'
candidate3_status='idk'
candidate4_status='idk'
candidate5_status='idk'
candidate6_status='idk'
candidate7_status='idk'
candidate8_status='idk'
candidate9_status='idk'
candidate10_status='idk'
candidate11_status='idk'
candidate12_status='idk'
candidate13_status='idk'
candidate14_status='idk'
candidate15_status='idk'
candidate16_status='idk'
candidate17_status='idk'
candidate18_status='idk'
candidate19_status='idk'
candidate20_status='idk'
candidate21_status='idk'
candidate22_status='idk'
candidate23_status='idk'
candidate24_status='idk'
candidate25_status='idk'






root=Tk()
root.title('Attendence')
root.geometry(size)



canvas1=Canvas(root)
canvas1.pack()

canvas2=Canvas(root)
canvas2.pack()

canvas3=Canvas(root)
canvas3.pack()

canvas4=Canvas(root)
canvas4.pack()

canvas5=Canvas(root)
canvas5.pack()

canvas6=Canvas(root)
canvas6.pack()



def nocommand():
	pass
'''
candidate=Button(canvas2, text='Candidate', width=button_width, height=button_height, borderwidth=button_borderwidth, command=nocommand)
candidate.grid(row=, column=)
'''



def update_time():
    global curtime
    global curdate

    hour=str(time.strftime('%I'))
    minute=str(time.strftime('%M'))
    second=str(time.strftime('%S'))
    am_pm=str(time.strftime('%p'))
    day=str(time.strftime('%d'))
    month=str(time.strftime('%m'))
    year=str(time.strftime('%y'))
    yearC=str(time.strftime('%Y'))
    day_of_week=str(time.strftime('%a'))
    hour24=time.strftime('%H')
    battery_percentage=psutil.sensors_battery()
    battery_percentage_int=str(battery_percentage.percent)
    curtime=hour+':'+minute+':'+second+' '+am_pm
    curdate=day+'/'+month+'/'+yearC+' '+day_of_week

    if 7<=int(hour24)<=17: #day mode

        plugged=battery_percentage.power_plugged
        plugged='Charging' if plugged else 'Battery'


        if plugged=='Charging' and battery_percentage_int=='100':
            plugged='Charged'

        else:
            pass


        if plugged=='Charged':
            label_time.config(bg='silver', fg='black') #background colour pale blue
            label_time.config(text=multiplicate*' '+hour+':'+minute+' '+am_pm+multiplicate*' ')
            label_date.config(bg='silver', fg='black')

        else:

            if plugged=='Charging':
                label_time.config(bg='#9effb3', fg='black')
                label_date.config(bg='#9effb3', fg='black') #background colour pale green

            elif plugged=='Battery' and int(battery_percentage_int)>50:
                label_time.config(bg='#fff99e', fg='black')
                label_date.config(bg='#fff99e', fg='black') #background colour pale yellow

            elif plugged=='Battery' and 34<=int(battery_percentage_int)<=50:
                label_time.config(bg='#ffb3b3', fg='colour_black')
                label_date.config(bg='#ffb3b3', fg='colour_black') #background colour pale red

            elif plugged=='Battery' and int(battery_percentage_int)<=33:
                label_time.config(bg='red', fg='white')
                label_date.config(bg='red', fg='white') #blood red to indicate battery sooooon ill die

            else:
                label_time.config(bg='silver',fg='colour_black')
                label_date.config(bg='silver',fg='colour_black') #background colour silver

            label_time.config(text=multiplicate*' '+hour+':'+minute+' '+am_pm+4*' '+battery_percentage_int+'%'+multiplicate*' ')



    elif 18<=int(hour24)<=23 or 0<=int(hour24)<=6: #night mode

        plugged=battery_percentage.power_plugged
        plugged='Charging' if plugged else 'Battery'


        if plugged=='Charging' and battery_percentage_int=='100':
            plugged='Charged'

        else:
            pass


        if plugged=='Charged':
            label_time.config(bg=colour_black, fg=colour_pale_silver) #background colour silver
            label_time.config(text=multiplicate*' '+hour+':'+minute+' '+am_pm+multiplicate*' ')
            label_date.config(bg=colour_black, fg=colour_pale_silver)

        else:

            if plugged=='Charging':
                label_time.config(bg=colour_black, fg=pale_green)
                label_date.config(bg=colour_black, fg=pale_green) #background colour pale green

            elif plugged=='Battery' and int(battery_percentage_int)>50:
                label_time.config(bg=colour_black, fg=pale_yellow)
                label_date.config(bg=colour_black, fg=pale_yellow) #background colour pale yellow

            elif plugged=='Battery' and 34<=int(battery_percentage_int)<=50:
                label_time.config(bg=colour_black, fg=pale_red)
                label_date.config(bg=colour_black, fg=pale_red) #background colour pale red

            elif plugged=='Battery' and int(battery_percentage_int)<=33:
                label_time.config(bg=colour_black, fg=red)
                label_date.config(bg=colour_black, fg=red) #blood red to indicate battery sooooon ill die

            else:
                label_time.config(bg=colour_black,fg=colour_pale_silver)
                label_date.config(bg=colour_black,fg=colour_pale_silver) #background colour silver

            label_time.config(text=multiplicate*' '+hour+':'+minute+' '+am_pm+4*' '+battery_percentage_int+'%'+multiplicate*' ')


    label_date.config(text=multiplicate*' '+day+'/'+month+'/'+year+' '+day_of_week+multiplicate*' ')
    label_time.after(1000, update_time)






def Candidate1():
	global candidate1_status
	candidate1_status='present'
	candidate1.config(bg=colour_deep_blue, fg=colour_white)

def Candidate2():
	global candidate2_status
	candidate2_status='present'
	candidate2.config(bg=colour_deep_blue, fg=colour_white)

def Candidate3():
	global candidate3_status
	candidate3_status='present'
	candidate3.config(bg=colour_deep_blue, fg=colour_white)

def Candidate4():
	global candidate4_status
	candidate4_status='present'
	candidate4.config(bg=colour_deep_blue, fg=colour_white)

def Candidate5():
	global candidate5_status
	candidate5_status='present'
	candidate5.config(bg=colour_deep_blue, fg=colour_white)

def Candidate6():
	global candidate6_status
	candidate6_status='present'
	candidate6.config(bg=colour_deep_blue, fg=colour_white)

def Candidate7():
	global candidate7_status
	candidate7_status='present'
	candidate7.config(bg=colour_deep_blue, fg=colour_white)

def Candidate8():
	global candidate8_status
	candidate8_status='present'
	candidate8.config(bg=colour_deep_blue, fg=colour_white)

def Candidate9():
	global candidate9_status
	candidate9_status='present'
	candidate9.config(bg=colour_deep_blue, fg=colour_white)

def Candidate10():
	global candidate10_status
	candidate10_status='present'
	candidate10.config(bg=colour_deep_blue, fg=colour_white)

def Candidate11():
	global candidate11_status
	candidate11_status='present'
	candidate11.config(bg=colour_deep_blue, fg=colour_white)

def Candidate12():
	global candidate12_status
	candidate12_status='present'
	candidate12.config(bg=colour_deep_blue, fg=colour_white)

def Candidate13():
	global candidate13_status
	candidate13_status='present'
	candidate13.config(bg=colour_deep_blue, fg=colour_white)

def Candidate14():
	global candidate14_status
	candidate14_status='present'
	candidate14.config(bg=colour_deep_blue, fg=colour_white)

def Candidate15():
	global candidate15_status
	candidate15_status='present'
	candidate15.config(bg=colour_deep_blue, fg=colour_white)

def Candidate16():
	global candidate16_status
	candidate16_status='present'
	candidate16.config(bg=colour_deep_blue, fg=colour_white)

def Candidate17():
	global candidate17_status
	candidate17_status='present'
	candidate17.config(bg=colour_deep_blue, fg=colour_white)

def Candidate18():
	global candidate18_status
	candidate18_status='present'
	candidate18.config(bg=colour_deep_blue, fg=colour_white)

def Candidate19():
	global candidate19_status
	candidate19_status='present'
	candidate19.config(bg=colour_deep_blue, fg=colour_white)

def Candidate20():
	global candidate20_status
	candidate20_status='present'
	candidate20.config(bg=colour_deep_blue, fg=colour_white)

def Candidate21():
	global candidate21_status
	candidate21_status='present'
	candidate21.config(bg=colour_deep_blue, fg=colour_white)

def Candidate22():
	global candidate22_status
	candidate22_status='present'
	candidate22.config(bg=colour_deep_blue, fg=colour_white)

def Candidate23():
	global candidate23_status
	candidate23_status='present'
	candidate23.config(bg=colour_deep_blue, fg=colour_white)

def Candidate24():
	global candidate24_status
	candidate24_status='present'
	candidate24.config(bg=colour_deep_blue, fg=colour_white)

def Candidate25():
	global candidate25_status
	candidate25_status='present'
	candidate25.config(bg=colour_deep_blue, fg=colour_white)


















def Confirm():
	global confirm_status

	if confirm_status=='active':
		button_yes_confirm.grid(row=1, column=1)
		button_no_confirm.grid(row=1, column=2)
		confirm_status='inactive'

	elif confirm_status=='inactive':
		pass



def YesConfirm():
	global confirm_status

	if candidate1_status=='idk':
		candidate1.config(bg=colour_blood_red, fg=colour_white)
	else:
		candidate1.config(bg=colour_deep_blue, fg=colour_white)


	if candidate2_status=='idk':
		candidate2.config(bg=colour_blood_red, fg=colour_white)
	else:
		candidate2.config(bg=colour_deep_blue, fg=colour_white)


	if candidate3_status=='idk':
		candidate3.config(bg=colour_blood_red, fg=colour_white)
	else:
		candidate3.config(bg=colour_deep_blue, fg=colour_white)


	if candidate4_status=='idk':
		candidate4.config(bg=colour_blood_red, fg=colour_white)
	else:
		candidate4.config(bg=colour_deep_blue, fg=colour_white)


	if candidate5_status=='idk':
		candidate5.config(bg=colour_blood_red, fg=colour_white)
	else:
		candidate5.config(bg=colour_deep_blue, fg=colour_white)


	if candidate6_status=='idk':
		candidate6.config(bg=colour_blood_red, fg=colour_white)
	else:
		candidate6.config(bg=colour_deep_blue, fg=colour_white)


	if candidate7_status=='idk':
		candidate7.config(bg=colour_blood_red, fg=colour_white)
	else:
		candidate7.config(bg=colour_deep_blue, fg=colour_white)


	if candidate8_status=='idk':
		candidate8.config(bg=colour_blood_red, fg=colour_white)
	else:
		candidate8.config(bg=colour_deep_blue, fg=colour_white)


	if candidate9_status=='idk':
		candidate9.config(bg=colour_blood_red, fg=colour_white)
	else:
		candidate9.config(bg=colour_deep_blue, fg=colour_white)


	if candidate10_status=='idk':
		candidate10.config(bg=colour_blood_red, fg=colour_white)
	else:
		candidate10.config(bg=colour_deep_blue, fg=colour_white)


	if candidate11_status=='idk':
		candidate11.config(bg=colour_blood_red, fg=colour_white)
	else:
		candidate11.config(bg=colour_deep_blue, fg=colour_white)


	if candidate12_status=='idk':
		candidate12.config(bg=colour_blood_red, fg=colour_white)
	else:
		candidate12.config(bg=colour_deep_blue, fg=colour_white)


	if candidate13_status=='idk':
		candidate13.config(bg=colour_blood_red, fg=colour_white)
	else:
		candidate13.config(bg=colour_deep_blue, fg=colour_white)


	if candidate14_status=='idk':
		candidate14.config(bg=colour_blood_red, fg=colour_white)
	else:
		candidate14.config(bg=colour_deep_blue, fg=colour_white)


	if candidate15_status=='idk':
		candidate15.config(bg=colour_blood_red, fg=colour_white)
	else:
		candidate15.config(bg=colour_deep_blue, fg=colour_white)


	if candidate16_status=='idk':
		candidate16.config(bg=colour_blood_red, fg=colour_white)
	else:
		candidate16.config(bg=colour_deep_blue, fg=colour_white)


	if candidate17_status=='idk':
		candidate17.config(bg=colour_blood_red, fg=colour_white)
	else:
		candidate17.config(bg=colour_deep_blue, fg=colour_white)


	if candidate18_status=='idk':
		candidate18.config(bg=colour_blood_red, fg=colour_white)
	else:
		candidate18.config(bg=colour_deep_blue, fg=colour_white)


	if candidate19_status=='idk':
		candidate19.config(bg=colour_blood_red, fg=colour_white)
	else:
		candidate19.config(bg=colour_deep_blue, fg=colour_white)


	if candidate20_status=='idk':
		candidate20.config(bg=colour_blood_red, fg=colour_white)
	else:
		candidate20.config(bg=colour_deep_blue, fg=colour_white)


	if candidate21_status=='idk':
		candidate21.config(bg=colour_blood_red, fg=colour_white)
	else:
		candidate21.config(bg=colour_deep_blue, fg=colour_white)


	if candidate22_status=='idk':
		candidate22.config(bg=colour_blood_red, fg=colour_white)
	else:
		candidate22.config(bg=colour_deep_blue, fg=colour_white)


	if candidate23_status=='idk':
		candidate23.config(bg=colour_blood_red, fg=colour_white)
	else:
		candidate23.config(bg=colour_deep_blue, fg=colour_white)


	if candidate24_status=='idk':
		candidate24.config(bg=colour_blood_red, fg=colour_white)
	else:
		candidate24.config(bg=colour_deep_blue, fg=colour_white)


	if candidate25_status=='idk':
		candidate25.config(bg=colour_blood_red, fg=colour_white)
	else:
		candidate25.config(bg=colour_deep_blue, fg=colour_white)


	button_yes_confirm.grid_forget()
	button_no_confirm.grid_forget()
	button_confirm.grid_forget()
	button_save.grid(row=1, column=1, pady=10)
	button_clear.grid(row=1, column=2, pady=10)
	confirm_status='active'


def NoConfirm():
	global confirm_status
	button_yes_confirm.grid_forget()
	button_no_confirm.grid_forget()
	confirm_status='active'


def Clear():
	button_yes_clear.grid(row=1, column=1)
	button_no_clear.grid(row=1, column=2)


def YesClear():
	candidate1.config(bg=colour_pale_silver, fg=colour_black)
	candidate2.config(bg=colour_pale_silver, fg=colour_black)
	candidate3.config(bg=colour_pale_silver, fg=colour_black)
	candidate4.config(bg=colour_pale_silver, fg=colour_black)
	candidate5.config(bg=colour_pale_silver, fg=colour_black)
	candidate6.config(bg=colour_pale_silver, fg=colour_black)
	candidate7.config(bg=colour_pale_silver, fg=colour_black)
	candidate8.config(bg=colour_pale_silver, fg=colour_black)
	candidate9.config(bg=colour_pale_silver, fg=colour_black)
	candidate10.config(bg=colour_pale_silver, fg=colour_black)
	candidate11.config(bg=colour_pale_silver, fg=colour_black)
	candidate12.config(bg=colour_pale_silver, fg=colour_black)
	candidate13.config(bg=colour_pale_silver, fg=colour_black)
	candidate14.config(bg=colour_pale_silver, fg=colour_black)
	candidate15.config(bg=colour_pale_silver, fg=colour_black)
	candidate16.config(bg=colour_pale_silver, fg=colour_black)
	candidate17.config(bg=colour_pale_silver, fg=colour_black)
	candidate18.config(bg=colour_pale_silver, fg=colour_black)
	candidate19.config(bg=colour_pale_silver, fg=colour_black)
	candidate20.config(bg=colour_pale_silver, fg=colour_black)
	candidate21.config(bg=colour_pale_silver, fg=colour_black)
	candidate22.config(bg=colour_pale_silver, fg=colour_black)
	candidate23.config(bg=colour_pale_silver, fg=colour_black)
	candidate24.config(bg=colour_pale_silver, fg=colour_black)
	candidate25.config(bg=colour_pale_silver, fg=colour_black)
	button_yes_clear.grid_forget()
	button_no_clear.grid_forget()
	button_save.grid_forget()
	button_clear.grid_forget()
	button_confirm.grid(row=1, column=1, pady=10)

	global candidate1_status
	candidate1_status='idk'

	global candidate2_status
	candidate2_status='idk'

	global candidate3_status
	candidate3_status='idk'

	global candidate4_status
	candidate4_status='idk'

	global candidate5_status
	candidate5_status='idk'

	global candidate6_status
	candidate6_status='idk'

	global candidate7_status
	candidate7_status='idk'

	global candidate8_status
	candidate8_status='idk'

	global candidate9_status
	candidate9_status='idk'

	global candidate10_status
	candidate10_status='idk'

	global candidate11_status
	candidate11_status='idk'

	global candidate12_status
	candidate12_status='idk'

	global candidate13_status
	candidate13_status='idk'

	global candidate14_status
	candidate14_status='idk'

	global candidate15_status
	candidate15_status='idk'

	global candidate16_status
	candidate16_status='idk'

	global candidate17_status
	candidate17_status='idk'

	global candidate18_status
	candidate18_status='idk'

	global candidate19_status
	candidate19_status='idk'

	global candidate20_status
	candidate20_status='idk'



def NoClear():
	button_yes_clear.grid_forget()
	button_no_clear.grid_forget()

def Save():
	global save_status

	if save_status=='active':
		button_yes_save.grid(row=1, column=1)
		button_no_save.grid(row=1, column=2)
		save_status='inactive'

	elif save_status=='inactive':
		pass
		

def YesSave():
	#file handling must go on here
	global save_status
	button_yes_save.grid_forget()
	button_no_save.grid_forget()
	button_done.pack()


	file=open('Record.txt', 'a')
	var_present=''
	var_absent=''
	present_count=0
	absent_count=0


	if candidate1_status=='present':
		var_present+=('Candidate1'+', ')
		present_count+=1

	if candidate2_status=='present':
		var_present+=('Candidate2'+', ')
		present_count+=1

	if candidate3_status=='present':
		var_present+=('Candidate3'+', ')
		present_count+=1

	if candidate4_status=='present':
		var_present+=('Candidate4'+', ')
		present_count+=1

	if candidate5_status=='present':
		var_present+=('Candidate5'+', ')
		present_count+=1

	if candidate6_status=='present':
		var_present+=('Candidate6'+', ')
		present_count+=1

	if candidate7_status=='present':
		var_present+=('Candidate7'+', ')
		present_count+=1

	if candidate8_status=='present':
		var_present+=('Candidate8'+', ')
		present_count+=1

	if candidate9_status=='present':
		var_present+=('Candidate9'+', ')
		present_count+=1

	if candidate10_status=='present':
		var_present+=('Candidate10'+', ')
		present_count+=1

	if candidate11_status=='present':
		var_present+=('Candidate11'+', ')
		present_count+=1

	if candidate12_status=='present':
		var_present+=('Candidate12'+', ')
		present_count+=1

	if candidate13_status=='present':
		var_present+=('Candidate13'+', ')
		present_count+=1

	if candidate14_status=='present':
		var_present+=('Candidate14'+', ')
		present_count+=1

	if candidate15_status=='present':
		var_present+=('Candidate15'+', ')
		present_count+=1

	if candidate16_status=='present':
		var_present+=('Candidate16'+', ')
		present_count+=1

	if candidate17_status=='present':
		var_present+=('Candidate17'+', ')
		present_count+=1

	if candidate18_status=='present':
		var_present+=('Candidate18'+', ')
		present_count+=1

	if candidate19_status=='present':
		var_present+=('Candidate19'+', ')
		present_count+=1

	if candidate20_status=='present':
		var_present+=('Candidate20'+', ')
		present_count+=1

	if candidate21_status=='present':
		var_present+=('Candidate21'+', ')
		present_count+=1

	if candidate22_status=='present':
		var_present+=('Candidate22'+', ')
		present_count+=1

	if candidate23_status=='present':
		var_present+=('Candidate23'+', ')
		present_count+=1

	if candidate24_status=='present':
		var_present+=('Candidate24'+', ')
		present_count+=1

	if candidate25_status=='present':
		var_present+=('Candidate25'+', ')
		present_count+=1


	temp1=''
	for a in range((0), (len(var_present)-2)):
		temp1+=var_present[a]
	var_present=temp1
	temp1=''



	if candidate1_status=='idk':
		var_absent+=('Candidate1'+', ')
		absent_count+=1

	if candidate2_status=='idk':
		var_absent+=('Candidate2'+', ')
		absent_count+=1

	if candidate3_status=='idk':
		var_absent+=('Candidate3'+', ')
		absent_count+=1

	if candidate4_status=='idk':
		var_absent+=('Candidate4'+', ')
		absent_count+=1

	if candidate5_status=='idk':
		var_absent+=('Candidate5'+', ')
		absent_count+=1

	if candidate6_status=='idk':
		var_absent+=('Candidate6'+', ')
		absent_count+=1

	if candidate7_status=='idk':
		var_absent+=('Candidate7'+', ')
		absent_count+=1

	if candidate8_status=='idk':
		var_absent+=('Candidate8'+', ')
		absent_count+=1

	if candidate9_status=='idk':
		var_absent+=('Candidate9'+', ')
		absent_count+=1

	if candidate10_status=='idk':
		var_absent+=('Candidate10'+', ')
		absent_count+=1

	if candidate11_status=='idk':
		var_absent+=('Candidate11'+', ')
		absent_count+=1

	if candidate12_status=='idk':
		var_absent+=('Candidate12'+', ')
		absent_count+=1

	if candidate13_status=='idk':
		var_absent+=('Candidate13'+', ')
		absent_count+=1

	if candidate14_status=='idk':
		var_absent+=('Candidate14'+', ')
		absent_count+=1

	if candidate15_status=='idk':
		var_absent+=('Candidate15'+', ')
		absent_count+=1

	if candidate16_status=='idk':
		var_absent+=('Candidate16'+', ')
		absent_count+=1

	if candidate17_status=='idk':
		var_absent+=('Candidate17'+', ')
		absent_count+=1

	if candidate18_status=='idk':
		var_absent+=('Candidate18'+', ')
		absent_count+=1

	if candidate19_status=='idk':
		var_absent+=('Candidate19'+', ')
		absent_count+=1

	if candidate20_status=='idk':
		var_absent+=('Candidate20'+', ')
		absent_count+=1

	if candidate21_status=='idk':
		var_absent+=('Candidate21'+', ')
		absent_count+=1

	if candidate22_status=='idk':
		var_absent+=('Candidate22'+', ')
		absent_count+=1

	if candidate23_status=='idk':
		var_absent+=('Candidate23'+', ')
		absent_count+=1

	if candidate24_status=='idk':
		var_absent+=('Candidate24'+', ')
		absent_count+=1

	if candidate25_status=='idk':
		var_absent+=('Candidate25'+', ')
		absent_count+=1


	temp2=''
	for b in range((0), (len(var_absent)-2)):
		temp2+=var_absent[b]
	var_absent=temp2
	temp2=''


	global curtime
	global curdate

	file.write('\n'+40*('-')+'\n')
	file.write('Attendance taken on: '+curdate+'\n')
	file.write('At: '+curtime+'\n\n')
	file.write('Present: '+var_present+'\n')
	file.write('Total Present: '+str(present_count)+'\n\n')
	file.write('Absent: '+var_absent+'\n')
	file.write('Total Absent: '+str(absent_count)+'\n\n')
	file.write('Total Students: '+str(present_count+absent_count)+'\n\n'+40*('-'))

	save_label.config(text='Attendence has been recorded')
	save_status='active'


def NoSave():
	global save_status
	button_yes_save.grid_forget()
	button_no_save.grid_forget()
	save_status='active'


def Done():
	save_label.config(text='')
	button_done.pack_forget()
	button_save.grid_forget()








#--------------------------------------------------------------------------------------
label_time=Label(canvas1, text='', font=label_time_font)
label_time.pack()

label_date=Label(canvas1, text='', font=label_date_font)
label_date.pack()


save_label=Label(canvas5, text='')
save_label.pack()





candidate1=Button(canvas2, text='Candidate 1', width=button_width, height=button_height, borderwidth=button_borderwidth, command=Candidate1, bg=colour_pale_silver)
candidate1.grid(row=1, column=1)

candidate2=Button(canvas2, text='Candidate 2', width=button_width, height=button_height, borderwidth=button_borderwidth, command=Candidate2, bg=colour_pale_silver)
candidate2.grid(row=2, column=1)

candidate3=Button(canvas2, text='Candidate 3', width=button_width, height=button_height, borderwidth=button_borderwidth, command=Candidate3, bg=colour_pale_silver)
candidate3.grid(row=3, column=1)

candidate4=Button(canvas2, text='Candidate 4', width=button_width, height=button_height, borderwidth=button_borderwidth, command=Candidate4, bg=colour_pale_silver)
candidate4.grid(row=4, column=1)

candidate5=Button(canvas2, text='Candidate 5', width=button_width, height=button_height, borderwidth=button_borderwidth, command=Candidate5, bg=colour_pale_silver)
candidate5.grid(row=5, column=1)

candidate6=Button(canvas2, text='Candidate 6', width=button_width, height=button_height, borderwidth=button_borderwidth, command=Candidate6, bg=colour_pale_silver)
candidate6.grid(row=1, column=2)

candidate7=Button(canvas2, text='Candidate 7', width=button_width, height=button_height, borderwidth=button_borderwidth, command=Candidate7, bg=colour_pale_silver)
candidate7.grid(row=2, column=2)

candidate8=Button(canvas2, text='Candidate 8', width=button_width, height=button_height, borderwidth=button_borderwidth, command=Candidate8, bg=colour_pale_silver)
candidate8.grid(row=3, column=2)

candidate9=Button(canvas2, text='Candidate 9', width=button_width, height=button_height, borderwidth=button_borderwidth, command=Candidate9, bg=colour_pale_silver)
candidate9.grid(row=4, column=2)

candidate10=Button(canvas2, text='Candidate 10', width=button_width, height=button_height, borderwidth=button_borderwidth, command=Candidate10, bg=colour_pale_silver)
candidate10.grid(row=5, column=2)

candidate11=Button(canvas2, text='Candidate 11', width=button_width, height=button_height, borderwidth=button_borderwidth, command=Candidate11, bg=colour_pale_silver)
candidate11.grid(row=1, column=3)

candidate12=Button(canvas2, text='Candidate 12', width=button_width, height=button_height, borderwidth=button_borderwidth, command=Candidate12, bg=colour_pale_silver)
candidate12.grid(row=2, column=3)

candidate13=Button(canvas2, text='Candidate 13', width=button_width, height=button_height, borderwidth=button_borderwidth, command=Candidate13, bg=colour_pale_silver)
candidate13.grid(row=3, column=3)

candidate14=Button(canvas2, text='Candidate 14', width=button_width, height=button_height, borderwidth=button_borderwidth, command=Candidate14, bg=colour_pale_silver)
candidate14.grid(row=4, column=3)

candidate15=Button(canvas2, text='Candidate 15', width=button_width, height=button_height, borderwidth=button_borderwidth, command=Candidate15, bg=colour_pale_silver)
candidate15.grid(row=5, column=3)

candidate16=Button(canvas2, text='Candidate 16', width=button_width, height=button_height, borderwidth=button_borderwidth, command=Candidate16, bg=colour_pale_silver)
candidate16.grid(row=1, column=4)

candidate17=Button(canvas2, text='Candidate 17', width=button_width, height=button_height, borderwidth=button_borderwidth, command=Candidate17, bg=colour_pale_silver)
candidate17.grid(row=2, column=4)

candidate18=Button(canvas2, text='Candidate 18', width=button_width, height=button_height, borderwidth=button_borderwidth, command=Candidate18, bg=colour_pale_silver)
candidate18.grid(row=3, column=4)

candidate19=Button(canvas2, text='Candidate 19', width=button_width, height=button_height, borderwidth=button_borderwidth, command=Candidate19, bg=colour_pale_silver)
candidate19.grid(row=4, column=4)

candidate20=Button(canvas2, text='Candidate 20', width=button_width, height=button_height, borderwidth=button_borderwidth, command=Candidate20, bg=colour_pale_silver)
candidate20.grid(row=5, column=4)

candidate21=Button(canvas2, text='Candidate 21', width=button_width, height=button_height, borderwidth=button_borderwidth, command=Candidate21, bg=colour_pale_silver)
candidate21.grid(row=1, column=5)

candidate22=Button(canvas2, text='Candidate 22', width=button_width, height=button_height, borderwidth=button_borderwidth, command=Candidate22, bg=colour_pale_silver)
candidate22.grid(row=2, column=5)

candidate23=Button(canvas2, text='Candidate 23', width=button_width, height=button_height, borderwidth=button_borderwidth, command=Candidate23, bg=colour_pale_silver)
candidate23.grid(row=3, column=5)

candidate24=Button(canvas2, text='Candidate 24', width=button_width, height=button_height, borderwidth=button_borderwidth, command=Candidate24, bg=colour_pale_silver)
candidate24.grid(row=4, column=5)

candidate25=Button(canvas2, text='Candidate 25', width=button_width, height=button_height, borderwidth=button_borderwidth, command=Candidate25, bg=colour_pale_silver)
candidate25.grid(row=5, column=5)







button_confirm=Button(canvas3, text='Review', width=button_width, height=button_height, borderwidth=button_borderwidth, command=Confirm, bg=colour_pale_silver)
button_confirm.grid(row=1, column=1, pady=10)

button_save=Button(canvas3, text='Save', width=button_width, height=button_height, borderwidth=button_borderwidth, command=Save, bg=colour_pale_silver)

button_clear=Button(canvas3, text='Clear', width=button_width, height=button_height, borderwidth=button_borderwidth, command=Clear, bg=colour_pale_silver)





button_yes_confirm=Button(canvas4, text='Yes', width=button_width//2, height=button_height//2, borderwidth=button_borderwidth, command=YesConfirm, bg=colour_green, fg=colour_black)

button_no_confirm=Button(canvas4, text='No', width=button_width//2, height=button_height//2, borderwidth=button_borderwidth, command=NoConfirm, bg=colour_red, fg=colour_white)

button_yes_clear=Button(canvas4, text='Yes', width=button_width//2, height=button_height//2, borderwidth=button_borderwidth, command=YesClear, bg=colour_green, fg=colour_black)

button_no_clear=Button(canvas4, text='No', width=button_width//2, height=button_height//2, borderwidth=button_borderwidth, command=NoClear, bg=colour_red, fg=colour_white)

button_yes_save=Button(canvas4, text='Yes', width=button_width//2, height=button_height//2, borderwidth=button_borderwidth, command=YesSave, bg=colour_green, fg=colour_black)

button_no_save=Button(canvas4, text='No', width=button_width//2, height=button_height//2, borderwidth=button_borderwidth, command=NoSave, bg=colour_red, fg=colour_white)

button_done=Button(canvas6, text='Done', width=button_width//2, height=button_height//2, borderwidth=button_borderwidth, command=Done)



update_time()
root.mainloop()