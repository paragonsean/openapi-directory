# ConnectorsApi.ConfigVariableTemplate

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authorizationCodeLink** | [**AuthorizationCodeLink**](AuthorizationCodeLink.md) |  | [optional] 
**description** | **String** | Description. | [optional] 
**displayName** | **String** | Display name of the parameter. | [optional] 
**enumOptions** | [**[EnumOption]**](EnumOption.md) | Enum options. To be populated if &#x60;ValueType&#x60; is &#x60;ENUM&#x60; | [optional] 
**isAdvanced** | **Boolean** | Indicates if current template is part of advanced settings | [optional] 
**key** | **String** | Key of the config variable. | [optional] 
**locationType** | **String** | Optional. Location Tyep denotes where this value should be sent in BYOC connections. | [optional] 
**required** | **Boolean** | Flag represents that this &#x60;ConfigVariable&#x60; must be provided for a connection. | [optional] 
**requiredCondition** | [**LogicalExpression**](LogicalExpression.md) |  | [optional] 
**roleGrant** | [**RoleGrant**](RoleGrant.md) |  | [optional] 
**state** | **String** | State of the config variable. | [optional] 
**validationRegex** | **String** | Regular expression in RE2 syntax used for validating the &#x60;value&#x60; of a &#x60;ConfigVariable&#x60;. | [optional] 
**valueType** | **String** | Type of the parameter: string, int, bool etc. consider custom type for the benefit for the validation. | [optional] 



## Enum: LocationTypeEnum


* `LOCATION_TYPE_UNSPECIFIED` (value: `"LOCATION_TYPE_UNSPECIFIED"`)

* `HEADER` (value: `"HEADER"`)

* `PAYLOAD` (value: `"PAYLOAD"`)

* `QUERY_PARAM` (value: `"QUERY_PARAM"`)

* `PATH_PARAM` (value: `"PATH_PARAM"`)





## Enum: StateEnum


* `STATE_UNSPECIFIED` (value: `"STATE_UNSPECIFIED"`)

* `ACTIVE` (value: `"ACTIVE"`)

* `DEPRECATED` (value: `"DEPRECATED"`)





## Enum: ValueTypeEnum


* `VALUE_TYPE_UNSPECIFIED` (value: `"VALUE_TYPE_UNSPECIFIED"`)

* `STRING` (value: `"STRING"`)

* `INT` (value: `"INT"`)

* `BOOL` (value: `"BOOL"`)

* `SECRET` (value: `"SECRET"`)

* `ENUM` (value: `"ENUM"`)

* `AUTHORIZATION_CODE` (value: `"AUTHORIZATION_CODE"`)

* `ENCRYPTION_KEY` (value: `"ENCRYPTION_KEY"`)




