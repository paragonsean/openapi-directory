# MatchApi.AddMerchantMerchant

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | [**Address**](Address.md) |  | [optional] 
**altPhoneNumber** | **String** | The Business or Merchant&#39;s alternate phone number. | [optional] 
**cATFlag** | **String** | Cardholder-activated terminal indicator. | 
**comments** | **String** | Brief comments on why Merchant is added | [optional] 
**countrySubdivisionTaxId** | **String** | The Merchant&#39;s state tax ID; for the U.S region only. Return value will be hidden. | 
**dateClosed** | **String** | Date the agreement was terminated with the merchant | 
**dateOpened** | **String** | Date the merchant entered into agreement with the acquirer | 
**doingBusinessAsName** | **String** | The name used by a merchant that could be different from the legal name of the business. Such as Bait R Us instead of the legal name, The Bait Shop | [optional] 
**merchantCategory** | **String** | A classification code used in authorization, clearing, and other transactions or reports to identify the type of merchant. | 
**merchantId** | **String** | The identifier assigned to a merchant by an Acquirer. An Acquirer Id and Merchant Id combination must be unique. | 
**name** | **String** | The name of the Business which has been terminated. | 
**nationalTaxId** | **String** | The National tax ID or business registration number. Return value will be hidden. | [optional] 
**phoneNumber** | **String** | The Business or Merchant&#39;s phone number. | 
**principal** | [**Principal**](Principal.md) |  | [optional] 
**reasonCode** | **String** | A two digit numeric code indication why a particular merchant was terminated.  01   Account Data Compromise, 02   Common Points of Purchase, 03   Laundering, 04   Excessive Chargebacks, 05   Excessive Fraud, 06   Reserved for Future Use, 07   Fraud Conviction, 08   MasterCard Questionable Merchant Audit Program, 09   Bankruptcy/Liquidation/Insolvency, 10   Violation of MasterCard Standards, 11   Merchant collusion, 12   PCI Data Security Standard, Noncompliance, 13   Illegal Transactions, 14   Identity Theft | 
**serviceProvDBA** | **String** | The name of the service provider associated with the merchant listed in the MATCH. | [optional] 
**serviceProvLegal** | **String** | The name of the service provider associated with the merchant listed in the MATCH. | [optional] 
**url** | **[String]** |  | [optional] 


