<h1 align="center">Traveling Tournament Problem (TTP)</h1>

Organize the shedule season of sport teams (1 match per week):

- Each team plays every other team twice, once at home and once in the other's stadium.
- No team plays the same opponent in two consecutive weeks.
- No team plays more than three games in a row at home, or three games in a row on the road.


## Best Solution: local Search

6 types of swapping moves for the optimization:
- swap homes
- swap rounds
- swap teams
- partial swap rounds
- partial swap teams


## [Datasets](https://mat.tepper.cmu.edu/TOURN)

| Instances                                           | GWO/ESA | MBBO/ESA | ACO    | PSO    | BBO/SA |
| :-------------------------------------------------: | :-----: | :------: | :----: | :----: | :----: |
| [NL8](https://mat.tepper.cmu.edu/TOURN/data8.txt)   | 39721   | 39721    | 44112  | 43805  | 42568  |
| [NL10](https://mat.tepper.cmu.edu/TOURN/data10.txt) | 58190   | 58769    | 67264  | 66331  | 66121  |
| [NL12](https://mat.tepper.cmu.edu/TOURN/data12.txt) | 110519  | 111064   | 121981 | 121070 | 120040 |
| [NL14](https://mat.tepper.cmu.edu/TOURN/data14.txt) | 182996  | 183631   | 208086 | 210132 | 207848 |
| [NL16](https://mat.tepper.cmu.edu/TOURN/data16.txt) | 253957  | 254242   | 290188 | 291394 | 281963 |




