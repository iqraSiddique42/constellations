"""Created on Sep 17 16:56:09 2022."""

from numpy import array

from utilities.Constellations import constellations

star_names = {0: 'alpha', 1: 'beta', 2: 'gamma', 3: 'delta', 4: 'epsilon', 5: 'zeta^1', 6: 'zeta^2', 7: 'eta',
              8: 'theta', 9: 'iota', 10: 'kappa', 11: 'lambda', 12: 'mu', 13: 'nu^1', 14: 'nu^2', 15: 'xi',
              16: 'omicron', 17: 'pi', 18:'rho', 19: 'sigma', 20: 'tau', 21: 'upsilon'}

corona_borealis_coordinates = array([('15:34:41.26800', '26:42:52.8900'), ('15:27:49.73080', '29:06:20.5300'),
                                     ('15:42:44.56551', '26:17:44.2847'), ('15:49:35.64682', '26:04:06.2065'),
                                     ('15:57:35.25147', '26:52:40.3635'), ('15:39:22.24700', '36:38:12.4200'),
                                     ('15:39:22.66800', '36:38:08.7800'), ('15:23:12.31000', '30:17:16.1700'),
                                     ('15:32:55.78214', '31:21:32.8762'), ('16:01:26.56488', '29:51:03.8243'),
                                     ('15:51:13.93150', '35:39:26.5647'), ('15:55:47.58774', '37:56:49.0397'),
                                     ('15:35:14.91848', '39:00:36.2473'), ('16:22:21.42545', '33:47:56.5825'),
                                     ('16:22:29.21855', '33:42:12.5274'), ('16:22:05.82391', '30:53:31.1837'),
                                     ('15:20:08.55900', '29:36:58.3500'), ('15:43:59.29973', '32:30:56.9047'),
                                     ('16:01:02.66200', '33:18:12.6300'), ('16:14:40.85400', '33:51:31.0200'),
                                     ('16:08:58.30151', '36:29:27.3740'), ('16:16:44.78733', '29:09:00.9399')])

draw_lines = [(0, 1), (1, 8), (0, 2), (2, 3), (3, 4), (4, 9)]

constellations(coordinates=corona_borealis_coordinates, star_names=star_names, constellation_name='Corona Borealis',
               short_name='crb', line_coordinates=draw_lines)
