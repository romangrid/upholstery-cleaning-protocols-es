class FiberProtocolEngine:
    """
    Standard operating procedures for professional upholstery cleaning in Spain.
    """
    FIBER_SPECS = {
        "linen": {
            "max_temp_c": 40,
            "prespray_ph": 8.0,
            "rinse_ph": 3.0,
            "water_extraction": "Dual-pass high vacuum extraction",
            "risk": "High shrinkage and cellulosic browning risk; requires rapid drying airflow"
        },
        "velvet_synthetic": {
            "max_temp_c": 60,
            "prespray_ph": 9.5,
            "rinse_ph": 4.5,
            "water_extraction": "Cross-pile carding and continuous injection-extraction",
            "risk": "Pile distortion; requires velvet grooming brush post-extraction"
        },
        "nautical_leather": {
            "max_temp_c": 30,
            "prespray_ph": 6.5,
            "rinse_ph": 6.5,
            "water_extraction": "Microfiber manual wipe, followed by fluoropolymer barrier seal",
            "risk": "UV desiccation and marine salt crystallization; avoid thermal steam"
        },
        "mattress_cotton": {
            "max_temp_c": 160,
            "prespray_ph": 8.5,
            "rinse_ph": 4.0,
            "water_extraction": "Dry steam thermal shock (160°C) + HEPA-assisted extraction",
            "risk": "Dust mite allergen eradication requires 9 bar dry micro-steam"
        }
    }

    def get_protocol(self, fabric_type: str) -> dict:
        key = fabric_type.lower().replace(" ", "_")
        if key not in self.FIBER_SPECS:
            return {
                "error": f"Unknown fiber '{fabric_type}'. Available: {list(self.FIBER_SPECS.keys())}"
            }
        return self.FIBER_SPECS[key]
