# VaultApi.Log

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apiStyle** | **String** | Indicates if the request was made via REST or Graphql endpoint. | 
**baseUrl** | **String** | The Apideck base URL the request was made to. | 
**childRequest** | **Boolean** | Indicates whether or not this is a child or parent request. | 
**consumerId** | **String** | The consumer Id associated with the request. | 
**duration** | **Number** | The entire execution time in milliseconds it took to call the Apideck service provider. | 
**errorMessage** | **String** | If error occurred, this is brief explanation | [optional] 
**execution** | **Number** | The entire execution time in milliseconds it took to make the request. | 
**hasChildren** | **Boolean** | When request is a parent request, this indicates if there are child requests associated. | 
**httpMethod** | **String** | HTTP Method of request. | 
**id** | **String** | UUID acting as Request Identifier. | 
**latency** | **Number** | Latency added by making this request via Unified Api. | 
**operation** | [**LogOperation**](LogOperation.md) |  | 
**parentId** | **String** | When request is a child request, this UUID indicates it&#39;s parent request. | 
**path** | **String** | The path component of the URI the request was made to. | 
**sandbox** | **Boolean** | Indicates whether the request was made using Apidecks sandbox credentials or not. | 
**service** | [**LogService**](LogService.md) |  | 
**sourceIp** | **String** | The IP address of the source of the request. | [optional] 
**statusCode** | **Number** | HTTP Status code that was returned. | 
**success** | **Boolean** | Whether or not the request was successful. | 
**timestamp** | **String** | ISO Date and time when the request was made. | 
**unifiedApi** | **String** | Which Unified Api request was made to. | 



## Enum: UnifiedApiEnum


* `crm` (value: `"crm"`)

* `lead` (value: `"lead"`)

* `proxy` (value: `"proxy"`)

* `vault` (value: `"vault"`)

* `accounting` (value: `"accounting"`)

* `hris` (value: `"hris"`)

* `ats` (value: `"ats"`)

* `ecommerce` (value: `"ecommerce"`)

* `issue-tracking` (value: `"issue-tracking"`)

* `pos` (value: `"pos"`)

* `file-storage` (value: `"file-storage"`)

* `sms` (value: `"sms"`)




