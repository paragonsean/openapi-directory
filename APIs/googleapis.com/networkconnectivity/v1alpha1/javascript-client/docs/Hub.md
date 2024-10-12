# NetworkConnectivityApi.Hub

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**createTime** | **String** | Time when the Hub was created. | [optional] 
**description** | **String** | Short description of the hub resource. | [optional] 
**labels** | **{String: String}** | User-defined labels. | [optional] 
**name** | **String** | Immutable. The name of a Hub resource. | [optional] 
**spokes** | **[String]** | Output only. A list of the URIs of all attached spokes. This field is deprecated and will not be included in future API versions. Call ListSpokes on each region instead. | [optional] [readonly] 
**state** | **String** | Output only. The current lifecycle state of this Hub. | [optional] [readonly] 
**uniqueId** | **String** | Output only. Google-generated UUID for this resource. This is unique across all Hub resources. If a Hub resource is deleted and another with the same name is created, it gets a different unique_id. | [optional] [readonly] 
**updateTime** | **String** | Time when the Hub was updated. | [optional] 



## Enum: StateEnum


* `STATE_UNSPECIFIED` (value: `"STATE_UNSPECIFIED"`)

* `CREATING` (value: `"CREATING"`)

* `ACTIVE` (value: `"ACTIVE"`)

* `DELETING` (value: `"DELETING"`)

* `UPDATING` (value: `"UPDATING"`)




