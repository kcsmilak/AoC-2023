Games.....

<h1>Summary</h1>
<pre>
05: Reverse Map
12: Unrolled springs
17> Pathfind min heat. Seems very close
18: Painted lagoon?
19= Math...
20: Pulse propagation
21: Repeating garden plots conways game
22= Remove sand slab
23: Longest route 
24: Perfect snowball
    
</pre>


<pre>
----------------------------------------------------------------------
-- Day 1: Trebuchet?!                                           [*][*]

    1abc2
    pqr3stu8vwx
    a1b2c3d4e5f
    treb7uchet
    
----------------------------------------------------------------------
-- Day 2: Cube Conundrum                                        [*][*]

    Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
    Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
    Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green.
    Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue..
    Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
    
----------------------------------------------------------------------
-- Day 3: Gear Ratios                                           [*][*]

    467..114..
    ...*......
    ..35..633.
    ......#...
    617*......
    .....+.58.
    ..592.....
    ......755.
    ...$.*....
    .664.598..
    
----------------------------------------------------------------------
-- Day 4: Scratchcards                                          [*][*]

    Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
    Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
    Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
    Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
    Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
    Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11

----------------------------------------------------------------------
-- Day 5: Seed Fertilizer                                       [*][ ]

    seeds: 79 14 55 13

    seed-to-soil map:
    50 98 2
    52 50 48

    ...

    humidity-to-location map:
    60 56 37
    56 93 4

Seems like you should be able to reverse the map, but is inefficient

----------------------------------------------------------------------
-- Day 6: Wait for It                                           [*][*]

    Time:      7  15   30
    Distance:  9  40  200

----------------------------------------------------------------------
-- Day 7: Camel Cards                                           [*][*]

    32T3K 765
    T55J5 684
    KK677 28
    KTJJT 220
    QQQJA 483
    
----------------------------------------------------------------------
-- Day 8: Haunted Wasteland                                     [*][*]

    RL
    
    AAA = (BBB, CCC)
    BBB = (DDD, EEE)
    CCC = (ZZZ, GGG)
    DDD = (DDD, DDD)
    EEE = (EEE, EEE)
    GGG = (GGG, GGG)
    ZZZ = (ZZZ, ZZZ)

----------------------------------------------------------------------
-- Day 9: Mirage Maintenance                                    [*][*]

    0   3   6   9  12  15
      3   3   3   3   3
        0   0   0   0

----------------------------------------------------------------------
-- Day 10: Pipe Maze                                            [*][*]

    ..F7.
    .FJ|.
    SJ.L7
    |F--J
    LJ...

----------------------------------------------------------------------
-- Day 11: Cosmic Expansion                                     [*][*]


----------------------------------------------------------------------
-- Day 12: Hot Springs                                          [*][ ]

    #.#.### 1,1,3
    .#...#....###. 1,1,3
    .#.###.#.###### 1,3,1,6
    ####.#...#... 4,1,1
    #....######..#####. 1,6,5
    .###.##....# 3,2,1

Stuck on being able to "unfold" the hose and still finish
efficiently

----------------------------------------------------------------------
-- Day 13: Point of Incidence                                   [*][*]

    #.##..##.
    ..#.##.#.
    ##......#
    ##......#
    ..#.##.#.
    ..##..##.
    #.#.##.#.
    
    #...##..#
    #....#..#
    ..##..###
    #####.##.
    #####.##.
    ..##..###
    #....#..#

----------------------------------------------------------------------
-- Day 14: Parabolic Reflector Dish                             [*][*]

    O....#....
    O.OO#....#
    .....##...
    OO.#O....O
    .O.....O#.
    O.#..O.#.#
    ..O..#O..O
    .......O..
    #....###..
    #OO..#....

----------------------------------------------------------------------
-- Day 15: Lens Library                                         [*][*]

    rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7

----------------------------------------------------------------------
-- Day 16: The Floor Will Be Lava                               [*][*]

    >|<<<\....
    |v-.\^....
    .v...|->>>
    .v...v^.|.
    .v...v^...
    .v...v^..\
    .v../2\\..
    <->-/vv|..
    .|<<<2-|.\
    .v//.|.v..

----------------------------------------------------------------------
-- Day 17: Clumsy Crucible                                      [*][ ]

    2>>34^>>>1323
    32v>>>35v5623
    32552456v>>54
    3446585845v52
    4546657867v>6
    14385987984v4
    44578769877v6
    36378779796v>
    465496798688v
    456467998645v
    12246868655<v
    25465488877v5
    43226746555v>

