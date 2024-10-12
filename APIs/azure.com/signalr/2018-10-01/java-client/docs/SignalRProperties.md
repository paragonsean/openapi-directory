

# SignalRProperties

A class that describes the properties of the SignalR service that should contain more read-only properties than AzSignalR.Models.SignalRCreateOrUpdateProperties

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**externalIP** | **String** | The publicly accessible IP of the SignalR service. |  [optional] [readonly] |
|**hostName** | **String** | FQDN of the SignalR service instance. Format: xxx.service.signalr.net |  [optional] [readonly] |
|**provisioningState** | [**ProvisioningStateEnum**](#ProvisioningStateEnum) | Provisioning state of the resource. |  [optional] [readonly] |
|**publicPort** | **Integer** | The publicly accessible port of the SignalR service which is designed for browser/client side usage. |  [optional] [readonly] |
|**serverPort** | **Integer** | The publicly accessible port of the SignalR service which is designed for customer server side usage. |  [optional] [readonly] |
|**version** | **String** | Version of the SignalR resource. Probably you need the same or higher version of client SDKs. |  [optional] |
|**cors** | [**SignalRCorsSettings**](SignalRCorsSettings.md) |  |  [optional] |
|**features** | [**List&lt;SignalRFeature&gt;**](SignalRFeature.md) | List of SignalR featureFlags. e.g. ServiceMode.    FeatureFlags that are not included in the parameters for the update operation will not be modified.  And the response will only include featureFlags that are explicitly set.   When a featureFlag is not explicitly set, SignalR service will use its globally default value.   But keep in mind, the default value doesn&#39;t mean \&quot;false\&quot;. It varies in terms of different FeatureFlags. |  [optional] |
|**hostNamePrefix** | **String** | Prefix for the hostName of the SignalR service. Retained for future use.  The hostname will be of format: &amp;lt;hostNamePrefix&amp;gt;.service.signalr.net. |  [optional] |



## Enum: ProvisioningStateEnum

| Name | Value |
|---- | -----|
| UNKNOWN | &quot;Unknown&quot; |
| SUCCEEDED | &quot;Succeeded&quot; |
| FAILED | &quot;Failed&quot; |
| CANCELED | &quot;Canceled&quot; |
| RUNNING | &quot;Running&quot; |
| CREATING | &quot;Creating&quot; |
| UPDATING | &quot;Updating&quot; |
| DELETING | &quot;Deleting&quot; |
| MOVING | &quot;Moving&quot; |



