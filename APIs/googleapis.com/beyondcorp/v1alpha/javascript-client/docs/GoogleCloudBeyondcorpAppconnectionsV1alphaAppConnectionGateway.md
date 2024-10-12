# BeyondCorpApi.GoogleCloudBeyondcorpAppconnectionsV1alphaAppConnectionGateway

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**appGateway** | **String** | Required. AppGateway name in following format: &#x60;projects/{project_id}/locations/{location_id}/appgateways/{gateway_id}&#x60; | [optional] 
**ingressPort** | **Number** | Output only. Ingress port reserved on the gateways for this AppConnection, if not specified or zero, the default port is 19443. | [optional] [readonly] 
**l7psc** | **String** | Output only. L7 private service connection for this resource. | [optional] [readonly] 
**type** | **String** | Required. The type of hosting used by the gateway. | [optional] 
**uri** | **String** | Output only. Server-defined URI for this resource. | [optional] [readonly] 



## Enum: TypeEnum


* `TYPE_UNSPECIFIED` (value: `"TYPE_UNSPECIFIED"`)

* `GCP_REGIONAL_MIG` (value: `"GCP_REGIONAL_MIG"`)




