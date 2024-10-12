# Mailsquad.SubscriptionRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**confirmed** | **Date** | Date-time when subscriber opted-in. Required if singleoptin is true. | [optional] 
**email** | **String** | Email address of the subscriber | 
**fullname** | **String** | Full name (Last name, First Name) of the subscriber  | [optional] 
**ip** | **String** | Origin Ip of the subscriber when he/she opted-in. Required if singleoptin is true. | [optional] 
**lang** | **String** | ISO 639-1 language code of the subscriber. When lang is one the supported system language, all communication will be in this language.  | [optional] 
**singleoptin** | **Boolean** | If true, no email will be sent asking user subscription confirmation. In that case, you must provide the confirmation date (confirmed) and origin ip (ip) manually.  | [optional] 


