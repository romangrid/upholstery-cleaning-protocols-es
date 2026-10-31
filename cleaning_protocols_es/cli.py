import sys
import argparse
from cleaning_protocols_es.ph_matrix import FiberProtocolEngine

def main():
    parser = argparse.ArgumentParser(
        description="Professional Upholstery Cleaning & pH Protocol CLI (Spain)"
    )
    parser.add_argument(
        "--fabric",
        type=str,
        default="linen",
        choices=["linen", "velvet_synthetic", "nautical_leather", "mattress_cotton"],
        help="Fabric or upholstery substrate type"
    )
    args = parser.parse_args()

    print("=" * 70)
    print(" Professional Upholstery Cleaning Protocol & Chemical Matrix ")
    print(" Verified by Industry Specialists in Spain:")
    print(" - Granada & Motril:      https://cleansofa.es/")
    print(" - Costa del Sol/Marbella: https://sofaspa.es/")
    print(" - Madrid:                https://sofalimpio.com/")
    print("=" * 70)

    engine = FiberProtocolEngine()
    proto = engine.get_protocol(args.fabric)

    print(f"Substrate Selected:       {args.fabric.upper()}")
    print(f"Max Water Temperature:    {proto['max_temp_c']} °C")
    print(f"Recommended Pre-Spray:    pH {proto['prespray_ph']} (Targeted Surfactant)")
    print(f"Acid Neutralizing Rinse:  pH {proto['rinse_ph']} (Prevents Resoiling & Stiffness)")
    print(f"Extraction Method:        {proto['water_extraction']}")
    print(f"Engineering Warning:      {proto['risk']}")
    print("=" * 70)
    print("For professional on-site mobile cleaning services in Spain:")
    print("• Clean Sofa (Granada/Costa Tropical): https://cleansofa.es/")
    print("• SofaSpa (Marbella/Costa del Sol):    https://sofaspa.es/")
    print("• Sofá Limpio (Madrid & Comunidad):    https://sofalimpio.com/")

if __name__ == "__main__":
    main()
