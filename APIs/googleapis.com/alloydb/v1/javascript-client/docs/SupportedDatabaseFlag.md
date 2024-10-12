# AlloyDbApi.SupportedDatabaseFlag

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**acceptsMultipleValues** | **Boolean** | Whether the database flag accepts multiple values. If true, a comma-separated list of stringified values may be specified. | [optional] 
**flagName** | **String** | The name of the database flag, e.g. \&quot;max_allowed_packets\&quot;. The is a possibly key for the Instance.database_flags map field. | [optional] 
**integerRestrictions** | [**IntegerRestrictions**](IntegerRestrictions.md) |  | [optional] 
**name** | **String** | The name of the flag resource, following Google Cloud conventions, e.g.: * projects/{project}/locations/{location}/flags/{flag} This field currently has no semantic meaning. | [optional] 
**requiresDbRestart** | **Boolean** | Whether setting or updating this flag on an Instance requires a database restart. If a flag that requires database restart is set, the backend will automatically restart the database (making sure to satisfy any availability SLO&#39;s). | [optional] 
**stringRestrictions** | [**StringRestrictions**](StringRestrictions.md) |  | [optional] 
**supportedDbVersions** | **[String]** | Major database engine versions for which this flag is supported. | [optional] 
**valueType** | **String** |  | [optional] 



## Enum: [SupportedDbVersionsEnum]


* `DATABASE_VERSION_UNSPECIFIED` (value: `"DATABASE_VERSION_UNSPECIFIED"`)

* `POSTGRES_13` (value: `"POSTGRES_13"`)

* `POSTGRES_14` (value: `"POSTGRES_14"`)

* `POSTGRES_15` (value: `"POSTGRES_15"`)





## Enum: ValueTypeEnum


* `VALUE_TYPE_UNSPECIFIED` (value: `"VALUE_TYPE_UNSPECIFIED"`)

* `STRING` (value: `"STRING"`)

* `INTEGER` (value: `"INTEGER"`)

* `FLOAT` (value: `"FLOAT"`)

* `NONE` (value: `"NONE"`)




