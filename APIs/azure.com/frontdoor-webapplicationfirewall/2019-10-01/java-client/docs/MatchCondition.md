

# MatchCondition

Define a match condition.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**matchValue** | **List&lt;String&gt;** | List of possible match values. |  |
|**matchVariable** | [**MatchVariableEnum**](#MatchVariableEnum) | Request variable to compare with. |  |
|**negateCondition** | **Boolean** | Describes if the result of this condition should be negated. |  [optional] |
|**operator** | [**OperatorEnum**](#OperatorEnum) | Comparison type to use for matching with the variable value. |  |
|**selector** | **String** | Match against a specific key from the QueryString, PostArgs, RequestHeader or Cookies variables. Default is null. |  [optional] |
|**transforms** | **List&lt;TransformType&gt;** | List of transforms. |  [optional] |



## Enum: MatchVariableEnum

| Name | Value |
|---- | -----|
| REMOTE_ADDR | &quot;RemoteAddr&quot; |
| REQUEST_METHOD | &quot;RequestMethod&quot; |
| QUERY_STRING | &quot;QueryString&quot; |
| POST_ARGS | &quot;PostArgs&quot; |
| REQUEST_URI | &quot;RequestUri&quot; |
| REQUEST_HEADER | &quot;RequestHeader&quot; |
| REQUEST_BODY | &quot;RequestBody&quot; |
| COOKIES | &quot;Cookies&quot; |
| SOCKET_ADDR | &quot;SocketAddr&quot; |



## Enum: OperatorEnum

| Name | Value |
|---- | -----|
| ANY | &quot;Any&quot; |
| IP_MATCH | &quot;IPMatch&quot; |
| GEO_MATCH | &quot;GeoMatch&quot; |
| EQUAL | &quot;Equal&quot; |
| CONTAINS | &quot;Contains&quot; |
| LESS_THAN | &quot;LessThan&quot; |
| GREATER_THAN | &quot;GreaterThan&quot; |
| LESS_THAN_OR_EQUAL | &quot;LessThanOrEqual&quot; |
| GREATER_THAN_OR_EQUAL | &quot;GreaterThanOrEqual&quot; |
| BEGINS_WITH | &quot;BeginsWith&quot; |
| ENDS_WITH | &quot;EndsWith&quot; |
| REG_EX | &quot;RegEx&quot; |



