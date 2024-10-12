

# Flag

A flag resource.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**allowedIntValues** | **List&lt;String&gt;** | Use this field if only certain integers are accepted. Can be combined with min_value and max_value to add additional values. |  [optional] |
|**allowedStringValues** | **List&lt;String&gt;** | For &#x60;STRING&#x60; flags, a list of strings that the value can be set to. |  [optional] |
|**appliesTo** | [**List&lt;AppliesToEnum&gt;**](#List&lt;AppliesToEnum&gt;) | The database version this flag applies to. Can be MySQL instances: &#x60;MYSQL_8_0&#x60;, &#x60;MYSQL_8_0_18&#x60;, &#x60;MYSQL_8_0_26&#x60;, &#x60;MYSQL_5_7&#x60;, or &#x60;MYSQL_5_6&#x60;. PostgreSQL instances: &#x60;POSTGRES_9_6&#x60;, &#x60;POSTGRES_10&#x60;, &#x60;POSTGRES_11&#x60; or &#x60;POSTGRES_12&#x60;. SQL Server instances: &#x60;SQLSERVER_2017_STANDARD&#x60;, &#x60;SQLSERVER_2017_ENTERPRISE&#x60;, &#x60;SQLSERVER_2017_EXPRESS&#x60;, &#x60;SQLSERVER_2017_WEB&#x60;, &#x60;SQLSERVER_2019_STANDARD&#x60;, &#x60;SQLSERVER_2019_ENTERPRISE&#x60;, &#x60;SQLSERVER_2019_EXPRESS&#x60;, or &#x60;SQLSERVER_2019_WEB&#x60;. See [the complete list](/sql/docs/mysql/admin-api/rest/v1/SqlDatabaseVersion). |  [optional] |
|**inBeta** | **Boolean** | Whether or not the flag is considered in beta. |  [optional] |
|**kind** | **String** | This is always &#x60;sql#flag&#x60;. |  [optional] |
|**maxValue** | **String** | For &#x60;INTEGER&#x60; flags, the maximum allowed value. |  [optional] |
|**minValue** | **String** | For &#x60;INTEGER&#x60; flags, the minimum allowed value. |  [optional] |
|**name** | **String** | This is the name of the flag. Flag names always use underscores, not hyphens, for example: &#x60;max_allowed_packet&#x60; |  [optional] |
|**requiresRestart** | **Boolean** | Indicates whether changing this flag will trigger a database restart. Only applicable to Second Generation instances. |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | The type of the flag. Flags are typed to being &#x60;BOOLEAN&#x60;, &#x60;STRING&#x60;, &#x60;INTEGER&#x60; or &#x60;NONE&#x60;. &#x60;NONE&#x60; is used for flags which do not take a value, such as &#x60;skip_grant_tables&#x60;. |  [optional] |



## Enum: List&lt;AppliesToEnum&gt;

| Name | Value |
|---- | -----|
| SQL_DATABASE_VERSION_UNSPECIFIED | &quot;SQL_DATABASE_VERSION_UNSPECIFIED&quot; |
| MYSQL_5_1 | &quot;MYSQL_5_1&quot; |
| MYSQL_5_5 | &quot;MYSQL_5_5&quot; |
| MYSQL_5_6 | &quot;MYSQL_5_6&quot; |
| MYSQL_5_7 | &quot;MYSQL_5_7&quot; |
| SQLSERVER_2017_STANDARD | &quot;SQLSERVER_2017_STANDARD&quot; |
| SQLSERVER_2017_ENTERPRISE | &quot;SQLSERVER_2017_ENTERPRISE&quot; |
| SQLSERVER_2017_EXPRESS | &quot;SQLSERVER_2017_EXPRESS&quot; |
| SQLSERVER_2017_WEB | &quot;SQLSERVER_2017_WEB&quot; |
| POSTGRES_9_6 | &quot;POSTGRES_9_6&quot; |
| POSTGRES_10 | &quot;POSTGRES_10&quot; |
| POSTGRES_11 | &quot;POSTGRES_11&quot; |
| POSTGRES_12 | &quot;POSTGRES_12&quot; |
| POSTGRES_13 | &quot;POSTGRES_13&quot; |
| POSTGRES_14 | &quot;POSTGRES_14&quot; |
| POSTGRES_15 | &quot;POSTGRES_15&quot; |
| MYSQL_8_0 | &quot;MYSQL_8_0&quot; |
| MYSQL_8_0_18 | &quot;MYSQL_8_0_18&quot; |
| MYSQL_8_0_26 | &quot;MYSQL_8_0_26&quot; |
| MYSQL_8_0_27 | &quot;MYSQL_8_0_27&quot; |
| MYSQL_8_0_28 | &quot;MYSQL_8_0_28&quot; |
| MYSQL_8_0_29 | &quot;MYSQL_8_0_29&quot; |
| MYSQL_8_0_30 | &quot;MYSQL_8_0_30&quot; |
| MYSQL_8_0_31 | &quot;MYSQL_8_0_31&quot; |
| MYSQL_8_0_32 | &quot;MYSQL_8_0_32&quot; |
| MYSQL_8_0_33 | &quot;MYSQL_8_0_33&quot; |
| MYSQL_8_0_34 | &quot;MYSQL_8_0_34&quot; |
| MYSQL_8_0_35 | &quot;MYSQL_8_0_35&quot; |
| MYSQL_8_0_36 | &quot;MYSQL_8_0_36&quot; |
| SQLSERVER_2019_STANDARD | &quot;SQLSERVER_2019_STANDARD&quot; |
| SQLSERVER_2019_ENTERPRISE | &quot;SQLSERVER_2019_ENTERPRISE&quot; |
| SQLSERVER_2019_EXPRESS | &quot;SQLSERVER_2019_EXPRESS&quot; |
| SQLSERVER_2019_WEB | &quot;SQLSERVER_2019_WEB&quot; |
| SQLSERVER_2022_STANDARD | &quot;SQLSERVER_2022_STANDARD&quot; |
| SQLSERVER_2022_ENTERPRISE | &quot;SQLSERVER_2022_ENTERPRISE&quot; |
| SQLSERVER_2022_EXPRESS | &quot;SQLSERVER_2022_EXPRESS&quot; |
| SQLSERVER_2022_WEB | &quot;SQLSERVER_2022_WEB&quot; |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| SQL_FLAG_TYPE_UNSPECIFIED | &quot;SQL_FLAG_TYPE_UNSPECIFIED&quot; |
| BOOLEAN | &quot;BOOLEAN&quot; |
| STRING | &quot;STRING&quot; |
| INTEGER | &quot;INTEGER&quot; |
| NONE | &quot;NONE&quot; |
| MYSQL_TIMEZONE_OFFSET | &quot;MYSQL_TIMEZONE_OFFSET&quot; |
| FLOAT | &quot;FLOAT&quot; |
| REPEATED_STRING | &quot;REPEATED_STRING&quot; |



