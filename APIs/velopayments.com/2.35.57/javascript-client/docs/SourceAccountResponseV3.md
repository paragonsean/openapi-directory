# VeloPaymentsApis.SourceAccountResponseV3

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**autoTopUpConfig** | [**AutoTopUpConfigV3**](AutoTopUpConfigV3.md) |  | [optional] 
**balance** | **Number** | Decimal implied | [optional] 
**country** | **String** | Valid ISO 3166 2 character country code. See the &lt;a href&#x3D;\&quot;https://www.iso.org/iso-3166-country-codes.html\&quot; target&#x3D;\&quot;_blank\&quot; a&gt;ISO specification&lt;/a&gt; for details. | [optional] 
**currency** | **String** | Valid ISO 4217 3 letter currency code. See the &lt;a href&#x3D;\&quot;https://www.iso.org/iso-4217-currency-codes.html\&quot; target&#x3D;\&quot;_blank\&quot; a&gt;ISO specification&lt;/a&gt; for details. | [optional] 
**customerId** | **String** |  | [optional] 
**deleted** | **Boolean** | An optional flag for whether the source account has been deleted. Only present in the response if true. | [optional] 
**deletedAt** | **Date** | An optional timestamp when the source account has been deleted. Only present in the response if deleted. | [optional] 
**fundingRef** | **String** | The funding reference (will not be set for DECOUPLED accounts). | [optional] 
**id** | **String** | Source Account Id | 
**name** | **String** |  | [optional] 
**notifications** | [**NotificationsV3**](NotificationsV3.md) |  | [optional] 
**payorId** | **String** |  | [optional] 
**physicalAccountId** | **String** | The physical account id (will not be set for DECOUPLED accounts). | [optional] 
**physicalAccountName** | **String** | The physical account name (will not be set for DECOUPLED accounts). | [optional] 
**pooled** | **Boolean** | The pooled account flag (will not be set for DECOUPLED accounts). | [optional] 
**railsId** | **String** |  | 
**type** | **String** |  | 
**userDeleted** | **Boolean** | An optional flag for whether the source account has been deleted by a user. Only present in the response if true. | [optional] 


