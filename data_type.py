# data_type.py

class DataType:
    def __init__(self, name, size_kb_per_unit, priority, transmit_type,
                 unit_time_sec=1, latency_tolerance_ms=None,
                 transmission_duration_sec=1, traffic_type="streaming",
                 processed_data_reduction_factor=1.0): 
        """
        Αντιπροσωπεύει έναν τύπο δεδομένων που μεταδίδεται από το πλοίο.

        :param name: Όνομα του τύπου δεδομένων (π.χ., "GPS Data").
        :param size_kb_per_unit: Μέγεθος δεδομένων σε KB ανά μονάδα (π.χ., KB/δευτερόλεπτο, KB/γεγονός).
        :param priority: Προτεραιότητα δεδομένων ("Critical", "High", "Medium", "Low").
        :param transmit_type: Τύπος μετάδοσης ("TX" για αποστολή, "RX" για λήψη, "Both").
        :param unit_time_sec: Το χρονικό διάστημα στο οποίο παράγεται/μεταδίδεται το `size_kb_per_unit`.
                              (π.χ., 1 για κάθε δευτερόλεπτο, 60 για κάθε λεπτό).
                              Εάν είναι για "on-demand" ή "event-driven", μπορεί να είναι η μέση συχνότητα.
        :param latency_tolerance_ms: Μέγιστη αποδεκτή καθυστέρηση σε ms. Αν None, χρησιμοποιείται default από το πλοίο.
        :param transmission_duration_sec: Πόσο χρόνο χρειάζεται η μεταφορά αυτού του 'unit' δεδομένων σε δευτερόλεπτα.
                                          Για συνεχή ροή, είναι συνήθως 1 δευτερόλεπτο.
        :param traffic_type: Κατηγορία κίνησης ("streaming", "periodic", "on-demand", "event-driven", "batch").
        :param processed_data_reduction_factor: Συντελεστής μείωσης μεγέθους λόγω επεξεργασίας/συμπίεσης επί του πλοίου (0.0-1.0).
                                                Π.χ., 0.1 σημαίνει ότι μεταφέρεται το 10% του αρχικού μεγέθους.
        """
        self.name = name
        self.size_kb_per_unit = size_kb_per_unit
        self.priority = priority
        self.transmit_type = transmit_type
        self.unit_time_sec = unit_time_sec
        self.latency_tolerance_ms = latency_tolerance_ms
        self.transmission_duration_sec = transmission_duration_sec
        self.traffic_type = traffic_type
        self.processed_data_reduction_factor = processed_data_reduction_factor

    def get_effective_size_kb(self):
        """Επιστρέφει το πραγματικό μέγεθος σε KB που μεταφέρεται μετά την επεξεργασία."""
        return self.size_kb_per_unit * self.processed_data_reduction_factor

    def get_required_data_rate_mbps(self):
        """
        Υπολογίζει τον απαιτούμενο ρυθμό δεδομένων σε Mbps με βάση το **μειωμένο** μέγεθος.
        """
        if self.unit_time_sec == 0 or self.transmission_duration_sec == 0:
            return float('inf')
        
        # Υπολογισμός ρυθμού με βάση το πραγματικά μεταφερόμενο μέγεθος
        return (self.get_effective_size_kb() * 8) / (self.transmission_duration_sec * 1000)

    def __str__(self):
        return f"DataType: {self.name} (Priority: {self.priority}, Size: {self.size_kb_per_unit} KB -> {self.get_effective_size_kb():.2f} KB, Type: {self.traffic_type})"