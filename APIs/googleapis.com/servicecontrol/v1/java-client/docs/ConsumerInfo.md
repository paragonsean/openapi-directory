

# ConsumerInfo

`ConsumerInfo` provides information about the consumer.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**consumerNumber** | **String** | The consumer identity number, can be Google cloud project number, folder number or organization number e.g. 1234567890. A value of 0 indicates no consumer number is found. |  [optional] |
|**projectNumber** | **String** | The Google cloud project number, e.g. 1234567890. A value of 0 indicates no project number is found. NOTE: This field is deprecated after Chemist support flexible consumer id. New code should not depend on this field anymore. |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | The type of the consumer which should have been defined in [Google Resource Manager](https://cloud.google.com/resource-manager/). |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| CONSUMER_TYPE_UNSPECIFIED | &quot;CONSUMER_TYPE_UNSPECIFIED&quot; |
| PROJECT | &quot;PROJECT&quot; |
| FOLDER | &quot;FOLDER&quot; |
| ORGANIZATION | &quot;ORGANIZATION&quot; |
| SERVICE_SPECIFIC | &quot;SERVICE_SPECIFIC&quot; |



