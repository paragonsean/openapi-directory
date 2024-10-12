

# GoogleCloudAiplatformV1ManualBatchTuningParameters

Manual batch tuning parameters.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**batchSize** | **Integer** | Immutable. The number of the records (e.g. instances) of the operation given in each batch to a machine replica. Machine type, and size of a single record should be considered when setting this parameter, higher value speeds up the batch operation&#39;s execution, but too high value will result in a whole batch not fitting in a machine&#39;s memory, and the whole operation will fail. The default value is 64. |  [optional] |