Should be easy greedy path finder but pruning is taking too long...

----------------------------------------------------------------------
-- Day 18: Lavaduct Lagoon                                      [*][ ]

    R 6 (#70c710)
    D 5 (#0dc571)
    L 2 (#5713f0)
    D 2 (#d2c081)
    R 2 (#59c680)
    D 2 (#411b91)
    L 5 (#8ceee2)
    U 2 (#caa173)
    L 1 (#1b58a2)
    U 2 (#caa171)
    R 2 (#7807d2)
    U 3 (#a77fa3)
    L 2 (#015232)
    U 2 (#7a21e3)

Paint an area based on x,y positions

----------------------------------------------------------------------
-- Day 19: Aplenty                                              [*][ ]

    px{a<2006:qkq,m>2090:A,rfg}
    pv{a>1716:R,A}
    lnx{m>1548:A,A}
    rfg{s<537:gd,x>2440:R,A}
    qs{s>3448:A,lnx}
    qkq{x<1416:A,crn}
    crn{x>2662:A,R}
    in{s<1351:px,qqz}
    qqz{s>2770:qs,m<1801:hdj,R}
    gd{a>3333:R,R}
    hdj{m>838:A,pv}
    
    {x=787,m=2655,a=1222,s=2876}
    {x=1679,m=44,a=2067,s=496}
    {x=2036,m=264,a=79,s=2244}
    {x=2461,m=1339,a=466,s=291}
    {x=2127,m=1623,a=2188,s=1013}

Ryan finished this...
        
----------------------------------------------------------------------
-- Day 20: ...                                                  [*][ ]

    broadcaster -> a, b, c
    %a -> b
    %b -> c
    %c -> inv
    &inv -> a
    
----------------------------------------------------------------------
-- Day 21: Step Counter                                         [*][ ]

    ...........
    .....###.#.
    .###.##..#.
    ..#.#.O.#..
    ...O#O#....
    .##.OS####.
    .##O.#...#.
    ....O..##..
    .##.#.####.
    .##..##.##.
    ...........

Conway's algorithm with repeating map and huge cycle count

----------------------------------------------------------------------
-- Day 22: ...                                                  [*][ ]

    1,0,1~1,2,1
    0,0,2~2,0,2
    0,2,3~2,2,3
    0,0,4~0,2,4
    2,0,5~2,2,5
    0,1,6~2,1,6
    1,1,8~1,1,9

Ryan finished this...

Pick a block, remove it, run the drops, count how many fall, then
repeat for each block to see which causes the most to fall
        
----------------------------------------------------------------------
-- Day 23: A Long Walk                                          [*][ ]

    #.#####################
    #.......#########...###
    #######.#########.#.###
    ###.....#.>.>.###.#.###
    ###v#####.#v#.###.#.###
    ###.>...#.#.#.....#...#
    ###v###.#.#.#########.#
    ###...#.#.#.......#...#
    #####.#.#.#######.#.###
    #.....#.#.#.......#...#
    #.#####.#.#.#########v#
    #.#...#...#...###...>.#
    #.#.#v#######v###.###v#
    #...#.>.#...>.>.#.###.#
    #####v#.#.###v#.#.###.#
    #.....#...#...#.#.#...#
    #.#########.###.#.#.###
    #...###...#...#...#.###
    ###.###.#.###v#####v###
    #...#...#.#.>.>.#.>.###
    #.###.###.#.###.#.#v###
    #.....###...###...#...#
    #####################.#

Inverse pathfinding...

----------------------------------------------------------------------
-- Day 24: Never Tell Me The Odds                               [*][ ]

    19, 13, 30 @ -2,  1, -2
    18, 19, 22 @ -1, -1, -2
    20, 25, 34 @ -2, -2, -4
    12, 31, 28 @ -1, -2, -1
    20, 19, 15 @  1, -5, -3

Stand in the *exact* position to shoot all snowballs
        
---------------------------------------------------------------------
-- Day 25: Snowverload                                         [*][ ]

    jqt: rhn xhk nvd
    rsh: frs pzl lsr
    xhk: hfx
    cmg: qnr nvd lhk bvb
    rhn: xhk bvb hfx
    bvb: xhk hfx
    pzl: lsr hfx nvd
    qnr: nvd
    ntq: jqt hfx bvb xhk
    nvd: lhk
    lsr: lhk
    rzs: qnr cmg lsr rsh
    frs: qnr lhk lsr
    
</PRE>
