

# SecurityProfileSearchCriteria

<p>The search criteria to be used to return security profiles.</p> <note> <p>The <code>name</code> field support \"contains\" queries with a minimum of 2 characters and maximum of 25 characters. Any queries with character lengths outside of this range will throw invalid results.</p> </note>

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**orConditions** | [**List**](List.md) |  |  [optional] |
|**andConditions** | [**List**](List.md) |  |  [optional] |
|**stringCondition** | [**StringCondition**](StringCondition.md) |  |  [optional] |



