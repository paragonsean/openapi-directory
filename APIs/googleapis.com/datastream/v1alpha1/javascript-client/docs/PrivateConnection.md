# DatastreamApi.PrivateConnection

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**createTime** | **String** | Output only. The create time of the resource. | [optional] [readonly] 
**displayName** | **String** | Required. Display name. | [optional] 
**error** | [**Error**](Error.md) |  | [optional] 
**labels** | **{String: String}** | Labels. | [optional] 
**name** | **String** | Output only. The resource&#39;s name. | [optional] [readonly] 
**state** | **String** | Output only. The state of the Private Connection. | [optional] [readonly] 
**updateTime** | **String** | Output only. The update time of the resource. | [optional] [readonly] 
**vpcPeeringConfig** | [**VpcPeeringConfig**](VpcPeeringConfig.md) |  | [optional] 



## Enum: StateEnum


* `STATE_UNSPECIFIED` (value: `"STATE_UNSPECIFIED"`)

* `CREATING` (value: `"CREATING"`)

* `CREATED` (value: `"CREATED"`)

* `FAILED` (value: `"FAILED"`)

* `DELETING` (value: `"DELETING"`)

* `FAILED_TO_DELETE` (value: `"FAILED_TO_DELETE"`)




