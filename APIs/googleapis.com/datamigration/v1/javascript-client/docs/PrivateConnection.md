# DatabaseMigrationApi.PrivateConnection

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**createTime** | **String** | Output only. The create time of the resource. | [optional] [readonly] 
**displayName** | **String** | The private connection display name. | [optional] 
**error** | [**Status**](Status.md) |  | [optional] 
**labels** | **{String: String}** | The resource labels for private connections to use to annotate any related underlying resources such as Compute Engine VMs. An object containing a list of \&quot;key\&quot;: \&quot;value\&quot; pairs. Example: &#x60;{ \&quot;name\&quot;: \&quot;wrench\&quot;, \&quot;mass\&quot;: \&quot;1.3kg\&quot;, \&quot;count\&quot;: \&quot;3\&quot; }&#x60;. | [optional] 
**name** | **String** | The name of the resource. | [optional] 
**state** | **String** | Output only. The state of the private connection. | [optional] [readonly] 
**updateTime** | **String** | Output only. The last update time of the resource. | [optional] [readonly] 
**vpcPeeringConfig** | [**VpcPeeringConfig**](VpcPeeringConfig.md) |  | [optional] 



## Enum: StateEnum


* `STATE_UNSPECIFIED` (value: `"STATE_UNSPECIFIED"`)

* `CREATING` (value: `"CREATING"`)

* `CREATED` (value: `"CREATED"`)

* `FAILED` (value: `"FAILED"`)

* `DELETING` (value: `"DELETING"`)

* `FAILED_TO_DELETE` (value: `"FAILED_TO_DELETE"`)

* `DELETED` (value: `"DELETED"`)




