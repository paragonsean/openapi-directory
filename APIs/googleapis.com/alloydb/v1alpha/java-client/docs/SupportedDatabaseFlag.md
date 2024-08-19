

# SupportedDatabaseFlag

SupportedDatabaseFlag gives general information about a database flag, like type and allowed values. This is a static value that is defined on the server side, and it cannot be modified by callers. To set the Database flags on a particular Instance, a caller should modify the Instance.database_flags field.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**acceptsMultipleValues** | **Boolean** | Whether the database flag accepts multiple values. If true, a comma-separated list of stringified values may be specified. |  [optional] |
|**flagName** | **String** | The name of the database flag, e.g. \&quot;max_allowed_packets\&quot;. The is a possibly key for the Instance.database_flags map field. |  [optional] |
|**integerRestrictions** | [**IntegerRestrictions**](IntegerRestrictions.md) |  |  [optional] |
|**name** | **String** | The name of the flag resource, following Google Cloud conventions, e.g.: * projects/{project}/locations/{location}/flags/{flag} This field currently has no semantic meaning. |  [optional] |
|**requiresDbRestart** | **Boolean** | Whether setting or updating this flag on an Instance requires a database restart. If a flag that requires database restart is set, the backend will automatically restart the database (making sure to satisfy any availability SLO&#39;s). |  [optional] |
|**stringRestrictions** | [**StringRestrictions**](StringRestrictions.md) |  |  [optional] |
|**supportedDbVersions** | [**List&lt;SupportedDbVersionsEnum&gt;**](#List&lt;SupportedDbVersionsEnum&gt;) | Major database engine versions for which this flag is supported. |  [optional] |
|**valueType** | [**ValueTypeEnum**](#ValueTypeEnum) |  |  [optional] |



## Enum: List&lt;SupportedDbVersionsEnum&gt;

| Name | Value |
|---- | -----|
| DATABASE_VERSION_UNSPECIFIED | &quot;DATABASE_VERSION_UNSPECIFIED&quot; |
| POSTGRES_13 | &quot;POSTGRES_13&quot; |
| POSTGRES_14 | &quot;POSTGRES_14&quot; |
| POSTGRES_15 | &quot;POSTGRES_15&quot; |



## Enum: ValueTypeEnum

| Name | Value |
|---- | -----|
| VALUE_TYPE_UNSPECIFIED | &quot;VALUE_TYPE_UNSPECIFIED&quot; |
| STRING | &quot;STRING&quot; |
| INTEGER | &quot;INTEGER&quot; |
| FLOAT | &quot;FLOAT&quot; |
| NONE | &quot;NONE&quot; |



