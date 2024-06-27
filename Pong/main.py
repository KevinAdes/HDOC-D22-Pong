from playfield import PlayArea
from score import ScoreManager
from paddle import Paddle
from ball import Ball

play_area = PlayArea()
score_manager = ScoreManager(60, 250)
ball = Ball()
p1_paddle = Paddle(-375, 0)
p2_paddle = Paddle(375, 0)

play_area.play_area.listen()
play_area.play_area.onkeypress(key="w", fun=p1_paddle.velocity_up)
play_area.play_area.onkeypress(key="s", fun=p1_paddle.velocity_down)
play_area.play_area.onkeyrelease(key="w", fun=p1_paddle.velocity_null)
play_area.play_area.onkeyrelease(key="s", fun=p1_paddle.velocity_null)

play_area.play_area.listen()
play_area.play_area.onkeypress(key="Up", fun=p2_paddle.velocity_up)
play_area.play_area.onkeypress(key="Down", fun=p2_paddle.velocity_down)
play_area.play_area.onkeyrelease(key="Up", fun=p2_paddle.velocity_null)
play_area.play_area.onkeyrelease(key="Down", fun=p2_paddle.velocity_null)

run_game = True
ball.prime_ball()

while run_game:
    if -250 < p1_paddle.pos()[1]+p1_paddle.velocity < 250:
        p1_paddle.update_location()
    if -250 < p2_paddle.pos()[1]+p2_paddle.velocity < 250:
        p2_paddle.update_location()
    ball.update_location()
    ball.paddle_bounce(p1_paddle)
    ball.paddle_bounce(p2_paddle)
    play_area.play_area.update()
    if ball.pos()[0] < -400:
        score_manager.increment_p2_score()
        ball.prime_ball()
    if ball.pos()[0] > 400:
        score_manager.increment_p1_score()
        ball.prime_ball()
    if ball.pos()[1] < -300 or ball.pos()[1] > 300:
        ball.vertical_bounce()

play_area.play_area.exitonclick()
