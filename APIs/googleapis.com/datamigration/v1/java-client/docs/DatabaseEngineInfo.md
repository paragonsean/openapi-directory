

# DatabaseEngineInfo

The type and version of a source or destination database.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**engine** | [**EngineEnum**](#EngineEnum) | Required. Engine type. |  [optional] |
|**version** | **String** | Required. Engine version, for example \&quot;12.c.1\&quot;. |  [optional] |



## Enum: EngineEnum

| Name | Value |
|---- | -----|
| DATABASE_ENGINE_UNSPECIFIED | &quot;DATABASE_ENGINE_UNSPECIFIED&quot; |
| MYSQL | &quot;MYSQL&quot; |
| POSTGRESQL | &quot;POSTGRESQL&quot; |
| ORACLE | &quot;ORACLE&quot; |



