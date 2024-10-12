

# RoutingProfileSearchCriteria

<p>The search criteria to be used to return routing profiles.</p> <note> <p>The <code>name</code> and <code>description</code> fields support \"contains\" queries with a minimum of 2 characters and a maximum of 25 characters. Any queries with character lengths outside of this range will throw invalid results. </p> </note>

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**orConditions** | [**List**](List.md) |  |  [optional] |
|**andConditions** | [**List**](List.md) |  |  [optional] |
|**stringCondition** | [**SearchPromptsRequestSearchCriteriaStringCondition**](SearchPromptsRequestSearchCriteriaStringCondition.md) |  |  [optional] |



