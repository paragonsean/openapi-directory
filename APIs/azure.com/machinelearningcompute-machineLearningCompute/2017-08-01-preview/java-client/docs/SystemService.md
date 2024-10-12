

# SystemService

Information about a system service deployed in the cluster

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**publicIpAddress** | **String** | The public IP address of the system service |  [optional] [readonly] |
|**systemServiceType** | [**SystemServiceTypeEnum**](#SystemServiceTypeEnum) | The system service type |  |
|**version** | **String** | The state of the system service |  [optional] [readonly] |



## Enum: SystemServiceTypeEnum

| Name | Value |
|---- | -----|
| NONE | &quot;None&quot; |
| SCORING_FRONT_END | &quot;ScoringFrontEnd&quot; |
| BATCH_FRONT_END | &quot;BatchFrontEnd&quot; |



