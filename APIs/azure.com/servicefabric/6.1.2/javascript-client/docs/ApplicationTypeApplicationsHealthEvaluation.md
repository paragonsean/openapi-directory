# ServiceFabricClientApis.ApplicationTypeApplicationsHealthEvaluation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**applicationTypeName** | **String** | The application type name as defined in the application manifest. | [optional] 
**maxPercentUnhealthyApplications** | **Number** | Maximum allowed percentage of unhealthy applications for the application type, specified as an entry in ApplicationTypeHealthPolicyMap. | [optional] 
**totalCount** | **Number** | Total number of applications of the application type found in the health store. | [optional] 
**unhealthyEvaluations** | [**[HealthEvaluationWrapper]**](HealthEvaluationWrapper.md) | List of health evaluations that resulted in the current aggregated health state. | [optional] 


