# Mailsquad.Contact

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **String** | Unique 16 characters ID | [optional] 
**clientid** | **String** | Unique 16 characters ID of the client owner | [optional] 
**confirmed** | **Date** | Date+time subscriber confirmed his/her list opt-in | [optional] 
**customfields** | **Object** | Dictionnary of field key to value | [optional] 
**email** | **String** | Email address | [optional] 
**fullname** | **String** | Full name (Last name, First Name) of the subscriber  | [optional] 
**ip** | **String** | Subscriber&#39;s IP address when he/she confirmed list opt-in | [optional] 
**lang** | **String** | ISO 639-1 language code of the subscriber. When lang is one the supported system language, all communication will be in this language.   | [optional] 
**listid** | **String** | Unique 16 characters ID of the list owner | [optional] 
**status** | **Number** | Status (   1- Active,   2- Unconfirmed,   3- Unsubscribed,   4- Deleted,   5- Cleaned because of hard bounce or spam complaint)  | [optional] 


