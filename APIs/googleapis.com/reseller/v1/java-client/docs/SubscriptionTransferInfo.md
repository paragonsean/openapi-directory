

# SubscriptionTransferInfo

Read-only transfer related information for the subscription. For more information, see retrieve transferable subscriptions for a customer.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**currentLegacySkuId** | **String** | The &#x60;skuId&#x60; of the current resold subscription. This is populated only when the customer has a subscription with a legacy SKU and the subscription resource is populated with the &#x60;skuId&#x60; of the SKU recommended for the transfer. |  [optional] |
|**minimumTransferableSeats** | **Integer** | When inserting a subscription, this is the minimum number of seats listed in the transfer order for this product. For example, if the customer has 20 users, the reseller cannot place a transfer order of 15 seats. The minimum is 20 seats. |  [optional] |
|**transferabilityExpirationTime** | **String** | The time when transfer token or intent to transfer will expire. The time is in milliseconds using UNIX Epoch format. |  [optional] |



