

# GoogleAdsSearchads360V0ErrorsQuotaErrorDetails

Additional quota error details when there is QuotaError.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**rateName** | **String** | The high level description of the quota bucket. Examples are \&quot;Get requests for standard access\&quot; or \&quot;Requests per account\&quot;. |  [optional] |
|**rateScope** | [**RateScopeEnum**](#RateScopeEnum) | The rate scope of the quota limit. |  [optional] |
|**retryDelay** | **String** | Backoff period that customers should wait before sending next request. |  [optional] |



## Enum: RateScopeEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;UNSPECIFIED&quot; |
| UNKNOWN | &quot;UNKNOWN&quot; |
| ACCOUNT | &quot;ACCOUNT&quot; |
| DEVELOPER | &quot;DEVELOPER&quot; |



