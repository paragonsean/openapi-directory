# XeroAccountingApi.User

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**emailAddress** | **String** | Email address of user | [optional] 
**firstName** | **String** | First name of user | [optional] 
**isSubscriber** | **Boolean** | Boolean to indicate if user is the subscriber | [optional] 
**lastName** | **String** | Last name of user | [optional] 
**organisationRole** | **String** | User role that defines permissions in Xero and via API (READONLY, INVOICEONLY, STANDARD, FINANCIALADVISER, etc) | [optional] 
**updatedDateUTC** | **String** | Timestamp of last change to user | [optional] [readonly] 
**userID** | **String** | Xero identifier | [optional] 



## Enum: OrganisationRoleEnum


* `READONLY` (value: `"READONLY"`)

* `INVOICEONLY` (value: `"INVOICEONLY"`)

* `STANDARD` (value: `"STANDARD"`)

* `FINANCIALADVISER` (value: `"FINANCIALADVISER"`)

* `MANAGEDCLIENT` (value: `"MANAGEDCLIENT"`)

* `CASHBOOKCLIENT` (value: `"CASHBOOKCLIENT"`)

* `UNKNOWN` (value: `"UNKNOWN"`)




