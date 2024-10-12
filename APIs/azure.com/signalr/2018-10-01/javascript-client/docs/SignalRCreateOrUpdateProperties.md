# SignalRManagementClient.SignalRCreateOrUpdateProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cors** | [**SignalRCorsSettings**](SignalRCorsSettings.md) |  | [optional] 
**features** | [**[SignalRFeature]**](SignalRFeature.md) | List of SignalR featureFlags. e.g. ServiceMode.    FeatureFlags that are not included in the parameters for the update operation will not be modified.  And the response will only include featureFlags that are explicitly set.   When a featureFlag is not explicitly set, SignalR service will use its globally default value.   But keep in mind, the default value doesn&#39;t mean \&quot;false\&quot;. It varies in terms of different FeatureFlags. | [optional] 
**hostNamePrefix** | **String** | Prefix for the hostName of the SignalR service. Retained for future use.  The hostname will be of format: &amp;lt;hostNamePrefix&amp;gt;.service.signalr.net. | [optional] 


