# AwsMainframeModernization.CreateDataSetImportTaskRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**clientToken** | **String** |  Unique, case-sensitive identifier you provide to ensure the idempotency of the request to create a data set import. The service generates the clientToken when the API call is triggered. The token expires after one hour, so if you retry the API within this timeframe with the same clientToken, you will get the same response. The service also handles deleting the clientToken after it expires.  | [optional] 
**importConfig** | [**CreateDataSetImportTaskRequestImportConfig**](CreateDataSetImportTaskRequestImportConfig.md) |  | 


