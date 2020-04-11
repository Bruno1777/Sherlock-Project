from graphics import *
from Button import *
from Search import*



def main():
    WINDOW_HEIGHT = 400
    WINDOW_WIDTH = 800



    window = GraphWin('SHERLOCK', WINDOW_WIDTH, WINDOW_HEIGHT)
    window.setBackground('white')
    bg = Image(Point(WINDOW_WIDTH  / 2, WINDOW_HEIGHT / 2), "SpyBg.gif")
    bg.draw(window)
    intro = Text(Point(WINDOW_WIDTH / 2, 20), "Welcome to Sherlock")
    intro.setSize(20)
    intro.draw(window)


    intro1 = Text(Point(WINDOW_WIDTH  / 2, WINDOW_HEIGHT / 2 - 40), "Enter your website")
    intro1.setSize(20)
    intro1.draw(window)
    answerBox = Entry(Point(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2), 50)
    answerBox.setSize(20)
    answerBox.setText("http://")
    answerBox.draw(window)
    intro2 = Text(Point(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2 + 40), "Click to Submit Search")
    intro2.setSize(20)
    intro2.draw(window)



    submit = Button(Point(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2 + 80), 100, 30, "Submit")
    submit.activate()
    submit.draw(window)

    click = window.getMouse()
    while not submit.isClicked(click):
        click = window.getMouse()
    text = answerBox.getText()
    webs = Search(text)


    intro.undraw()
    intro1.undraw()
    intro2.undraw()
    answerBox.undraw()
    submit.undraw()

    if webs.isValid():
        if webs.isCredible("credible.txt","noncredible.txt"):
            output1 = Text(Point(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2), "Your Source is Credible.")
            output1.setSize(20)
            output1.draw(window)
        else:
            output1 = Text(Point(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2), "Your Source is not Credible.")
            output1.setSize(20)
            output1.draw(window)
    else:
        output1 = Text(Point(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2), "Not a valid website.")
        output1.setSize(20)
        output1.draw(window)

    window.getMouse()
    window.close()
main()

