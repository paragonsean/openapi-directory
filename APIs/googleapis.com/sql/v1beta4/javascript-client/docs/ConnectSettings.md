# CloudSqlAdminApi.ConnectSettings

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**backendType** | **String** | &#x60;SECOND_GEN&#x60;: Cloud SQL database instance. &#x60;EXTERNAL&#x60;: A database server that is not managed by Google. This property is read-only; use the &#x60;tier&#x60; property in the &#x60;settings&#x60; object to determine the database type. | [optional] 
**databaseVersion** | **String** | The database engine type and version. The &#x60;databaseVersion&#x60; field cannot be changed after instance creation. MySQL instances: &#x60;MYSQL_8_0&#x60;, &#x60;MYSQL_5_7&#x60; (default), or &#x60;MYSQL_5_6&#x60;. PostgreSQL instances: &#x60;POSTGRES_9_6&#x60;, &#x60;POSTGRES_10&#x60;, &#x60;POSTGRES_11&#x60; or &#x60;POSTGRES_12&#x60; (default), &#x60;POSTGRES_13&#x60;, or &#x60;POSTGRES_14&#x60;. SQL Server instances: &#x60;SQLSERVER_2017_STANDARD&#x60; (default), &#x60;SQLSERVER_2017_ENTERPRISE&#x60;, &#x60;SQLSERVER_2017_EXPRESS&#x60;, &#x60;SQLSERVER_2017_WEB&#x60;, &#x60;SQLSERVER_2019_STANDARD&#x60;, &#x60;SQLSERVER_2019_ENTERPRISE&#x60;, &#x60;SQLSERVER_2019_EXPRESS&#x60;, or &#x60;SQLSERVER_2019_WEB&#x60;. | [optional] 
**dnsName** | **String** | The dns name of the instance. | [optional] 
**ipAddresses** | [**[IpMapping]**](IpMapping.md) | The assigned IP addresses for the instance. | [optional] 
**kind** | **String** | This is always &#x60;sql#connectSettings&#x60;. | [optional] 
**pscEnabled** | **Boolean** | Whether PSC connectivity is enabled for this instance. | [optional] 
**region** | **String** | The cloud region for the instance. e.g. &#x60;us-central1&#x60;, &#x60;europe-west1&#x60;. The region cannot be changed after instance creation. | [optional] 
**serverCaCert** | [**SslCert**](SslCert.md) |  | [optional] 



## Enum: BackendTypeEnum


* `SQL_BACKEND_TYPE_UNSPECIFIED` (value: `"SQL_BACKEND_TYPE_UNSPECIFIED"`)

* `FIRST_GEN` (value: `"FIRST_GEN"`)

* `SECOND_GEN` (value: `"SECOND_GEN"`)

* `EXTERNAL` (value: `"EXTERNAL"`)





## Enum: DatabaseVersionEnum


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




