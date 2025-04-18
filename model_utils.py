
def get_hr_score(barrel_rate, exit_velocity, xSLG, sweet_spot, rpi,
                 hr9, hard_hit_pct, fatigue,
                 park_factor, wind_boost, temp_boost):
    # Final recalibrated BPS
    bps = (
        (barrel_rate * 1.25) +           # more realistic impact
        (exit_velocity * 1.0) +          
        (xSLG * 125) +                   # tighter top-end scaling
        (sweet_spot * 1.0)
    )

    # Pitcher HR/9 only (still scaled strong)
    pvs = hr9 * 30

    # Final score: more balanced
    total = bps * 0.7 + pvs * 0.3

    # Sleeper = good metrics but score under 85
    sleeper = (barrel_rate > 12 and xSLG > 0.500 and total < 85)

    return min(round(total, 1), 100), sleeper
