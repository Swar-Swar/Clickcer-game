import tkinter
from tkinter import messagebox
from tkinter import PhotoImage
import shelve

def save_points(points, auto_clicker_bought, auto_clicker_active): #To save the stats
    with shelve.open('points.db') as shelf:
        shelf['points'] = points
        shelf['auto_clicker_bought'] = auto_clicker_bought
        shelf['auto_clicker_active'] = auto_clicker_active

def load_points():                                                 #To load the saved stats
    try:
        with shelve.open('points.db') as shelf:
            points = shelf.get('points', 0)
            auto_clicker_bought = shelf.get('auto_clicker_bought', False)
            auto_clicker_active = shelf.get('auto_clicker_active', False)
    except KeyError:
        points = 0
        auto_clicker_bought = False
        auto_clicker_active = False
    return points, auto_clicker_active, auto_clicker_bought

points, auto_clicker_bought, auto_clicker_active = load_points()

def save_need_points(need_points, fex_points, re_points):                        #To save the attributes in the data-base
    with shelve.open('need_points.db') as shelf:
        shelf['need_points'] = need_points
        shelf['fex_points'] = fex_points
        shelf['re_points'] = re_points

def load_need_points():                                   #To load the attributes from the data-base
    with shelve.open('need_points.db') as shelf:
        need_points = shelf.get('need_points', 0)
        fex_points = shelf.get('fex_points', 1)
        re_points = shelf.get('re_points', 500)
        return need_points, fex_points, re_points
    
need_points, fex_points, re_points = load_need_points()

def save_cost_points(cost_points, known_points, already_done):
    with shelve.open('cost_points.db') as shelf:
        shelf['cost_points'] = cost_points
        shelf['known_points'] = known_points
        shelf['already_done'] = already_done

def load_cost_points():
    with shelve.open('cost_points.db') as shelf:
        cost_points	= shelf.get('cost_points', 500)
        known_points = shelf.get('known_points', 1)
        already_done = shelf.get('already_done', False)
        return cost_points, known_points, already_done
    
cost_points, known_points, already_done = load_cost_points()

def save_done1(already_done2, already_done3, already_done4):
   with shelve.open('done.db') as shelf:
      shelf['already_done2'] = already_done2
      shelf['already_done3'] = already_done3
      shelf['already_done4'] = already_done4

def load_done1():
   with shelve.open('already_done2.db') as shelf:
      already_done2 = shelf.get('already_done2', False)
      already_done3 = shelf.get('already_done3', False)
      already_done4 = shelf.get('already_done4', False)
      return already_done2, already_done3, already_done4

already_done2, already_done3, already_done4 = load_done1()


def save_done2(already_done5, already_done6, already_done7):
    with shelve.open('done2.db') as shelf:
        shelf['already_done5'] = already_done5
        shelf['already_done6'] = already_done6
        shelf['already_done7'] = already_done7

def load_done2():
    with shelve.open('done2.db') as shelf:
        already_done5 = shelf.get('already_done5', False)
        already_done6 = shelf.get('already_done6', False)
        already_done7 = shelf.get('already_done7', False)
        return already_done5, already_done6, already_done7
    
already_done5, already_done6, already_done7 = load_done2()

def save_claimed_rewards(claimed1, claimed2, claimed3):
    with shelve.open('claimed1.db') as shelf:
       shelf['claimed'] = claimed1
       shelf['claimed2'] = claimed2
       shelf['claimed3'] = claimed3

def load_claimed_rewards():
    with shelve.open('claimed1.db') as shelf:
        claimed1 = shelf.get('claimed', False)
        claimed2 = shelf.get('claimed2', False)
        claimed3 = shelf.get('claimed3', False)
        return claimed1, claimed2, claimed3
    
claimed1, claimed2, claimed3 = load_claimed_rewards()

def save_claimed_rewards2(claimed4, claimed5, claimed6):
    with shelve.open('claimed2.db') as shelf:
       shelf['claimed4'] = claimed4
       shelf['claimed5'] = claimed5
       shelf['claimed6'] = claimed6

