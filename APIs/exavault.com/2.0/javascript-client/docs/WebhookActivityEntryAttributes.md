# ExaVault.WebhookActivityEntryAttributes

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accountId** | **String** | Unique ID of account | [optional] 
**attemptId** | **String** | Event - retry identifier | [optional] 
**created** | **String** | Date and time of webhook message being generated by system | [optional] 
**details** | [**WebhookV1Details**](WebhookV1Details.md) |  | [optional] 
**endpointUrl** | **String** | The URL the message was sent to | [optional] 
**event** | **String** | Event type | [optional] 
**ipAddress** | **String** | IP Address of related activity | [optional] 
**resend** | **Boolean** | Whether this attempt was a re-send of a previous attempt | [optional] 
**resourcePath** | **String** | Path of resource that matched webhook | [optional] 
**response** | **String** | Body of web response returned by webhook listener | [optional] 
**status** | **Number** | HTTP Status Code returned by webhook listener | [optional] 
**username** | **String** | Username of related activity | [optional] 
**webhookFormat** | **String** | What version of webhook message is being sent &#x60;v1&#x60; | [optional] 
**webhookId** | **Number** | Unique ID of webhook configuration | [optional] 
**webhookPath** | **String** | Path that webhook is watching | [optional] 



## Enum: EventEnum


* `resources.upload` (value: `"resources.upload"`)

* `resources.download` (value: `"resources.download"`)

* `resources.delete` (value: `"resources.delete"`)

* `resources.rename` (value: `"resources.rename"`)

* `resources.copy` (value: `"resources.copy"`)

* `resources.move` (value: `"resources.move"`)

* `resources.compress` (value: `"resources.compress"`)

* `resources.extract` (value: `"resources.extract"`)

* `resources.createFolder` (value: `"resources.createFolder"`)

* `shares.formSubmit` (value: `"shares.formSubmit"`)




