

# DirectiveRuleCompliance


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**compliance** | **Float** | Directive compliance level |  |
|**complianceDetails** | [**DirectiveNodeComplianceComplianceDetails**](DirectiveNodeComplianceComplianceDetails.md) |  |  |
|**components** | [**List&lt;DirectiveRuleComplianceComponentsInner&gt;**](DirectiveRuleComplianceComponentsInner.md) |  |  [optional] |
|**id** | **UUID** | id of the rule |  |
|**mode** | [**ModeEnum**](#ModeEnum) |  |  [optional] |
|**name** | **String** | Name of the rule |  |



## Enum: ModeEnum

| Name | Value |
|---- | -----|
| FULL_COMPLIANCE | &quot;full-compliance&quot; |
| CHANGES_ONLY | &quot;changes-only&quot; |
| REPORTS_DISABLED | &quot;reports-disabled&quot; |



