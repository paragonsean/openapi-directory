# CloudFirestoreApi.GoogleFirestoreAdminV1beta2Index

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fields** | [**[GoogleFirestoreAdminV1beta2IndexField]**](GoogleFirestoreAdminV1beta2IndexField.md) | The fields supported by this index. For composite indexes, this is always 2 or more fields. The last field entry is always for the field path &#x60;__name__&#x60;. If, on creation, &#x60;__name__&#x60; was not specified as the last field, it will be added automatically with the same direction as that of the last field defined. If the final field in a composite index is not directional, the &#x60;__name__&#x60; will be ordered ASCENDING (unless explicitly specified). For single field indexes, this will always be exactly one entry with a field path equal to the field path of the associated field. | [optional] 
**name** | **String** | Output only. A server defined name for this index. The form of this name for composite indexes will be: &#x60;projects/{project_id}/databases/{database_id}/collectionGroups/{collection_id}/indexes/{composite_index_id}&#x60; For single field indexes, this field will be empty. | [optional] 
**queryScope** | **String** | Indexes with a collection query scope specified allow queries against a collection that is the child of a specific document, specified at query time, and that has the same collection id. Indexes with a collection group query scope specified allow queries against all collections descended from a specific document, specified at query time, and that have the same collection id as this index. | [optional] 
**state** | **String** | Output only. The serving state of the index. | [optional] 



## Enum: QueryScopeEnum


* `QUERY_SCOPE_UNSPECIFIED` (value: `"QUERY_SCOPE_UNSPECIFIED"`)

* `COLLECTION` (value: `"COLLECTION"`)

* `COLLECTION_GROUP` (value: `"COLLECTION_GROUP"`)





## Enum: StateEnum


* `STATE_UNSPECIFIED` (value: `"STATE_UNSPECIFIED"`)

* `CREATING` (value: `"CREATING"`)

* `READY` (value: `"READY"`)

* `NEEDS_REPAIR` (value: `"NEEDS_REPAIR"`)




