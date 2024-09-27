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

print(generate_leader_string(scrape_national, curr, prev, config['dem_contender'], config['rep_contender']))

if config['dem_contender'] == scrape_national[0]:
    config['national_previous'] = curr
else:
    config['national_previous'] = curr * -1.0

print(RESET + "\n*****SWING*STATE*AVERAGES*****\n")

state_index = 0
for state in config['swing_states']:

    scrape_state = do_driver("" + config['base_url'] + config['year'] + "/" + state,
                 ["hover-leader-fg", "hover-leader-amt"])
    state_prev = float(config['state_previous'][state_index])
    state_curr = float(scrape_state[1].replace("+", ""))

    state_leader_string = generate_leader_string(scrape_state, state_curr, state_prev,
                                                 config['dem_contender'], config['rep_contender'])

    print(BOLD + state.replace("-", " ").title() + ": " + RESET + state_leader_string + RESET)

    if config['dem_contender'] == scrape_state[0]:
        config['state_previous'][state_index] = state_curr
    else:
        config['state_previous'][state_index] = state_curr * -1.0

    state_index = state_index + 1

print("******************************\n")

with open("config.yaml", "w") as yamlfile:
    yaml.dump(config, yamlfile)