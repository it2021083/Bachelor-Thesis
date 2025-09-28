
import matplotlib.pyplot as plt
import numpy as np

from communication_technology import CommunicationTechnology
from data_type import DataType
from ship import Ship
from simulation_engine import SimulationEngine

# --- 1. Ορισμός Τεχνολογιών Επικοινωνίας ανά Εποχή ---

# Τεχνολογίες του 2010
techs_2010 = [
    CommunicationTechnology(name="Inmarsat FleetBroadband (FB500) (2010)", max_bandwidth_mbps=0.432, typical_latency_ms=850, reliability_percentage=99.9, availability_condition="Near Global", weather_impact_bandwidth_multiplier=0.9, is_primary=True),
    CommunicationTechnology(name="Inmarsat C (2010)", max_bandwidth_mbps=0.0006, typical_latency_ms=60000, reliability_percentage=99.9, availability_condition="Near Global", weather_impact_bandwidth_multiplier=1.0, is_primary=False),
    CommunicationTechnology(name="Iridium OpenPort (2010)", max_bandwidth_mbps=0.134, typical_latency_ms=650, reliability_percentage=99.0, availability_condition="Global", weather_impact_bandwidth_multiplier=0.95, is_primary=True),
    CommunicationTechnology(name="Maritime VSAT (C-band) (2010)", max_bandwidth_mbps=1.5, typical_latency_ms=750, reliability_percentage=99.5, availability_condition="Near Global", weather_impact_bandwidth_multiplier=0.8, is_primary=True),
    CommunicationTechnology(name="Maritime VSAT (Ku-band) (2010)", max_bandwidth_mbps=3.0, typical_latency_ms=750, reliability_percentage=98.5, availability_condition="Regional", weather_impact_bandwidth_multiplier=0.5, is_primary=True),
    CommunicationTechnology(name="3G (UMTS/HSPA) (2010)", max_bandwidth_mbps=4.5, typical_latency_ms=150, reliability_percentage=99.0, availability_condition="Coastal/Port", weather_impact_bandwidth_multiplier=0.95, is_primary=True),
    CommunicationTechnology(name="2G (GPRS/EDGE) (2010)", max_bandwidth_mbps=0.000236, typical_latency_ms=500, reliability_percentage=99.5, availability_condition="Coastal/Port", weather_impact_bandwidth_multiplier=1.0, is_primary=False),
]

# Τεχνολογίες του 2020 
techs_2020 = [
    CommunicationTechnology(name="Inmarsat Fleet Xpress (2020)", max_bandwidth_mbps=40.0, typical_latency_ms=650, reliability_percentage=99.9, availability_condition="Global", weather_impact_bandwidth_multiplier=0.4, is_primary=True),
    CommunicationTechnology(name="Maritime VSAT (HTS Ku-band) (2020)", max_bandwidth_mbps=100.0, typical_latency_ms=700, reliability_percentage=99.5, availability_condition="Regional", weather_impact_bandwidth_multiplier=0.5, is_primary=True),
    CommunicationTechnology(name="Maritime VSAT (HTS C-band) (2020)", max_bandwidth_mbps=50.0, typical_latency_ms=700, reliability_percentage=99.8, availability_condition="Near Global", weather_impact_bandwidth_multiplier=0.8, is_primary=True),
    CommunicationTechnology(name="Iridium Certus (2020)", max_bandwidth_mbps=0.704, typical_latency_ms=500, reliability_percentage=99.9, availability_condition="Global", weather_impact_bandwidth_multiplier=0.95, is_primary=True),
    CommunicationTechnology(name="Inmarsat FleetBroadband (2020)", max_bandwidth_mbps=0.432, typical_latency_ms=900, reliability_percentage=99.9, availability_condition="Near Global", weather_impact_bandwidth_multiplier=0.9, is_primary=False),
    CommunicationTechnology(name="Inmarsat C (2020)", max_bandwidth_mbps=0.0006, typical_latency_ms=60000, reliability_percentage=99.9, availability_condition="Near Global", weather_impact_bandwidth_multiplier=1.0, is_primary=False),
    CommunicationTechnology(name="4G (LTE/LTE-A) (2020)", max_bandwidth_mbps=50.0, typical_latency_ms=50, reliability_percentage=99.0, availability_condition="Coastal/Port (0-40 NM from shore)", weather_impact_bandwidth_multiplier=0.95, is_primary=True),
    CommunicationTechnology(name="5G (NR) (2020)", max_bandwidth_mbps=500.0, typical_latency_ms=20, reliability_percentage=99.0, availability_condition="Port", weather_impact_bandwidth_multiplier=0.9, is_primary=True)
]

