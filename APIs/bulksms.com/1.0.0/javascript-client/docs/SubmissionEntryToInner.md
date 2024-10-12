# BulkSmsJsonRestApi.SubmissionEntryToInner

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **String** | The phone number of the recipient.  It must be supplied if the &#x60;type&#x60; is INTERNATIONAL | [optional] 
**fields** | **[String]** | Custom fields that can be used in the message body. A value can be given if the &#x60;type&#x60; is INTERNATIONAL  Read the [body templates section](#tag/Message) for more information.  | [optional] 
**id** | **String** | The id of a group in your phonebook.  A value can be given if the &#x60;type&#x60; is GROUP. | [optional] 
**name** | **String** | The name of a group in your phonebook. A value can be given if the &#x60;type&#x60; is GROUP. | [optional] 
**type** | **String** | Type of the recipient. The default value is INTERNATIONAL. | [optional] 



## Enum: TypeEnum


* `INTERNATIONAL` (value: `"INTERNATIONAL"`)

* `GROUP` (value: `"GROUP"`)




