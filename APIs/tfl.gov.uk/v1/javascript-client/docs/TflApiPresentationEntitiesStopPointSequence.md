# TransportForLondonUnifiedApi.TflApiPresentationEntitiesStopPointSequence

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**branchId** | **Number** | The id of this branch. | [optional] 
**direction** | **String** |  | [optional] 
**lineId** | **String** |  | [optional] 
**lineName** | **String** |  | [optional] 
**nextBranchIds** | **[Number]** | The ids of the next branch(es) in the sequence. Note that the next and previous branch id can be              identical in the case of a looped route e.g. the Circle line. | [optional] 
**prevBranchIds** | **[Number]** | The ids of the previous branch(es) in the sequence. Note that the next and previous branch id can be              identical in the case of a looped route e.g. the Circle line. | [optional] 
**serviceType** | **String** |  | [optional] 
**stopPoint** | [**[TflApiPresentationEntitiesMatchedStop]**](TflApiPresentationEntitiesMatchedStop.md) |  | [optional] 



## Enum: ServiceTypeEnum


* `Regular` (value: `"Regular"`)

* `Night` (value: `"Night"`)




