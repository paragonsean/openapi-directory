

# GoogleCloudMlV1ManualScaling

Options for manually scaling a model.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**nodes** | **Integer** | The number of nodes to allocate for this model. These nodes are always up, starting from the time the model is deployed, so the cost of operating this model will be proportional to &#x60;nodes&#x60; * number of hours since last billing cycle plus the cost for each prediction performed. |  [optional] |



