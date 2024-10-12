

# CreateEndpointRequest

The request to create an Endpoint in the AKS.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**aadAuthEnabled** | **Boolean** | Whether or not AAD authentication is enabled. |  [optional] |
|**appInsightsEnabled** | **Boolean** | Whether or not Application Insights is enabled. |  [optional] |
|**authEnabled** | **Boolean** | Whether or not authentication is enabled. |  [optional] |
|**computeName** | **String** | The name of the compute resource. |  [optional] |
|**namespace** | **String** | Kubernetes namespace for the service. |  [optional] |
|**variants** | [**List&lt;AKSServiceCreateRequest&gt;**](AKSServiceCreateRequest.md) | The service tag list. |  [optional] |



