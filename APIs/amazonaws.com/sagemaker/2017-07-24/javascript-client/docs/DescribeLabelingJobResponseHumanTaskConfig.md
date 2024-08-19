# AmazonSageMakerService.DescribeLabelingJobResponseHumanTaskConfig

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workteamArn** | **String** |  | 
**uiConfig** | [**HumanTaskConfigUiConfig**](HumanTaskConfigUiConfig.md) |  | 
**preHumanTaskLambdaArn** | **String** |  | 
**taskKeywords** | **Array** |  | [optional] 
**taskTitle** | **String** |  | 
**taskDescription** | **String** |  | 
**numberOfHumanWorkersPerDataObject** | **Number** |  | 
**taskTimeLimitInSeconds** | **Number** |  | 
**taskAvailabilityLifetimeInSeconds** | **Number** |  | [optional] 
**maxConcurrentTaskCount** | **Number** |  | [optional] 
**annotationConsolidationConfig** | [**HumanTaskConfigAnnotationConsolidationConfig**](HumanTaskConfigAnnotationConsolidationConfig.md) |  | 
**publicWorkforceTaskPrice** | [**HumanTaskConfigPublicWorkforceTaskPrice**](HumanTaskConfigPublicWorkforceTaskPrice.md) |  | [optional] 


