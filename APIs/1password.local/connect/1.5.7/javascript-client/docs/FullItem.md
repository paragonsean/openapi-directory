# 1PasswordConnect.FullItem

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category** | **String** |  | 
**createdAt** | **Date** |  | [optional] [readonly] 
**favorite** | **Boolean** |  | [optional] [default to false]
**id** | **String** |  | [optional] 
**lastEditedBy** | **String** |  | [optional] [readonly] 
**state** | **String** |  | [optional] [readonly] 
**tags** | **[String]** |  | [optional] 
**title** | **String** |  | [optional] 
**updatedAt** | **Date** |  | [optional] [readonly] 
**urls** | [**[ItemUrlsInner]**](ItemUrlsInner.md) |  | [optional] 
**vault** | [**ItemVault**](ItemVault.md) |  | 
**version** | **Number** |  | [optional] 
**fields** | [**[Field]**](Field.md) |  | [optional] 
**files** | **[File]** |  | [optional] 
**sections** | [**[FullItemAllOfSections]**](FullItemAllOfSections.md) |  | [optional] 



## Enum: CategoryEnum


* `LOGIN` (value: `"LOGIN"`)

* `PASSWORD` (value: `"PASSWORD"`)

* `API_CREDENTIAL` (value: `"API_CREDENTIAL"`)

* `SERVER` (value: `"SERVER"`)

* `DATABASE` (value: `"DATABASE"`)

* `CREDIT_CARD` (value: `"CREDIT_CARD"`)

* `MEMBERSHIP` (value: `"MEMBERSHIP"`)

* `PASSPORT` (value: `"PASSPORT"`)

* `SOFTWARE_LICENSE` (value: `"SOFTWARE_LICENSE"`)

* `OUTDOOR_LICENSE` (value: `"OUTDOOR_LICENSE"`)

* `SECURE_NOTE` (value: `"SECURE_NOTE"`)

* `WIRELESS_ROUTER` (value: `"WIRELESS_ROUTER"`)

* `BANK_ACCOUNT` (value: `"BANK_ACCOUNT"`)

* `DRIVER_LICENSE` (value: `"DRIVER_LICENSE"`)

* `IDENTITY` (value: `"IDENTITY"`)

* `REWARD_PROGRAM` (value: `"REWARD_PROGRAM"`)

* `DOCUMENT` (value: `"DOCUMENT"`)

* `EMAIL_ACCOUNT` (value: `"EMAIL_ACCOUNT"`)

* `SOCIAL_SECURITY_NUMBER` (value: `"SOCIAL_SECURITY_NUMBER"`)

* `MEDICAL_RECORD` (value: `"MEDICAL_RECORD"`)

* `SSH_KEY` (value: `"SSH_KEY"`)

* `CUSTOM` (value: `"CUSTOM"`)





## Enum: StateEnum


* `ARCHIVED` (value: `"ARCHIVED"`)

* `DELETED` (value: `"DELETED"`)




