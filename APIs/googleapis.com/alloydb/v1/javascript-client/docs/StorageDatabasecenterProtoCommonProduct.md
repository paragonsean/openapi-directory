# AlloyDbApi.StorageDatabasecenterProtoCommonProduct

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**engine** | **String** | The specific engine that the underlying database is running. | [optional] 
**type** | **String** | Type of specific database product. It could be CloudSQL, AlloyDB etc.. | [optional] 
**version** | **String** | Version of the underlying database engine. Example values: For MySQL, it could be \&quot;8.0\&quot;, \&quot;5.7\&quot; etc.. For Postgres, it could be \&quot;14\&quot;, \&quot;15\&quot; etc.. | [optional] 



## Enum: EngineEnum


* `ENGINE_UNSPECIFIED` (value: `"ENGINE_UNSPECIFIED"`)

* `ENGINE_MYSQL` (value: `"ENGINE_MYSQL"`)

* `MYSQL` (value: `"MYSQL"`)

* `ENGINE_POSTGRES` (value: `"ENGINE_POSTGRES"`)

* `POSTGRES` (value: `"POSTGRES"`)

* `ENGINE_SQL_SERVER` (value: `"ENGINE_SQL_SERVER"`)

* `SQL_SERVER` (value: `"SQL_SERVER"`)

* `ENGINE_NATIVE` (value: `"ENGINE_NATIVE"`)

* `NATIVE` (value: `"NATIVE"`)

* `ENGINE_CLOUD_SPANNER_WITH_POSTGRES_DIALECT` (value: `"ENGINE_CLOUD_SPANNER_WITH_POSTGRES_DIALECT"`)

* `ENGINE_CLOUD_SPANNER_WITH_GOOGLESQL_DIALECT` (value: `"ENGINE_CLOUD_SPANNER_WITH_GOOGLESQL_DIALECT"`)

* `ENGINE_MEMORYSTORE_FOR_REDIS` (value: `"ENGINE_MEMORYSTORE_FOR_REDIS"`)

* `ENGINE_MEMORYSTORE_FOR_REDIS_CLUSTER` (value: `"ENGINE_MEMORYSTORE_FOR_REDIS_CLUSTER"`)

* `ENGINE_OTHER` (value: `"ENGINE_OTHER"`)





## Enum: TypeEnum


* `PRODUCT_TYPE_UNSPECIFIED` (value: `"PRODUCT_TYPE_UNSPECIFIED"`)

* `PRODUCT_TYPE_CLOUD_SQL` (value: `"PRODUCT_TYPE_CLOUD_SQL"`)

* `CLOUD_SQL` (value: `"CLOUD_SQL"`)

* `PRODUCT_TYPE_ALLOYDB` (value: `"PRODUCT_TYPE_ALLOYDB"`)

* `ALLOYDB` (value: `"ALLOYDB"`)

* `PRODUCT_TYPE_SPANNER` (value: `"PRODUCT_TYPE_SPANNER"`)

* `PRODUCT_TYPE_ON_PREM` (value: `"PRODUCT_TYPE_ON_PREM"`)

* `ON_PREM` (value: `"ON_PREM"`)

* `PRODUCT_TYPE_MEMORYSTORE` (value: `"PRODUCT_TYPE_MEMORYSTORE"`)

* `PRODUCT_TYPE_OTHER` (value: `"PRODUCT_TYPE_OTHER"`)




