# CloudComposerApi.OperationMetadata

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**createTime** | **String** | Output only. The time the operation was submitted to the server. | [optional] 
**endTime** | **String** | Output only. The time when the operation terminated, regardless of its success. This field is unset if the operation is still ongoing. | [optional] 
**operationType** | **String** | Output only. The type of operation being performed. | [optional] 
**resource** | **String** | Output only. The resource being operated on, as a [relative resource name]( /apis/design/resource_names#relative_resource_name). | [optional] 
**resourceUuid** | **String** | Output only. The UUID of the resource being operated on. | [optional] 
**state** | **String** | Output only. The current operation state. | [optional] 



## Enum: OperationTypeEnum


* `TYPE_UNSPECIFIED` (value: `"TYPE_UNSPECIFIED"`)

* `CREATE` (value: `"CREATE"`)

* `DELETE` (value: `"DELETE"`)

* `UPDATE` (value: `"UPDATE"`)

* `CHECK` (value: `"CHECK"`)

* `SAVE_SNAPSHOT` (value: `"SAVE_SNAPSHOT"`)

* `LOAD_SNAPSHOT` (value: `"LOAD_SNAPSHOT"`)

* `DATABASE_FAILOVER` (value: `"DATABASE_FAILOVER"`)





## Enum: StateEnum


* `STATE_UNSPECIFIED` (value: `"STATE_UNSPECIFIED"`)

* `PENDING` (value: `"PENDING"`)

* `RUNNING` (value: `"RUNNING"`)

* `SUCCEEDED` (value: `"SUCCEEDED"`)

* `SUCCESSFUL` (value: `"SUCCESSFUL"`)

* `FAILED` (value: `"FAILED"`)




