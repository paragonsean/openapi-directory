

# CoverageAmount


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**cover** | [**Money**](Money.md) |  |  [optional] |
|**limitType** | [**LimitTypeEnum**](#LimitTypeEnum) | The type of coverage limit indicates if the coverage is in-network or out-of-network.&lt;br&gt;&lt;br&gt;&lt;b&gt;Aggregated / Manual&lt;/b&gt;: Aggregated&lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;: insurance,investment&lt;br&gt;&lt;b&gt;Endpoints&lt;/b&gt;:&lt;ul&gt;&lt;li&gt;GET accounts&lt;/li&gt;&lt;li&gt;GET accounts/{accountId}&lt;/li&gt;&lt;/ul&gt;&lt;b&gt;Applicable Values:&lt;/b&gt;&lt;br&gt; |  [optional] [readonly] |
|**met** | [**Money**](Money.md) |  |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | The type of coverage provided to an individual or an entity.&lt;br&gt;&lt;br&gt;&lt;b&gt;Aggregated / Manual&lt;/b&gt;: Aggregated&lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;: insurance,investment&lt;br&gt;&lt;b&gt;Endpoints&lt;/b&gt;:&lt;ul&gt;&lt;li&gt;GET accounts&lt;/li&gt;&lt;li&gt;GET accounts/{accountId}&lt;/li&gt;&lt;/ul&gt;&lt;b&gt;Applicable Values:&lt;/b&gt;&lt;br&gt; |  [optional] [readonly] |
|**unitType** | [**UnitTypeEnum**](#UnitTypeEnum) | The type of coverage unit indicates if the coverage is for an individual or a family.&lt;br&gt;&lt;br&gt;&lt;b&gt;Aggregated / Manual&lt;/b&gt;: Aggregated&lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;: insurance,investment&lt;br&gt;&lt;b&gt;Endpoints&lt;/b&gt;:&lt;ul&gt;&lt;li&gt;GET accounts&lt;/li&gt;&lt;li&gt;GET accounts/{accountId}&lt;/li&gt;&lt;/ul&gt;&lt;b&gt;Applicable Values:&lt;/b&gt;&lt;br&gt; |  [optional] [readonly] |



## Enum: LimitTypeEnum

| Name | Value |
|---- | -----|
| IN_NETWORK | &quot;IN_NETWORK&quot; |
| OUT_NETWORK | &quot;OUT_NETWORK&quot; |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| DEDUCTIBLE | &quot;DEDUCTIBLE&quot; |
| OUT_OF_POCKET | &quot;OUT_OF_POCKET&quot; |
| ANNUAL_BENEFIT | &quot;ANNUAL_BENEFIT&quot; |
| MAX_BENEFIT | &quot;MAX_BENEFIT&quot; |
| COVERAGE_AMOUNT | &quot;COVERAGE_AMOUNT&quot; |
| MONTHLY_BENEFIT | &quot;MONTHLY_BENEFIT&quot; |
| OTHER | &quot;OTHER&quot; |



## Enum: UnitTypeEnum

| Name | Value |
|---- | -----|
| FAMILY | &quot;PER_FAMILY&quot; |
| MEMBER | &quot;PER_MEMBER&quot; |



