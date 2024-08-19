

# GroupQuery

The criteria defining the group

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**composition** | [**CompositionEnum**](#CompositionEnum) | Boolean operator to use between each  &#x60;where&#x60; criteria. |  [optional] |
|**select** | **String** | What kind of data we want to include. Here we can get policy servers/relay by setting &#x60;nodeAndPolicyServer&#x60;. Only used if &#x60;where&#x60; is defined. |  [optional] |
|**where** | [**List&lt;GroupQueryWhereInner&gt;**](GroupQueryWhereInner.md) | List of criteria |  [optional] |



## Enum: CompositionEnum

| Name | Value |
|---- | -----|
| AND | &quot;and&quot; |
| OR | &quot;or&quot; |



