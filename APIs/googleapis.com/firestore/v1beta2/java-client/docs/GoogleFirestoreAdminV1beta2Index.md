

# GoogleFirestoreAdminV1beta2Index

Cloud Firestore indexes enable simple and complex queries against documents in a database.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**fields** | [**List&lt;GoogleFirestoreAdminV1beta2IndexField&gt;**](GoogleFirestoreAdminV1beta2IndexField.md) | The fields supported by this index. For composite indexes, this is always 2 or more fields. The last field entry is always for the field path &#x60;__name__&#x60;. If, on creation, &#x60;__name__&#x60; was not specified as the last field, it will be added automatically with the same direction as that of the last field defined. If the final field in a composite index is not directional, the &#x60;__name__&#x60; will be ordered ASCENDING (unless explicitly specified). For single field indexes, this will always be exactly one entry with a field path equal to the field path of the associated field. |  [optional] |
|**name** | **String** | Output only. A server defined name for this index. The form of this name for composite indexes will be: &#x60;projects/{project_id}/databases/{database_id}/collectionGroups/{collection_id}/indexes/{composite_index_id}&#x60; For single field indexes, this field will be empty. |  [optional] |
|**queryScope** | [**QueryScopeEnum**](#QueryScopeEnum) | Indexes with a collection query scope specified allow queries against a collection that is the child of a specific document, specified at query time, and that has the same collection id. Indexes with a collection group query scope specified allow queries against all collections descended from a specific document, specified at query time, and that have the same collection id as this index. |  [optional] |
|**state** | [**StateEnum**](#StateEnum) | Output only. The serving state of the index. |  [optional] |



## Enum: QueryScopeEnum

| Name | Value |
|---- | -----|
| QUERY_SCOPE_UNSPECIFIED | &quot;QUERY_SCOPE_UNSPECIFIED&quot; |
| COLLECTION | &quot;COLLECTION&quot; |
| COLLECTION_GROUP | &quot;COLLECTION_GROUP&quot; |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| STATE_UNSPECIFIED | &quot;STATE_UNSPECIFIED&quot; |
| CREATING | &quot;CREATING&quot; |
| READY | &quot;READY&quot; |
| NEEDS_REPAIR | &quot;NEEDS_REPAIR&quot; |



