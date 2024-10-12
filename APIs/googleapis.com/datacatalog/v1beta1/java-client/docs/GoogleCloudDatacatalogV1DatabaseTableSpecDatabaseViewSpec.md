

# GoogleCloudDatacatalogV1DatabaseTableSpecDatabaseViewSpec

Specification that applies to database view.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**baseTable** | **String** | Name of a singular table this view reflects one to one. |  [optional] |
|**sqlQuery** | **String** | SQL query used to generate this view. |  [optional] |
|**viewType** | [**ViewTypeEnum**](#ViewTypeEnum) | Type of this view. |  [optional] |



## Enum: ViewTypeEnum

| Name | Value |
|---- | -----|
| VIEW_TYPE_UNSPECIFIED | &quot;VIEW_TYPE_UNSPECIFIED&quot; |
| STANDARD_VIEW | &quot;STANDARD_VIEW&quot; |
| MATERIALIZED_VIEW | &quot;MATERIALIZED_VIEW&quot; |



