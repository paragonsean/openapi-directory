

# AccountQuotaValues



## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**noticeEnabled** | **Boolean** | Whether the system should email the account owner if the account storage exceeds the noticeThreshold value. Storage notice emails are sent no mo once per day. |  [optional] |
|**noticeThreshold** | **Integer** | Percent of account storage that would trigger a notice email. Must be a whole number between 70 and 100 (inclusive). |  [optional] |
|**transactionsNoticeEnabled** | **Boolean** | Whether the system should email the account owner if the daily transaction usage exceeds the transactionsNoticeThreshold value. Transaction notice emails are sent no more than once per day. |  [optional] |
|**transactionsNoticeThreshold** | **Integer** | Percent of daily transaction usage that would trigger a notice email. Must be a whole number between 70 and 100 (inclusive). |  [optional] |



