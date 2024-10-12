# YodleeCoreApis.AccountDataset

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**additionalStatus** | **String** | The status of last update attempted for the dataset. &lt;br&gt;&lt;br&gt;&lt;b&gt;Account Type&lt;/b&gt;: Aggregated&lt;br&gt;&lt;b&gt;Endpoints&lt;/b&gt;:&lt;ul&gt;&lt;li&gt;GET accounts&lt;/li&gt;&lt;li&gt;GET accounts/{accountId}&lt;/li&gt;&lt;li&gt;GET providerAccounts&lt;/li&gt;&lt;li&gt;POST providerAccounts&lt;/li&gt;&lt;li&gt;PUT providerAccounts/{providerAccountId}&lt;/li&gt;&lt;li&gt;GET providerAccounts/{providerAccountId}&lt;/li&gt;&lt;/ul&gt;&lt;b&gt;Applicable Values&lt;/b&gt;&lt;br&gt; | [optional] [readonly] 
**lastUpdateAttempt** | **String** | Indicate when the last attempt was performed to update the dataset for the given provider account&lt;br&gt;&lt;br&gt;&lt;b&gt;Account Type&lt;/b&gt;: Aggregated&lt;br&gt;&lt;b&gt;Endpoints&lt;/b&gt;:&lt;ul&gt;&lt;li&gt;GET accounts&lt;/li&gt;&lt;li&gt;GET accounts/{accountId}&lt;/li&gt;&lt;li&gt;GET providerAccounts&lt;/li&gt;&lt;li&gt;POST providerAccounts&lt;/li&gt;&lt;li&gt;PUT providerAccounts/{providerAccountId}&lt;/li&gt;&lt;li&gt;GET providerAccounts/{providerAccountId}&lt;/li&gt;&lt;/ul&gt; | [optional] [readonly] 
**lastUpdated** | **String** | Indicate when the dataset is last updated successfully for the given provider account.&lt;br&gt;&lt;br&gt;&lt;b&gt;Account Type&lt;/b&gt;: Aggregated&lt;br&gt;&lt;b&gt;Endpoints&lt;/b&gt;:&lt;ul&gt;&lt;li&gt;GET accounts&lt;/li&gt;&lt;li&gt;GET accounts/{accountId}&lt;/li&gt;&lt;li&gt;GET providerAccounts&lt;/li&gt;&lt;li&gt;POST providerAccounts&lt;/li&gt;&lt;li&gt;PUT providerAccounts/{providerAccountId}&lt;/li&gt;&lt;li&gt;GET providerAccounts/{providerAccountId}&lt;/li&gt;&lt;/ul&gt; | [optional] [readonly] 
**name** | **String** | The name of the dataset requested from the provider site&lt;br&gt;&lt;br&gt;&lt;b&gt;Account Type&lt;/b&gt;: Manual&lt;br&gt;&lt;b&gt;Endpoints&lt;/b&gt;:&lt;ul&gt;&lt;li&gt;GET accounts&lt;/li&gt;&lt;li&gt;GET accounts/{accountId}&lt;/li&gt;&lt;li&gt;GET providerAccounts&lt;/li&gt;&lt;li&gt;POST providerAccounts&lt;/li&gt;&lt;li&gt;PUT providerAccounts/{providerAccountId}&lt;/li&gt;&lt;li&gt;GET providerAccounts/{providerAccountId}&lt;/li&gt;&lt;li&gt;GET providers/{providerId}&lt;/li&gt;&lt;li&gt;GET providers&lt;/li&gt;&lt;/ul&gt;&lt;b&gt;Applicable Values&lt;/b&gt;&lt;br&gt; | [optional] 
**nextUpdateScheduled** | **String** | Indicates when the next attempt to update the dataset is scheduled.&lt;br&gt;&lt;br&gt;&lt;b&gt;Account Type&lt;/b&gt;: Aggregated&lt;br&gt;&lt;b&gt;Endpoints&lt;/b&gt;:&lt;ul&gt;&lt;li&gt;GET accounts&lt;/li&gt;&lt;li&gt;GET accounts/{accountId}&lt;/li&gt;&lt;li&gt;GET providerAccounts&lt;/li&gt;&lt;li&gt;POST providerAccounts&lt;/li&gt;&lt;li&gt;PUT providerAccounts/{providerAccountId}&lt;/li&gt;&lt;li&gt;GET providerAccounts/{providerAccountId}&lt;/li&gt;&lt;/ul&gt; | [optional] [readonly] 
**updateEligibility** | **String** | Indicate whether the dataset is eligible for update or not.&lt;br&gt;&lt;br&gt;&lt;b&gt;Account Type&lt;/b&gt;: Aggregated&lt;br&gt;&lt;b&gt;Endpoints&lt;/b&gt;:&lt;ul&gt;&lt;li&gt;GET accounts&lt;/li&gt;&lt;li&gt;GET accounts/{accountId}&lt;/li&gt;&lt;li&gt;GET providerAccounts&lt;/li&gt;&lt;li&gt;POST providerAccounts&lt;/li&gt;&lt;li&gt;PUT providerAccounts/{providerAccountId}&lt;/li&gt;&lt;li&gt;GET providerAccounts/{providerAccountId}&lt;/li&gt;&lt;/ul&gt;&lt;b&gt;Applicable Values&lt;/b&gt;&lt;br&gt; | [optional] [readonly] 



