

# IoTSecurityDeviceAlert

Statistic information about the number of alerts per alert type during the last period

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**alertDisplayName** | **String** | Display name of the alert |  [optional] [readonly] |
|**alertsCount** | **Integer** | the number of alerts raised for this alert type |  [optional] [readonly] |
|**reportedSeverity** | [**ReportedSeverityEnum**](#ReportedSeverityEnum) | Estimated severity of this alert |  [optional] [readonly] |



## Enum: ReportedSeverityEnum

| Name | Value |
|---- | -----|
| INFORMATIONAL | &quot;Informational&quot; |
| LOW | &quot;Low&quot; |
| MEDIUM | &quot;Medium&quot; |
| HIGH | &quot;High&quot; |



