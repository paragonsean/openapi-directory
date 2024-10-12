

# GoogleDatastoreAdminV1Index

Datastore composite index definition.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**ancestor** | [**AncestorEnum**](#AncestorEnum) | Required. The index&#39;s ancestor mode. Must not be ANCESTOR_MODE_UNSPECIFIED. |  [optional] |
|**indexId** | **String** | Output only. The resource ID of the index. |  [optional] [readonly] |
|**kind** | **String** | Required. The entity kind to which this index applies. |  [optional] |
|**projectId** | **String** | Output only. Project ID. |  [optional] [readonly] |
|**properties** | [**List&lt;GoogleDatastoreAdminV1IndexedProperty&gt;**](GoogleDatastoreAdminV1IndexedProperty.md) | Required. An ordered sequence of property names and their index attributes. Requires: * A maximum of 100 properties. |  [optional] |
|**state** | [**StateEnum**](#StateEnum) | Output only. The state of the index. |  [optional] [readonly] |



## Enum: AncestorEnum

| Name | Value |
|---- | -----|
| ANCESTOR_MODE_UNSPECIFIED | &quot;ANCESTOR_MODE_UNSPECIFIED&quot; |
| NONE | &quot;NONE&quot; |
| ALL_ANCESTORS | &quot;ALL_ANCESTORS&quot; |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| STATE_UNSPECIFIED | &quot;STATE_UNSPECIFIED&quot; |
| CREATING | &quot;CREATING&quot; |
| READY | &quot;READY&quot; |
| DELETING | &quot;DELETING&quot; |
| ERROR | &quot;ERROR&quot; |



