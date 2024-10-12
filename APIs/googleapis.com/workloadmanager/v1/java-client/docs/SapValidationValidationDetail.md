

# SapValidationValidationDetail

Message describing the SAP validation metrics.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**details** | **Map&lt;String, String&gt;** | Optional. The pairs of metrics data: field name &amp; field value. |  [optional] |
|**isPresent** | **Boolean** | Optional. Was there a SAP system detected for this validation type. |  [optional] |
|**sapValidationType** | [**SapValidationTypeEnum**](#SapValidationTypeEnum) | Optional. The SAP system that the validation data is from. |  [optional] |



## Enum: SapValidationTypeEnum

| Name | Value |
|---- | -----|
| SAP_VALIDATION_TYPE_UNSPECIFIED | &quot;SAP_VALIDATION_TYPE_UNSPECIFIED&quot; |
| SYSTEM | &quot;SYSTEM&quot; |
| COROSYNC | &quot;COROSYNC&quot; |
| PACEMAKER | &quot;PACEMAKER&quot; |
| HANA | &quot;HANA&quot; |
| NETWEAVER | &quot;NETWEAVER&quot; |
| HANA_SECURITY | &quot;HANA_SECURITY&quot; |
| CUSTOM | &quot;CUSTOM&quot; |



