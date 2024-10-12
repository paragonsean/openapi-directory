# YodleeCoreApis.AutoRefresh

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**additionalStatus** | **String** | Indicates the reason for the status.&lt;br&gt;&lt;br&gt;&lt;b&gt;Endpoints&lt;/b&gt;:&lt;ul&gt;&lt;li&gt;GET accounts&lt;/li&gt;&lt;li&gt;GET accounts/{accountId}&lt;/li&gt;&lt;/ul&gt;&lt;b&gt;Applicable Values&lt;/b&gt;&lt;br&gt; | [optional] [readonly] 
**asOfDate** | **String** | Date on which the auto refresh status is determined.&lt;br&gt;&lt;br&gt;&lt;b&gt;Endpoints&lt;/b&gt;:&lt;ul&gt;&lt;li&gt;GET accounts&lt;/li&gt;&lt;li&gt;GET accounts/{accountId}&lt;/li&gt;&lt;/ul&gt; | [optional] [readonly] 
**status** | **String** | Indicates whether auto refresh is enabled or disabled.&lt;br&gt;&lt;br&gt;&lt;b&gt;Endpoints&lt;/b&gt;:&lt;ul&gt;&lt;li&gt;GET accounts&lt;/li&gt;&lt;li&gt;GET accounts/{accountId}&lt;/li&gt;&lt;/ul&gt;&lt;b&gt;Applicable Values&lt;/b&gt;&lt;br&gt; | [optional] [readonly] 



## Enum: AdditionalStatusEnum


* `SCHEDULED` (value: `"SCHEDULED"`)

* `TEMP_ERROR` (value: `"TEMP_ERROR"`)

* `SITE_BLOCKING` (value: `"SITE_BLOCKING"`)

* `SITE_NOT_SUPPORTED` (value: `"SITE_NOT_SUPPORTED"`)

* `REAL_TIME_MFA_REQUIRED` (value: `"REAL_TIME_MFA_REQUIRED"`)

* `USER_ACTION_REQUIRED` (value: `"USER_ACTION_REQUIRED"`)

* `UNSUBSCRIBED` (value: `"UNSUBSCRIBED"`)

* `MANUAL_ACCOUNT` (value: `"MANUAL_ACCOUNT"`)





## Enum: StatusEnum


* `ENABLED` (value: `"ENABLED"`)

* `DISABLED` (value: `"DISABLED"`)




