# communication_technology.py

class CommunicationTechnology:
    def __init__(self, name, max_bandwidth_mbps, typical_latency_ms, reliability_percentage,
                 availability_condition, weather_impact_bandwidth_multiplier=1.0,
                 weather_impact_latency_multiplier=1.0, is_primary=True):
        self.name = name
        self.max_bandwidth_mbps = max_bandwidth_mbps
        self.typical_latency_ms = typical_latency_ms
        self.reliability_percentage = reliability_percentage
        self.availability_condition = availability_condition
        self.weather_impact_bandwidth_multiplier = weather_impact_bandwidth_multiplier
        self.weather_impact_latency_multiplier = weather_impact_latency_multiplier
        self.is_primary = is_primary

        # Μετρητές για την προσομοίωση
        self.successful_transfers = 0
        self.failed_transfers_capacity = 0
        self.failed_transfers_latency = 0
        self.failed_transfers_availability = 0
        self.total_data_handled_mb = 0.0

    def get_effective_bandwidth(self, weather_condition_multiplier=1.0):
        # Επίδραση καιρού και αξιοπιστίας
        return self.max_bandwidth_mbps * self.weather_impact_bandwidth_multiplier * weather_condition_multiplier * (self.reliability_percentage / 100)

    def get_effective_latency(self, weather_condition_multiplier=1.0):
        # Επίδραση καιρού στην καθυστέρηση
        return self.typical_latency_ms * self.weather_impact_latency_multiplier * weather_condition_multiplier

    def reset_metrics(self):
        # Επαναφορά μετρητών για νέα προσομοίωση
        self.successful_transfers = 0
        self.failed_transfers_capacity = 0
        self.failed_transfers_latency = 0
        self.failed_transfers_availability = 0
        self.total_data_handled_mb = 0.0

    def __str__(self):
        return (f"Tech: {self.name} | Max BW: {self.max_bandwidth_mbps} Mbps | "
                f"Latency: {self.typical_latency_ms} ms | Reliability: {self.reliability_percentage}%")