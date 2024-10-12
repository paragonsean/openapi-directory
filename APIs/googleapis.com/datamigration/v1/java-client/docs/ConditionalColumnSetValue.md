

# ConditionalColumnSetValue

Options to configure rule type ConditionalColumnSetValue. The rule is used to transform the data which is being replicated/migrated. The rule filter field can refer to one or more entities. The rule scope can be one of: Column.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**customFeatures** | **Map&lt;String, Object&gt;** | Optional. Custom engine specific features. |  [optional] |
|**sourceNumericFilter** | [**SourceNumericFilter**](SourceNumericFilter.md) |  |  [optional] |
|**sourceTextFilter** | [**SourceTextFilter**](SourceTextFilter.md) |  |  [optional] |
|**valueTransformation** | [**ValueTransformation**](ValueTransformation.md) |  |  [optional] |



