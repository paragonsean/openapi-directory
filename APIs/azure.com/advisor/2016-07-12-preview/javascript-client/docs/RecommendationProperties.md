# AdvisorManagementClient.RecommendationProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category** | **String** | The category of the recommendation. | [optional] 
**impact** | **String** | The business impact of the recommendation. | [optional] 
**impactedField** | **String** | The resource type identified by Advisor. | [optional] 
**impactedValue** | **String** | The resource identified by Advisor. | [optional] 
**lastUpdated** | **Date** | The most recent time that Advisor checked the validity of the recommendation. | [optional] 
**metadata** | **{String: Object}** | The recommendation metadata. | [optional] 
**recommendationTypeId** | **String** | The recommendation-type GUID. | [optional] 
**risk** | **String** | The potential risk of not implementing the recommendation. | [optional] 
**shortDescription** | [**ShortDescription**](ShortDescription.md) |  | [optional] 



## Enum: CategoryEnum


* `HighAvailability` (value: `"HighAvailability"`)

* `Security` (value: `"Security"`)

* `Performance` (value: `"Performance"`)

* `Cost` (value: `"Cost"`)





## Enum: ImpactEnum


* `High` (value: `"High"`)

* `Medium` (value: `"Medium"`)

* `Low` (value: `"Low"`)





## Enum: RiskEnum


* `Error` (value: `"Error"`)

* `Warning` (value: `"Warning"`)

* `None` (value: `"None"`)




