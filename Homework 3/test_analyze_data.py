from analyze_data import net_profit
from analyze_data import best_rating
from analyze_data import most_frequent_actor
import pytest

def test_net_profit():
    # TODO: write unit tests for net profit function 
    test_data = [
        {'Title': 'Enders Game', 'budget': 100000, 'grossWorldWide': 200000},

        {'Title': 'Snow White', 'budget': 150000, 'grossWorldWide': 250000},

        {'Title': 'Dr. Dolittle', 'budget': 200000, 'grossWorldWide': 300000},
    ]

    test_data2 = [
        {'Title': 'Last Breath', 'budget': 100000, 'grossWorldWide': 400000},

        {'Title': 'The Gorge', 'budget': 160000, 'grossWorldWide': 350000},

        {'Title': '2073', 'budget': 170000, 'grossWorldWide': 250000},
    ]

    test_data3 = [
        {'Title': 'Woman in the Yard', 'budget': 125000, 'grossWorldWide': 450000},

        {'Title': 'Heretic', 'budget': 155000, 'grossWorldWide': 500000},

        {'Title': 'Mickey 17', 'budget': 200500, 'grossWorldWide': 750000},
    ]

    assert net_profit(test_data) == 'Dr. Dolittle'
    assert net_profit(test_data2) == 'Last Breath'
    assert net_profit(test_data3) == 'Mickey 17'

# TODO: write unit tests for second function in analyze_data.py
def test_best_rating():
    test_data = [
        {'Title': 'Captain America: Civil War', 'Rating': 6.5},

        {'Title': 'Doctor Strange', 'Rating': 8.3},

        {'Title': 'Iron Man', 'Rating': 9.2},
    ]

    test_data2 = [
        {'Title': 'X-Men', 'Rating': 6.8},

        {'Title': 'Venom', 'Rating': 6.6},

        {'Title': 'Thor', 'Rating': 8.5},
    ]
    test_data3 = [
        {'Title': 'Deadpool', 'Rating': 9.1},

        {'Title': 'The Incredible Hulk', 'Rating': 6.4},

        {'Title': 'Logan', 'Rating': 7.7},
    ]

    assert best_rating(test_data) == ('Iron Man', 9.2)
    assert best_rating(test_data2) == ('Thor', 8.5)
    assert best_rating(test_data3) == ('Deadpool', 9.1)

# TODO: write unit tests for second function in analyze_data.py

def test_most_frequent_actor():
    test_data = [
        {'Title': 'Captain America: Civil War', 'stars': ['Chris Evans', 'Robert Downey Jr.']},

        {'Title': 'Doctor Strange', 'stars': ['Benedict Cumberbatch', 'Tilda Swinton']}, 

        {'Title': 'Iron Man', 'stars': ['Robert Downey Jr.', 'Gwyneth Paltrow']}
    ]

    test_data2 = [
        {'Title': 'Deadpool', 'stars': ['Ryan Reynolds', 'Morena Baccarin']},
        
        {'Title': 'Deadpool 2', 'stars': ['Ryan Reynolds', 'Josh Brolin']},

        {'Title': 'Logan', 'stars': ['Hugh Jackman', 'Patrick Stewart']}
    ]

    test_data3 = [
        {'Title': 'The Avengers', 'stars': ['Chris Hemsworth', 'Tom Hiddleston']},

        {'Title': 'Thor', 'stars': ['Chris Hemsworth', 'Natalie Portman']},

        {'Title': 'Thor: Ragnarok', 'stars': ['Chris Hemsworth', 'Tessa Thompson']}
        
    ]

    assert most_frequent_actor(test_data) == ('Robert Downey Jr.', 2)
    assert most_frequent_actor(test_data2) == ('Ryan Reynolds', 2)
    assert most_frequent_actor(test_data3) == ('Chris Hemsworth', 3)
