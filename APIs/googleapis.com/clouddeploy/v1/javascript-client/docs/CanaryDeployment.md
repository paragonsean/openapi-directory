# CloudDeployApi.CanaryDeployment

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**percentages** | **[Number]** | Required. The percentage based deployments that will occur as a part of a &#x60;Rollout&#x60;. List is expected in ascending order and each integer n is 0 &lt;&#x3D; n &lt; 100. | [optional] 
**postdeploy** | [**Postdeploy**](Postdeploy.md) |  | [optional] 
**predeploy** | [**Predeploy**](Predeploy.md) |  | [optional] 
**verify** | **Boolean** | Whether to run verify tests after each percentage deployment. | [optional] 


