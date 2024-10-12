# ApiGatewayApi.ApigatewayApi

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**createTime** | **String** | Output only. Created time. | [optional] [readonly] 
**displayName** | **String** | Optional. Display name. | [optional] 
**labels** | **{String: String}** | Optional. Resource labels to represent user-provided metadata. Refer to cloud documentation on labels for more details. https://cloud.google.com/compute/docs/labeling-resources | [optional] 
**managedService** | **String** | Optional. Immutable. The name of a Google Managed Service ( https://cloud.google.com/service-infrastructure/docs/glossary#managed). If not specified, a new Service will automatically be created in the same project as this API. | [optional] 
**name** | **String** | Output only. Resource name of the API. Format: projects/{project}/locations/global/apis/{api} | [optional] [readonly] 
**state** | **String** | Output only. State of the API. | [optional] [readonly] 
**updateTime** | **String** | Output only. Updated time. | [optional] [readonly] 



## Enum: StateEnum


* `STATE_UNSPECIFIED` (value: `"STATE_UNSPECIFIED"`)

* `CREATING` (value: `"CREATING"`)

* `ACTIVE` (value: `"ACTIVE"`)

* `FAILED` (value: `"FAILED"`)

* `DELETING` (value: `"DELETING"`)

* `UPDATING` (value: `"UPDATING"`)




