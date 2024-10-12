

# NumberLease

Represents a lease object for a given phone number

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**autoRenew** | **Boolean** | Enables the auto renewal of number lease at end of each billing cycle |  [optional] |
|**callFeatureStatus** | [**CallFeatureStatusEnum**](#CallFeatureStatusEnum) | A status of a call feature. Available values: DISABLED, ENABLED |  [optional] |
|**labels** | **List&lt;String&gt;** | ~ |  [optional] |
|**leaseBegin** | **Long** | A date and time of a lease start. Timestamp, formatted in unix time milliseconds (read only). Example: 1473781817000 |  [optional] |
|**leaseEnd** | **Long** | A data and time of a lease finish. Timestamp, formatted in unix time milliseconds (read only). Example: 1473781817000 |  [optional] |
|**nationalFormat** | **String** | Formatted number with a country code |  [optional] |
|**number** | **String** | A phone number in E.164 format (11-digit). Example: 12132000384 |  [optional] |
|**region** | [**Region**](Region.md) |  |  [optional] |
|**sendEmailOnCreate** | **Boolean** | ~ |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | A lease status. Available values: PENDING, ACTIVE, RELEASED, UNAVAILABLE |  [optional] [readonly] |
|**textFeatureStatus** | [**TextFeatureStatusEnum**](#TextFeatureStatusEnum) | A status of a text feature. Available values: DISABLED, ENABLED |  [optional] |
|**tollFree** | **Boolean** | A  toll-free number |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | ~ |  [optional] |



## Enum: CallFeatureStatusEnum

| Name | Value |
|---- | -----|
| UNSUPPORTED | &quot;UNSUPPORTED&quot; |
| PENDING | &quot;PENDING&quot; |
| DISABLED | &quot;DISABLED&quot; |
| ENABLED | &quot;ENABLED&quot; |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| PENDING | &quot;PENDING&quot; |
| ACTIVE | &quot;ACTIVE&quot; |
| RELEASED | &quot;RELEASED&quot; |
| UNAVAILABLE | &quot;UNAVAILABLE&quot; |



## Enum: TextFeatureStatusEnum

| Name | Value |
|---- | -----|
| UNSUPPORTED | &quot;UNSUPPORTED&quot; |
| PENDING | &quot;PENDING&quot; |
| DISABLED | &quot;DISABLED&quot; |
| ENABLED | &quot;ENABLED&quot; |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| PLAN | &quot;PLAN&quot; |
| EXTRA | &quot;EXTRA&quot; |



