# CampaignManager360Api.ReportFloodlightCriteriaReportProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**includeAttributedIPConversions** | **Boolean** | Include conversions that have no cookie, but do have an exposure path. | [optional] 
**includeUnattributedCookieConversions** | **Boolean** | Include conversions of users with a DoubleClick cookie but without an exposure. That means the user did not click or see an ad from the advertiser within the Floodlight group, or that the interaction happened outside the lookback window. | [optional] 
**includeUnattributedIPConversions** | **Boolean** | Include conversions that have no associated cookies and no exposures. It’s therefore impossible to know how the user was exposed to your ads during the lookback window prior to a conversion. | [optional] 


