"""Created on Sep 06 16:26:36 2022."""

from numpy import array

from src.constellations.utilities.Constellations import constellations

star_names = {0: 'alpha', 1: 'beta', 2: 'gamma', 3: 'delta', 4: 'epsilon', 5: 'zeta', 6: 'eta', 7: 'theta', 8: 'iota',
              9: 'kappa', 10: 'lambda', 11: 'mu', 12: 'nu^1', 13: 'nu^2', 14: 'nu^3', 15: 'xi^1', 16: 'xi^2',
              17: 'omicron^1', 18: 'omicron^2', 19: 'pi', 20: 'sigma', 21: 'tau', 22: 'omega'}

canis_major_coordinates = array([('06:45:08.91700', '-16:42:58.0200'), ('06:22:41.98535', '-17:57:21.3073'),
                                 ('07:03:45.49305', '-15:37:59.8300'), ('07:08:23.48608', '-26:23:35.5474'),
                                 ('06:58:37.60000', '-28:58:19.0000'), ('06:20:18.79204', '-30:03:48.1202'),
                                 ('07:24:05.70228', '-29:18:11.1789'), ('06:54:11.93877', '-12:02:19.0674'),
                                 ('06:56:08.22413', '-17:03:15.2675'), ('06:49:50.45933', '-32:30:30.5225'),
                                 ('06:28:10.20747', '-32:34:48.2455'), ('06:56:06.64589', '-14:02:36.3520'),
                                 ('06:36:22.85133', '-18:39:35.6838'), ('06:36:41.03758', '-19:15:21.1659'),
                                 ('06:37:53.42144', '-18:14:14.9218'), ('06:31:51.36636', '-23:52:06.3181'),
                                 ('06:35:03.38859', '-22:57:53.2913'), ('06:54:07.95237', '-24:11:03.1597'),
                                 ('07:03:01.47211', '-23:49:59.8523'), ('06:55:37.43099', '-20:08:11.3902'),
                                 ('07:01:43.14779', '-27:56:05.3898'), ('07:18:42.48648', '-24:57:15.7413'),
                                 ('07:14:48.65387', '-26:46:21.6097')])

draw_line = [(0, 1), (0, 18), (18, 3), (3, 20), (3, 6), (20, 4), (0, 8), (8, 2), (2, 7), (7, 8),
             (1, 13), (13, 17), (17, 4)]

constellations(coordinates=canis_major_coordinates, star_names=star_names, constellation_name='Canis Major',
               short_name='cma', line_coordinates=draw_line)