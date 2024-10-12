# FrankieFinancialApi.ReportCreditReport

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**courtJudgements** | [**[CourtJudgement]**](CourtJudgement.md) | CreditorWatch aggregate data from courts around Australia to provide a summary of court actions against an entity. When available, details of the action include location, case number, state, plaintiff, nature of the claim, action type and dollar amount. | [optional] 
**creditEnquiries** | **Number** | Credit enquiries provide an indication of the number of times an entity&#39;s credit file has been accessed. | [optional] 
**insolvencyNotices** | [**[InsolvencyNotice]**](InsolvencyNotice.md) | Insolvency and other published notices are provided by ASIC. These published notices provide details on external administrations, winding up applications (voluntary or by a court) and proposed company deregistrations, amongst other things. The notices contain important contact details and dates for creditors. These notices are provided directly from the ASIC insolvency notices website. If you require further information, visit:     https://insolvencynotices.asic.gov.au. | [optional] 
**loans** | [**[Loan]**](Loan.md) |  | [optional] 
**mercantileEnquiries** | [**[MercantileEnquiry]**](MercantileEnquiry.md) | A Mercantile enquiry is an indication that a mercantile agency (or debt collection agency) has conducted an enquiry on this entity for the purpose of debt collection. | [optional] 
**paymentDefaults** | [**[PaymentDefault]**](PaymentDefault.md) | A default indicates that the debtor has failed to make a payment for goods or services. Payment Defaults are unique to CreditorWatch and  can have one of three statuses:    - outstanding   - partial payment   - settled.  | [optional] 


