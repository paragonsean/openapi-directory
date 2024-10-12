

# KeywordLease

Represents a lease object for a given keyword

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**autoRenew** | **Boolean** | Enables the auto renewal of a keyword lease at the end of each billing cycle |  [optional] |
|**contactListId** | **Long** | Existing contact list ID |  [optional] |
|**doubleOptInEnabled** | **Boolean** | Enable/disable double opt in feature |  [optional] |
|**keyword** | **String** | A text used as a keyword |  [optional] |
|**labels** | **List&lt;String&gt;** | ~ |  [optional] |
|**leaseBegin** | **Long** | A time of a lease timestamp, formatted in unix time milliseconds (read only). Example: 1473781817000 for Sat, 05 Jan 1985 14:03:37 GMT |  [optional] |
|**leaseEnd** | **Long** | A date and time when the keyword lease is finishes. Timestamp, formatted in unix time milliseconds (read only). Example: 1473781817000 |  [optional] |
|**number** | **String** | A number assigned to keyword. Example: 12132212344 |  [optional] |
|**optInConfirmationMessage** | **String** | Opt in confirmation message |  [optional] |
|**shortCode** | **String** | A short code assigned to keyword. Example: 67076 (Deprecated - please use number instead) |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | A lease status. Available values: PENDING, ACTIVE, RELEASED, UNAVAILABLE |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | ~ |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| PENDING | &quot;PENDING&quot; |
| ACTIVE | &quot;ACTIVE&quot; |
| RELEASED | &quot;RELEASED&quot; |
| UNAVAILABLE | &quot;UNAVAILABLE&quot; |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| PLAN | &quot;PLAN&quot; |
| EXTRA | &quot;EXTRA&quot; |



