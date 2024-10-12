# CloudDatastoreApi.GoogleDatastoreAdminV1Index

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ancestor** | **String** | Required. The index&#39;s ancestor mode. Must not be ANCESTOR_MODE_UNSPECIFIED. | [optional] 
**indexId** | **String** | Output only. The resource ID of the index. | [optional] [readonly] 
**kind** | **String** | Required. The entity kind to which this index applies. | [optional] 
**projectId** | **String** | Output only. Project ID. | [optional] [readonly] 
**properties** | [**[GoogleDatastoreAdminV1IndexedProperty]**](GoogleDatastoreAdminV1IndexedProperty.md) | Required. An ordered sequence of property names and their index attributes. Requires: * A maximum of 100 properties. | [optional] 
**state** | **String** | Output only. The state of the index. | [optional] [readonly] 



## Enum: AncestorEnum


* `ANCESTOR_MODE_UNSPECIFIED` (value: `"ANCESTOR_MODE_UNSPECIFIED"`)

* `NONE` (value: `"NONE"`)

* `ALL_ANCESTORS` (value: `"ALL_ANCESTORS"`)





## Enum: StateEnum


* `STATE_UNSPECIFIED` (value: `"STATE_UNSPECIFIED"`)

* `CREATING` (value: `"CREATING"`)

* `READY` (value: `"READY"`)

* `DELETING` (value: `"DELETING"`)

* `ERROR` (value: `"ERROR"`)




