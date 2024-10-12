# RealTimeBiddingApi.PolicyTopicEntry

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**evidences** | [**[PolicyTopicEvidence]**](PolicyTopicEvidence.md) | Pieces of evidence associated with this policy topic entry. | [optional] 
**helpCenterUrl** | **String** | URL of the help center article describing this policy topic. | [optional] 
**missingCertificate** | **Boolean** | Whether or not the policy topic is missing a certificate. Some policy topics require a certificate to unblock serving in some regions. For more information about creative certification, refer to: https://support.google.com/authorizedbuyers/answer/7450776 | [optional] 
**policyTopic** | **String** | Policy topic this entry refers to. For example, \&quot;ALCOHOL\&quot;, \&quot;TRADEMARKS_IN_AD_TEXT\&quot;, or \&quot;DESTINATION_NOT_WORKING\&quot;. The set of possible policy topics is not fixed for a particular API version and may change at any time. Can be used to filter the response of the creatives.list method | [optional] 


