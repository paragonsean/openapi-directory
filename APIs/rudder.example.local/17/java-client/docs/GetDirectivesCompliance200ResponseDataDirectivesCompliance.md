

# GetDirectivesCompliance200ResponseDataDirectivesCompliance


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**compliance** | **Float** | Directive compliance level |  |
|**complianceDetails** | [**GetDirectivesCompliance200ResponseDataDirectivesComplianceComplianceDetails**](GetDirectivesCompliance200ResponseDataDirectivesComplianceComplianceDetails.md) |  |  |
|**id** | **UUID** | id of the directive |  |
|**mode** | [**ModeEnum**](#ModeEnum) |  |  |
|**name** | **String** | Name of the directive |  |
|**nodes** | [**DirectiveNodeCompliance**](DirectiveNodeCompliance.md) |  |  |
|**rules** | [**DirectiveRuleCompliance**](DirectiveRuleCompliance.md) |  |  |



## Enum: ModeEnum

| Name | Value |
|---- | -----|
| FULL_COMPLIANCE | &quot;full-compliance&quot; |
| CHANGES_ONLY | &quot;changes-only&quot; |
| REPORTS_DISABLED | &quot;reports-disabled&quot; |



