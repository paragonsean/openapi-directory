# FrankieFinancialApi.BackgroundCheckResultObject

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**backgroundCheckType** | [**EnumBackgroundCheckType**](EnumBackgroundCheckType.md) |  | [optional] 
**checkDetails** | [**[KeyValuePairObject]**](KeyValuePairObject.md) | Any additional notes that may relate to the state. Free form notes that may contain JSON blobs needing further interpretation. | [optional] 
**checkFrequency** | [**EnumBackgroundCheckFrequency**](EnumBackgroundCheckFrequency.md) |  | [optional] 
**checkId** | **String** | Unique identifier for every check/comparison/verification. Make sure you reference this ID whenever updating check details. This ID will also be used when pushing check results back to you. | [optional] 
**checkPerformedBy** | **String** | Service provider that performed the check. Basically the name of the connector, without the leading con_  | [optional] 
**checkSource** | **String** | Code that can be used to determine the underlying nature or data source of the checks performed. This may or may not be known by the connector, or may be a provider specific type (e.g. type \&quot;O\&quot;)  | [optional] 
**confidenceLevel** | **Number** | Confidence in the current results on a scale of 0 (none) to 100 (as certain as possible). Whole integers only. | [optional] 
**currentState** | [**EnumBackgroundCheckState**](EnumBackgroundCheckState.md) |  | [optional] 
**firstCheckDate** | **Date** | The date and time the item was first checked. | [optional] 
**latestCheckDate** | **Date** | The date and time the item was last checked to provide this result. | [optional] 


