

# ConfigVariableTemplate

ConfigVariableTemplate provides metadata about a `ConfigVariable` that is used in a Connection.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**authorizationCodeLink** | [**AuthorizationCodeLink**](AuthorizationCodeLink.md) |  |  [optional] |
|**description** | **String** | Description. |  [optional] |
|**displayName** | **String** | Display name of the parameter. |  [optional] |
|**enumOptions** | [**List&lt;EnumOption&gt;**](EnumOption.md) | Enum options. To be populated if &#x60;ValueType&#x60; is &#x60;ENUM&#x60; |  [optional] |
|**isAdvanced** | **Boolean** | Indicates if current template is part of advanced settings |  [optional] |
|**key** | **String** | Key of the config variable. |  [optional] |
|**locationType** | [**LocationTypeEnum**](#LocationTypeEnum) | Optional. Location Tyep denotes where this value should be sent in BYOC connections. |  [optional] |
|**required** | **Boolean** | Flag represents that this &#x60;ConfigVariable&#x60; must be provided for a connection. |  [optional] |
|**requiredCondition** | [**LogicalExpression**](LogicalExpression.md) |  |  [optional] |
|**roleGrant** | [**RoleGrant**](RoleGrant.md) |  |  [optional] |
|**state** | [**StateEnum**](#StateEnum) | State of the config variable. |  [optional] |
|**validationRegex** | **String** | Regular expression in RE2 syntax used for validating the &#x60;value&#x60; of a &#x60;ConfigVariable&#x60;. |  [optional] |
|**valueType** | [**ValueTypeEnum**](#ValueTypeEnum) | Type of the parameter: string, int, bool etc. consider custom type for the benefit for the validation. |  [optional] |



## Enum: LocationTypeEnum

| Name | Value |
|---- | -----|
| LOCATION_TYPE_UNSPECIFIED | &quot;LOCATION_TYPE_UNSPECIFIED&quot; |
| HEADER | &quot;HEADER&quot; |
| PAYLOAD | &quot;PAYLOAD&quot; |
| QUERY_PARAM | &quot;QUERY_PARAM&quot; |
| PATH_PARAM | &quot;PATH_PARAM&quot; |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| STATE_UNSPECIFIED | &quot;STATE_UNSPECIFIED&quot; |
| ACTIVE | &quot;ACTIVE&quot; |
| DEPRECATED | &quot;DEPRECATED&quot; |



## Enum: ValueTypeEnum

| Name | Value |
|---- | -----|
| VALUE_TYPE_UNSPECIFIED | &quot;VALUE_TYPE_UNSPECIFIED&quot; |
| STRING | &quot;STRING&quot; |
| INT | &quot;INT&quot; |
| BOOL | &quot;BOOL&quot; |
| SECRET | &quot;SECRET&quot; |
| ENUM | &quot;ENUM&quot; |
| AUTHORIZATION_CODE | &quot;AUTHORIZATION_CODE&quot; |
| ENCRYPTION_KEY | &quot;ENCRYPTION_KEY&quot; |



