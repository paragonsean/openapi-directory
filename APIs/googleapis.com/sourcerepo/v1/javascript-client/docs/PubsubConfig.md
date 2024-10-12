# CloudSourceRepositoriesApi.PubsubConfig

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**messageFormat** | **String** | The format of the Cloud Pub/Sub messages. | [optional] 
**serviceAccountEmail** | **String** | Email address of the service account used for publishing Cloud Pub/Sub messages. This service account needs to be in the same project as the PubsubConfig. When added, the caller needs to have iam.serviceAccounts.actAs permission on this service account. If unspecified, it defaults to the compute engine default service account. | [optional] 
**topic** | **String** | A topic of Cloud Pub/Sub. Values are of the form &#x60;projects//topics/&#x60;. The project needs to be the same project as this config is in. | [optional] 



## Enum: MessageFormatEnum


* `MESSAGE_FORMAT_UNSPECIFIED` (value: `"MESSAGE_FORMAT_UNSPECIFIED"`)

* `PROTOBUF` (value: `"PROTOBUF"`)

* `JSON` (value: `"JSON"`)




