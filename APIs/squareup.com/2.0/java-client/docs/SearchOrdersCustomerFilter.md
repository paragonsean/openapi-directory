

# SearchOrdersCustomerFilter

A filter based on the order `customer_id` and any tender `customer_id` associated with the order. It does not filter based on the [FulfillmentRecipient](https://developer.squareup.com/reference/square_2021-08-18/objects/OrderFulfillmentRecipient) `customer_id`.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**customerIds** | **List&lt;String&gt;** | A list of customer IDs to filter by.  Max: 10 customer IDs. |  [optional] |



