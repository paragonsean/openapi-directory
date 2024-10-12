# ServiceFabricClientApis.ApplicationProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**debugParams** | **String** | Internal use. | [optional] 
**description** | **String** | User readable description of the application. | [optional] 
**diagnostics** | [**DiagnosticsDescription**](DiagnosticsDescription.md) |  | [optional] 
**healthState** | [**HealthState**](HealthState.md) |  | [optional] 
**serviceNames** | **[String]** | Names of the services in the application. | [optional] [readonly] 
**services** | [**[ServiceResourceDescription]**](ServiceResourceDescription.md) | describes the services in the application. | [optional] 
**status** | **String** | Status of the application resource. | [optional] [readonly] 
**statusDetails** | **String** | Gives additional information about the current status of the application deployment. | [optional] [readonly] 
**unhealthyEvaluation** | **String** | When the application&#39;s health state is not &#39;Ok&#39;, this additional details from service fabric Health Manager for the user to know why the application is marked unhealthy. | [optional] [readonly] 



## Enum: StatusEnum


* `Invalid` (value: `"Invalid"`)

* `Ready` (value: `"Ready"`)

* `Upgrading` (value: `"Upgrading"`)

* `Creating` (value: `"Creating"`)

* `Deleting` (value: `"Deleting"`)

* `Failed` (value: `"Failed"`)




