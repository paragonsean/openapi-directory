# AiPlatformTrainingPredictionApi.GoogleCloudMlV1OperationMetadata

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**createTime** | **String** | The time the operation was submitted. | [optional] 
**endTime** | **String** | The time operation processing completed. | [optional] 
**isCancellationRequested** | **Boolean** | Indicates whether a request to cancel this operation has been made. | [optional] 
**labels** | **{String: String}** | The user labels, inherited from the model or the model version being operated on. | [optional] 
**modelName** | **String** | Contains the name of the model associated with the operation. | [optional] 
**operationType** | **String** | The operation type. | [optional] 
**projectNumber** | **String** | Contains the project number associated with the operation. | [optional] 
**startTime** | **String** | The time operation processing started. | [optional] 
**version** | [**GoogleCloudMlV1Version**](GoogleCloudMlV1Version.md) |  | [optional] 



## Enum: OperationTypeEnum


* `OPERATION_TYPE_UNSPECIFIED` (value: `"OPERATION_TYPE_UNSPECIFIED"`)

* `CREATE_VERSION` (value: `"CREATE_VERSION"`)

* `DELETE_VERSION` (value: `"DELETE_VERSION"`)

* `DELETE_MODEL` (value: `"DELETE_MODEL"`)

* `UPDATE_MODEL` (value: `"UPDATE_MODEL"`)

* `UPDATE_VERSION` (value: `"UPDATE_VERSION"`)

* `UPDATE_CONFIG` (value: `"UPDATE_CONFIG"`)




