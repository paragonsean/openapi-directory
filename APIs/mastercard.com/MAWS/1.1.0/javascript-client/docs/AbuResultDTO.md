# MasterCardAbuApi.AbuResultDTO

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**discretionaryData** | **String** | Discretionary data as in the request. | [optional] 
**ica** | **String** | ICA number as in the request. | [optional] 
**merchantId** | **String** | Merchant ID as in the request. | [optional] 
**newAccountNumber** | **String** | New account number. | [optional] 
**newExpirationDate** | **String** | New account number expiration date, in MMYY format. | [optional] 
**oldAccountNumber** | **String** | Account number on file as in the request. | [optional] 
**oldExpirationDate** | **String** | Expiration date on file as in the request. | [optional] 
**reasonIdentifier** | **String** | Response Type based on requested account. | [optional] 
**responseIndicator** | **String** | One character additional data, returned bases on  reasonIdentifier.(Note- ResponseIndicator displayed only when ReasonIdentifier is VALID or UNKNWN) | [optional] 
**subMerchantId** | **String** | SubMerchantID as in the request. | [optional] 
**subscriptionIdentifier** | **String** | &lt;p class&#x3D;\&quot;suffix-required\&quot; style&#x3D;\&quot;margin-bottom:5px\&quot;&gt;[Field used by Push Model only]&lt;/p&gt; Response Type based on the status of subscribe/un-subscribe or query subscription status for PAN. | [optional] 
**subscriptionIndicator** | **String** | &lt;p class&#x3D;\&quot;suffix-required\&quot; style&#x3D;\&quot;margin-bottom:5px\&quot;&gt;[Field used by Push Model only]&lt;/p&gt; One character additional data, returned based on subscriptionIdentifier:&lt;ul&gt;&lt;li&gt;\&quot;S\&quot; for success&lt;/li&gt;&lt;li&gt;\&quot;F\&quot; for failures&lt;/li&gt;&lt;li&gt;\&quot;T\&quot; for token results.&lt;/li&gt;&lt;/ul&gt; | [optional] 


