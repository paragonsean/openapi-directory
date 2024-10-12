# FireFinancialServicesBusinessApi.User

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**emailAddress** | **String** | email address for user | [optional] 
**firstName** | **String** | User first name | [optional] 
**id** | **Number** | The User ID for this User | [optional] 
**lastName** | **String** | User second name | [optional] 
**lastlogin** | **String** | Timestamp on when user last logged in. | [optional] 
**mobileApplicationDetails** | [**MobileApplication**](MobileApplication.md) |  | [optional] 
**mobileNumber** | **String** | User mobile number | [optional] 
**role** | **String** | User role | [optional] 
**status** | **String** | Status of user | [optional] 
**userCvl** | **String** | Users Cvl type ID (shows up when status is LIVE) | [optional] 



## Enum: RoleEnum


* `ADMIN` (value: `"ADMIN"`)

* `FULL_USER` (value: `"FULL_USER"`)

* `READ_ONLY` (value: `"READ_ONLY"`)

* `CARD_ONLY` (value: `"CARD_ONLY"`)





## Enum: StatusEnum


* `LIVE` (value: `"LIVE"`)

* `CLOSED` (value: `"CLOSED"`)

* `FROZEN` (value: `"FROZEN"`)

* `INVITE_SENT` (value: `"INVITE_SENT"`)

* `SMS_CODE_SENT` (value: `"SMS_CODE_SENT"`)




