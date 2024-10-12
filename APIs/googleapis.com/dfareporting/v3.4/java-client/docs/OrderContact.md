

# OrderContact

Contact of an order.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**contactInfo** | **String** | Free-form information about this contact. It could be any information related to this contact in addition to type, title, name, and signature user profile ID. |  [optional] |
|**contactName** | **String** | Name of this contact. |  [optional] |
|**contactTitle** | **String** | Title of this contact. |  [optional] |
|**contactType** | [**ContactTypeEnum**](#ContactTypeEnum) | Type of this contact. |  [optional] |
|**signatureUserProfileId** | **String** | ID of the user profile containing the signature that will be embedded into order documents. |  [optional] |



## Enum: ContactTypeEnum

| Name | Value |
|---- | -----|
| BUYER_CONTACT | &quot;PLANNING_ORDER_CONTACT_BUYER_CONTACT&quot; |
| BUYER_BILLING_CONTACT | &quot;PLANNING_ORDER_CONTACT_BUYER_BILLING_CONTACT&quot; |
| SELLER_CONTACT | &quot;PLANNING_ORDER_CONTACT_SELLER_CONTACT&quot; |



