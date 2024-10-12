

# Control

Selects and configures the service controller used by the service. Example: control: environment: servicecontrol.googleapis.com

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**environment** | **String** | The service controller environment to use. If empty, no control plane feature (like quota and billing) will be enabled. The recommended value for most services is servicecontrol.googleapis.com |  [optional] |
|**methodPolicies** | [**List&lt;MethodPolicy&gt;**](MethodPolicy.md) | Defines policies applying to the API methods of the service. |  [optional] |



