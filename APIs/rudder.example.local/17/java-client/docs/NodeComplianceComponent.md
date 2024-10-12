

# NodeComplianceComponent


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**compliance** | **Float** | Directive compliance level |  |
|**complianceDetails** | [**DirectiveNodeComplianceComplianceDetails**](DirectiveNodeComplianceComplianceDetails.md) |  |  |
|**id** | **UUID** | id of the node |  |
|**mode** | [**ModeEnum**](#ModeEnum) |  |  [optional] |
|**name** | **String** | Name of the node |  |
|**values** | [**List&lt;NodeComplianceComponentValuesInner&gt;**](NodeComplianceComponentValuesInner.md) |  |  |



## Enum: ModeEnum

| Name | Value |
|---- | -----|
| FULL_COMPLIANCE | &quot;full-compliance&quot; |
| CHANGES_ONLY | &quot;changes-only&quot; |
| REPORTS_DISABLED | &quot;reports-disabled&quot; |



