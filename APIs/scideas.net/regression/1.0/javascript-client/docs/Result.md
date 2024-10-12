# RegressionAnalysisApi.Result

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**calls** | [**ResultCalls**](ResultCalls.md) |  | [optional] 
**dataCount** | **Number** | number of data rows processed | [optional] 
**datesConvertedTo** | **String** | either month or week | [optional] 
**footer** | **String** | text for pdf footer | [optional] 
**header** | **String** | text for pdf header | [optional] 
**numberObservations** | **Number** | number of data rows used for analysis | [optional] 
**numberTests** | **Number** | number of data rows used to test model accuracy | [optional] 
**outcomeVariable** | **String** | the name of the variable processed as the outcome | [optional] 
**paid** | **String** | yes if paid subscriber, otherwise no | [optional] 
**pdf** | **String** | url of pdf summary | [optional] 
**predictionMeanAccuracy** | **Number** | percentage accuracy of model created | [optional] 
**standardizedCoefficients** | [**[ResultStandardizedCoefficients]**](ResultStandardizedCoefficients.md) |  | [optional] 
**summary** | **[Object]** |  | [optional] 
**testedVariables** | **[String]** |  | [optional] 


