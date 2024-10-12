# RudderApi.GetDirectivesCompliance200ResponseDataDirectivesCompliance

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**compliance** | **Number** | Directive compliance level | 
**complianceDetails** | [**GetDirectivesCompliance200ResponseDataDirectivesComplianceComplianceDetails**](GetDirectivesCompliance200ResponseDataDirectivesComplianceComplianceDetails.md) |  | 
**id** | **String** | id of the directive | 
**mode** | **String** |  | 
**name** | **String** | Name of the directive | 
**nodes** | [**DirectiveNodeCompliance**](DirectiveNodeCompliance.md) |  | 
**rules** | [**DirectiveRuleCompliance**](DirectiveRuleCompliance.md) |  | 



## Enum: ModeEnum


* `full-compliance` (value: `"full-compliance"`)

* `changes-only` (value: `"changes-only"`)

* `reports-disabled` (value: `"reports-disabled"`)




