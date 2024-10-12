

# GoogleCloudMlV1BuiltInAlgorithmOutput

Represents output related to a built-in algorithm Job.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**framework** | **String** | Framework on which the built-in algorithm was trained. |  [optional] |
|**modelPath** | **String** | The Cloud Storage path to the &#x60;model/&#x60; directory where the training job saves the trained model. Only set for successful jobs that don&#39;t use hyperparameter tuning. |  [optional] |
|**pythonVersion** | **String** | Python version on which the built-in algorithm was trained. |  [optional] |
|**runtimeVersion** | **String** | AI Platform runtime version on which the built-in algorithm was trained. |  [optional] |



