# simulation_engine.py

import random
from ship import Ship
from data_type import DataType
from communication_technology import CommunicationTechnology
import matplotlib.pyplot as plt
import numpy as np

class SimulationEngine:
    def __init__(self, ships, autonomous_data_types):
        self.ships = ships
        self.autonomous_data_types = autonomous_data_types
        self.results = {} # Θα αποθηκεύσει τα αποτελέσματα της προσομοίωσης

    def run_simulation(self, duration_hours=24, location_scenario="Ocean", weather_scenario="Normal"):
        """
        Εκτελεί την προσομοίωση για ένα συγκεκριμένο χρονικό διάστημα με χρονικό βήμα 1 δευτερόλεπτο.
        :param duration_hours: Διάρκεια προσομοίωσης σε ώρες.
        :param location_scenario: "Ocean", "Coastal", "Port" - Καθορίζει τη γεωγραφική θέση για διαθεσιμότητα τεχνολογιών.
        :param weather_scenario: "Normal", "Rain", "Heavy Rain", "Storm" - Επηρεάζει την απόδοση των τεχνολογιών.
        """
        print(f"Starting simulation for {duration_hours} hours in {location_scenario} with {weather_scenario} weather...")

        # Reset metrics for all ships and technologies before a new run
        for ship in self.ships:
            ship.reset_tech_metrics()

        # Καθορισμός weather_multiplier
        weather_multiplier = 1.0
        if weather_scenario == "Rain":
            weather_multiplier = 0.8
        elif weather_scenario == "Heavy Rain":
            weather_multiplier = 0.5
        elif weather_scenario == "Storm":
            weather_multiplier = 0.3

        total_simulation_seconds = duration_hours * 3600

        # Προσομοίωση κάθε δευτερολέπτου
        for current_second in range(total_simulation_seconds):
            for ship in self.ships:
                for data_type in self.autonomous_data_types:
                    # Λογική για την ενεργοποίηση της μεταφοράς δεδομένων:
                    should_attempt_transfer = False

                    if data_type.traffic_type == "streaming":
                        # Συνεχής ροή, προσπάθεια κάθε unit_time_sec (1 δευτερόλεπτο)
                        if (current_second % data_type.unit_time_sec) == 0:
                            should_attempt_transfer = True
                    elif data_type.traffic_type == "periodic":
                        # Περιοδικά δεδομένα, προσπάθεια κάθε unit_time_sec
                        if (current_second % data_type.unit_time_sec) == 0:
                            should_attempt_transfer = True
                    elif data_type.traffic_type == "on-demand" or data_type.traffic_type == "event-driven" or data_type.traffic_type == "batch":
                        # Για on-demand, event-driven και batch, χρησιμοποιούμε πιθανότητα
                        # based on average frequency (unit_time_sec).
                        # Π.χ. αν unit_time_sec = 3600, πιθανότητα 1/3600 σε κάθε δευτερόλεπτο
                        if data_type.unit_time_sec > 0:
                            probability_per_second = 1.0 / data_type.unit_time_sec
                            if random.random() < probability_per_second:
                                should_attempt_transfer = True
                        
                        # Εάν είναι "batch" και έχει μεγάλη διάρκεια, θα πρέπει να διασφαλίσουμε ότι θα ξεκινήσει έστω και μία φορά
                        # μέσα στο σύνολο της προσομοίωσης αν η πιθανότητα είναι πολύ χαμηλή.
                        # Για την απλότητα, η πιθανότητα θα είναι αρκετή για αρχή.
                        # Μια πιο σύνθετη προσέγγιση θα ήταν να προγραμματίζονται τα batch transfers.
                    
                    # Η απλοποιημένη εκδοχή είναι να χρησιμοποιούμε την ίδια μέθοδο για Receive and Transfer
                    if should_attempt_transfer:
                        # Attempt transfer (TX)
                        if data_type.transmit_type == "TX" or data_type.transmit_type == "Both":
                            transferred_tech, transfer_duration = ship.attempt_data_transfer(
                                data_type, location_scenario, weather_multiplier
                            )
                        # Attempt transfer (RX)
                        if data_type.transmit_type == "RX" or data_type.transmit_type == "Both":
                            transferred_tech, transfer_duration = ship.attempt_data_transfer(
                                data_type, location_scenario, weather_multiplier
                            )

        print("Simulation finished.")
        self._aggregate_results()

    def _aggregate_results(self):
        """Συγκεντρώνει τα αποτελέσματα από όλα τα πλοία και τις τεχνολογίες."""
        self.results = {}
        for ship in self.ships:
            ship_results = {
                "total_successful_transfers": ship.total_successful_data_transfers_overall,
                "total_failed_transfers": ship.total_failed_data_transfers_overall,
                "total_data_mb": 0.0,
                "tech_breakdown": {}
            }
            total_data_handled_by_ship = 0.0
            for tech in ship.communication_technologies:
                # Το tech_breakdown εξακολουθεί να δείχνει τις αποτυχίες ανά τεχνολογία
                total_failures = tech.failed_transfers_capacity + tech.failed_transfers_latency + tech.failed_transfers_availability
                ship_results["tech_breakdown"][tech.name] = {
                    "successful": tech.successful_transfers,
                    "failed_capacity": tech.failed_transfers_capacity,
                    "failed_latency": tech.failed_transfers_latency,
                    "failed_availability": tech.failed_transfers_availability,
                    "total_handled_mb": tech.total_data_handled_mb
                }
                total_data_handled_by_ship += tech.total_data_handled_mb
            ship_results["total_data_mb"] = total_data_handled_by_ship
            self.results[ship.name] = ship_results

    def plot_results(self, scenario_name="Results"):
        """Εμφανίζει γραφήματα με τα αποτελέσματα της προσομοίωσης."""
        if not self.results:
            print("No simulation results to plot. Run simulation first.")
            return

        ship_names = list(self.results.keys())
        successful_transfers = [self.results[name]["total_successful_transfers"] for name in ship_names]
        failed_transfers = [self.results[name]["total_failed_transfers"] for name in ship_names]
        total_data_mb = [self.results[name]["total_data_mb"] for name in ship_names]

        # Γράφημα 1: Συνολικές επιτυχίες και αποτυχίες
        fig1, ax1 = plt.subplots(figsize=(10, 6))
        bar_width = 0.35
        index = np.arange(len(ship_names))
        ax1.bar(index, successful_transfers, bar_width, label='Successful Transfers', color='g')
        ax1.bar(index + bar_width, failed_transfers, bar_width, label='Failed Transfers', color='r')
        ax1.set_xlabel('Ship Type')
        ax1.set_ylabel('Number of Data Transfers')
        ax1.set_title(f'Total Data Transfers: Successful vs. Failed - {scenario_name}')
        ax1.set_xticks(index + bar_width / 2)
        ax1.set_xticklabels(ship_names)
        ax1.legend()
        plt.tight_layout()

        # Γράφημα 2: Συνολικός όγκος δεδομένων που μεταφέρθηκαν επιτυχώς
        fig2, ax2 = plt.subplots(figsize=(10, 6))
        ax2.bar(ship_names, total_data_mb, color=['skyblue', 'lightcoral'])
        ax2.set_xlabel('Ship Type')
        ax2.set_ylabel('Total Data Transferred (MB)')
        ax2.set_title(f'Total Data Successfully Transferred per Ship Type - {scenario_name}')
        plt.tight_layout()

        # Γράφημα 3: Ανάλυση αποτυχιών ανά τεχνολογία για κάθε πλοίο
        for ship_name, ship_res in self.results.items():
            tech_names = list(ship_res["tech_breakdown"].keys())
            if not tech_names:
                continue

            tech_failed_capacity = [ship_res["tech_breakdown"][tn]["failed_capacity"] for tn in tech_names]
            tech_failed_latency = [ship_res["tech_breakdown"][tn]["failed_latency"] for tn in tech_names]
            tech_failed_availability = [ship_res["tech_breakdown"][tn]["failed_availability"] for tn in tech_names]
            tech_successful = [ship_res["tech_breakdown"][tn]["successful"] for tn in tech_names]

            if all(v == 0 for v in tech_failed_capacity + tech_failed_latency + tech_failed_availability + tech_successful):
                print(f"No transfer attempts recorded for {ship_name} technologies in detail plot. Skipping.")
                continue

            fig3, ax3 = plt.subplots(figsize=(12, 7))
            bar_width = 0.18
            index = np.arange(len(tech_names))

            ax3.bar(index - 1.5 * bar_width, tech_successful, bar_width, label='Successful', color='lightgreen')
            ax3.bar(index - 0.5 * bar_width, tech_failed_capacity, bar_width, label='Failed (Capacity)', color='orange')
            ax3.bar(index + 0.5 * bar_width, tech_failed_latency, bar_width, label='Failed (Latency)', color='red')
            ax3.bar(index + 1.5 * bar_width, tech_failed_availability, bar_width, label='Failed (Availability)', color='purple')

            ax3.set_xlabel('Communication Technology')
            ax3.set_ylabel('Number of Transfer Attempts')
            ax3.set_title(f'Transfer Outcomes per Technology for {ship_name} - {scenario_name}')
            ax3.set_xticks(index + bar_width / 2)
            ax3.set_xticklabels(tech_names, rotation=45, ha='right')
            ax3.legend()
            plt.tight_layout()

        plt.show()