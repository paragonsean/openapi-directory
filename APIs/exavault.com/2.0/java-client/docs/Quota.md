

# Quota


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**bandwidthLimit** | **Long** | Total number of bytes that can be transferred per month. |  [optional] |
|**bandwidthUsed** | **Long** | Number of bytes transferred this month. |  [optional] |
|**diskLimit** | **Long** | Amount of disk space that the account has available to it. This may be increased by upgrading to a larger plan. |  [optional] |
|**diskUsed** | **Long** | Amount of disk space currently in use. |  [optional] |
|**noticeEnabled** | **Boolean** | Should a quota warning be sent to the account owner when a threshold level of space utilization is reached? |  [optional] |
|**noticeThreshold** | **Integer** | Treshold that triggers a quota notification. This represents the \&quot;percent full\&quot; your account must be before the quota notification is generated. |  [optional] |
|**transactionsLimit** | **Integer** | Total number of transactions allowed in a 24-hour period. |  [optional] |
|**transactionsNoticeEnabled** | **Boolean** | Whether an email should be sent to the account owner up to once per day if transaction usage exceeds &#x60;transactionsNoticeThreshold&#x60; value. |  [optional] |
|**transactionsNoticeThreshold** | **Integer** | Percent of daily transactions limit that will trigger an email if activity exceeds it. |  [optional] |