# Υποθετικές Τεχνολογίες (2025-2030) - περιλαμβάνουν τις 2020 καθώς είναι αναβαθμίσεις
# Έχουν προστεθεί Starlink και 6G, και οι υποθετικές τεχνολογίες LaserCom και PicoSat
techs_2025_2030 = [
    CommunicationTechnology(name="Inmarsat Fleet Xpress (2020)", max_bandwidth_mbps=40.0, typical_latency_ms=650, reliability_percentage=99.9, availability_condition="Global", weather_impact_bandwidth_multiplier=0.4, is_primary=True),
    CommunicationTechnology(name="Maritime VSAT (HTS Ku-band) (2020)", max_bandwidth_mbps=100.0, typical_latency_ms=700, reliability_percentage=99.5, availability_condition="Regional", weather_impact_bandwidth_multiplier=0.5, is_primary=True),
    CommunicationTechnology(name="Maritime VSAT (HTS C-band) (2020)", max_bandwidth_mbps=50.0, typical_latency_ms=700, reliability_percentage=99.8, availability_condition="Near Global", weather_impact_bandwidth_multiplier=0.8, is_primary=True),
    CommunicationTechnology(name="Iridium Certus (2020)", max_bandwidth_mbps=0.704, typical_latency_ms=500, reliability_percentage=99.9, availability_condition="Global", weather_impact_bandwidth_multiplier=0.95, is_primary=True),
    CommunicationTechnology(name="Inmarsat FleetBroadband (2020)", max_bandwidth_mbps=0.432, typical_latency_ms=900, reliability_percentage=99.9, availability_condition="Near Global", weather_impact_bandwidth_multiplier=0.9, is_primary=False),
    CommunicationTechnology(name="Inmarsat C (2020)", max_bandwidth_mbps=0.0006, typical_latency_ms=60000, reliability_percentage=99.9, availability_condition="Near Global", weather_impact_bandwidth_multiplier=1.0, is_primary=False),

    # Νέες Τεχνολογίες που προστέθηκαν ( 6G λίγο αυθαίρετα, είναι η χρήση UAV εναέριων πλατφορμών για την διεύρυνση των επίγειων δικτύων(3G,4G,5G) σε θαλάσσιες περιοχές)
    CommunicationTechnology(name="Starlink (LEO) (2020-onwards)", max_bandwidth_mbps=250.0, typical_latency_ms=50, reliability_percentage=98.0, availability_condition="Global", weather_impact_bandwidth_multiplier=0.7, is_primary=True),
    CommunicationTechnology(name="6G (NR) (2025-onwards)", max_bandwidth_mbps=1000.0, typical_latency_ms=10, reliability_percentage=99.5, availability_condition="Regional", weather_impact_bandwidth_multiplier=0.85, is_primary=True),
    
    # Νέες Υποθετικές Τεχνολογίες
    CommunicationTechnology(name="Satellite Laser Communications (Lasercom)", max_bandwidth_mbps=50000.0, typical_latency_ms=35, reliability_percentage=99.0, availability_condition="Regional", weather_impact_bandwidth_multiplier=0.3, is_primary=True), # Πολύ ευαίσθητο στον καιρό
    CommunicationTechnology(name="Picosatellite Constellations", max_bandwidth_mbps=5.0, typical_latency_ms=65, reliability_percentage=98.0, availability_condition="Near Global", weather_impact_bandwidth_multiplier=0.95, is_primary=True) # Χαμηλότερο bandwidth, πολύ αξιόπιστο
]


# --- 2. Ορισμός Τύπων Δεδομένων για Αυτόνομη Λειτουργία ---

