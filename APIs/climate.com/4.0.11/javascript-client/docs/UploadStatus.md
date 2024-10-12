# ClimateFieldViewPlatformApis.UploadStatus

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **String** | Unique identifier for the upload. | 
**status** | **String** | Current status of the upload:   * &#x60;UPLOADING&#x60; - Uploading has started, parts are still coming in.   * &#x60;INVALID&#x60; - Upload has failed validity check.   * &#x60;PENDING&#x60; - Upload has been received by Climate and is being processed.   * &#x60;INBOX&#x60; - The upload is awaiting user acceptance in their Data Inbox.   * &#x60;DECLINED&#x60; - The user has declined the upload in their Data Inbox.   * &#x60;IMPORTING&#x60; - The user has accepted the upload and it is being imported into their account.   * &#x60;SUCCESS&#x60; - The upload has been successfully imported.  | 



## Enum: StatusEnum


* `UPLOADING` (value: `"UPLOADING"`)

* `INVALID` (value: `"INVALID"`)

* `PENDING` (value: `"PENDING"`)

* `INBOX` (value: `"INBOX"`)

* `DECLINED` (value: `"DECLINED"`)

* `IMPORTING` (value: `"IMPORTING"`)

* `SUCCESS` (value: `"SUCCESS"`)




