# CloudAssetApi.GoogleCloudAssetV1Rule

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allowAll** | **Boolean** | Setting this to true means that all values are allowed. This field can be set only in Policies for list constraints. | [optional] 
**condition** | [**Expr**](Expr.md) |  | [optional] 
**conditionEvaluation** | [**ConditionEvaluation**](ConditionEvaluation.md) |  | [optional] 
**denyAll** | **Boolean** | Setting this to true means that all values are denied. This field can be set only in Policies for list constraints. | [optional] 
**enforce** | **Boolean** | If &#x60;true&#x60;, then the &#x60;Policy&#x60; is enforced. If &#x60;false&#x60;, then any configuration is acceptable. This field can be set only in Policies for boolean constraints. | [optional] 
**values** | [**GoogleCloudAssetV1StringValues**](GoogleCloudAssetV1StringValues.md) |  | [optional] 


