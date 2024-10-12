

# IoTSecurityDeviceRecommendation

Statistical information about the number of recommendations per device, per recommendation type.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**devicesCount** | **Integer** | Number of devices with this recommendation. |  [optional] [readonly] |
|**recommendationDisplayName** | **String** | Display name of the recommendation. |  [optional] [readonly] |
|**reportedSeverity** | [**ReportedSeverityEnum**](#ReportedSeverityEnum) | Assessed recommendation severity. |  [optional] [readonly] |



## Enum: ReportedSeverityEnum

| Name | Value |
|---- | -----|
| INFORMATIONAL | &quot;Informational&quot; |
| LOW | &quot;Low&quot; |
| MEDIUM | &quot;Medium&quot; |
| HIGH | &quot;High&quot; |



