

# DatabaseType

A message defining the database engine and provider.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**engine** | [**EngineEnum**](#EngineEnum) | The database engine. |  [optional] |
|**provider** | [**ProviderEnum**](#ProviderEnum) | The database provider. |  [optional] |



## Enum: EngineEnum

| Name | Value |
|---- | -----|
| DATABASE_ENGINE_UNSPECIFIED | &quot;DATABASE_ENGINE_UNSPECIFIED&quot; |
| MYSQL | &quot;MYSQL&quot; |
| POSTGRESQL | &quot;POSTGRESQL&quot; |
| ORACLE | &quot;ORACLE&quot; |



## Enum: ProviderEnum

| Name | Value |
|---- | -----|
| DATABASE_PROVIDER_UNSPECIFIED | &quot;DATABASE_PROVIDER_UNSPECIFIED&quot; |
| CLOUDSQL | &quot;CLOUDSQL&quot; |
| RDS | &quot;RDS&quot; |
| AURORA | &quot;AURORA&quot; |
| ALLOYDB | &quot;ALLOYDB&quot; |



