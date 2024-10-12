# CloudDeployApi.PipelineReadyCondition

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **Boolean** | True if the Pipeline is in a valid state. Otherwise at least one condition in &#x60;PipelineCondition&#x60; is in an invalid state. Iterate over those conditions and see which condition(s) has status &#x3D; false to find out what is wrong with the Pipeline. | [optional] 
**updateTime** | **String** | Last time the condition was updated. | [optional] 


