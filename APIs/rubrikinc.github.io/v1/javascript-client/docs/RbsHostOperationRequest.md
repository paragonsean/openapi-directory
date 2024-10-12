# RubrikRestApi.RbsHostOperationRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **String** | IP address or hostname of the host. | 
**operationTimeout** | **Number** | Number of seconds after which the operation is terminated if it has not completed execution. Default value is 600 seconds. | [optional] [default to 600]
**password** | **String** | Password associated with the username that has access to the host. | 
**username** | **String** | Name of the user account that has sudo/admin privileges on the RBS host. This is required to install/uninstall/upgrade RBS packages on the RBS host. | 
**operationMode** | [**OperationMode**](OperationMode.md) |  | [optional] 


