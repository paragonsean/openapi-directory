# ApiV1.CombinedSubmissionAction

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**actionCategory** | **String** |  | 
**actionType** | **String** |  | 
**id** | **String** |  | 
**integrationId** | **String** |  | 
**resultData** | **Object** |  | 
**state** | **String** |  | 



## Enum: ActionCategoryEnum


* `notification` (value: `"notification"`)

* `file_upload` (value: `"file_upload"`)





## Enum: ActionTypeEnum


* `webhook` (value: `"webhook"`)

* `slack_webhook` (value: `"slack_webhook"`)

* `email` (value: `"email"`)

* `aws_s3_upload` (value: `"aws_s3_upload"`)





## Enum: StateEnum


* `pending` (value: `"pending"`)

* `processed` (value: `"processed"`)

* `failed` (value: `"failed"`)

* `error` (value: `"error"`)




