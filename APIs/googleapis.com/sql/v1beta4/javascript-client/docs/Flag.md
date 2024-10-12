# CloudSqlAdminApi.Flag

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allowedIntValues** | **[String]** | Use this field if only certain integers are accepted. Can be combined with min_value and max_value to add additional values. | [optional] 
**allowedStringValues** | **[String]** | For &#x60;STRING&#x60; flags, a list of strings that the value can be set to. | [optional] 
**appliesTo** | **[String]** | The database version this flag applies to. Can be MySQL instances: &#x60;MYSQL_8_0&#x60;, &#x60;MYSQL_8_0_18&#x60;, &#x60;MYSQL_8_0_26&#x60;, &#x60;MYSQL_5_7&#x60;, or &#x60;MYSQL_5_6&#x60;. PostgreSQL instances: &#x60;POSTGRES_9_6&#x60;, &#x60;POSTGRES_10&#x60;, &#x60;POSTGRES_11&#x60; or &#x60;POSTGRES_12&#x60;. SQL Server instances: &#x60;SQLSERVER_2017_STANDARD&#x60;, &#x60;SQLSERVER_2017_ENTERPRISE&#x60;, &#x60;SQLSERVER_2017_EXPRESS&#x60;, &#x60;SQLSERVER_2017_WEB&#x60;, &#x60;SQLSERVER_2019_STANDARD&#x60;, &#x60;SQLSERVER_2019_ENTERPRISE&#x60;, &#x60;SQLSERVER_2019_EXPRESS&#x60;, or &#x60;SQLSERVER_2019_WEB&#x60;. See [the complete list](/sql/docs/mysql/admin-api/rest/v1/SqlDatabaseVersion). | [optional] 
**inBeta** | **Boolean** | Whether or not the flag is considered in beta. | [optional] 
**kind** | **String** | This is always &#x60;sql#flag&#x60;. | [optional] 
**maxValue** | **String** | For &#x60;INTEGER&#x60; flags, the maximum allowed value. | [optional] 
**minValue** | **String** | For &#x60;INTEGER&#x60; flags, the minimum allowed value. | [optional] 
**name** | **String** | This is the name of the flag. Flag names always use underscores, not hyphens, for example: &#x60;max_allowed_packet&#x60; | [optional] 
**requiresRestart** | **Boolean** | Indicates whether changing this flag will trigger a database restart. Only applicable to Second Generation instances. | [optional] 
**type** | **String** | The type of the flag. Flags are typed to being &#x60;BOOLEAN&#x60;, &#x60;STRING&#x60;, &#x60;INTEGER&#x60; or &#x60;NONE&#x60;. &#x60;NONE&#x60; is used for flags which do not take a value, such as &#x60;skip_grant_tables&#x60;. | [optional] 



## Enum: [AppliesToEnum]


* `SQL_DATABASE_VERSION_UNSPECIFIED` (value: `"SQL_DATABASE_VERSION_UNSPECIFIED"`)

* `MYSQL_5_1` (value: `"MYSQL_5_1"`)

* `MYSQL_5_5` (value: `"MYSQL_5_5"`)

* `MYSQL_5_6` (value: `"MYSQL_5_6"`)

* `MYSQL_5_7` (value: `"MYSQL_5_7"`)

* `SQLSERVER_2017_STANDARD` (value: `"SQLSERVER_2017_STANDARD"`)

* `SQLSERVER_2017_ENTERPRISE` (value: `"SQLSERVER_2017_ENTERPRISE"`)

* `SQLSERVER_2017_EXPRESS` (value: `"SQLSERVER_2017_EXPRESS"`)

* `SQLSERVER_2017_WEB` (value: `"SQLSERVER_2017_WEB"`)

* `POSTGRES_9_6` (value: `"POSTGRES_9_6"`)

* `POSTGRES_10` (value: `"POSTGRES_10"`)

* `POSTGRES_11` (value: `"POSTGRES_11"`)

* `POSTGRES_12` (value: `"POSTGRES_12"`)

* `POSTGRES_13` (value: `"POSTGRES_13"`)

* `POSTGRES_14` (value: `"POSTGRES_14"`)

* `POSTGRES_15` (value: `"POSTGRES_15"`)

* `MYSQL_8_0` (value: `"MYSQL_8_0"`)

* `MYSQL_8_0_18` (value: `"MYSQL_8_0_18"`)

* `MYSQL_8_0_26` (value: `"MYSQL_8_0_26"`)

* `MYSQL_8_0_27` (value: `"MYSQL_8_0_27"`)

* `MYSQL_8_0_28` (value: `"MYSQL_8_0_28"`)

* `MYSQL_8_0_29` (value: `"MYSQL_8_0_29"`)

* `MYSQL_8_0_30` (value: `"MYSQL_8_0_30"`)

* `MYSQL_8_0_31` (value: `"MYSQL_8_0_31"`)

* `MYSQL_8_0_32` (value: `"MYSQL_8_0_32"`)

* `MYSQL_8_0_33` (value: `"MYSQL_8_0_33"`)

* `MYSQL_8_0_34` (value: `"MYSQL_8_0_34"`)

* `MYSQL_8_0_35` (value: `"MYSQL_8_0_35"`)

* `MYSQL_8_0_36` (value: `"MYSQL_8_0_36"`)

* `SQLSERVER_2019_STANDARD` (value: `"SQLSERVER_2019_STANDARD"`)

* `SQLSERVER_2019_ENTERPRISE` (value: `"SQLSERVER_2019_ENTERPRISE"`)

* `SQLSERVER_2019_EXPRESS` (value: `"SQLSERVER_2019_EXPRESS"`)

* `SQLSERVER_2019_WEB` (value: `"SQLSERVER_2019_WEB"`)

* `SQLSERVER_2022_STANDARD` (value: `"SQLSERVER_2022_STANDARD"`)

* `SQLSERVER_2022_ENTERPRISE` (value: `"SQLSERVER_2022_ENTERPRISE"`)

* `SQLSERVER_2022_EXPRESS` (value: `"SQLSERVER_2022_EXPRESS"`)

* `SQLSERVER_2022_WEB` (value: `"SQLSERVER_2022_WEB"`)





## Enum: TypeEnum


* `SQL_FLAG_TYPE_UNSPECIFIED` (value: `"SQL_FLAG_TYPE_UNSPECIFIED"`)

* `BOOLEAN` (value: `"BOOLEAN"`)

* `STRING` (value: `"STRING"`)

* `INTEGER` (value: `"INTEGER"`)

* `NONE` (value: `"NONE"`)

* `MYSQL_TIMEZONE_OFFSET` (value: `"MYSQL_TIMEZONE_OFFSET"`)

* `FLOAT` (value: `"FLOAT"`)

* `REPEATED_STRING` (value: `"REPEATED_STRING"`)




