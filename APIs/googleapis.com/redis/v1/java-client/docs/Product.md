

# Product

Product specification for Condor resources.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**engine** | [**EngineEnum**](#EngineEnum) | The specific engine that the underlying database is running. |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | Type of specific database product. It could be CloudSQL, AlloyDB etc.. |  [optional] |
|**version** | **String** | Version of the underlying database engine. Example values: For MySQL, it could be \&quot;8.0\&quot;, \&quot;5.7\&quot; etc.. For Postgres, it could be \&quot;14\&quot;, \&quot;15\&quot; etc.. |  [optional] |



## Enum: EngineEnum

| Name | Value |
|---- | -----|
| ENGINE_UNSPECIFIED | &quot;ENGINE_UNSPECIFIED&quot; |
| ENGINE_MYSQL | &quot;ENGINE_MYSQL&quot; |
| MYSQL | &quot;MYSQL&quot; |
| ENGINE_POSTGRES | &quot;ENGINE_POSTGRES&quot; |
| POSTGRES | &quot;POSTGRES&quot; |
| ENGINE_SQL_SERVER | &quot;ENGINE_SQL_SERVER&quot; |
| SQL_SERVER | &quot;SQL_SERVER&quot; |
| ENGINE_NATIVE | &quot;ENGINE_NATIVE&quot; |
| NATIVE | &quot;NATIVE&quot; |
| ENGINE_CLOUD_SPANNER_WITH_POSTGRES_DIALECT | &quot;ENGINE_CLOUD_SPANNER_WITH_POSTGRES_DIALECT&quot; |
| ENGINE_CLOUD_SPANNER_WITH_GOOGLESQL_DIALECT | &quot;ENGINE_CLOUD_SPANNER_WITH_GOOGLESQL_DIALECT&quot; |
| ENGINE_MEMORYSTORE_FOR_REDIS | &quot;ENGINE_MEMORYSTORE_FOR_REDIS&quot; |
| ENGINE_MEMORYSTORE_FOR_REDIS_CLUSTER | &quot;ENGINE_MEMORYSTORE_FOR_REDIS_CLUSTER&quot; |
| ENGINE_OTHER | &quot;ENGINE_OTHER&quot; |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| PRODUCT_TYPE_UNSPECIFIED | &quot;PRODUCT_TYPE_UNSPECIFIED&quot; |
| PRODUCT_TYPE_CLOUD_SQL | &quot;PRODUCT_TYPE_CLOUD_SQL&quot; |
| CLOUD_SQL | &quot;CLOUD_SQL&quot; |
| PRODUCT_TYPE_ALLOYDB | &quot;PRODUCT_TYPE_ALLOYDB&quot; |
| ALLOYDB | &quot;ALLOYDB&quot; |
| PRODUCT_TYPE_SPANNER | &quot;PRODUCT_TYPE_SPANNER&quot; |
| PRODUCT_TYPE_ON_PREM | &quot;PRODUCT_TYPE_ON_PREM&quot; |
| ON_PREM | &quot;ON_PREM&quot; |
| PRODUCT_TYPE_MEMORYSTORE | &quot;PRODUCT_TYPE_MEMORYSTORE&quot; |
| PRODUCT_TYPE_OTHER | &quot;PRODUCT_TYPE_OTHER&quot; |



