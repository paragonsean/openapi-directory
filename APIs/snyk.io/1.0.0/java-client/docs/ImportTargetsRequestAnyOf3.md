

# ImportTargetsRequestAnyOf3


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**exclusionGlobs** | **String** | a comma-separated list of up to 10 folder names to exclude from scanning. If not specified, it will default to \&quot;fixtures, tests, \\_\\_tests\\_\\_, node_modules\&quot;. If an empty string is provided - no folders will be excluded. This attribute is only respected with Open Source and Container scan targets. |  [optional] |
|**files** | **List&lt;Object&gt;** | an array of file objects |  [optional] |
|**target** | [**ImportTargetsRequestAnyOf3Target**](ImportTargetsRequestAnyOf3Target.md) |  |  [optional] |