def load_claimed_rewards2():
    with shelve.open('claimed2.db') as shelf:
        claimed4 = shelf.get('claimed4', False)
        claimed5 = shelf.get('claimed5', False)
        claimed6 = shelf.get('claimed6', False)
        return claimed4, claimed5, claimed6
    
claimed4, claimed5, claimed6 = load_claimed_rewards2()

def save_claimed_rewards3(claimed7):
    with shelve.open('claimed3.db') as shelf:
        shelf['claimed7'] = claimed7

def load_claimed_rewards3():
    with shelve.open('claimed3.db') as shelf:
        claimed7 = shelf.get('claimed7', False)
        return claimed7

claimed7 = load_claimed_rewards3()

def button_click():
    global points
    global known_points
    global auto_clicker_active
    points += known_points                                                #fex_points and known_points start with the value of 1
    label2.config(text=points)
    save_points(points, auto_clicker_bought, auto_clicker_active)
    save_need_points(need_points, re_points, fex_points)
    save_cost_points(known_points, cost_points, already_done)
    check_achievements()

def check_achievements():
    global points
    global already_done
    global already_done2
    global already_done3
    global already_done4
    global already_done5
    global already_done6
    global already_done7            

    if points == 100 and not already_done:
        messagebox.showinfo('Achievement!', 'Achievement unlocked!, \'Good start!"')
        messagebox.showinfo('See', 'See the achievement in the Achievements section!')
        already_done = True
    else:
        pass
        
    if points == 200 and not already_done2:
        messagebox.showinfo('Achievement!', 'Achievement unlocked!, \'Good Clicker!"')
        messagebox.showinfo('See', 'See the achievement in the Achievements section!')
        already_done2 = True
    else:
        pass

    if points == 500 and not already_done3:
        messagebox.showinfo('Achievement!', 'Achievement unlocked!, \'We are going somewhere!"')
        messagebox.showinfo('See', 'See the achievement in the Achievements section!')
        already_done3 = True
    else:
        pass

    if points == 1000 and not already_done4:
        messagebox.showinfo('Achievement!', 'Achievement unlocked!, \'Amateur Clicker!"')
        messagebox.showinfo('See', 'See the achievement in the Achievements section!')
        already_done4 = True
    else:
        pass

    if points == 1500 and not already_done5:
        messagebox.showinfo('Achievement!', 'Achievement unlocked!, \'You dont dissapoint"')
        messagebox.showinfo('See', 'See the achievement in the Achievements section!')
        already_done5 = True
    else:
        pass

    if points == 3000 and not already_done6:
        messagebox.showinfo('Achievement!', 'Achievement unlocked!, \'Professional CLicker!"')
        messagebox.showinfo('See', 'See the achievement in the Achievements section!')
        already_done6 = True
    else:
        pass

    if points == 4000 and not already_done7:
        messagebox.showinfo('Achievement!', 'Achievement unlocked!, \'I am amazed!"')
        messagebox.showinfo('See', 'See the achievement in the Achievements section!')
        already_done7 = True
    else:
        pass
    
    save_cost_points(cost_points, already_done, known_points)
    save_done1(already_done2, already_done3, already_done4)
    save_done2(already_done5, already_done6, already_done7)


