# Configuration 1: Rapid execution with a low issue rate
FloatSimdFU = MinorFU(opLat=1, issueLat=6, count=1)

# Configuration 2: Moderate execution alongside a moderate issue rate
FloatSimdFU = MinorFU(opLat=2, issueLat=5, count=1)

# Configuration 3: Equally balanced execution and issue rate
FloatSimdFU = MinorFU(opLat=3, issueLat=4, count=1)

# Configuration 4: Reduced execution speed with an increased issue rate
FloatSimdFU = MinorFU(opLat=4, issueLat=3, count=1)

# Configuration 5: Elevated execution speed with a rapid issue rate
FloatSimdFU = MinorFU(opLat=5, issueLat=2, count=1)

# Configuration 6: Extremely high execution latency paired with an exceptionally fast issue rate
FloatSimdFU = MinorFU(opLat=6, issueLat=1, count=1)
