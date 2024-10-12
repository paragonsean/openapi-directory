

# DataSource

Data Source is a way for us to know the source of instances. A single type can have data coming in from multiple places. In activities we use this to determine precedence rules.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**dataSourceReferenceId** | **String** | The data source reference id. |  [optional] [readonly] |
|**dataSourceType** | [**DataSourceTypeEnum**](#DataSourceTypeEnum) | The data source type. |  [optional] [readonly] |
|**id** | **Integer** | The data source ID. |  [optional] [readonly] |
|**name** | **String** | The data source name |  [optional] [readonly] |
|**status** | [**StatusEnum**](#StatusEnum) | The data source status. |  [optional] [readonly] |



## Enum: DataSourceTypeEnum

| Name | Value |
|---- | -----|
| CONNECTOR | &quot;Connector&quot; |
| LINK_INTERACTION | &quot;LinkInteraction&quot; |
| SYSTEM_DEFAULT | &quot;SystemDefault&quot; |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| NONE | &quot;None&quot; |
| ACTIVE | &quot;Active&quot; |
| DELETED | &quot;Deleted&quot; |



