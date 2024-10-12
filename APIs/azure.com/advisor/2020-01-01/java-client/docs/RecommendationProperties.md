

# RecommendationProperties

The properties of the recommendation.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**category** | [**CategoryEnum**](#CategoryEnum) | The category of the recommendation. |  [optional] |
|**extendedProperties** | **Map&lt;String, String&gt;** | Extended properties |  [optional] |
|**impact** | [**ImpactEnum**](#ImpactEnum) | The business impact of the recommendation. |  [optional] |
|**impactedField** | **String** | The resource type identified by Advisor. |  [optional] |
|**impactedValue** | **String** | The resource identified by Advisor. |  [optional] |
|**lastUpdated** | **OffsetDateTime** | The most recent time that Advisor checked the validity of the recommendation. |  [optional] |
|**metadata** | **Map&lt;String, Object&gt;** | The recommendation metadata. |  [optional] |
|**recommendationTypeId** | **String** | The recommendation-type GUID. |  [optional] |
|**risk** | [**RiskEnum**](#RiskEnum) | The potential risk of not implementing the recommendation. |  [optional] |
|**shortDescription** | [**ShortDescription**](ShortDescription.md) |  |  [optional] |
|**suppressionIds** | **List&lt;UUID&gt;** | The list of snoozed and dismissed rules for the recommendation. |  [optional] |



## Enum: CategoryEnum

| Name | Value |
|---- | -----|
| HIGH_AVAILABILITY | &quot;HighAvailability&quot; |
| SECURITY | &quot;Security&quot; |
| PERFORMANCE | &quot;Performance&quot; |
| COST | &quot;Cost&quot; |
| OPERATIONAL_EXCELLENCE | &quot;OperationalExcellence&quot; |



## Enum: ImpactEnum

| Name | Value |
|---- | -----|
| HIGH | &quot;High&quot; |
| MEDIUM | &quot;Medium&quot; |
| LOW | &quot;Low&quot; |



## Enum: RiskEnum

| Name | Value |
|---- | -----|
| ERROR | &quot;Error&quot; |
| WARNING | &quot;Warning&quot; |
| NONE | &quot;None&quot; |



