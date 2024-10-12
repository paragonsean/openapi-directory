

# Coverage


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**amount** | [**List&lt;CoverageAmount&gt;**](CoverageAmount.md) | The coverage amount-related details.&lt;br&gt;&lt;br&gt;&lt;b&gt;Aggregated / Manual&lt;/b&gt;: Aggregated&lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;: insurance,investment&lt;br&gt;&lt;b&gt;Endpoints&lt;/b&gt;:&lt;ul&gt;&lt;li&gt;GET accounts&lt;/li&gt;&lt;li&gt;GET accounts/{accountId}&lt;/li&gt;&lt;/ul&gt; |  [optional] [readonly] |
|**endDate** | **String** | The date on which the coverage for the account ends or expires.&lt;br&gt;&lt;br&gt;&lt;b&gt;Aggregated / Manual&lt;/b&gt;: Aggregated&lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;: insurance,investment&lt;br&gt;&lt;b&gt;Endpoints&lt;/b&gt;:&lt;ul&gt;&lt;li&gt;GET accounts&lt;/li&gt;&lt;li&gt;GET accounts/{accountId}&lt;/li&gt;&lt;/ul&gt; |  [optional] [readonly] |
|**planType** | [**PlanTypeEnum**](#PlanTypeEnum) | The plan type for an insurance provided to an individual or an entity.&lt;br&gt;&lt;br&gt;&lt;b&gt;Aggregated / Manual&lt;/b&gt;: Aggregated&lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;: insurance&lt;br&gt;&lt;b&gt;Endpoints&lt;/b&gt;:&lt;ul&gt;&lt;li&gt;GET accounts&lt;/li&gt;&lt;li&gt;GET accounts/{accountId}&lt;/li&gt;&lt;/ul&gt;&lt;b&gt;Applicable Values:&lt;/b&gt;&lt;br&gt; |  [optional] [readonly] |
|**startDate** | **String** | The date on which the coverage for the account starts.&lt;br&gt;&lt;br&gt;&lt;b&gt;Aggregated / Manual&lt;/b&gt;: Aggregated&lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;: insurance,investment&lt;br&gt;&lt;b&gt;Endpoints&lt;/b&gt;:&lt;ul&gt;&lt;li&gt;GET accounts&lt;/li&gt;&lt;li&gt;GET accounts/{accountId}&lt;/li&gt;&lt;/ul&gt; |  [optional] [readonly] |
|**type** | [**TypeEnum**](#TypeEnum) | The type of coverage provided to an individual or an entity.&lt;br&gt;&lt;br&gt;&lt;b&gt;Aggregated / Manual&lt;/b&gt;: Aggregated&lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;: insurance,investment&lt;br&gt;&lt;b&gt;Endpoints&lt;/b&gt;:&lt;ul&gt;&lt;li&gt;GET accounts&lt;/li&gt;&lt;li&gt;GET accounts/{accountId}&lt;/li&gt;&lt;/ul&gt;&lt;b&gt;Applicable Values:&lt;/b&gt;&lt;br&gt; |  [optional] [readonly] |



## Enum: PlanTypeEnum

| Name | Value |
|---- | -----|
| PPO | &quot;PPO&quot; |
| HMO | &quot;HMO&quot; |
| UNKNOWN | &quot;UNKNOWN&quot; |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| VISION | &quot;VISION&quot; |
| DENTAL | &quot;DENTAL&quot; |
| MEDICAL | &quot;MEDICAL&quot; |
| HEALTH | &quot;HEALTH&quot; |
| DEATH_COVER | &quot;DEATH_COVER&quot; |
| TOTAL_PERMANENT_DISABILITY | &quot;TOTAL_PERMANENT_DISABILITY&quot; |
| ACCIDENTAL_DEATH_COVER | &quot;ACCIDENTAL_DEATH_COVER&quot; |
| INCOME_PROTECTION | &quot;INCOME_PROTECTION&quot; |
| DEATH_TOTAL_PERMANENT_DISABILITY | &quot;DEATH_TOTAL_PERMANENT_DISABILITY&quot; |
| OTHER | &quot;OTHER&quot; |



