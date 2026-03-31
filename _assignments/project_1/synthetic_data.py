import random

COUNTIES = ["Fulton", "DeKalb", "Cobb", "Gwinnett", "Clayton"]
PARTIES = ["Democrat", "Republican", "Independent"]
INCOME_BRACKETS = ["<50K", "50-100K", ">100K"]

def generate_voter(voter_id):
    age = random.randint(18, 90)

    county = random.choice(COUNTIES)
    party = random.choices(
        PARTIES,
        weights=[0.45, 0.40, 0.15],
        k=1
    )[0]

    income = random.choices(
        INCOME_BRACKETS,
        weights=[0.40, 0.40, 0.20],
        k=1
    )[0]

    # Turnout probability increases with age and past participation
    base_turnout = min(0.3 + age / 120, 0.9)

    turnout = [
        int(random.random() < base_turnout) for _ in range(4)
    ]

    return {
        "voter_id": voter_id,
        "age": age,
        "county": county,
        "party": party,
        "income_bracket": income,
        "t_2016": turnout[0],
        "t_2018": turnout[1],
        "t_2020": turnout[2],
        "t_2022": turnout[3],
    }



def generate_dataset(n=10_000):
    # Generate n unique random voter IDs
    voter_ids = random.sample(range(1_000_000_000, 9_999_999_999), n)

    return [generate_voter(voter_id) for voter_id in voter_ids]
