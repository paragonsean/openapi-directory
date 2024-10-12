# PolicySimulatorApi.GoogleCloudOrgpolicyV2PolicySpecPolicyRule

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allowAll** | **Boolean** | Setting this to true means that all values are allowed. This field can be set only in policies for list constraints. | [optional] 
**condition** | [**GoogleTypeExpr**](GoogleTypeExpr.md) |  | [optional] 
**denyAll** | **Boolean** | Setting this to true means that all values are denied. This field can be set only in policies for list constraints. | [optional] 
**enforce** | **Boolean** | If &#x60;true&#x60;, then the policy is enforced. If &#x60;false&#x60;, then any configuration is acceptable. This field can be set only in policies for boolean constraints. | [optional] 
**values** | [**GoogleCloudOrgpolicyV2PolicySpecPolicyRuleStringValues**](GoogleCloudOrgpolicyV2PolicySpecPolicyRuleStringValues.md) |  | [optional] 


