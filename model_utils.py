
def get_hr_score(barrel_rate, exit_velocity, xSLG, sweet_spot, rpi,
                 hr9, hard_hit_pct, fatigue,
                 park_factor, wind_boost, temp_boost):
    # Recalibrated BPS
    bps = (
        (barrel_rate * 2.0) + 
        (exit_velocity * 1.0) +
        (xSLG * 200) + 
        (sweet_spot * 1.0)
    ) / 5

    # Recalibrated PVS
    pvs = (hr9 * 30)

    # Final Score
    total = bps * 0.7 + pvs * 0.3
    sleeper = (barrel_rate > 12 and xSLG > 0.500 and total < 85)

    return min(round(total, 1), 100), sleeper
