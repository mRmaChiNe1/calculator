import pstats
from pstats import SortKey
p = pstats.Stats('profile_data.txt')
p.strip_dirs().sort_stats(SortKey.TIME).print_stats()