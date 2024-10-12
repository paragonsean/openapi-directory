# BooksApi.ConcurrentAccessRestriction

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deviceAllowed** | **Boolean** | Whether access is granted for this (user, device, volume). | [optional] 
**kind** | **String** | Resource type. | [optional] 
**maxConcurrentDevices** | **Number** | The maximum number of concurrent access licenses for this volume. | [optional] 
**message** | **String** | Error/warning message. | [optional] 
**nonce** | **String** | Client nonce for verification. Download access and client-validation only. | [optional] 
**reasonCode** | **String** | Error/warning reason code. | [optional] 
**restricted** | **Boolean** | Whether this volume has any concurrent access restrictions. | [optional] 
**signature** | **String** | Response signature. | [optional] 
**source** | **String** | Client app identifier for verification. Download access and client-validation only. | [optional] 
**timeWindowSeconds** | **Number** | Time in seconds for license auto-expiration. | [optional] 
**volumeId** | **String** | Identifies the volume for which this entry applies. | [optional] 


