

# SubscriptionProduct


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**label** | **String** | A human readable description of the Product that is subscribed |  |
|**namespace** | **String** | Grouping of related Subscriptions |  |
|**pfid** | **Integer** | Unique identifier of the Product that is subscribed |  |
|**productGroupKey** | **String** | Primary key of a grouping of related Subscriptions |  |
|**renewalPeriod** | **Integer** | The number of &#x60;renewalPeriodUnits&#x60; that will be added by the &#x60;renewalPfid&#x60; |  |
|**renewalPeriodUnit** | [**RenewalPeriodUnitEnum**](#RenewalPeriodUnitEnum) | The unit of time that &#x60;renewalPeriod&#x60; is measured in |  |
|**renewalPfid** | **Integer** | Unique identifier of the renewal Product |  |
|**supportBillOn** | **Boolean** | Whether the product supports the &#x60;billOn&#x60; option on the renewal endpoint |  |



## Enum: RenewalPeriodUnitEnum

| Name | Value |
|---- | -----|
| MONTH | &quot;MONTH&quot; |
| QUARTER | &quot;QUARTER&quot; |
| SEMI_ANNUAL | &quot;SEMI_ANNUAL&quot; |
| YEAR | &quot;YEAR&quot; |



