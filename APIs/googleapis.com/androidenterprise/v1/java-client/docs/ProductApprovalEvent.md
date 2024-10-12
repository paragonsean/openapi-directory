

# ProductApprovalEvent

An event generated when a product's approval status is changed.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**approved** | [**ApprovedEnum**](#ApprovedEnum) | Whether the product was approved or unapproved. This field will always be present. |  [optional] |
|**productId** | **String** | The id of the product (e.g. \&quot;app:com.google.android.gm\&quot;) for which the approval status has changed. This field will always be present. |  [optional] |



## Enum: ApprovedEnum

| Name | Value |
|---- | -----|
| UNKNOWN | &quot;unknown&quot; |
| APPROVED | &quot;approved&quot; |
| UNAPPROVED | &quot;unapproved&quot; |