autonomous_data_types = [
    # Δεδομένα Ελέγχου και Λειτουργίας του Πλοίου (Critical Operational Data)
    DataType(name="GPS/GNSS Δεδομένα", size_kb_per_unit=0.3, priority="Critical", transmit_type="TX",
             unit_time_sec=1, latency_tolerance_ms=100, transmission_duration_sec=1, traffic_type="streaming",
             processed_data_reduction_factor=0.9),
    DataType(name="Δεδομένα AIS", size_kb_per_unit=0.2, priority="Critical", transmit_type="TX",
             unit_time_sec=5, latency_tolerance_ms=500, transmission_duration_sec=1, traffic_type="periodic",
             processed_data_reduction_factor=0.9),
    DataType(name="Δεδομένα Ραντάρ (επεξεργασμένα)", size_kb_per_unit=50, priority="Critical", transmit_type="TX",
             unit_time_sec=1, latency_tolerance_ms=150, transmission_duration_sec=1, traffic_type="streaming",
             processed_data_reduction_factor=0.5),
    DataType(name="Δεδομένα Ραντάρ (ακατέργαστα - High Resolution)", size_kb_per_unit=2500, priority="High", transmit_type="TX",
             unit_time_sec=3600, latency_tolerance_ms=500, transmission_duration_sec=5, traffic_type="on-demand",
             processed_data_reduction_factor=0.05),
    DataType(name="Δεδομένα LiDAR (σημεία νέφους)", size_kb_per_unit=5000, priority="High", transmit_type="TX",
             unit_time_sec=3600, latency_tolerance_ms=500, transmission_duration_sec=10, traffic_type="on-demand",
             processed_data_reduction_factor=0.02),
    DataType(name="Live Camera Feeds (compressed)", size_kb_per_unit=2500, priority="Critical", transmit_type="TX",
             unit_time_sec=1, latency_tolerance_ms=150, transmission_duration_sec=1, traffic_type="streaming",
             processed_data_reduction_factor=0.2), 
    DataType(name="Ενημερώσεις Ηλεκτρονικών Χαρτών (ENC)", size_kb_per_unit=500, priority="High", transmit_type="RX",
             unit_time_sec=86400, latency_tolerance_ms=3600000, transmission_duration_sec=60, traffic_type="periodic",
             processed_data_reduction_factor=0.8), 
    DataType(name="Τηλεμετρία Μηχανών/Συστημάτων", size_kb_per_unit=30, priority="Critical", transmit_type="TX",
             unit_time_sec=1, latency_tolerance_ms=200, transmission_duration_sec=1, traffic_type="streaming",
             processed_data_reduction_factor=0.7), 
    DataType(name="Διαγνωστικά Δεδομένα (Προγνωστική Συντήρηση)", size_kb_per_unit=500, priority="High", transmit_type="TX",
             unit_time_sec=300, latency_tolerance_ms=1000, transmission_duration_sec=10, traffic_type="periodic",
             processed_data_reduction_factor=0.3), 
    DataType(name="Εντολές Ελέγχου (Πλοήγηση/Μηχανές)", size_kb_per_unit=2, priority="Critical", transmit_type="RX",
             unit_time_sec=1, latency_tolerance_ms=50, transmission_duration_sec=0.1, traffic_type="event-driven",
             processed_data_reduction_factor=0.95),
    DataType(name="Ενημερώσεις Λογισμικού (Over-The-Air)", size_kb_per_unit=50000, priority="High", transmit_type="RX",
             unit_time_sec=2592000, latency_tolerance_ms=86400000, transmission_duration_sec=3600, traffic_type="batch",
             processed_data_reduction_factor=0.8), 
    DataType(name="Αρχεία Καταγραφής (Logs) Συστημάτων", size_kb_per_unit=5000, priority="Medium", transmit_type="TX",
             unit_time_sec=3600, latency_tolerance_ms=7200000, transmission_duration_sec=60, traffic_type="periodic",
             processed_data_reduction_factor=0.1), 

    # Δεδομένα Ασφαλείας και Ασφάλειας (Safety & Security Data)
    DataType(name="GMDSS/Distress Alerts", size_kb_per_unit=0.5, priority="Critical", transmit_type="TX",
             unit_time_sec=1, latency_tolerance_ms=100, transmission_duration_sec=0.1, traffic_type="event-driven",
             processed_data_reduction_factor=0.99),
    DataType(name="SSAS (Ship Security Alert)", size_kb_per_unit=0.1, priority="Critical", transmit_type="TX",
             unit_time_sec=1, latency_tolerance_ms=100, transmission_duration_sec=0.1, traffic_type="event-driven",
             processed_data_reduction_factor=0.99),
    DataType(name="Navtex/SafetyNET Messages", size_kb_per_unit=5, priority="Critical", transmit_type="RX",
             unit_time_sec=3600, latency_tolerance_ms=300000, transmission_duration_sec=5, traffic_type="periodic",
             processed_data_reduction_factor=0.9), 
    DataType(name="CCTV Feeds (Security - On-Demand)", size_kb_per_unit=2500, priority="High", transmit_type="TX",
             unit_time_sec=3600, latency_tolerance_ms=500, transmission_duration_sec=1, traffic_type="on-demand",
             processed_data_reduction_factor=0.15),
    DataType(name="Cybersecurity Logs", size_kb_per_unit=500, priority="High", transmit_type="TX",
             unit_time_sec=3600, latency_tolerance_ms=3600000, transmission_duration_sec=30, traffic_type="periodic",
             processed_data_reduction_factor=0.1), 
    DataType(name="Ενημερώσεις Cybersecurity", size_kb_per_unit=5000, priority="High", transmit_type="RX",
             unit_time_sec=86400, latency_tolerance_ms=3600000, transmission_duration_sec=60, traffic_type="batch",
             processed_data_reduction_factor=0.7), 

    # Δεδομένα Φορτίου και Εμπορικής Λειτουργίας (Cargo & Commercial Data)
    DataType(name="Δεδομένα Κατάστασης Φορτίου", size_kb_per_unit=50, priority="High", transmit_type="TX",
             unit_time_sec=60, latency_tolerance_ms=60000, transmission_duration_sec=5, traffic_type="periodic",
             processed_data_reduction_factor=0.4), 
    DataType(name="Δεδομένα Βελτιστοποίησης Διαδρομής", size_kb_per_unit=50, priority="High", transmit_type="RX",
             unit_time_sec=86400, latency_tolerance_ms=3600000, transmission_duration_sec=30, traffic_type="periodic",
             processed_data_reduction_factor=0.8), 
    DataType(name="Δελτία Καιρού/Ωκεανογραφικά", size_kb_per_unit=250, priority="High", transmit_type="RX",
             unit_time_sec=21600, latency_tolerance_ms=7200000, transmission_duration_sec=10, traffic_type="periodic",
             processed_data_reduction_factor=0.6), 
    DataType(name="Τελωνειακά/Λιμενικά Έγγραφα", size_kb_per_unit=500, priority="Medium", transmit_type="Both",
             unit_time_sec=10800, latency_tolerance_ms=1800000, transmission_duration_sec=60, traffic_type="on-demand",
             processed_data_reduction_factor=0.5), 

    # Δεδομένα Υποδομής και Διαχείρισης (Infrastructure & Management Data)
    DataType(name="VoIP Επικοινωνία (Κέντρο Ελέγχου)", size_kb_per_unit=150, priority="High", transmit_type="Both",
             unit_time_sec=1, latency_tolerance_ms=200, transmission_duration_sec=1, traffic_type="streaming",
             processed_data_reduction_factor=0.3), 
    DataType(name="Δεδομένα Ενεργειακής Απόδοσης", size_kb_per_unit=30, priority="Medium", transmit_type="TX",
             unit_time_sec=60, latency_tolerance_ms=60000, transmission_duration_sec=1, traffic_type="periodic",
             processed_data_reduction_factor=0.5), 
    DataType(name="Health Monitoring (General)", size_kb_per_unit=10, priority="Medium", transmit_type="TX",
             unit_time_sec=60, latency_tolerance_ms=60000, transmission_duration_sec=1, traffic_type="periodic",
             processed_data_reduction_factor=0.7), 
    DataType(name="Δεδομένα Telepresence/Virtual Reality", size_kb_per_unit=25000, priority="High", transmit_type="Both",
             unit_time_sec=3600, latency_tolerance_ms=500, transmission_duration_sec=30, traffic_type="on-demand",
             processed_data_reduction_factor=0.05) 
]


