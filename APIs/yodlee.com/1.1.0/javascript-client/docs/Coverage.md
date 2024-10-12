# YodleeCoreApis.Coverage

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | [**[CoverageAmount]**](CoverageAmount.md) | The coverage amount-related details.&lt;br&gt;&lt;br&gt;&lt;b&gt;Aggregated / Manual&lt;/b&gt;: Aggregated&lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;: insurance,investment&lt;br&gt;&lt;b&gt;Endpoints&lt;/b&gt;:&lt;ul&gt;&lt;li&gt;GET accounts&lt;/li&gt;&lt;li&gt;GET accounts/{accountId}&lt;/li&gt;&lt;/ul&gt; | [optional] [readonly] 
**endDate** | **String** | The date on which the coverage for the account ends or expires.&lt;br&gt;&lt;br&gt;&lt;b&gt;Aggregated / Manual&lt;/b&gt;: Aggregated&lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;: insurance,investment&lt;br&gt;&lt;b&gt;Endpoints&lt;/b&gt;:&lt;ul&gt;&lt;li&gt;GET accounts&lt;/li&gt;&lt;li&gt;GET accounts/{accountId}&lt;/li&gt;&lt;/ul&gt; | [optional] [readonly] 
**planType** | **String** | The plan type for an insurance provided to an individual or an entity.&lt;br&gt;&lt;br&gt;&lt;b&gt;Aggregated / Manual&lt;/b&gt;: Aggregated&lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;: insurance&lt;br&gt;&lt;b&gt;Endpoints&lt;/b&gt;:&lt;ul&gt;&lt;li&gt;GET accounts&lt;/li&gt;&lt;li&gt;GET accounts/{accountId}&lt;/li&gt;&lt;/ul&gt;&lt;b&gt;Applicable Values:&lt;/b&gt;&lt;br&gt; | [optional] [readonly] 
**startDate** | **String** | The date on which the coverage for the account starts.&lt;br&gt;&lt;br&gt;&lt;b&gt;Aggregated / Manual&lt;/b&gt;: Aggregated&lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;: insurance,investment&lt;br&gt;&lt;b&gt;Endpoints&lt;/b&gt;:&lt;ul&gt;&lt;li&gt;GET accounts&lt;/li&gt;&lt;li&gt;GET accounts/{accountId}&lt;/li&gt;&lt;/ul&gt; | [optional] [readonly] 
**type** | **String** | The type of coverage provided to an individual or an entity.&lt;br&gt;&lt;br&gt;&lt;b&gt;Aggregated / Manual&lt;/b&gt;: Aggregated&lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;: insurance,investment&lt;br&gt;&lt;b&gt;Endpoints&lt;/b&gt;:&lt;ul&gt;&lt;li&gt;GET accounts&lt;/li&gt;&lt;li&gt;GET accounts/{accountId}&lt;/li&gt;&lt;/ul&gt;&lt;b&gt;Applicable Values:&lt;/b&gt;&lt;br&gt; | [optional] [readonly] 



## Enum: PlanTypeEnum


* `PPO` (value: `"PPO"`)

* `HMO` (value: `"HMO"`)

* `UNKNOWN` (value: `"UNKNOWN"`)





## Enum: TypeEnum


* `VISION` (value: `"VISION"`)

* `DENTAL` (value: `"DENTAL"`)

* `MEDICAL` (value: `"MEDICAL"`)

* `HEALTH` (value: `"HEALTH"`)

* `DEATH_COVER` (value: `"DEATH_COVER"`)

* `TOTAL_PERMANENT_DISABILITY` (value: `"TOTAL_PERMANENT_DISABILITY"`)

* `ACCIDENTAL_DEATH_COVER` (value: `"ACCIDENTAL_DEATH_COVER"`)

* `INCOME_PROTECTION` (value: `"INCOME_PROTECTION"`)

* `DEATH_TOTAL_PERMANENT_DISABILITY` (value: `"DEATH_TOTAL_PERMANENT_DISABILITY"`)

* `OTHER` (value: `"OTHER"`)