def achievements():
    global image2
    global achievements
    global already_done5
    def check_done():
     if points >= 100 or already_done == True:
        a2.config(image=image2)
     else:
        a2.config(image=image3)

     if points >= 200 or already_done2 == True:
        a21.config(image=image2)
     else:
        a21.config(image=image3)

     if points >= 500 or already_done3 == True:
        a22.config(image=image2)
     else:
        a22.config(image=image3)

     if points >= 1000 or already_done4 == True:
        a23.config(image=image2)
     else:
        a23.config(image=image3)

     if points >= 1500 or already_done5 == True:
        a24.config(image=image2)
     else:
        a24.config(image=image3)

     if points >= 3000 or already_done6 == True:
        a25.config(image=image2)
     else:
        a25.config(image=image3)

     if points >= 4000 or already_done7 == True:
        a26.config(image=image2)
     else:
        a26.config(image=image3)


    new_tab = tkinter.Toplevel()  
    new_tab.title('Achievements!')
    new_tab.geometry('500x500')
    new_tab.resizable(False, False)

    a1 = tkinter.Label(new_tab, text='Good Start!--->', font=('Arial 20'))
    a1.place(x=10, y=10)

    a3 = tkinter.Label(new_tab, text='Good Clicker!--->', font=('Arial 20'))
    a3.place(x=10, y=40)

    a4 = tkinter.Label(new_tab, text='We are going somewhere!--->', font=('Arial 20'))
    a4.place(x=10, y=70)

    a5 = tkinter.Label(new_tab, text='Amateur Clicker!--->', font=('Arial 20'))
    a5.place(x=10, y=100)

    a6 = tkinter.Label(new_tab, text='You dont dissapoint!--->', font=('Arial 20'))
    a6.place(x=10, y=130)

    a7 = tkinter.Label(new_tab, text='Professional Clicker!--->', font=('Arial 20'))
    a7.place(x=10, y=170)

    a8 = tkinter.Label(new_tab, text='I am amazed!--->', font=('Arial 20'))
    a8.place(x=10, y=200)

    a2 = tkinter.Label(new_tab)                                                                   #Markers
    a2.place(x=200, y=10)

    a21 = tkinter.Label(new_tab)
    a21.place(x=230, y=40)

    a22 = tkinter.Label(new_tab)
    a22.place(x=380, y=70)

    a23 = tkinter.Label(new_tab)
    a23.place(x=270, y=100)

    a24= tkinter.Label(new_tab)
    a24.place(x=300, y=130)

    a25 = tkinter.Label(new_tab)
    a25.place(x=300, y=170)

    a26 = tkinter.Label(new_tab)
    a26.place(x=230, y=210)

    next_pg = tkinter.Button(new_tab, text='-->', font=('Arial 20'))
    next_pg.config(width = 3, height = 2)
    next_pg.place(x = 440, y= 100)
    
    save_cost_points(cost_points, known_points, already_done)
    save_done1(already_done2, already_done3, already_done4)
    save_done2(already_done6, already_done5, already_done7)
    check_done() 
   
def items_tab():
    global points
    global auto_clicker_bought
    global auto_clicker_active

    def buy_system():
        global points
        global auto_clicker_bought
        global auto_clicker_active
        if points >= 150 and not auto_clicker_bought:
            points -= 150
            auto_clicker_bought = True
            auto_clicker_active = True
            messagebox.showinfo('Transaction sucessful!', 'You have bought auto-clicker sucessfully!')
            save_points(points, auto_clicker_bought, auto_clicker_active)
            label2.config(text=points)
            if auto_clicker_active:
               auto_clicker()  
        elif auto_clicker_bought:
            messagebox.showinfo('Already bought!', 'Auto clicker has already been bought!')
        else:
            messagebox.showerror('Not enough Clicks!', 'Not enough Clicks!')

    item_win = tkinter.Toplevel()
    item_win.title('Shop')
    item_win.geometry('500x500')
    item_win.resizable(False, False)

    auto = tkinter.Label(item_win, image=image4)
    auto.place(x=10, y=50)

    label3 = tkinter.Label(item_win, text='Auto clicker--->150 clicks', font=('Arial 20'))
    label3.place(x=10, y=25)

    buy1 = tkinter.Button(item_win, text='Buy', font=('Arial 10'), command=buy_system)
    buy1.config(width=10, height=2)
    buy1.place(x=10, y=200)

def auto_clicker():
    global points
    global auto_clicker_active
    points += fex_points           #fex_points and known_points start with the value of 1
    label2.config(text=points)
    save_points(points, auto_clicker_bought, auto_clicker_active)
    save_need_points(need_points, fex_points, re_points)
    root.after(1000, auto_clicker)

