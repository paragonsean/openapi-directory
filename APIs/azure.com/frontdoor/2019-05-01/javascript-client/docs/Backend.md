# FrontDoorManagementClient.Backend

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **String** | Location of the backend (IP address or FQDN) | [optional] 
**backendHostHeader** | **String** | The value to use as the host header sent to the backend. If blank or unspecified, this defaults to the incoming host. | [optional] 
**enabledState** | **String** | Whether to enable use of this backend. Permitted values are &#39;Enabled&#39; or &#39;Disabled&#39; | [optional] 
**httpPort** | **Number** | The HTTP TCP port number. Must be between 1 and 65535. | [optional] 
**httpsPort** | **Number** | The HTTPS TCP port number. Must be between 1 and 65535. | [optional] 
**priority** | **Number** | Priority to use for load balancing. Higher priorities will not be used for load balancing if any lower priority backend is healthy. | [optional] 
**weight** | **Number** | Weight of this endpoint for load balancing purposes. | [optional] 



## Enum: EnabledStateEnum


* `Enabled` (value: `"Enabled"`)

* `Disabled` (value: `"Disabled"`)




