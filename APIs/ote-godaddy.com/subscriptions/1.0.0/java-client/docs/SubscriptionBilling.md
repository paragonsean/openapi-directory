

# SubscriptionBilling


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**commitment** | [**CommitmentEnum**](#CommitmentEnum) | The financial commitment the customer has in the product |  |
|**pastDueTypes** | [**List&lt;PastDueTypesEnum&gt;**](#List&lt;PastDueTypesEnum&gt;) | The types of charges that are past due when &#x60;status&#x60; is PAST_DUE |  [optional] |
|**renewAt** | **String** | The point in time after which the Subscription will bill for automatic renewal |  |
|**status** | [**StatusEnum**](#StatusEnum) | Whether payments are past due |  |



## Enum: CommitmentEnum

| Name | Value |
|---- | -----|
| PAID | &quot;PAID&quot; |
| FREE | &quot;FREE&quot; |
| TRIAL | &quot;TRIAL&quot; |



## Enum: List&lt;PastDueTypesEnum&gt;

| Name | Value |
|---- | -----|
| ADDON | &quot;ADDON&quot; |
| BURST | &quot;BURST&quot; |
| SUBSCRIPTION | &quot;SUBSCRIPTION&quot; |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| CURRENT | &quot;CURRENT&quot; |
| PAST_DUE | &quot;PAST_DUE&quot; |



