

# GoogleCloudPaymentsResellerSubscriptionV1EntitleSubscriptionRequestLineItemEntitlementDetails

The details of the line item to be entitled.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**lineItemIndex** | **Integer** | Required. The index of the line item to be entitled. |  [optional] |
|**products** | **List&lt;String&gt;** | Optional. Only applicable if the line item corresponds to a hard bundle. Product resource names that identify the bundle elements to be entitled in the line item. If unspecified, all bundle elements will be entitled. The format is &#39;partners/{partner_id}/products/{product_id}&#39;. |  [optional] |



