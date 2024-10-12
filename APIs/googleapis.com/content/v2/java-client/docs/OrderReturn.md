

# OrderReturn


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**actor** | **String** | The actor that created the refund. Acceptable values are: - \&quot;&#x60;customer&#x60;\&quot; - \&quot;&#x60;googleBot&#x60;\&quot; - \&quot;&#x60;googleCustomerService&#x60;\&quot; - \&quot;&#x60;googlePayments&#x60;\&quot; - \&quot;&#x60;googleSabre&#x60;\&quot; - \&quot;&#x60;merchant&#x60;\&quot;  |  [optional] |
|**creationDate** | **String** | Date on which the item has been created, in ISO 8601 format. |  [optional] |
|**quantity** | **Integer** | Quantity that is returned. |  [optional] |
|**reason** | **String** | The reason for the return. Acceptable values are: - \&quot;&#x60;customerDiscretionaryReturn&#x60;\&quot; - \&quot;&#x60;customerInitiatedMerchantCancel&#x60;\&quot; - \&quot;&#x60;deliveredTooLate&#x60;\&quot; - \&quot;&#x60;expiredItem&#x60;\&quot; - \&quot;&#x60;invalidCoupon&#x60;\&quot; - \&quot;&#x60;malformedShippingAddress&#x60;\&quot; - \&quot;&#x60;other&#x60;\&quot; - \&quot;&#x60;productArrivedDamaged&#x60;\&quot; - \&quot;&#x60;productNotAsDescribed&#x60;\&quot; - \&quot;&#x60;qualityNotAsExpected&#x60;\&quot; - \&quot;&#x60;undeliverableShippingAddress&#x60;\&quot; - \&quot;&#x60;unsupportedPoBoxAddress&#x60;\&quot; - \&quot;&#x60;wrongProductShipped&#x60;\&quot;  |  [optional] |
|**reasonText** | **String** | The explanation of the reason. |  [optional] |



