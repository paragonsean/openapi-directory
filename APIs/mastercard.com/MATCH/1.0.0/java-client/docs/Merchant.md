

# Merchant


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**addedByAcquirerID** | **String** | The Member ICA that has added the merchant to the MATCH system |  [optional] |
|**addedOnDate** | **String** | Date the merchant was added to the MATCH database. |  [optional] |
|**address** | [**Address**](Address.md) |  |  [optional] |
|**altPhoneNumber** | **String** | The Business or Merchant&#39;s alternate phone number, including the area code. Within the USA, phone numbers have a length of 10, and for out outside the US, a max length of 25. Within the U.S. phone numbers can not start with 0 or 1. If the number is outside the U.S. region; do not include the country code. The number must be digits only, with no format characters such as parenthesis or dashes. |  [optional] |
|**countrySubdivisionTaxId** | **String** | The Merchant Country Subdivision tax ID, leave blank if not in the U.S region. |  [optional] |
|**doingBusinessAsName** | **String** | The name used by a merchant that could be different from the legal name of the business. Such as Bait R Us instead of the legal name, The Bait Shop. |  [optional] |
|**name** | **String** | The name of the business assigned by the principal owner(s) |  |
|**nationalTaxId** | **String** | The Merchant national tax ID, leave blank if not in the U.S region. |  [optional] |
|**phoneNumber** | **String** | The Business or Merchant&#39;s phone number, including the area code. Within the USA, phone numbers have a length of 10, and for outside the US, it can be any length with a maximum of 12 digits. Within the U.S. phone numbers can not start with 0 or 1. If the number is outside the U.S. region; do not include the country code. The phone number must be digits only, with no format characters such as parenthesis or dashes. |  [optional] |
|**principal** | [**List&lt;Principal&gt;**](Principal.md) | The details for the principal owner of the business.  A maximum of 5 principals may be submitted. |  [optional] |
|**searchCriteria** | [**SearchCriteria**](SearchCriteria.md) |  |  [optional] |
|**serviceProvDBA** | **String** | The name of the service provider associated with the merchant listed in the MATCH |  [optional] |
|**serviceProvLegal** | **String** | The name of the service provider associated with the merchant listed in the MATCH |  [optional] |
|**terminationReasonCode** | **String** | A two digit numeric code indication why a particular merchant was terminated.  01   Account Data Compromise, 02   Common Points of Purchase, 03   Laundering, 04   Excessive Chargebacks, 05   Excessive Fraud, 06   Reserved for Future Use, 07   Fraud Conviction, 08   MasterCard Questionable Merchant Audit Program, 09   Bankruptcy/Liquidation/Insolvency, 10   Violation of MasterCard Standards, 11   Merchant collusion, 12   PCI Data Security Standard, Noncompliance, 13   Illegal Transactions, 14   Identity Theft |  [optional] |
|**url** | **String** | Website address of the merchant. A request may include multiple URLs. The total cumulative size of the URLs cannot exceed 20,000 bytes. |  [optional] |
|**urlGroup** | [**List&lt;UrlGroup&gt;**](UrlGroup.md) |  |  [optional] |



