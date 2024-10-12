

# UpdateTransferJobRequest

Request passed to UpdateTransferJob.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**projectId** | **String** | Required. The ID of the Google Cloud project that owns the job. |  [optional] |
|**transferJob** | [**TransferJob**](TransferJob.md) |  |  [optional] |
|**updateTransferJobFieldMask** | **String** | The field mask of the fields in &#x60;transferJob&#x60; that are to be updated in this request. Fields in &#x60;transferJob&#x60; that can be updated are: description, transfer_spec, notification_config, logging_config, and status. To update the &#x60;transfer_spec&#x60; of the job, a complete transfer specification must be provided. An incomplete specification missing any required fields is rejected with the error INVALID_ARGUMENT. |  [optional] |



