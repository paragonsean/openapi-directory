

# GetLinkAttributesRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**typedLinkSpecifier** | [**DetachTypedLinkRequestTypedLinkSpecifier**](DetachTypedLinkRequestTypedLinkSpecifier.md) |  |  |
|**attributeNames** | **List&lt;String&gt;** | A list of attribute names whose values will be retrieved. |  |
|**consistencyLevel** | [**ConsistencyLevelEnum**](#ConsistencyLevelEnum) | The consistency level at which to retrieve the attributes on a typed link. |  [optional] |



## Enum: ConsistencyLevelEnum

| Name | Value |
|---- | -----|
| SERIALIZABLE | &quot;SERIALIZABLE&quot; |
| EVENTUAL | &quot;EVENTUAL&quot; |



