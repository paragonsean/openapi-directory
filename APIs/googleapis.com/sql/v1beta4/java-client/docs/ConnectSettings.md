

# ConnectSettings

Connect settings retrieval response.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**backendType** | [**BackendTypeEnum**](#BackendTypeEnum) | &#x60;SECOND_GEN&#x60;: Cloud SQL database instance. &#x60;EXTERNAL&#x60;: A database server that is not managed by Google. This property is read-only; use the &#x60;tier&#x60; property in the &#x60;settings&#x60; object to determine the database type. |  [optional] |
|**databaseVersion** | [**DatabaseVersionEnum**](#DatabaseVersionEnum) | The database engine type and version. The &#x60;databaseVersion&#x60; field cannot be changed after instance creation. MySQL instances: &#x60;MYSQL_8_0&#x60;, &#x60;MYSQL_5_7&#x60; (default), or &#x60;MYSQL_5_6&#x60;. PostgreSQL instances: &#x60;POSTGRES_9_6&#x60;, &#x60;POSTGRES_10&#x60;, &#x60;POSTGRES_11&#x60; or &#x60;POSTGRES_12&#x60; (default), &#x60;POSTGRES_13&#x60;, or &#x60;POSTGRES_14&#x60;. SQL Server instances: &#x60;SQLSERVER_2017_STANDARD&#x60; (default), &#x60;SQLSERVER_2017_ENTERPRISE&#x60;, &#x60;SQLSERVER_2017_EXPRESS&#x60;, &#x60;SQLSERVER_2017_WEB&#x60;, &#x60;SQLSERVER_2019_STANDARD&#x60;, &#x60;SQLSERVER_2019_ENTERPRISE&#x60;, &#x60;SQLSERVER_2019_EXPRESS&#x60;, or &#x60;SQLSERVER_2019_WEB&#x60;. |  [optional] |
|**dnsName** | **String** | The dns name of the instance. |  [optional] |
|**ipAddresses** | [**List&lt;IpMapping&gt;**](IpMapping.md) | The assigned IP addresses for the instance. |  [optional] |
|**kind** | **String** | This is always &#x60;sql#connectSettings&#x60;. |  [optional] |
|**pscEnabled** | **Boolean** | Whether PSC connectivity is enabled for this instance. |  [optional] |
|**region** | **String** | The cloud region for the instance. e.g. &#x60;us-central1&#x60;, &#x60;europe-west1&#x60;. The region cannot be changed after instance creation. |  [optional] |
|**serverCaCert** | [**SslCert**](SslCert.md) |  |  [optional] |



## Enum: BackendTypeEnum

| Name | Value |
|---- | -----|
| SQL_BACKEND_TYPE_UNSPECIFIED | &quot;SQL_BACKEND_TYPE_UNSPECIFIED&quot; |
| FIRST_GEN | &quot;FIRST_GEN&quot; |
| SECOND_GEN | &quot;SECOND_GEN&quot; |
| EXTERNAL | &quot;EXTERNAL&quot; |



## Enum: DatabaseVersionEnum

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



