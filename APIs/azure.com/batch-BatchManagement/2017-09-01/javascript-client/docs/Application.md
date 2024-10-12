# BatchManagement.Application

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allowUpdates** | **Boolean** | A value indicating whether packages within the application may be overwritten using the same version string. | [optional] 
**defaultVersion** | **String** | The package to use if a client requests the application but does not specify a version. | [optional] 
**displayName** | **String** | The display name for the application. | [optional] 
**id** | **String** | A string that uniquely identifies the application within the account. | [optional] 
**packages** | [**[ApplicationPackage]**](ApplicationPackage.md) | The list of packages under this application. | [optional] 


