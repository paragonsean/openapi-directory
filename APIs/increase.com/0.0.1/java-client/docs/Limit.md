

# Limit

You can set limits at the Account, Account Number, or Card level. Limits applied to Accounts will apply to all Account Numbers and Cards in the Account. You can specify any number of Limits and they will all be applied to inbound debits and card authorizations. Volume and count Limits are designed to prevent unauthorized debits.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** | The Limit identifier. |  |
|**interval** | [**IntervalEnum**](#IntervalEnum) | The interval for the metric. This is required if &#x60;metric&#x60; is &#x60;count&#x60; or &#x60;volume&#x60;. |  |
|**metric** | [**MetricEnum**](#MetricEnum) | The metric for the Limit. |  |
|**modelId** | **String** | The identifier of the Account Number, Account, or Card the Limit applies to. |  |
|**modelType** | [**ModelTypeEnum**](#ModelTypeEnum) | The type of the model you wish to associate the Limit with. |  |
|**status** | [**StatusEnum**](#StatusEnum) | The current status of the Limit. |  |
|**type** | [**TypeEnum**](#TypeEnum) | A constant representing the object&#39;s type. For this resource it will always be &#x60;limit&#x60;. |  |
|**value** | **Integer** | The value to evaluate the Limit against. |  |



## Enum: IntervalEnum

| Name | Value |
|---- | -----|
| TRANSACTION | &quot;transaction&quot; |
| DAY | &quot;day&quot; |
| WEEK | &quot;week&quot; |
| MONTH | &quot;month&quot; |
| YEAR | &quot;year&quot; |
| ALL_TIME | &quot;all_time&quot; |



## Enum: MetricEnum

| Name | Value |
|---- | -----|
| COUNT | &quot;count&quot; |
| VOLUME | &quot;volume&quot; |



## Enum: ModelTypeEnum

| Name | Value |
|---- | -----|
| ACCOUNT | &quot;account&quot; |
| ACCOUNT_NUMBER | &quot;account_number&quot; |
| CARD | &quot;card&quot; |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| ACTIVE | &quot;active&quot; |
| INACTIVE | &quot;inactive&quot; |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| LIMIT | &quot;limit&quot; |



