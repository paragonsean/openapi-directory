

# V1ModelsSourceSourceOutput


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**dataset** | **String** |  |  |
|**description** | **String** |  |  |
|**maximumRisk** | [**MaximumRiskEnum**](#MaximumRiskEnum) |  |  |
|**maximumScore** | **Integer** |  |  |
|**minimumRisk** | [**MinimumRiskEnum**](#MinimumRiskEnum) |  |  |
|**minimumScore** | **Integer** |  |  |
|**name** | **String** |  |  |
|**refresh** | [**RefreshEnum**](#RefreshEnum) |  |  |
|**self** | **String** |  |  |
|**source** | **String** |  |  |
|**subscriptions** | [**List&lt;SubscriptionsEnum&gt;**](#List&lt;SubscriptionsEnum&gt;) |  |  |
|**timeRanges** | **List&lt;String&gt;** |  |  |
|**updatedAt** | **Integer** |  |  |
|**url** | **String** |  |  |



## Enum: MaximumRiskEnum

| Name | Value |
|---- | -----|
| UNKNOWN | &quot;UNKNOWN&quot; |
| LOW | &quot;LOW&quot; |
| MEDIUM | &quot;MEDIUM&quot; |
| HIGH | &quot;HIGH&quot; |



## Enum: MinimumRiskEnum

| Name | Value |
|---- | -----|
| UNKNOWN | &quot;UNKNOWN&quot; |
| LOW | &quot;LOW&quot; |
| MEDIUM | &quot;MEDIUM&quot; |
| HIGH | &quot;HIGH&quot; |



## Enum: RefreshEnum

| Name | Value |
|---- | -----|
| _1_H | &quot;1H&quot; |
| _6_H | &quot;6H&quot; |
| _12_H | &quot;12H&quot; |
| _1_D | &quot;1D&quot; |
| _7_D | &quot;7D&quot; |
| _30_D | &quot;30D&quot; |
| _90_D | &quot;90D&quot; |
| _180_D | &quot;180D&quot; |
| _365_D | &quot;365D&quot; |



## Enum: List&lt;SubscriptionsEnum&gt;

| Name | Value |
|---- | -----|
| FREE | &quot;FREE&quot; |
| BASIC | &quot;BASIC&quot; |
| PRO | &quot;PRO&quot; |
| ENTERPRISE | &quot;ENTERPRISE&quot; |