def reset_progress():
    global points
    global auto_clicker_bought
    global auto_clicker_active
    
    def reset():
        global points
        global auto_clicker_active
        global auto_clicker_bought
        global re_birthed
        global known_points

        def reseted():
            global points
            global auto_clicker_active
            global auto_clicker_bought
            global cost_points
            global re_points
            global re_birthed 
            global known_points

            points = 0
            re_birthed = True
            re_points += 500
            cost_points += 500
            known_points = 5

            label2.config(text=points)
            cost2.config(text=cost_points)

            save_cost_points(cost_points, known_points, already_done) 

        if points < re_points:
            messagebox.showerror('Error', 'Not enough clicks!')
        else:
            messagebox.showinfo('Transaction sucessful', 'Re-Birthed successfully!')
            points -= re_points
            label2.config(text=points)
            reseted()

    reset_win = tkinter.Tk()
    reset_win.title('Re-Birth?')
    reset_win.geometry('500x500')
    reset_win.resizable(False, False)

    reset_Label = tkinter.Label(reset_win, text='Do you want to Re-birth?', font=('Arial 30'))
    reset_btn1 = tkinter.Button(reset_win, text='Yes, Re-Birth', font=('Arial 20'), command =  reset)

    cost = tkinter.Label(reset_win, text='Cost =(clicks)  ', font=('Arial 20'))
    cost2 = tkinter.Label(reset_win, text=cost_points, font=('Arial 20'))

    reset_btn1.config(width=10)

    reset_Label.place(x = 10, y = 10)
    reset_btn1.place(x = 50, y = 60)
    cost.place(x = 10, y = 300)
    cost2.place(x = 200 , y = 300)

    save_points(points, auto_clicker_active, auto_clicker_bought)
    save_cost_points(cost_points, known_points, already_done)
    save_need_points(need_points, ex_points, re_points)
    
def upgrade_tab():
    global points
    global auto_clicker
    global auto_clicker_active
    global auto_clicker_bought
    global upgrade_system
    global ex_points
    global need_points
    global price
    
    def upgrade_system():
        global need_points
        global points
        global fex_points
        
        if auto_clicker_bought:
            if points < need_points:
                messagebox.showerror('Error', 'Not enough clicks!')
            else:
                points -= need_points
                need_points += 50
                price.config(text=need_points)
                label2.config(text=points)
                fex_points += 1
                auto_clicker()
        else:
            messagebox.showerror('Error', 'Auto clicker has not been bought yet!')  

        save_points(points, auto_clicker_active, auto_clicker_bought)
        save_need_points(need_points, fex_points, re_points)      
            
    upgrade_win = tkinter.Toplevel()
    upgrade_win.title('Upgrade Tab')
    upgrade_win.resizable(False, False)
    upgrade_win.geometry('500x500')

    upgrade = tkinter.Button(upgrade_win, text='Upgrade', font=('Arial 20'), command = upgrade_system)
    upgrade_label = tkinter.Label(upgrade_win, text='Upgrade Auto-Clicker: +1', font =('Arial 20'))
    price_label = tkinter.Label(upgrade_win, text='Price -->', font=('Arial 20'))
    price = tkinter.Label(upgrade_win, text=need_points, font=('Arial 20'))

    upgrade.place(x = 100, y = 100)
    upgrade_label.place( x = 10, y = 10)
    price_label.place(x = 50, y = 50)
    price.place(x = 160, y = 50)

