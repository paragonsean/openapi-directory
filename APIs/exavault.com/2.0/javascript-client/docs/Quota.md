# ExaVault.Quota

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bandwidthLimit** | **Number** | Total number of bytes that can be transferred per month. | [optional] 
**bandwidthUsed** | **Number** | Number of bytes transferred this month. | [optional] 
**diskLimit** | **Number** | Amount of disk space that the account has available to it. This may be increased by upgrading to a larger plan. | [optional] 
**diskUsed** | **Number** | Amount of disk space currently in use. | [optional] 
**noticeEnabled** | **Boolean** | Should a quota warning be sent to the account owner when a threshold level of space utilization is reached? | [optional] 
**noticeThreshold** | **Number** | Treshold that triggers a quota notification. This represents the \&quot;percent full\&quot; your account must be before the quota notification is generated. | [optional] 
**transactionsLimit** | **Number** | Total number of transactions allowed in a 24-hour period. | [optional] 
**transactionsNoticeEnabled** | **Boolean** | Whether an email should be sent to the account owner up to once per day if transaction usage exceeds &#x60;transactionsNoticeThreshold&#x60; value. | [optional] 
**transactionsNoticeThreshold** | **Number** | Percent of daily transactions limit that will trigger an email if activity exceeds it. | [optional] 


