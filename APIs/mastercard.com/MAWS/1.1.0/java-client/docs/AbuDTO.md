

# AbuDTO


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**discretionaryData** | **String** | Optional data that can be used by the requested for matching to the original inquiry. |  [optional] |
|**ica** | **String** | &lt;p class&#x3D;&#39;suffix-required&#39; style&#x3D;&#39;margin-bottom:5px&#39;&gt;[This field is required when the multiple ICAs are registered under the same client key.]&lt;/p&gt;Data that can be used to inform the ICA number: Interbank Card Association. |  [optional] |
|**merchantId** | **String** | Registered merchant ID that is mapped to the Customer ID. |  |
|**oldAccountNumber** | **String** | Account number on file provided by merchant. |  |
|**oldExpirationDate** | **String** | Account number expiration date on file provided by merchant that must be in MMYY format. |  |
|**subMerchantId** | **String** | Optionally populated when the merchant ID is actually a previously populated payment facilitator or payment aggregator. |  [optional] |
|**subscribe** | **String** | &lt;p class&#x3D;\&quot;suffix-required\&quot; style&#x3D;\&quot;margin-bottom:5px\&quot;&gt;[Field used by Push Model only - REQUIRED]&lt;/p&gt;Optional data that can be used to subscribe, un-subscribe or query subscription status for PAN updates. Valid values are \&quot;subscribe\&quot;, \&quot;un-subscribe\&quot; and \&quot;query\&quot;. |  [optional] |



