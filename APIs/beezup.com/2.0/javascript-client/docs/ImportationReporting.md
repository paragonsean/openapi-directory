# BeezUpMerchantApi.ImportationReporting

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**autoImported** | **Boolean** | Indicate if this importation is an auto import or not. | [optional] 
**beginUtcDate** | **Date** | Indicate the begin UTC date of this importation. | 
**endUtcDate** | **Date** | Indicate the end UTC date of this importation. | [optional] 
**errors** | [**[BeezUPCommonUserErrorMessage]**](BeezUPCommonUserErrorMessage.md) | Indicate the error message list related to this importation. | [optional] 
**executionId** | **String** | The execution identifier of the catalog importation | 
**inputConfigurationUrl** | **String** | Indicate the input url of this importation. | [optional] 
**lastUpdateUtcDate** | **Date** | Indicate the last update UTC date of the reporting. | 
**links** | [**ImportationReportingLinks**](ImportationReportingLinks.md) |  | [optional] 
**stepName** | **String** | The last step name of the importation process | [optional] 
**steps** | **{String: Boolean}** | Indicate the steps that have been passed during the importation process | 
**success** | **Boolean** | Indicate if the importation succeed or not. | [optional] 
**totalProductCount** | **Number** | Indicate the total product count detected in the catalog during the importation. | [optional] 
**totalProductErrorCount** | **Number** | Indicate the total product count in error detected in the catalog during the importation. | [optional] 
**totalProductSuccessCount** | **Number** | Indicate the total product count in success in the catalog during the importation. | [optional] 
**userId** | **String** | The user identifier | [optional] 


