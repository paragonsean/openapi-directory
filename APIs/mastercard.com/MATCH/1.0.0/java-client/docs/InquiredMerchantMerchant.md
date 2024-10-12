

# InquiredMerchantMerchant


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**addedByAcquirerID** | **String** | The Member ICA that has added the merchant to the MATCH system |  [optional] |
|**addedOnDate** | **String** | The date on which the merchant was added to the MATCH system. Format MM/DD/YYYY |  [optional] |
|**address** | [**Address**](Address.md) |  |  [optional] |
|**altPhoneNumber** | **String** | The Business or Merchant&#39;s alternate phone number. |  [optional] |
|**countrySubdivisionTaxId** | **String** | The Merchant&#39;s state tax ID; for the U.S region only. Return value will be hidden. |  [optional] |
|**doingBusinessAsName** | **String** | The name used by a merchant that could be different from the legal name of the business. Such as Bait R Us instead of the legal name, The Bait Shop |  [optional] |
|**merchantMatch** | [**MerchantMatch**](MerchantMatch.md) |  |  [optional] |
|**name** | **String** | The name of the Business which has been terminated. |  [optional] |
|**nationalTaxId** | **String** | The National tax ID or business registration number. Return value will be hidden. |  [optional] |
|**phoneNumber** | **String** | The Business or Merchant&#39;s phone number. |  [optional] |
|**principal** | [**Principal**](Principal.md) |  |  [optional] |
|**serviceProvDBA** | **String** | The name of the service provider associated with the merchant listed in the MATCH. |  [optional] |
|**serviceProvLegal** | **String** | The name of the service provider associated with the merchant listed in the MATCH. |  [optional] |
|**terminationReasonCode** | **String** | A two digit numeric code indication why a particular merchant was terminated.  01   Account Data Compromise, 02   Common Points of Purchase, 03   Laundering, 04   Excessive Chargebacks, 05   Excessive Fraud, 06   Reserved for Future Use, 07   Fraud Conviction, 08   MasterCard Questionable Merchant Audit Program, 09   Bankruptcy/Liquidation/Insolvency, 10   Violation of MasterCard Standards, 11   Merchant collusion, 12   PCI Data Security Standard, Noncompliance, 13   Illegal Transactions, 14   Identity Theft |  [optional] |
|**urlGroup** | [**UrlGroup**](UrlGroup.md) |  |  [optional] |



