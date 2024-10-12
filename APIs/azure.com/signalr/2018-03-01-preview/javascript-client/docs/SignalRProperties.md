# SignalRManagementClient.SignalRProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**externalIP** | **String** | The publicly accessible IP of the SignalR service. | [optional] [readonly] 
**hostName** | **String** | FQDN of the SignalR service instance. Format: xxx.service.signalr.net | [optional] [readonly] 
**provisioningState** | **String** | Provisioning state of the resource. | [optional] [readonly] 
**publicPort** | **Number** | The publicly accessibly port of the SignalR service which is designed for browser/client side usage. | [optional] [readonly] 
**serverPort** | **Number** | The publicly accessibly port of the SignalR service which is designed for customer server side usage. | [optional] [readonly] 
**version** | **String** | Version of the SignalR resource. Probably you need the same or higher version of client SDKs. | [optional] 
**hostNamePrefix** | **String** | Prefix for the hostName of the SignalR service. Retained for future use.  The hostname will be of format: &amp;lt;hostNamePrefix&amp;gt;.service.signalr.net. | [optional] 



## Enum: ProvisioningStateEnum


* `Unknown` (value: `"Unknown"`)

* `Succeeded` (value: `"Succeeded"`)

* `Failed` (value: `"Failed"`)

* `Canceled` (value: `"Canceled"`)

* `Running` (value: `"Running"`)

* `Creating` (value: `"Creating"`)

* `Updating` (value: `"Updating"`)

* `Deleting` (value: `"Deleting"`)

* `Moving` (value: `"Moving"`)




