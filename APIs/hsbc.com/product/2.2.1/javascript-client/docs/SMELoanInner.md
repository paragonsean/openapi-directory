# ProductFinderApi.SMELoanInner

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identification** | **String** | The unique ID that has been internally assigned by the financial institution to each of the current account banking products they market to their retail and/or small to medium enterprise (SME) customers. | 
**name** | **String** | The name of the SME Loan product used for marketing purposes from a customer perspective. I.e. what the customer would recognise. | 
**otherSegment** | **Object** | Other segment code which is not available in the standard code set | [optional] 
**sMELoanMarketingState** | [**[SMELoanMarketingStateInner]**](SMELoanMarketingStateInner.md) | The marketing state (promotional or regular) of the SME Loan Product. | 
**segment** | **[String]** | Market segmentation is a marketing term referring to the aggregating of prospective buyers into groups, or segments, that have common needs and respond similarly to a marketing action. Market segmentation enables companies to target different categories of consumers who perceive the full value of certain products and services differently from one another.  Read more: Market Segmentation http://www.investopedia.com/terms/m/marketsegmentation.asp#ixzz4gfEEalTd  Follow us: Investopedia on Facebook  With respect to SME Loan products, they are segmented in relation to different markets that they wish to focus on. | 



## Enum: [SegmentEnum]


* `AgricultureSector` (value: `"AgricultureSector"`)

* `Business` (value: `"Business"`)

* `FlexibleBusinessLoan` (value: `"FlexibleBusinessLoan"`)

* `FixedGroup` (value: `"FixedGroup"`)

* `GovernmentScheme` (value: `"GovernmentScheme"`)

* `Other` (value: `"Other"`)

* `SectorSpecific` (value: `"SectorSpecific"`)




