import yaml
from util import *

BOLD = "\033[1m"
RESET = "\033[0m"
DEM = "\033[1;34m"
REP = "\033[1;31m"

# load config
with open("config.yaml", "r") as yamlfile:
    config = yaml.safe_load(yamlfile)

for i in range(15):
    print("\n")

print("******************************")
print("KIERAN'S")
print("▗▄▄▄▖▗▖   ▗▄▄▄▖ ▗▄▄▖▗▄▄▄▖▗▄▄▄▖ ▗▄▖ ▗▖  ▗▖\n"
      "▐▌   ▐▌   ▐▌   ▐▌     █    █  ▐▌ ▐▌▐▛▚▖▐▌\n"
      "▐▛▀▀▘▐▌   ▐▛▀▀▘▐▌     █    █  ▐▌ ▐▌▐▌ ▝▜▌\n"
      "▐▙▄▄▖▐▙▄▄▖▐▙▄▄▖▝▚▄▄▖  █  ▗▄█▄▖▝▚▄▞▘▐▌  ▐▌")
print("▗▄▄▄  ▗▄▖  ▗▄▄▖▗▖ ▗▖▗▄▄▖  ▗▄▖  ▗▄▖ ▗▄▄▖ ▗▄▄▄ \n"
      "▐▌  █▐▌ ▐▌▐▌   ▐▌ ▐▌▐▌ ▐▌▐▌ ▐▌▐▌ ▐▌▐▌ ▐▌▐▌  █\n"
      "▐▌  █▐▛▀▜▌ ▝▀▚▖▐▛▀▜▌▐▛▀▚▖▐▌ ▐▌▐▛▀▜▌▐▛▀▚▖▐▌  █\n"
      "▐▙▄▄▀▐▌ ▐▌▗▄▄▞▘▐▌ ▐▌▐▙▄▞▘▝▚▄▞▘▐▌ ▐▌▐▌ ▐▌▐▙▄▄▀")
print("******************************\n")

print("*****538*NATIONAL*AVERAGE*****\n")
scrape_national = do_driver("" + config['base_url'] + config['year'] + "/national/",
                 ["hover-leader-fg", "hover-leader-amt"])
prev = config['national_previous']

curr = float(scrape_national[1].replace("+", ""))

if config['rep_contender'] == scrape_national[0]:
    curr = curr * -1.0

diff = curr - prev

leader_string = ""

if config['dem_contender'] == scrape_national[0]:
    leader_string = leader_string + DEM
else:
    leader_string = leader_string + REP

leader_string = leader_string + scrape_national[0] + str(scrape_national[1])

if diff >= 0:
    if config['dem_contender'] == scrape_national[0]:
        leader_string = leader_string + RESET + DEM + " (" + "+"
    else:
        leader_string = leader_string + RESET + REP + " (" + "-"
else:
    if config['dem_contender'] == scrape_national[0]:
        leader_string = leader_string + RESET + REP + " (" + "-"
    else:
        leader_string = leader_string + RESET + DEM + " (" + "+"

leader_string = leader_string + str(abs(diff))[0:3] + ")"

print(leader_string)
config['national_previous'] = curr

print(RESET + "\n******************************")
print(RESET + "\n*****SWING*STATE*AVERAGES*****")

with open("config.yaml", "w") as yamlfile:
    yaml.dump(config, yamlfile)