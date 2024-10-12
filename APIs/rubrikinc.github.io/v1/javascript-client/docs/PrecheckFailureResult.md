# RubrikRestApi.PrecheckFailureResult

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cause** | **String** | The cause of the failure. | [optional] 
**errorCode** | **String** | The precheck failure error code. This is used as a reference to a KB article about the error. | 
**errorMessage** | **String** | The precheck failure message. | 
**id** | **String** | The ID of the precheck error message. | 
**isUpgradeBlocker** | **Boolean** | Specifies whether a failed precheck prevents an upgrade from starting. | 
**isUserRemediable** | **Boolean** | Can the user fix this precheck failure. | 
**precheckName** | **String** | The name of the failed upgrade precheck. | 
**remedy** | **String** | The user action needed to recover from this failure. | [optional] 


