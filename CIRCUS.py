import random
import csv

tickets_lost_total = 0
million_ticket_sum = 0
times = 1_000_000_000

outfile = "simulation_output.csv"

with open(outfile, "w") as fileout:
    writer = csv.writer(fileout)
    writer.writerow(["# of Sims", "Tickets lost in this million", "Total tickets lost", "rolling ticket loss average", "Expected Value this million", "rolling expected value"])

for i in range(1, times+1):
    duck_list = ['red', 'red', 'red', 'blue', 'blue', 'blue', 'blue', 'blue', 'green', 'green', 'green', 'green', 'green', 'green', 'green', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black']
    tickets = -2

    # Step 2: roll 2d4
    rolled = random.randint(1, 4) + random.randint(1, 4)
    chosen_ducks = random.sample(duck_list, rolled)

    # Count the number of unique colors in chosen ducks
    unique_colors = set(chosen_ducks)

    # Count the occurrences of each color in chosen ducks
    red_count = chosen_ducks.count("red")
    blue_count = chosen_ducks.count("blue")
    green_count = chosen_ducks.count("green")
    black_count = chosen_ducks.count("black")

    # Define win ticket values
    RED_WIN_TICKET = 12
    BLUE_WIN_TICKET = 4
    GREEN_WIN_TICKET = 3
    UNIQUE_DUCKS_WIN_TICKET = 2

    # Check conditions for winning tickets based on counts of each color
    if red_count == 3:
        tickets += RED_WIN_TICKET
    if blue_count == 3:
        tickets += BLUE_WIN_TICKET
    if green_count == 3:
        tickets += GREEN_WIN_TICKET

    # Check if number of unique colors matches the roll result
    if len(unique_colors) == rolled:
        tickets += UNIQUE_DUCKS_WIN_TICKET

    million_ticket_sum += tickets

    # Every 1,000,000 simulations, write results to the CSV
    if i % 1_000_000 == 0 and i != 0:
        tickets_lost_total += million_ticket_sum
        ticket_loss_avg = tickets_lost_total / (i / 1_000_000)
        ev_this = million_ticket_sum / 1_000_000
        rolling_ev = tickets_lost_total / i

        with open(outfile, "a") as fileout:
            writer = csv.writer(fileout)
            l = [i, million_ticket_sum, tickets_lost_total, ticket_loss_avg, ev_this, rolling_ev]
            writer.writerow(l)
            print("row", i)

        million_ticket_sum = 0