def rewards_tab():
    global points
    global already_done, already_done2, already_done3, already_done4, already_done5, already_done6, already_done7
    
    def rewards():
        global points
        global ex_points
        global claimed1 
        
        if claimed1 == False:

            if already_done == True:
                points += 50
                label2.config(text=points) 
                claimed1 = True
                if claimed1 == True:
                    reward_btn1.config(state='disabled')
                else:
                    reward_btn1.config(state='active')
            else:
                messagebox.showerror('Error', 'Achievement has not been obtained yet!')
        else:
            pass

    def rewards2():
        global points
        global ex_points
        global claimed2

        if claimed2 == False:

            if already_done2 == True:
                points += 100
                label2.config(text=points)
                claimed2 = True
                if claimed2 == True:
                    reward_btn2.config(state='disabled')
                else:
                    reward_btn2.config(state='active')
            else:
                messagebox.showerror('Error', 'Achievement has not been obtained yet!')
        else:
            pass

    def rewards3():
        global points
        global claimed3
        if claimed3 == False:
            
            if already_done3 == True:
                points += 150
                label2.config(text=points)
                claimed3 = True
                if claimed3 == True:
                    reward_btn3.config(state='disabled')
                else:
                    reward_btn3.config(state='active')
            else:
                messagebox.showerror('Error', 'Achievement has not been obtained yet!')
        else:
            pass

    def rewards4():
        global points
        global claimed4
        if claimed4 == False:
            
            if already_done4 == True:
                points += 150
                label2.config(text=points)
                claimed4 = True
                if claimed4 == True:
                    reward_btn4.config(state='disabled')
                else:
                    reward_btn4.config(state='active')
            else:
                messagebox.showerror('Error', 'Achievement has not been obtained yet!')
        else:
            pass

    def rewards5():
         global points
         global claimed5
         if claimed5 == False:
            
            if already_done5 == True:
                points += 450
                label2.config(text=points)
                claimed5 = True
                if claimed5 == True:
                    reward_btn5.config(state='disabled')
                else:
                    reward_btn5.config(state='active')
            else:
                messagebox.showerror('Error', 'Achievement has not been obtained yet!')
         else:
            pass
    
    def rewards6():
         global points
         global claimed6
         if claimed6 == False:
            
            if already_done6 == True:
                points += 700
                label2.config(text=points)
                claimed6 = True
                if claimed5 == True:
                    reward_btn6.config(state='disabled')
                else:
                    reward_btn6.config(state='active')
            else:
                messagebox.showerror('Error', 'Achievement has not been obtained yet!')
         else:
            pass
         
    def rewards7():
         global points
         global claimed7
         if claimed7 == False:
            
            if already_done7 == True:
                points += 1500
                label2.config(text=points)
                claimed7 = True
                if claimed7 == True:               
                    reward_btn7.config(state='disabled')
                else:
                    reward_btn7.config(state='active')
            else:
                messagebox.showerror('Error', 'Achievement has not been obtained yet!')
         else:
            pass

    rewards_win = tkinter.Tk()
    rewards_win.title('Rewards Tab')
    rewards_win.geometry('600x500')
    rewards_win.resizable(False, False)

    reward_Label1 = tkinter.Label(rewards_win, text = '1. Good start! --> 50 clicks', font=('Arial 20'))
    reward_Label2 = tkinter.Label(rewards_win, text = '2. Good clicker! --> 100 clicks', font=('Arial 20'))
    reward_Label3 = tkinter.Label(rewards_win, text = '3. We are going some where! --> 150 clicks', font=('Arial 20'))
    reward_Label4 = tkinter.Label(rewards_win, text = '4. Amateur clicker! --> 300 clicks', font=('Arial 20'))
    reward_Label5 = tkinter.Label(rewards_win, text = '5. You dont dissapoint! --> 450 clicks', font=('Arial 20'))
    reward_Label6 = tkinter.Label(rewards_win, text = '6. Professional clicker! --> 700 clicks', font=('Arial 20'))
    reward_Label7 = tkinter.Label(rewards_win, text = '7. I am amazed! --> 1500 clicks', font=('Arial 20'))

    reward_btn1 = tkinter.Button(rewards_win, text='Claim', font=('Arial 15'), command = rewards)
    reward_btn2 = tkinter.Button(rewards_win, text='Claim', font=('Arial 15'), command = rewards2)
    reward_btn3 = tkinter.Button(rewards_win, text='Claim', font=('Arial 15'), command = rewards3)
    reward_btn4 = tkinter.Button(rewards_win, text='Claim', font=('Arial 15'), command = rewards4)
    reward_btn5 = tkinter.Button(rewards_win, text='Claim', font=('Arial 15'), command = rewards5)
    reward_btn6 = tkinter.Button(rewards_win, text='Claim', font=('Arial 15'), command = rewards6)
    reward_btn7 = tkinter.Button(rewards_win, text='Claim', font=('Arial 15'), command = rewards7)

    reward_btn1.config(width=5, height=1)
    reward_btn2.config(width=5, height=1)
    reward_btn3.config(width=5, height=1)
    reward_btn4.config(width=5, height=1)
    reward_btn5.config(width=5, height=1)
    reward_btn6.config(width=5, height=1)
    reward_btn7.config(width=5, height=1)


    reward_Label1.place(x = 10, y = 10)
    reward_Label2.place(x = 10, y = 50)
    reward_Label3.place(x = 10, y = 100)
    reward_Label4.place(x = 10, y = 150)
    reward_Label5.place(x = 10, y = 200)
    reward_Label6.place(x = 10, y = 250)
    reward_Label7.place(x = 10, y = 300)

    reward_btn1.place(x = 350, y = 10)
    reward_btn2.place(x = 400, y = 50)
    reward_btn3.place(x = 545, y = 100)
    reward_btn4.place(x = 430, y = 150)
    reward_btn5.place(x = 480, y = 200)
    reward_btn6.place(x = 480, y = 250)
    reward_btn7.place(x = 400, y = 300)

    if claimed1 == True:
        reward_btn1.config(state='disabled')
    else:
        reward_btn1.config(state='active')

    if claimed2 == True:
        reward_btn2.config(state='disabled')
    else:
        reward_btn2.config(state='active')

    if claimed3 == True:
        reward_btn3.config(state='disabled')
    else:
        reward_btn3.config(state='active')

    if claimed4 == True:
        reward_btn4.config(state='disabled')
    else:
        reward_btn4.config(state='active')

    if claimed5 == True:
        reward_btn5.config(state='disabled')
    else:
        reward_btn4.config(state='active')

    if claimed6 == True:
        reward_btn6.config(state='disabled')
    else:
        reward_btn6.config(state='active')

    if claimed7 == True:
        reward_btn7.config(state='disabled')
    else:
        reward_btn7.config(state='active')

    save_claimed_rewards(claimed1, claimed2, claimed3)
    save_claimed_rewards2(claimed4, claimed5, claimed6)
    save_claimed_rewards3(claimed7)
    save_points(points, auto_clicker_active, auto_clicker_bought)
    save_done1(already_done2, already_done3, already_done4)
    save_done2(already_done5, already_done6, already_done7)
    