if __name__ == "__main__":
    # Δημιουργία αντικειμένων Ship (τεχνολογίες που υπάρχουν και έχουν γνωστά όρια)
    ship_2010 = Ship("Simple Ship (2010)", 2010, techs_2010)
    ship_2020 = Ship("Autonomous Ship (2020)", 2020, techs_2020)
    # Νέο πλοίο με τις υποθετικές τεχνολογίες
    ship_2025 = Ship("Advanced Autonomous Ship (2025)", 2025, techs_2025_2030)

    # Εκτέλεση προσομοίωσης με όλα τα πλοία
    simulator = SimulationEngine([ship_2010, ship_2020, ship_2025], autonomous_data_types)

    print("\n--- Scenario 1: Deep Ocean, Normal Weather ---")
    simulator.run_simulation(duration_hours=24, location_scenario="Deep Ocean", weather_scenario="Normal")
    simulator.plot_results(scenario_name="Ocean_Normal_Weather")

    print("\n--- Scenario 2: Ocean, Storm ---")
    simulator.run_simulation(duration_hours=24, location_scenario="Ocean", weather_scenario="Storm")
    simulator.plot_results(scenario_name="Ocean_Storm")

    print("\n--- Scenario 3: Polar, Normal ---")
    simulator.run_simulation(duration_hours=24, location_scenario="Polar", weather_scenario="Normal")
    simulator.plot_results(scenario_name="Polar_Normal_Weather")

    print("\n--- Scenario 4: Coastal, Rain ---")
    simulator.run_simulation(duration_hours=24, location_scenario="Coastal", weather_scenario="Rain")
    simulator.plot_results(scenario_name="Coastal_Rain")

    print("\n--- Scenario 5: Port, Normal Weather ---")
    simulator.run_simulation(duration_hours=24, location_scenario="Port", weather_scenario="Normal")
    simulator.plot_results(scenario_name="Port_Normal_Weather")

    