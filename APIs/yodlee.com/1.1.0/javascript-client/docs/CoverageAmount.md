# YodleeCoreApis.CoverageAmount

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cover** | [**Money**](Money.md) |  | [optional] 
**limitType** | **String** | The type of coverage limit indicates if the coverage is in-network or out-of-network.&lt;br&gt;&lt;br&gt;&lt;b&gt;Aggregated / Manual&lt;/b&gt;: Aggregated&lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;: insurance,investment&lt;br&gt;&lt;b&gt;Endpoints&lt;/b&gt;:&lt;ul&gt;&lt;li&gt;GET accounts&lt;/li&gt;&lt;li&gt;GET accounts/{accountId}&lt;/li&gt;&lt;/ul&gt;&lt;b&gt;Applicable Values:&lt;/b&gt;&lt;br&gt; | [optional] [readonly] 
**met** | [**Money**](Money.md) |  | [optional] 
**type** | **String** | The type of coverage provided to an individual or an entity.&lt;br&gt;&lt;br&gt;&lt;b&gt;Aggregated / Manual&lt;/b&gt;: Aggregated&lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;: insurance,investment&lt;br&gt;&lt;b&gt;Endpoints&lt;/b&gt;:&lt;ul&gt;&lt;li&gt;GET accounts&lt;/li&gt;&lt;li&gt;GET accounts/{accountId}&lt;/li&gt;&lt;/ul&gt;&lt;b&gt;Applicable Values:&lt;/b&gt;&lt;br&gt; | [optional] [readonly] 
**unitType** | **String** | The type of coverage unit indicates if the coverage is for an individual or a family.&lt;br&gt;&lt;br&gt;&lt;b&gt;Aggregated / Manual&lt;/b&gt;: Aggregated&lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;: insurance,investment&lt;br&gt;&lt;b&gt;Endpoints&lt;/b&gt;:&lt;ul&gt;&lt;li&gt;GET accounts&lt;/li&gt;&lt;li&gt;GET accounts/{accountId}&lt;/li&gt;&lt;/ul&gt;&lt;b&gt;Applicable Values:&lt;/b&gt;&lt;br&gt; | [optional] [readonly] 



## Enum: LimitTypeEnum


* `IN_NETWORK` (value: `"IN_NETWORK"`)

* `OUT_NETWORK` (value: `"OUT_NETWORK"`)





## Enum: TypeEnum


* `DEDUCTIBLE` (value: `"DEDUCTIBLE"`)

* `OUT_OF_POCKET` (value: `"OUT_OF_POCKET"`)

* `ANNUAL_BENEFIT` (value: `"ANNUAL_BENEFIT"`)

* `MAX_BENEFIT` (value: `"MAX_BENEFIT"`)

* `COVERAGE_AMOUNT` (value: `"COVERAGE_AMOUNT"`)

* `MONTHLY_BENEFIT` (value: `"MONTHLY_BENEFIT"`)

* `OTHER` (value: `"OTHER"`)





## Enum: UnitTypeEnum


* `FAMILY` (value: `"PER_FAMILY"`)

* `MEMBER` (value: `"PER_MEMBER"`)




