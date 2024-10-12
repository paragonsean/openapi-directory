# EqivoApi.BulkCallResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **String** | Response message | 
**requestUUID** | **[String]** | Unique identifiers of each Call request (UUIDv4) | 
**restApiServer** | **String** | API server which handled this request (an Eqivo extension) | 
**success** | **Boolean** | Whether the request was successful or not | 



## Enum: MessageEnum


* `BulkCalls Request Executed` (value: `"BulkCalls Request Executed"`)

* `Mandatory Parameters Missing` (value: `"Mandatory Parameters Missing"`)

* `This Delimiter is not allowed` (value: `"This Delimiter is not allowed"`)

* `BulkCalls should be used for at least 2 numbers` (value: `"BulkCalls should be used for at least 2 numbers"`)

* `&#39;To&#39; parameter length does not match &#39;Gateways&#39; Length` (value: `"'To' parameter length does not match 'Gateways' Length"`)

* `AnswerUrl is not Valid` (value: `"AnswerUrl is not Valid"`)

* `HangupUrl is not Valid` (value: `"HangupUrl is not Valid"`)

* `RingUrl is not Valid` (value: `"RingUrl is not Valid"`)

* `Unknown Core UUID` (value: `"Unknown Core UUID"`)




