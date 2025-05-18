import tkinter
from tkinter import messagebox
game = tkinter.Tk()
game.geometry("555x565")
game.configure(bg = "black")
team = "#74acb5"
teamx = "#18d0ed"
teamo = "#de1414"
boxes = []
turncheck = []

for index in range(9):
    boxes.append(tkinter.Button(game, bg=team, height="10", width="20"))
    turncheck.append(index)


def change(box):
    if box.widget["bg"] == team:
        box.widget["bg"] = teamx
        turn = 0
        tie = 0
    else:
        return()

    for d in range(9):
        turncheck[d] = str((boxes[d])["bg"])

    for a in range(3):
        if (boxes[0 + (a * 3)])["bg"] == teamo and (boxes[1 + (a * 3)])["bg"] == teamo:
            if (boxes[2 + (a * 3)])["bg"] == team:
                boxes[2 + (a * 3)].configure(bg=teamo)
                break
        if (boxes[1 + (a * 3)])["bg"] == teamo and (boxes[2 + (a * 3)])["bg"] == teamo:
            if (boxes[0 + (a * 3)])["bg"] == team:
                boxes[0 + (a * 3)].configure(bg=teamo)
                break
        if (boxes[0 + (a * 3)])["bg"] == teamo and (boxes[2 + (a * 3)])["bg"] == teamo:
            if (boxes[1 + (a * 3)])["bg"] == team:
                boxes[1 + (a * 3)].configure(bg=teamo)
                break
        if (boxes[0 + a])["bg"] == teamo and (boxes[3 + a])["bg"] == teamo:
            if (boxes[6 + a])["bg"] == team:
                boxes[6 + a].configure(bg=teamo)
                break
        if (boxes[0 + a])["bg"] == teamo and (boxes[6 + a])["bg"] == teamo:
            if (boxes[3 + a])["bg"] == team:
                boxes[3 + a].configure(bg=teamo)
                break
        if (boxes[3 + a])["bg"] == teamo and (boxes[6 + a])["bg"] == teamo:
            if (boxes[0 + a])["bg"] == team:
                boxes[0 + a].configure(bg=teamo)
                break
        if (boxes[0])["bg"] == teamo and (boxes[4])["bg"] == teamo:
            if (boxes[8])["bg"] == team:
                boxes[8].configure(bg=teamo)
                break
        if (boxes[0])["bg"] == teamo and (boxes[8])["bg"] == teamo:
            if (boxes[4])["bg"] == team:
                boxes[4].configure(bg=teamo)
                break
        if (boxes[4])["bg"] == teamo and (boxes[8])["bg"] == teamo:
            if (boxes[0])["bg"] == team:
                boxes[0].configure(bg=teamo)
                break
        if (boxes[2])["bg"] == teamo and (boxes[4])["bg"] == teamo:
            if (boxes[6])["bg"] == team:
                boxes[6].configure(bg=teamo)
                break
        if (boxes[2])["bg"] == teamo and (boxes[6])["bg"] == teamo:
            if (boxes[4])["bg"] == team:
                boxes[4].configure(bg=teamo)
                break
        if (boxes[4])["bg"] == teamo and (boxes[6])["bg"] == teamo:
            if (boxes[2])["bg"] == team:
                boxes[2].configure(bg=teamo)
                break

    for k in range(9):
        if turncheck[k] == (boxes[k])["bg"]:
            turn += 1
    if turn == 9:
        turn = 0
        for e in range(3):
            if (boxes[0 + (e * 3)])["bg"] == teamx and (boxes[1 + (e * 3)])["bg"] == teamx:
                if (boxes[2 + (e * 3)])["bg"] == team:
                    boxes[2 + (e * 3)].configure(bg=teamo)
                    break
            if (boxes[1 + (e * 3)])["bg"] == teamx and (boxes[2 + (a * 3)])["bg"] == teamx:
                if (boxes[0 + (e * 3)])["bg"] == team:
                    boxes[0 + (e * 3)].configure(bg=teamo)
                    break
            if (boxes[0 + (e * 3)])["bg"] == teamx and (boxes[2 + (e * 3)])["bg"] == teamx:
                if (boxes[1 + (e * 3)])["bg"] == team:
                    boxes[1 + (e * 3)].configure(bg=teamo)
                    break
            if (boxes[0 + e])["bg"] == teamx and (boxes[3 + e])["bg"] == teamx:
                if (boxes[6 + e])["bg"] == team:
                    boxes[6 + e].configure(bg=teamo)
                    break
            if (boxes[0 + e])["bg"] == teamx and (boxes[6 + e])["bg"] == teamx:
                if (boxes[3 + e])["bg"] == team:
                    boxes[3 + e].configure(bg=teamo)
                    break
            if (boxes[3 + e])["bg"] == teamx and (boxes[6 + e])["bg"] == teamx:
                if (boxes[0 + e])["bg"] == team:
                    boxes[0 + e].configure(bg=teamo)
                    break
            if (boxes[0])["bg"] == teamx and (boxes[4])["bg"] == teamx:
                if (boxes[8])["bg"] == team:
                    boxes[8].configure(bg=teamo)
                    break
            if (boxes[0])["bg"] == teamx and (boxes[8])["bg"] == teamx:
                if (boxes[4])["bg"] == team:
                    boxes[4].configure(bg=teamo)
                    break
            if (boxes[4])["bg"] == teamx and (boxes[8])["bg"] == teamx:
                if (boxes[0])["bg"] == team:
                    boxes[0].configure(bg=teamo)
                    break
            if (boxes[2])["bg"] == teamx and (boxes[4])["bg"] == teamx:
                if (boxes[6])["bg"] == team:
                    boxes[6].configure(bg=teamo)
                    break
            if (boxes[2])["bg"] == teamx and (boxes[6])["bg"] == teamx:
                if (boxes[4])["bg"] == team:
                    boxes[4].configure(bg=teamo)
                    break
            if (boxes[4])["bg"] == teamx and (boxes[6])["bg"] == teamx:
                if (boxes[2])["bg"] == team:
                    boxes[2].configure(bg=teamo)
                    break

    for b in range(9):
        if turncheck[b] == (boxes[b])["bg"]:
            turn += 1
    if turn == 9:
        if box.widget == boxes[0] or box.widget == boxes[2] or box.widget == boxes[6] or box.widget == boxes[8]:
            if (boxes[4])["bg"] == team:
                boxes[4].configure(bg = teamo)
            elif (boxes[1])["bg"] == team:
                boxes[1].configure(bg = teamo)
            elif (boxes[5])["bg"] == team:
                boxes[5].configure(bg = teamo)
            elif (boxes[3])["bg"] == team:
                boxes[3].configure(bg = teamo)
            elif (boxes[7])["bg"] == team:
                boxes[7].configure(bg = teamo)
        elif box.widget == boxes[1]:
            if (boxes[2])["bg"] == team:
                boxes[2].configure(bg = teamo)
            elif (boxes[0])["bg"] == team:
                boxes[0].configure(bg = teamo)
        elif box.widget == boxes[5]:
            if (boxes[2])["bg"] == team:
                boxes[2].configure(bg = teamo)
            elif (boxes[8])["bg"] == team:
                boxes[8].configure(bg = teamo)
        elif box.widget == boxes[3]:
            if (boxes[6])["bg"] == team:
                boxes[6].configure(bg = teamo)
            elif (boxes[0])["bg"] == team:
                boxes[0].configure(bg = teamo)
        elif box.widget == boxes[7]:
            if (boxes[6])["bg"] == team:
                boxes[6].configure(bg = teamo)
            elif (boxes[8])["bg"] == team:
                boxes[8].configure(bg = teamo)
        elif box.widget == boxes[4]:
            if (boxes[0])["bg"] == team:
                boxes[0].configure(bg = teamo)
            elif (boxes[2])["bg"] == team:
                boxes[2].configure(bg = teamo)
            elif (boxes[6])["bg"] == team:
                boxes[6].configure(bg = teamo)
            elif (boxes[8])["bg"] == team:
                boxes[8].configure(bg = teamo)

    for c in range(3):
        if (boxes[0 + (c * 3)])["bg"] == (boxes[1 + (c * 3)])["bg"] and (boxes[1 + (c * 3)])["bg"] == (boxes[2 + (c * 3)])["bg"]:
            if (boxes[0 + (c * 3)])["bg"] == team:
                pass
            elif (boxes[0 + (c * 3)])["bg"] == teamx:
                result = messagebox.showinfo( "Result", "You Win!")
                game.destroy()
                break
            elif (boxes[0 + (c * 3)])["bg"] == teamo:
                result = messagebox.showinfo( "Result", "You Lose!")
                game.destroy()
                break
        if (boxes[0 + c])["bg"] == (boxes[3 + c])["bg"] and (boxes[3 + c])["bg"] == (boxes[6 + c])["bg"]:
            if (boxes[0 + c])["bg"] == team:
                pass
            elif (boxes[0 + c])["bg"] == teamx:
                result = messagebox.showinfo("Result", "You Win!")
                game.destroy()
                break
            elif (boxes[0 + c])["bg"] == teamo:
                result = messagebox.showinfo("Result", "You Lose!")
                game.destroy()
                break
        if (boxes[2])["bg"] == (boxes[4])["bg"] and (boxes[4])["bg"] == (boxes[6])["bg"]:
            if (boxes[2])["bg"] == team:
                pass
            elif (boxes[2])["bg"] == teamx:
                result = messagebox.showinfo("Result", "You Win!")
                game.destroy()
                break
            elif (boxes[2])["bg"] == teamo:
                result = messagebox.showinfo("Result", "You Lose!")
                game.destroy()
                break
        if (boxes[0])["bg"] == (boxes[4])["bg"] and (boxes[4])["bg"] == (boxes[8])["bg"]:
            if (boxes[0])["bg"] == team:
                pass
            elif (boxes[0])["bg"] == teamx:
                result = messagebox.showinfo("Result", "You Win!")
                game.destroy()
                break
            elif (boxes[0])["bg"] == teamo:
                result = messagebox.showinfo("Result", "You Lose!")
                game.destroy()
                break
                
    for p in range(9):
        if (boxes[p])["bg"] != team:
            tie += 1
            print(tie)
        if tie == 9:
            result = messagebox.showinfo("Result", "You Tied (but u still suck)")
            game.destroy()
            break

for index1 in range(9):
    boxes[index1].bind("<Button>", change)

boxes[0].place(x = 0, y = 0)
boxes[1].place(x = 200, y = 0)
boxes[2].place(x = 400, y = 0)
boxes[3].place(x = 0, y = 200)
boxes[4].place(x = 200, y = 200)
boxes[5].place(x = 400, y = 200)
boxes[6].place(x = 0, y = 400)
boxes[7].place(x = 200, y = 400)
boxes[8].place(x = 400, y = 400)
game.mainloop()

#testing