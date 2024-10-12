

# Activation

Holds properties related to activation.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**azureRegistrationResourceIdentifier** | **String** | Azure registration resource identifier. |  [optional] |
|**displayName** | **String** | Name displayed for the product. |  [optional] |
|**expiration** | **String** | The activation expiration. |  [optional] |
|**marketplaceSyndicationEnabled** | **Boolean** | Value indicating whether the marketplace syndication feature is enabled. |  [optional] |
|**provisioningState** | [**ProvisioningStateEnum**](#ProvisioningStateEnum) | The provisioning state of the resource. |  [optional] |
|**usageReportingEnabled** | **Boolean** | Value indicating whether the usage reporting feature is enabled. |  [optional] |



## Enum: ProvisioningStateEnum

| Name | Value |
|---- | -----|
| STOPPED | &quot;Stopped&quot; |
| STARTING | &quot;Starting&quot; |
| RUNNING | &quot;Running&quot; |
| STOPPING | &quot;Stopping&quot; |
| SUCCEEDED | &quot;Succeeded&quot; |
| DOWNLOADING | &quot;Downloading&quot; |



