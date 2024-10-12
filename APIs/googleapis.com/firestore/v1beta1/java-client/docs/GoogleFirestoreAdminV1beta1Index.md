

# GoogleFirestoreAdminV1beta1Index

An index definition.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**collectionId** | **String** | The collection ID to which this index applies. Required. |  [optional] |
|**fields** | [**List&lt;GoogleFirestoreAdminV1beta1IndexField&gt;**](GoogleFirestoreAdminV1beta1IndexField.md) | The fields to index. |  [optional] |
|**name** | **String** | The resource name of the index. Output only. |  [optional] |
|**state** | [**StateEnum**](#StateEnum) | The state of the index. Output only. |  [optional] |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| STATE_UNSPECIFIED | &quot;STATE_UNSPECIFIED&quot; |
| CREATING | &quot;CREATING&quot; |
| READY | &quot;READY&quot; |
| ERROR | &quot;ERROR&quot; |



