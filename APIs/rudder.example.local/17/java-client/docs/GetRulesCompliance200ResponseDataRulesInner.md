

# GetRulesCompliance200ResponseDataRulesInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**compliance** | **Float** | Rule compliance level |  |
|**complianceDetails** | [**GetGlobalCompliance200ResponseDataGlobalComplianceComplianceDetails**](GetGlobalCompliance200ResponseDataGlobalComplianceComplianceDetails.md) |  |  |
|**id** | **UUID** | id of the rule |  |
|**mode** | [**ModeEnum**](#ModeEnum) |  |  |



## Enum: ModeEnum

| Name | Value |
|---- | -----|
| FULL_COMPLIANCE | &quot;full-compliance&quot; |
| CHANGES_ONLY | &quot;changes-only&quot; |
| REPORTS_DISABLED | &quot;reports-disabled&quot; |



