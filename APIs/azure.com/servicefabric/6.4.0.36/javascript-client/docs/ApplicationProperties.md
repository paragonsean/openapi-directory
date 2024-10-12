# ServiceFabricClientApis.ApplicationProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**debugParams** | **String** | Internal - used by Visual Studio to setup the debugging session on the local development environment. | [optional] 
**description** | **String** | User readable description of the application. | [optional] 
**diagnostics** | [**DiagnosticsDescription**](DiagnosticsDescription.md) |  | [optional] 
**healthState** | [**HealthState**](HealthState.md) |  | [optional] 
**serviceNames** | **[String]** | Names of the services in the application. | [optional] [readonly] 
**services** | [**[ServiceResourceDescription]**](ServiceResourceDescription.md) | Describes the services in the application. This property is used to create or modify services of the application. On get only the name of the service is returned. The service description can be obtained by querying for the service resource. | [optional] 
**status** | [**ResourceStatus**](ResourceStatus.md) |  | [optional] 
**statusDetails** | **String** | Gives additional information about the current status of the application. | [optional] [readonly] 
**unhealthyEvaluation** | **String** | When the application&#39;s health state is not &#39;Ok&#39;, this additional details from service fabric Health Manager for the user to know why the application is marked unhealthy. | [optional] [readonly] 


