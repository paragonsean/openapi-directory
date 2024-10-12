

# GoogleCloudBeyondcorpAppconnectionsV1AppConnectionGateway

Gateway represents a user facing component that serves as an entrance to enable connectivity.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**appGateway** | **String** | Required. AppGateway name in following format: &#x60;projects/{project_id}/locations/{location_id}/appgateways/{gateway_id}&#x60; |  [optional] |
|**ingressPort** | **Integer** | Output only. Ingress port reserved on the gateways for this AppConnection, if not specified or zero, the default port is 19443. |  [optional] [readonly] |
|**l7psc** | **String** | Output only. L7 private service connection for this resource. |  [optional] [readonly] |
|**type** | [**TypeEnum**](#TypeEnum) | Required. The type of hosting used by the gateway. |  [optional] |
|**uri** | **String** | Output only. Server-defined URI for this resource. |  [optional] [readonly] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| TYPE_UNSPECIFIED | &quot;TYPE_UNSPECIFIED&quot; |
| GCP_REGIONAL_MIG | &quot;GCP_REGIONAL_MIG&quot; |



