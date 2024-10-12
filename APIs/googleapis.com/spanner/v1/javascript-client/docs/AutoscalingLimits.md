# CloudSpannerApi.AutoscalingLimits

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**maxNodes** | **Number** | Maximum number of nodes allocated to the instance. If set, this number should be greater than or equal to min_nodes. | [optional] 
**maxProcessingUnits** | **Number** | Maximum number of processing units allocated to the instance. If set, this number should be multiples of 1000 and be greater than or equal to min_processing_units. | [optional] 
**minNodes** | **Number** | Minimum number of nodes allocated to the instance. If set, this number should be greater than or equal to 1. | [optional] 
**minProcessingUnits** | **Number** | Minimum number of processing units allocated to the instance. If set, this number should be multiples of 1000. | [optional] 


