

# EducationExpenseWithIdModel


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**annualCost** | **Double** |  |  [optional] |
|**educationExpenseId** | **Integer** |  |  [optional] |
|**educationGoalId** | **Integer** |  |  [optional] |
|**externalDestinationId** | **String** |  |  [optional] |
|**links** | [**List&lt;ObjectLink&gt;**](ObjectLink.md) |  |  [optional] |
|**member** | [**MemberEnum**](#MemberEnum) |  |  [optional] |
|**memberDependentId** | **Integer** |  |  [optional] |
|**startYear** | **OffsetDateTime** |  |  [optional] |
|**years** | **Integer** |  |  [optional] |



## Enum: MemberEnum

| Name | Value |
|---- | -----|
| CLIENT | &quot;Client&quot; |
| CO_CLIENT | &quot;CoClient&quot; |
| DEPENDENT | &quot;Dependent&quot; |



