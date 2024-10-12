# AppCenterClient.DataSubjectRightDeleteStatusRequest200Response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **String** | explanation message of the status | 
**sasUrl** | **String** | Azure Storage shared access signature (SAS) URL for exported user data. | [optional] 
**sasUrlExpired** | **Boolean** | Whether Azure Storage shared access signature (SAS) URL has expired or not. | [optional] 
**status** | **String** | Status of data subject right request | 



## Enum: StatusEnum


* `None` (value: `"None"`)

* `Created` (value: `"Created"`)

* `Queued` (value: `"Queued"`)

* `InProgress` (value: `"InProgress"`)

* `Completed` (value: `"Completed"`)

* `Failed` (value: `"Failed"`)




