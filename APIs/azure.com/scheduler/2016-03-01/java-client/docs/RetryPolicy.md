

# RetryPolicy


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**retryCount** | **Integer** | Gets or sets the number of times a retry should be attempted. |  [optional] |
|**retryInterval** | **String** | Gets or sets the retry interval between retries, specify duration in ISO 8601 format. |  [optional] |
|**retryType** | [**RetryTypeEnum**](#RetryTypeEnum) | Gets or sets the retry strategy to be used. |  [optional] |



## Enum: RetryTypeEnum

| Name | Value |
|---- | -----|
| NONE | &quot;None&quot; |
| FIXED | &quot;Fixed&quot; |



