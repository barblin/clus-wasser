class WasserIncrement:
    def __init__(self, wasser_margin, clus_data, runtime, overall_time):
        self.wasser_margin = float(wasser_margin)
        self.clusters = clus_data.clusters
        self.max_features = clus_data.max_features
        self.runtime = float(runtime)
        self.overall_time = float(overall_time)
