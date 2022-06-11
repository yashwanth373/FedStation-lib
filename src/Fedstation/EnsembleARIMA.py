class EnsembleARIMA:
  def __init__(self,models):
    self.models = models
  def predict(self,periods):
    results = []
    for model in self.models:
        result = model.predict(n_periods=periods)
        results.append(result)
    
    # Averaging of results in all models
    response = {}
    for i in range(periods):
        sum=0
        for result in results:
            sum += result[i]
        response[i] = sum/len(results)
    return response