## Enum: AdditionalStatusEnum


* `LOGIN_IN_PROGRESS` (value: `"LOGIN_IN_PROGRESS"`)

* `DATA_RETRIEVAL_IN_PROGRESS` (value: `"DATA_RETRIEVAL_IN_PROGRESS"`)

* `ACCT_SUMMARY_RECEIVED` (value: `"ACCT_SUMMARY_RECEIVED"`)

* `AVAILABLE_DATA_RETRIEVED` (value: `"AVAILABLE_DATA_RETRIEVED"`)

* `PARTIAL_DATA_RETRIEVED` (value: `"PARTIAL_DATA_RETRIEVED"`)

* `DATA_RETRIEVAL_FAILED` (value: `"DATA_RETRIEVAL_FAILED"`)

* `DATA_NOT_AVAILABLE` (value: `"DATA_NOT_AVAILABLE"`)

* `ACCOUNT_LOCKED` (value: `"ACCOUNT_LOCKED"`)

* `ADDL_AUTHENTICATION_REQUIRED` (value: `"ADDL_AUTHENTICATION_REQUIRED"`)

* `BETA_SITE_DEV_IN_PROGRESS` (value: `"BETA_SITE_DEV_IN_PROGRESS"`)

* `CREDENTIALS_UPDATE_NEEDED` (value: `"CREDENTIALS_UPDATE_NEEDED"`)

* `INCORRECT_CREDENTIALS` (value: `"INCORRECT_CREDENTIALS"`)

* `PROPERTY_VALUE_NOT_AVAILABLE` (value: `"PROPERTY_VALUE_NOT_AVAILABLE"`)

* `INVALID_ADDL_INFO_PROVIDED` (value: `"INVALID_ADDL_INFO_PROVIDED"`)

* `REQUEST_TIME_OUT` (value: `"REQUEST_TIME_OUT"`)

* `SITE_BLOCKING_ERROR` (value: `"SITE_BLOCKING_ERROR"`)

* `UNEXPECTED_SITE_ERROR` (value: `"UNEXPECTED_SITE_ERROR"`)

* `SITE_NOT_SUPPORTED` (value: `"SITE_NOT_SUPPORTED"`)

* `SITE_UNAVAILABLE` (value: `"SITE_UNAVAILABLE"`)

* `TECH_ERROR` (value: `"TECH_ERROR"`)

* `USER_ACTION_NEEDED_AT_SITE` (value: `"USER_ACTION_NEEDED_AT_SITE"`)

* `SITE_SESSION_INVALIDATED` (value: `"SITE_SESSION_INVALIDATED"`)

* `NEW_AUTHENTICATION_REQUIRED` (value: `"NEW_AUTHENTICATION_REQUIRED"`)

* `DATASET_NOT_SUPPORTED` (value: `"DATASET_NOT_SUPPORTED"`)

* `ENROLLMENT_REQUIRED_FOR_DATASET` (value: `"ENROLLMENT_REQUIRED_FOR_DATASET"`)

* `CONSENT_REQUIRED` (value: `"CONSENT_REQUIRED"`)

* `CONSENT_EXPIRED` (value: `"CONSENT_EXPIRED"`)

* `CONSENT_REVOKED` (value: `"CONSENT_REVOKED"`)

* `INCORRECT_OAUTH_TOKEN` (value: `"INCORRECT_OAUTH_TOKEN"`)

* `MIGRATION_IN_PROGRESS` (value: `"MIGRATION_IN_PROGRESS"`)





## Enum: NameEnum


* `BASIC_AGG_DATA` (value: `"BASIC_AGG_DATA"`)

* `ADVANCE_AGG_DATA` (value: `"ADVANCE_AGG_DATA"`)

* `ACCT_PROFILE` (value: `"ACCT_PROFILE"`)

* `DOCUMENT` (value: `"DOCUMENT"`)





## Enum: UpdateEligibilityEnum


* `ALLOW_UPDATE` (value: `"ALLOW_UPDATE"`)

* `ALLOW_UPDATE_WITH_CREDENTIALS` (value: `"ALLOW_UPDATE_WITH_CREDENTIALS"`)

* `DISALLOW_UPDATE` (value: `"DISALLOW_UPDATE"`)




