# BeezUpMerchantApi.ImportationMonitoring

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**beginUtcDate** | **Date** | The start date of the importation | 
**errors** | [**[BeezUPCommonUserErrorMessage]**](BeezUPCommonUserErrorMessage.md) | In case of error a description will be indicated | [optional] 
**executionId** | **String** | The execution identifier of the catalog importation | 
**lastUpdateUtcDate** | **Date** | The last update of the reporting | 
**links** | [**ImportationMonitoringLinks**](ImportationMonitoringLinks.md) |  | [optional] 
**steps** | **{String: Boolean}** | Contains all steps of the importation process with a boolean. If true the step has been passed, false the step is not complete | 
**success** | **Boolean** | Indicates if the importation was successfully completed or not | 
**userId** | **String** | The user identifier | [optional] 


