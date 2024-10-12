

# IpReputation

IP Reputation information for a set of IPs in a specific reputation category.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**ipCount** | **String** | Total number of unique IPs in this reputation category. This metric only pertains to traffic that passed [SPF](http://www.openspf.org/) or [DKIM](http://www.dkim.org/). |  [optional] |
|**reputation** | [**ReputationEnum**](#ReputationEnum) | The reputation category this IP reputation represents. |  [optional] |
|**sampleIps** | **List&lt;String&gt;** | A sample of IPs in this reputation category. |  [optional] |



## Enum: ReputationEnum

| Name | Value |
|---- | -----|
| REPUTATION_CATEGORY_UNSPECIFIED | &quot;REPUTATION_CATEGORY_UNSPECIFIED&quot; |
| HIGH | &quot;HIGH&quot; |
| MEDIUM | &quot;MEDIUM&quot; |
| LOW | &quot;LOW&quot; |
| BAD | &quot;BAD&quot; |



