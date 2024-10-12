# AmazonLookoutForVision.StartModelRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**minInferenceUnits** | **Number** | The minimum number of inference units to use. A single inference unit represents 1 hour of processing. Use a higher number to increase the TPS throughput of your model. You are charged for the number of inference units that you use.  | 
**maxInferenceUnits** | **Number** | The maximum number of inference units to use for auto-scaling the model. If you don&#39;t specify a value, Amazon Lookout for Vision doesn&#39;t auto-scale the model. | [optional] 


