

# RecommendedActionErrorInfo

Contains error information for an Azure SQL Database, Server or Elastic Pool Recommended Action.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**errorCode** | **String** | Gets the reason why the recommended action was put to error state. e.g., DatabaseHasQdsOff, IndexAlreadyExists |  [optional] [readonly] |
|**isRetryable** | [**IsRetryableEnum**](#IsRetryableEnum) | Gets whether the error could be ignored and recommended action could be retried. Possible values are: Yes/No |  [optional] [readonly] |



## Enum: IsRetryableEnum

| Name | Value |
|---- | -----|
| YES | &quot;Yes&quot; |
| NO | &quot;No&quot; |



