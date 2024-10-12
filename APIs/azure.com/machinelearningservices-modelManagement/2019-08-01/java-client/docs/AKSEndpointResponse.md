

# AKSEndpointResponse

The response for an AKS Endpoint.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**aadAuthEnabled** | **Boolean** | Whether or not AAD authentication is enabled. |  [optional] |
|**appInsightsEnabled** | **Boolean** | Whether or not Application Insights is enabled. |  [optional] |
|**authEnabled** | **Boolean** | Whether or not authentication is enabled. |  [optional] |
|**computeName** | **String** | The name of the compute resource. |  [optional] |
|**namespace** | **String** | The Kubernetes namespace of the deployment. |  [optional] |
|**scoringUri** | **String** | The Uri for sending scoring requests. |  [optional] |
|**swaggerUri** | **String** | The Uri for sending swagger requests. |  [optional] |
|**variants** | [**List&lt;AKSServiceResponse&gt;**](AKSServiceResponse.md) | All the variants that belongs to this endpoint. |  [optional] |



