

# ApplicationResourceProperties

This type describes properties of an application resource.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**provisioningState** | **String** | State of the resource. |  [optional] [readonly] |
|**debugParams** | **String** | Internal use. |  [optional] |
|**description** | **String** | User readable description of the application. |  [optional] |
|**diagnostics** | [**DiagnosticsDescription**](DiagnosticsDescription.md) |  |  [optional] |
|**healthState** | **HealthState** |  |  [optional] |
|**serviceNames** | **List&lt;String&gt;** | Names of the services in the application. |  [optional] [readonly] |
|**services** | [**List&lt;ServiceResourceDescription&gt;**](ServiceResourceDescription.md) | describes the services in the application. |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | Status of the application resource. |  [optional] [readonly] |
|**statusDetails** | **String** | Gives additional information about the current status of the application deployment. |  [optional] [readonly] |
|**unhealthyEvaluation** | **String** | When the application&#39;s health state is not &#39;Ok&#39;, this additional details from service fabric Health Manager for the user to know why the application is marked unhealthy. |  [optional] [readonly] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| INVALID | &quot;Invalid&quot; |
| READY | &quot;Ready&quot; |
| UPGRADING | &quot;Upgrading&quot; |
| CREATING | &quot;Creating&quot; |
| DELETING | &quot;Deleting&quot; |
| FAILED | &quot;Failed&quot; |



