# ApiGatewayApi.ApigatewayGateway

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apiConfig** | **String** | Required. Resource name of the API Config for this Gateway. Format: projects/{project}/locations/global/apis/{api}/configs/{apiConfig} | [optional] 
**createTime** | **String** | Output only. Created time. | [optional] [readonly] 
**defaultHostname** | **String** | Output only. The default API Gateway host name of the form &#x60;{gateway_id}-{hash}.{region_code}.gateway.dev&#x60;. | [optional] [readonly] 
**displayName** | **String** | Optional. Display name. | [optional] 
**labels** | **{String: String}** | Optional. Resource labels to represent user-provided metadata. Refer to cloud documentation on labels for more details. https://cloud.google.com/compute/docs/labeling-resources | [optional] 
**name** | **String** | Output only. Resource name of the Gateway. Format: projects/{project}/locations/{location}/gateways/{gateway} | [optional] [readonly] 
**state** | **String** | Output only. The current state of the Gateway. | [optional] [readonly] 
**updateTime** | **String** | Output only. Updated time. | [optional] [readonly] 



## Enum: StateEnum


* `STATE_UNSPECIFIED` (value: `"STATE_UNSPECIFIED"`)

* `CREATING` (value: `"CREATING"`)

* `ACTIVE` (value: `"ACTIVE"`)

* `FAILED` (value: `"FAILED"`)

* `DELETING` (value: `"DELETING"`)

* `UPDATING` (value: `"UPDATING"`)




