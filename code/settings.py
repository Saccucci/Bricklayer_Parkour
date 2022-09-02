# mapa_atual = [p3, p4, p5]

# mapa_fixo = [m0]
# gerador_de_mapas = [m1, m2, m3, m4, m5, m6, m7, m8]

# Todos mapas tem que ter um marcador no canto direito

# x = 0
# y = randint

# Priemiro Mapa Fixo
level_map = [
'                                                        ',
'                                                        ',
'                                                        ',
'                                                        ',
'                                                        ',
'                                                        ',
'                                                        ',
'                                                        ',
'                                                        ',
'                                                        ',
'                                                        ',
'                                                        ',
'                                                        ',
'                                                        ',
'                                                        ',
'                                                    XXXX',
'                                                 XXXXXXX',
'                                             XXXXXXXXXXX',
'                                         XXXXXXXXXXXXXXX',
'                                       XXXXXXXXXXXXXXXXX',
'        P   T          E             XXXXXXXXXXXXXXXXXXX',
'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX']

level_map1 = [
'J                                                      M',
'                                                        ',
' XXX                                                    ',
'                                                        ',
'                                                        ',
'                                                        ',
'                                                        ',
'                                                        ',
'                                                        ',
'                                                        ',
'                           E                            ',
'                           X                            ',
'                                                        ',
'                                                        ',
'                                                        ',
'                                                        ',
'                                                        ',
'                                                        ',
'X                  E              E                     ',
'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
'               X                                        ',
'                                                       X']

level_map2 = [
'J      X  XXXX                                         M',
'                                                        ',
'              X  XXXX                                   ',
' XX    XXX            XX                                ',
' XXXX                                                   ',
' XXXX         XX         XX                             ',
' XXXX       XX                                          ',
' XX    X  XXXX    XX  XX     XX    XXX            XX    ',
'       X  XXXX    XX  XX     XX    XXX            XX    ',
'    XXXX  XXXXXXXXXXXXXX     XX    XXX            XX    ',
'                             XX    XXX            XX    ',
' X                           XX    XXX            XX    ',
'        X       XX           XX    XXXXXXXXXXXXXXXXX    ',
' XX    XXX            XX     XX    XXX            XX    ',
' XX X                        XX    XXX            XX    ',
' XXXX         XX         XX  XX    XXX            XX    ',
' XXXX       XX               XX    XXX            XX    ',
' XX    X  XXXX    XX  XX     XX    XXX            XX    ',
'       X  XXXX    XX  XXX    XX    XXX            XX    ',
'    XXXX  XXXXXX  XX  XXXX   XX    XXX            XX    ',
'    XXXX  XXXXXX  XX  XXXX   XX    XXX            XX    ',
'XXXXXXXX  XXXXXX  XX  XXXX   XX    XXX            XX    ']

level_map3 = [
'J      X    XX  XX                 XX                  M',
'            E                                           ',
'       T    XX                             X            ',
' XX    X                  X   X                         ',
' X  X                   X                       XXXX    ',
' XXXX         XX         XX                             ',
'X       XX             X           E                    ',
' X     X  XXXX    XX   X     XX    XXX                  ',
'       X  XXXX    XX T X     XX    XXX                  ',
'    XX    XXXX    XXXXXX       XXXXXXXX         XXXX    ',
'                               XX    XXEX           XX  ',
' X                           XX       XXX         XX    ',
'    X           XX           XX    XXXXX   XXXX    X    ',
' XX    XXX            XX     XX    XXX            XX    ',
' XX X                        XX    XXX            XX    ',
' XXXX         XX             EX   XXX               XX  ',
' XXXX       XX               XX    XXX            XX    ',
' XX    X  XXXX    XX  XX     XX    XXX            XX    ',
'      X                                                 ',
'    X          XX  XXXXX   X  XEXX                    XX',
'    X     X XX             X X X         XXX      XXXXX ',
'XXXX  XX         XX          X                   X      ']

level_map4 = [
'J      X    XX  XX                 XX                  M',
'            E                                           ',
'       X    XX                             X            ',
' EX    X                  X   X                         ',
' X  X                  T                        XXXX    ',
' XX           XX       XX                               ',
'X       XX                         E                    ',
' X     X     X    XX         XX    XXX                  ',
'       X  X  X    XX T X     XX    XXX                  ',
'    XX    X XX    XXXXXX       XT   XX          X  X    ',
'                               XX    XXEX           T   ',
' X                           EX        X            X   ',
'                XX           XX    X XX   X X     T     ',
' X  T  X X          XX             X X            X     ',
'  X X                              EX              X    ',
' X  X         XX            XE    XXX               X   ',
' X          XX               XX                    X    ',
' XX    X   X X    XX        XX    XXX                   ',
'      X                                                 ',
'    X          XX  X X T  X  X       E                 X',
'    X     X XX        X X X          X X     X X T      ',
'X  X  XX              XX          X              X      ']
level_map5 = [
'J      X    XX  XX                 XX                  M',
'            E                                           ',
'       X    XX                             X            ',
' TX    X                  X   X                         ',
' X  X                 XTX                       X  X    ',
' XX           XX       XX                               ',
'X        X                         E                    ',
' X     X     T     X         X     X X                  ',
'       X  X  X    X  X X     X     X                    ',
'     X    X X      X  X        XX    T          X  X    ',
'                                X    XXEX           T   ',
' X                           EX        X    X       XX  ',
'    X           XX           XX    X  X   X X     TX    ',
' X     X X          XX               X      X      X    ',
'  X T                              EX       X XXXX     X',
' X  X                       XE    XX        X        X  ',
' E           T               XX             X       X   ',
' XX    X   X X    XX        XX    X X      XX           ',
'      X                                                 ',
'    X          XX  X X    X  X       E     TT          X',
'    X     X XX        E X X          X X   XX    E      ',
'X  X  XX              XX          X              X      ']

level_map6 = [
'J                           XXX    XXX                 M',
'                                                        ',
'        E                                               ',
' XX    XXX           XXX                                ',
' XX                        E               XX           ',
' XXXX                    XXXXXX    XXXXXXXX       XX    ',
' XXXX         T                    XXX            XX    ',
' XX    X  XXXXXXXXXX         XXXXXXXXX            XXXXXX',
'       X  XXXX    XX  XXX           XX            XX    ',
'    XXXX  XXXXXX  XX  XXXX                        XX    ',
'                          XXXXXXX                       ',
'                             XX  XXXXX                  ',
'                                   XXX XXXXXXXXXXXXX    ',
' XX    XXX            XX     XX    X              XXXXXX',
' XX X                        XX    XXX            XX    ',
' XXXX         XX         XX  XX    XXX            XX    ',
' XXXX       XX               XX    XXX            XX    ',
' XX    X  XXXX    XX  XX     XX    XXX            E     ',
'       X  XXXX    XX  XXX    XX    XXX            XX    ',
'    XXXX  XXXXXX  XX  XXXX   XX    XXX            XX    ',
'    XXXX  XXXXXX  XX  XXXX   XX    XXX            XX    ',
'XXXXXXXX  XXXXXX  XX  XXXX   XX    XXX            XX    ']


tile_size = 32
linha_del = -1000
linha_add = 1792 #3584 #4584   # 5376
screen_width = 1200
tam_map = 1792
screen_height = len(level_map) * tile_size
estado = 'menu'  # estado do jogo

#1792  ---  56 --- 32