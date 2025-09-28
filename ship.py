import random 

from communication_technology import CommunicationTechnology
from data_type import DataType

class Ship:
    def __init__(self, name, year, communication_technologies):
        self.name = name
        self.year = year
        self.communication_technologies = communication_technologies
        self.telemetry_history = {} 

        self.default_latency_tolerances = {
            "Critical": 150,
            "High": 500,
            "Medium": 2000,
            "Low": 5000
        }

        self._initialize_tech_lookup() # Καλείται πρώτο για να γεμίσει το self.tech_lookup

        # Καθορισμός προτιμώμενης σειράς τεχνολογιών ανά προτεραιότητα δεδομένων
        # Βασίζεται στο 'year' του πλοίου για να χρησιμοποιεί τις σωστές λίστες.
        self.priority_tech_preference = self._get_tech_preferences_by_year(year)
        
        self.total_successful_data_transfers_overall = 0
        self.total_failed_data_transfers_overall = 0

    def _initialize_tech_lookup(self):
        """Δημιουργεί ένα lookup dictionary για τις τεχνολογίες του πλοίου."""
        self.tech_lookup = {tech.name: tech for tech in self.communication_technologies}

    def _get_tech_preferences_by_year(self, year):
        """
        Επιστρέφει ένα dictionary με τις προτιμήσεις τεχνολογιών
        ανάλογα με το έτος του πλοίου.
        """
        if year == 2010:
            return {
                "Critical": [
                    "Maritime VSAT (C-band) (2010)",
                    "Inmarsat FleetBroadband (FB500) (2010)", 
                    "Iridium OpenPort (2010)", 
                    "3G (UMTS/HSPA) (2010)",
                    "Inmarsat C (2010)", 
                    "2G (GPRS/EDGE) (2010)"
                ],
                "High": [
                    "Maritime VSAT (C-band) (2010)",
                    "Inmarsat FleetBroadband (FB500) (2010)",
                    "Iridium OpenPort (2010)",
                    "3G (UMTS/HSPA) (2010)",
                    "Maritime VSAT (Ku-band) (2010)", 
                    "Inmarsat C (2010)",
                    "2G (GPRS/EDGE) (2010)"
                ],
                "Medium": [
                    "Inmarsat FleetBroadband (FB500) (2010)",
                    "Maritime VSAT (C-band) (2010)",
                    "Iridium OpenPort (2010)",
                    "3G (UMTS/HSPA) (2010)",
                    "Maritime VSAT (Ku-band) (2010)",
                    "Inmarsat C (2010)",
                    "2G (GPRS/EDGE) (2010)"
                ],
                "Low": [
                    "Inmarsat C (2010)",
                    "2G (GPRS/EDGE) (2010)",
                    "Inmarsat FleetBroadband (FB500) (2010)",
                    "Iridium OpenPort (2010)",
                    "Maritime VSAT (C-band) (2010)",
                    "3G (UMTS/HSPA) (2010)",
                    "Maritime VSAT (Ku-band) (2010)"
                ]
            }
        elif year == 2020:
            return {
                "Critical": [
                    "5G (NR) (2020)", 
                    "4G (LTE/LTE-A) (2020)", 
                    "Inmarsat Fleet Xpress (2020)",
                    "Maritime VSAT (HTS Ku-band) (2020)",
                    "Maritime VSAT (HTS C-band) (2020)", 
                    "Iridium Certus (2020)",
                    "Inmarsat FleetBroadband (2020)",
                    "Inmarsat C (2020)" 
                ],
                "High": [
                    "5G (NR) (2020)",
                    "4G (LTE/LTE-A) (2020)",
                    "Maritime VSAT (HTS Ku-band) (2020)",
                    "Inmarsat Fleet Xpress (2020)",
                    "Maritime VSAT (HTS C-band) (2020)",
                    "Iridium Certus (2020)",
                    "Inmarsat FleetBroadband (2020)",
                    "Inmarsat C (2020)"
                ],
                "Medium": [
                    "Maritime VSAT (HTS Ku-band) (2020)",
                    "Inmarsat Fleet Xpress (2020)",
                    "Iridium Certus (2020)",
                    "4G (LTE/LTE-A) (2020)",
                    "5G (NR) (2020)",
                    "Inmarsat FleetBroadband (2020)",
                    "Inmarsat C (2020)",
                    "Maritime VSAT (HTS C-band) (2020)"
                ],
                "Low": [
                    "Inmarsat FleetBroadband (2020)",
                    "Iridium Certus (2020)",
                    "Inmarsat C (2020)",
                    "Maritime VSAT (HTS Ku-band) (2020)",
                    "Inmarsat Fleet Xpress (2020)",
                    "4G (LTE/LTE-A) (2020)",
                    "5G (NR) (2020)",
                    "Maritime VSAT (HTS C-band) (2020)"
                ]
            }
        elif year == 2025: 
            return {
                "Critical": [
                    "6G (NR) (2025-onwards)", 
                    "Satellite Laser Communications (Lasercom)", 
                    "5G (NR) (2020)",
                    "Starlink (LEO) (2020-onwards)",
                    "4G (LTE/LTE-A) (2020)",
                    "Inmarsat Fleet Xpress (2020)",
                    "Maritime VSAT (HTS Ku-band) (2020)",
                    "Maritime VSAT (HTS C-band) (2020)",
                    "Iridium Certus (2020)",
                    "Picosatellite Constellations", 
                    "Inmarsat FleetBroadband (2020)",
                    "Inmarsat C (2020)"
                ],
                "High": [
                    "Satellite Laser Communications (Lasercom)",
                    "6G (NR) (2025-onwards)",
                    "Starlink (LEO) (2020-onwards)",
                    "Maritime VSAT (HTS Ku-band) (2020)",
                    "Inmarsat Fleet Xpress (2020)",
                    "5G (NR) (2020)",
                    "4G (LTE/LTE-A) (2020)",
                    "Maritime VSAT (HTS C-band) (2020)",
                    "Iridium Certus (2020)",
                    "Picosatellite Constellations",
                    "Inmarsat FleetBroadband (2020)",
                    "Inmarsat C (2020)"
                ],
                "Medium": [
                    "Starlink (LEO) (2020-onwards)",
                    "Maritime VSAT (HTS Ku-band) (2020)",
                    "Inmarsat Fleet Xpress (2020)",
                    "Iridium Certus (2020)",
                    "Satellite Laser Communications (Lasercom)",
                    "6G (NR) (2025-onwards)",
                    "4G (LTE/LTE-A) (2020)",
                    "5G (NR) (2020)",
                    "Picosatellite Constellations",
                    "Inmarsat FleetBroadband (2020)",
                    "Inmarsat C (2020)",
                    "Maritime VSAT (HTS C-band) (2020)"
                ],
                "Low": [
                    "Picosatellite Constellations",
                    "Inmarsat FleetBroadband (2020)",
                    "Iridium Certus (2020)",
                    "Inmarsat C (2020)",
                    "Starlink (LEO) (2020-onwards)",
                    "Maritime VSAT (HTS Ku-band) (2020)",
                    "Inmarsat Fleet Xpress (2020)",
                    "4G (LTE/LTE-A) (2020)",
                    "5G (NR) (2020)",
                    "Satellite Laser Communications (Lasercom)",
                    "6G (NR) (2025-onwards)",
                    "Maritime VSAT (HTS C-band) (2020)"
                ]
            }
        else:
            # Raise error
            print(f"Warning: No tolerated year input.")
            # Μπορείς να επιστρέψεις μια κενή λίστα 
            return None


    def attempt_data_transfer(self, data_type, current_location_type="Ocean", weather_multiplier=1.0):
        """
        Προσπαθεί να μεταφέρει έναν τύπο δεδομένων χρησιμοποιώντας τις διαθέσιμες τεχνολογίες.
        Εφαρμόζει λογική failover.
        Επιστρέφει την τεχνολογία που χρησιμοποιήθηκε (αν επιτυχής) και τη διάρκεια της μεταφοράς,
        αλλιώς None, None.
        """
        required_data_rate_for_transfer = data_type.get_required_data_rate_mbps()
        
        required_latency_ms = data_type.latency_tolerance_ms \
                              if data_type.latency_tolerance_ms is not None \
                              else self.default_latency_tolerances.get(data_type.priority, 5000)

        tech_preference_names = self.priority_tech_preference.get(data_type.priority, [])
        # Χρησιμοποιούμε self.tech_lookup για γρήγορη πρόσβαση στα αντικείμενα τεχνολογίας
        available_techs_for_data = [self.tech_lookup[name] for name in tech_preference_names if name in self.tech_lookup]

        for tech in available_techs_for_data:
            is_available_by_location = False
            # Λογική διαθεσιμότητας
            if "Global" in tech.availability_condition:
                is_available_by_location = True
            elif "Near Global" in tech.availability_condition and current_location_type in ["Deep Ocean", "Ocean", "Coastal", "Port"]:
                is_available_by_location = True
            elif "Regional" in tech.availability_condition and current_location_type in ["Ocean", "Coastal", "Port"]:
                is_available_by_location = True
            elif "Coastal/Port" in tech.availability_condition and current_location_type in ["Coastal", "Port"]:
                is_available_by_location = True


            if not is_available_by_location:
                tech.failed_transfers_availability += 1
                continue 

            effective_bw = tech.get_effective_bandwidth(weather_multiplier)
            effective_latency = tech.get_effective_latency(weather_multiplier)

            if effective_bw >= required_data_rate_for_transfer and effective_latency <= required_latency_ms:
                # Επιτυχής μεταφορά:
                tech.successful_transfers += 1
                tech.total_data_handled_mb += (data_type.get_effective_size_kb() / 1000.0) # KB to MB
                
                self.total_successful_data_transfers_overall += 1
                return tech, data_type.transmission_duration_sec
            elif effective_bw < required_data_rate_for_transfer:
                tech.failed_transfers_capacity += 1
            elif effective_latency > required_latency_ms:
                tech.failed_transfers_latency += 1

        self.total_failed_data_transfers_overall += 1
        return None, None

    def reset_tech_metrics(self):
        for tech in self.communication_technologies:
            tech.reset_metrics()
        self.total_successful_data_transfers_overall = 0
        self.total_failed_data_transfers_overall = 0

    def __str__(self):
        return f"Ship: {self.name} ({self.year} Technologies)"