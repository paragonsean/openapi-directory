

# RecommendedActionImpactRecord

Contains information of estimated or observed impact on various metrics for an Azure SQL Database, Server or Elastic Pool Recommended Action.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**absoluteValue** | **Double** | Gets the absolute value of this dimension if applicable. e.g., Number of Queries affected |  [optional] [readonly] |
|**changeValueAbsolute** | **Double** | Gets the absolute change in the value of this dimension. e.g., Absolute Disk space change in Megabytes |  [optional] [readonly] |
|**changeValueRelative** | **Double** | Gets the relative change in the value of this dimension. e.g., Relative Disk space change in Percentage |  [optional] [readonly] |
|**dimensionName** | **String** | Gets the name of the impact dimension. e.g., CPUChange, DiskSpaceChange, NumberOfQueriesAffected. |  [optional] [readonly] |
|**unit** | **String** | Gets the name of the impact dimension. e.g., CPUChange, DiskSpaceChange, NumberOfQueriesAffected. |  [optional] [readonly] |



