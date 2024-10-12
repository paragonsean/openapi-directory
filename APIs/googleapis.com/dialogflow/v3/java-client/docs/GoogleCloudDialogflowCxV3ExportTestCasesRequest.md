

# GoogleCloudDialogflowCxV3ExportTestCasesRequest

The request message for TestCases.ExportTestCases.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**dataFormat** | [**DataFormatEnum**](#DataFormatEnum) | The data format of the exported test cases. If not specified, &#x60;BLOB&#x60; is assumed. |  [optional] |
|**filter** | **String** | The filter expression used to filter exported test cases, see [API Filtering](https://aip.dev/160). The expression is case insensitive and supports the following syntax: name &#x3D; [OR name &#x3D; ] ... For example: * \&quot;name &#x3D; t1 OR name &#x3D; t2\&quot; matches the test case with the exact resource name \&quot;t1\&quot; or \&quot;t2\&quot;. |  [optional] |
|**gcsUri** | **String** | The [Google Cloud Storage](https://cloud.google.com/storage/docs/) URI to export the test cases to. The format of this URI must be &#x60;gs:///&#x60;. If unspecified, the serialized test cases is returned inline. Dialogflow performs a write operation for the Cloud Storage object on the caller&#39;s behalf, so your request authentication must have write permissions for the object. For more information, see [Dialogflow access control](https://cloud.google.com/dialogflow/cx/docs/concept/access-control#storage). |  [optional] |



## Enum: DataFormatEnum

| Name | Value |
|---- | -----|
| DATA_FORMAT_UNSPECIFIED | &quot;DATA_FORMAT_UNSPECIFIED&quot; |
| BLOB | &quot;BLOB&quot; |
| JSON | &quot;JSON&quot; |



