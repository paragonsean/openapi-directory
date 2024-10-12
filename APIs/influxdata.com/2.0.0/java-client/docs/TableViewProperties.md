

# TableViewProperties


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**colors** | [**List&lt;DashboardColor&gt;**](DashboardColor.md) | Colors define color encoding of data into a visualization |  |
|**decimalPlaces** | [**DecimalPlaces**](DecimalPlaces.md) |  |  |
|**fieldOptions** | [**List&lt;RenamableField&gt;**](RenamableField.md) | fieldOptions represent the fields retrieved by the query with customization options |  |
|**note** | **String** |  |  |
|**queries** | [**List&lt;DashboardQuery&gt;**](DashboardQuery.md) |  |  |
|**shape** | [**ShapeEnum**](#ShapeEnum) |  |  |
|**showNoteWhenEmpty** | **Boolean** | If true, will display note when empty |  |
|**tableOptions** | [**TableViewPropertiesTableOptions**](TableViewPropertiesTableOptions.md) |  |  |
|**timeFormat** | **String** | timeFormat describes the display format for time values according to moment.js date formatting |  |
|**type** | [**TypeEnum**](#TypeEnum) |  |  |



## Enum: ShapeEnum

| Name | Value |
|---- | -----|
| CHRONOGRAF_V2 | &quot;chronograf-v2&quot; |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| TABLE | &quot;table&quot; |



