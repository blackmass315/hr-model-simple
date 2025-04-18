
def get_hr_score(barrel_rate, exit_velocity, xSLG, sweet_spot, rpi,
                 hr9, hard_hit_pct, fatigue,
                 park_factor, wind_boost, temp_boost):
    # Recalibrated BPS with softened weights
    bps = (
        (barrel_rate * 1.5) +          # Slightly reduced barrel rate impact
        (exit_velocity * 1.0) +        # Keep EV strong
        (xSLG * 150) +                 # xSLG impact reduced from 200 → 150
        (sweet_spot * 1.0)
    )

    # Pitcher HR/9 only
    pvs = hr9 * 30

    # Final blended score
    total = bps * 0.7 + pvs * 0.3

    # Sleeper = good stats but total still < 85
    sleeper = (barrel_rate > 12 and xSLG > 0.500 and total < 85)

    return min(round(total, 1), 100), sleeper
