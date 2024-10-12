# BatchManagement.ApplicationPackageProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**format** | **String** | The format of the application package, if the package is active. | [optional] [readonly] 
**lastActivationTime** | **Date** | The time at which the package was last activated, if the package is active. | [optional] [readonly] 
**state** | **String** | The current state of the application package. | [optional] [readonly] 
**storageUrl** | **String** | The URL for the application package in Azure Storage. | [optional] [readonly] 
**storageUrlExpiry** | **Date** | The UTC time at which the Azure Storage URL will expire. | [optional] [readonly] 



## Enum: StateEnum


* `Pending` (value: `"Pending"`)

* `Active` (value: `"Active"`)




