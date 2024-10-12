

# IoTSecurityDeviceAlert

Statistical information about the number of alerts per alert type during last set number of days

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**alertDisplayName** | **String** | Display name of the alert |  [optional] [readonly] |
|**alertsCount** | **Integer** | Number of alerts raised for this alert type. |  [optional] [readonly] |
|**reportedSeverity** | [**ReportedSeverityEnum**](#ReportedSeverityEnum) | Assessed Alert severity. |  [optional] [readonly] |



## Enum: ReportedSeverityEnum

| Name | Value |
|---- | -----|
| INFORMATIONAL | &quot;Informational&quot; |
| LOW | &quot;Low&quot; |
| MEDIUM | &quot;Medium&quot; |
| HIGH | &quot;High&quot; |



