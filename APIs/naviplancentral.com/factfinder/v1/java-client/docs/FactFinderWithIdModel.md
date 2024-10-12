

# FactFinderWithIdModel


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**countryCode** | [**CountryCodeEnum**](#CountryCodeEnum) |  |  [optional] |
|**created** | **OffsetDateTime** |  |  [optional] |
|**factFinderId** | **Integer** |  |  [optional] |
|**householdId** | **Integer** |  |  [optional] |
|**lastStatusUpdate** | **OffsetDateTime** |  |  [optional] |
|**links** | [**List&lt;ObjectLink&gt;**](ObjectLink.md) |  |  [optional] |
|**modules** | [**FactFinderModulesModel**](FactFinderModulesModel.md) |  |  [optional] |
|**planId** | **Integer** |  |  [optional] |
|**planLevel** | [**PlanLevelEnum**](#PlanLevelEnum) |  |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) |  |  [optional] |



## Enum: CountryCodeEnum

| Name | Value |
|---- | -----|
| UNITED_STATES | &quot;UnitedStates&quot; |
| CANADA | &quot;Canada&quot; |



## Enum: PlanLevelEnum

| Name | Value |
|---- | -----|
| LEVEL2 | &quot;Level2&quot; |
| LEVEL1 | &quot;Level1&quot; |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| NEW | &quot;New&quot; |
| IN_PROGRESS | &quot;InProgress&quot; |
| CLIENT_SUBMITTED | &quot;ClientSubmitted&quot; |
| ADVISOR_ACCEPTED | &quot;AdvisorAccepted&quot; |
| CANCELED | &quot;Canceled&quot; |
| DRAFT | &quot;Draft&quot; |
| DELETED | &quot;Deleted&quot; |