root = tkinter.Tk()
root.title('Clicker game!')
root.geometry('500x500')
root.resizable(False, False)

label2 = tkinter.Label(text=points, font=('Arial 30'))
label2.place(x=200, y=10)

image = PhotoImage(file=r'C:\Users\Dell\Documents\click me.png')
image2 = PhotoImage(file=r'C:\Users\Dell\Documents\tick.png')
image3 = PhotoImage(file=r'C:\Users\Dell\Documents\cross.png')
image4 = PhotoImage(file=r"C:\Users\Dell\Documents\auto curser.png")

click_me = tkinter.Button(root, image=image, command = button_click)
click_me.config(width=120, height=125)
click_me.place(x=200, y=190)

label1 = tkinter.Label(root, text='Click me!', font=('Arial 20'))
label1.place(x=200, y=150)

achievements_tab = tkinter.Button(root, text='Achievements', font=('Arial 10'), command=achievements)
achievements_tab.config(width=10, height=2)
achievements_tab.place(x=10, y=50)

shop_tab = tkinter.Button(root, text='Shop', font=('Arial 10'),command=items_tab)
shop_tab.config(width=5 , height=2)
shop_tab.place(x=10, y= 400)

reset_btn = tkinter.Button(text='Re-Birth', font=('Arial 10'))
reset_btn.config(width=6, height=2, command=lambda: reset_progress())
reset_btn.place(x=400, y= 400)

upgrade_btn = tkinter.Button(text='Upgrade', font=('Arial 10'))
upgrade_btn.config(width=7, height=2, command = upgrade_tab)
upgrade_btn.place(x = 400, y= 50 )

rewards_btn = tkinter.Button(text='Rewards', font=('Arial 10'), command = rewards_tab)
rewards_btn.config(width=6, height=2)
rewards_btn.place(x = 10, y = 110)

if auto_clicker_bought:  
    auto_clicker()                #To activate auto-clicker when bought

save_points(points, auto_clicker_active, auto_clicker_active)
save_need_points(need_points, fex_points, re_points) 
save_cost_points(known_points, cost_points, already_done)
save_claimed_rewards(claimed1, claimed2, claimed3)
save_claimed_rewards2(claimed4, claimed5, claimed6)
save_claimed_rewards3(claimed7)
save_done1(already_done2, already_done3, already_done4)
save_done2(already_done5, already_done6, already_done7)
                                        
root.mainloop()
