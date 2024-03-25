"""Created on Oct 03 16:13:48 2022."""

from numpy import array

from utilities.Constellations import constellations

star_names = {0: 'alpha', 1: 'beta', 2: 'gamma', 3: 'delta^1', 4: 'delta^2', 5: 'epsilon^{1, 2}', 6: 'zeta^1',
              7: 'zeta^2', 8: 'eta', 9: 'theta', 10: 'iota', 11: 'kappa', 12: 'lambda', 13: 'mu', 14: 'nu^1',
              15: 'nu^2'}

lyra_coordinates = array([('18:36:53.33635', '38:47:01.2802'), ('18:50:04.79525', '33:21:45.6100'),
                          ('18:58:56.62241', '32:41:22.4003'), ('18:53:43.55924', '36:58:18.1891'),
                          ('18:54:30.28380', '36:53:55.0070'), ('18:44:20.34589', '39:40:12.4533'),
                          ('18:44:46.35735', '37:36:18.4171'), ('18:44:48.19919', '37:35:40.5585'),
                          ('19:13:45.48832', '39:08:45.4801'), ('19:16:22.09510', '38:08:01.4310'),
                          ('19:07:18.13251', '36:06:00.5592'), ('18:19:51.70908', '36:03:52.3691'),
                          ('19:00:00.82534', '32:08:43.8418'), ('18:24:13.78599', '39:30:26.0473'),
                          ('18:49:45.91431', '32:48:46.1656'), ('18:49:52.91721', '32:33:03.8153')])

draw_lines = [(0, 5), (0, 6), (5, 6), (6, 1), (1, 2), (2, 3), (3, 6)]

constellations(coordinates=lyra_coordinates, star_names=star_names, constellation_name='Lyra', short_name='lyr',
               line_coordinates=draw_lines)