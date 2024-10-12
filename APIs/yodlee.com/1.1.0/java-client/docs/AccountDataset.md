

# AccountDataset


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**additionalStatus** | [**AdditionalStatusEnum**](#AdditionalStatusEnum) | The status of last update attempted for the dataset. &lt;br&gt;&lt;br&gt;&lt;b&gt;Account Type&lt;/b&gt;: Aggregated&lt;br&gt;&lt;b&gt;Endpoints&lt;/b&gt;:&lt;ul&gt;&lt;li&gt;GET accounts&lt;/li&gt;&lt;li&gt;GET accounts/{accountId}&lt;/li&gt;&lt;li&gt;GET providerAccounts&lt;/li&gt;&lt;li&gt;POST providerAccounts&lt;/li&gt;&lt;li&gt;PUT providerAccounts/{providerAccountId}&lt;/li&gt;&lt;li&gt;GET providerAccounts/{providerAccountId}&lt;/li&gt;&lt;/ul&gt;&lt;b&gt;Applicable Values&lt;/b&gt;&lt;br&gt; |  [optional] [readonly] |
|**lastUpdateAttempt** | **String** | Indicate when the last attempt was performed to update the dataset for the given provider account&lt;br&gt;&lt;br&gt;&lt;b&gt;Account Type&lt;/b&gt;: Aggregated&lt;br&gt;&lt;b&gt;Endpoints&lt;/b&gt;:&lt;ul&gt;&lt;li&gt;GET accounts&lt;/li&gt;&lt;li&gt;GET accounts/{accountId}&lt;/li&gt;&lt;li&gt;GET providerAccounts&lt;/li&gt;&lt;li&gt;POST providerAccounts&lt;/li&gt;&lt;li&gt;PUT providerAccounts/{providerAccountId}&lt;/li&gt;&lt;li&gt;GET providerAccounts/{providerAccountId}&lt;/li&gt;&lt;/ul&gt; |  [optional] [readonly] |
|**lastUpdated** | **String** | Indicate when the dataset is last updated successfully for the given provider account.&lt;br&gt;&lt;br&gt;&lt;b&gt;Account Type&lt;/b&gt;: Aggregated&lt;br&gt;&lt;b&gt;Endpoints&lt;/b&gt;:&lt;ul&gt;&lt;li&gt;GET accounts&lt;/li&gt;&lt;li&gt;GET accounts/{accountId}&lt;/li&gt;&lt;li&gt;GET providerAccounts&lt;/li&gt;&lt;li&gt;POST providerAccounts&lt;/li&gt;&lt;li&gt;PUT providerAccounts/{providerAccountId}&lt;/li&gt;&lt;li&gt;GET providerAccounts/{providerAccountId}&lt;/li&gt;&lt;/ul&gt; |  [optional] [readonly] |
|**name** | [**NameEnum**](#NameEnum) | The name of the dataset requested from the provider site&lt;br&gt;&lt;br&gt;&lt;b&gt;Account Type&lt;/b&gt;: Manual&lt;br&gt;&lt;b&gt;Endpoints&lt;/b&gt;:&lt;ul&gt;&lt;li&gt;GET accounts&lt;/li&gt;&lt;li&gt;GET accounts/{accountId}&lt;/li&gt;&lt;li&gt;GET providerAccounts&lt;/li&gt;&lt;li&gt;POST providerAccounts&lt;/li&gt;&lt;li&gt;PUT providerAccounts/{providerAccountId}&lt;/li&gt;&lt;li&gt;GET providerAccounts/{providerAccountId}&lt;/li&gt;&lt;li&gt;GET providers/{providerId}&lt;/li&gt;&lt;li&gt;GET providers&lt;/li&gt;&lt;/ul&gt;&lt;b&gt;Applicable Values&lt;/b&gt;&lt;br&gt; |  [optional] |
|**nextUpdateScheduled** | **String** | Indicates when the next attempt to update the dataset is scheduled.&lt;br&gt;&lt;br&gt;&lt;b&gt;Account Type&lt;/b&gt;: Aggregated&lt;br&gt;&lt;b&gt;Endpoints&lt;/b&gt;:&lt;ul&gt;&lt;li&gt;GET accounts&lt;/li&gt;&lt;li&gt;GET accounts/{accountId}&lt;/li&gt;&lt;li&gt;GET providerAccounts&lt;/li&gt;&lt;li&gt;POST providerAccounts&lt;/li&gt;&lt;li&gt;PUT providerAccounts/{providerAccountId}&lt;/li&gt;&lt;li&gt;GET providerAccounts/{providerAccountId}&lt;/li&gt;&lt;/ul&gt; |  [optional] [readonly] |
|**updateEligibility** | [**UpdateEligibilityEnum**](#UpdateEligibilityEnum) | Indicate whether the dataset is eligible for update or not.&lt;br&gt;&lt;br&gt;&lt;b&gt;Account Type&lt;/b&gt;: Aggregated&lt;br&gt;&lt;b&gt;Endpoints&lt;/b&gt;:&lt;ul&gt;&lt;li&gt;GET accounts&lt;/li&gt;&lt;li&gt;GET accounts/{accountId}&lt;/li&gt;&lt;li&gt;GET providerAccounts&lt;/li&gt;&lt;li&gt;POST providerAccounts&lt;/li&gt;&lt;li&gt;PUT providerAccounts/{providerAccountId}&lt;/li&gt;&lt;li&gt;GET providerAccounts/{providerAccountId}&lt;/li&gt;&lt;/ul&gt;&lt;b&gt;Applicable Values&lt;/b&gt;&lt;br&gt; |  [optional] [readonly] |



## Enum: AdditionalStatusEnum

| Name | Value |
|---- | -----|
| LOGIN_IN_PROGRESS | &quot;LOGIN_IN_PROGRESS&quot; |
| DATA_RETRIEVAL_IN_PROGRESS | &quot;DATA_RETRIEVAL_IN_PROGRESS&quot; |
| ACCT_SUMMARY_RECEIVED | &quot;ACCT_SUMMARY_RECEIVED&quot; |
| AVAILABLE_DATA_RETRIEVED | &quot;AVAILABLE_DATA_RETRIEVED&quot; |
| PARTIAL_DATA_RETRIEVED | &quot;PARTIAL_DATA_RETRIEVED&quot; |
| DATA_RETRIEVAL_FAILED | &quot;DATA_RETRIEVAL_FAILED&quot; |
| DATA_NOT_AVAILABLE | &quot;DATA_NOT_AVAILABLE&quot; |
| ACCOUNT_LOCKED | &quot;ACCOUNT_LOCKED&quot; |
| ADDL_AUTHENTICATION_REQUIRED | &quot;ADDL_AUTHENTICATION_REQUIRED&quot; |
| BETA_SITE_DEV_IN_PROGRESS | &quot;BETA_SITE_DEV_IN_PROGRESS&quot; |
| CREDENTIALS_UPDATE_NEEDED | &quot;CREDENTIALS_UPDATE_NEEDED&quot; |
| INCORRECT_CREDENTIALS | &quot;INCORRECT_CREDENTIALS&quot; |
| PROPERTY_VALUE_NOT_AVAILABLE | &quot;PROPERTY_VALUE_NOT_AVAILABLE&quot; |
| INVALID_ADDL_INFO_PROVIDED | &quot;INVALID_ADDL_INFO_PROVIDED&quot; |
| REQUEST_TIME_OUT | &quot;REQUEST_TIME_OUT&quot; |
| SITE_BLOCKING_ERROR | &quot;SITE_BLOCKING_ERROR&quot; |
| UNEXPECTED_SITE_ERROR | &quot;UNEXPECTED_SITE_ERROR&quot; |
| SITE_NOT_SUPPORTED | &quot;SITE_NOT_SUPPORTED&quot; |
| SITE_UNAVAILABLE | &quot;SITE_UNAVAILABLE&quot; |
| TECH_ERROR | &quot;TECH_ERROR&quot; |
| USER_ACTION_NEEDED_AT_SITE | &quot;USER_ACTION_NEEDED_AT_SITE&quot; |
| SITE_SESSION_INVALIDATED | &quot;SITE_SESSION_INVALIDATED&quot; |
| NEW_AUTHENTICATION_REQUIRED | &quot;NEW_AUTHENTICATION_REQUIRED&quot; |
| DATASET_NOT_SUPPORTED | &quot;DATASET_NOT_SUPPORTED&quot; |
| ENROLLMENT_REQUIRED_FOR_DATASET | &quot;ENROLLMENT_REQUIRED_FOR_DATASET&quot; |
| CONSENT_REQUIRED | &quot;CONSENT_REQUIRED&quot; |
| CONSENT_EXPIRED | &quot;CONSENT_EXPIRED&quot; |
| CONSENT_REVOKED | &quot;CONSENT_REVOKED&quot; |
| INCORRECT_OAUTH_TOKEN | &quot;INCORRECT_OAUTH_TOKEN&quot; |
| MIGRATION_IN_PROGRESS | &quot;MIGRATION_IN_PROGRESS&quot; |



## Enum: NameEnum

| Name | Value |
|---- | -----|
| BASIC_AGG_DATA | &quot;BASIC_AGG_DATA&quot; |
| ADVANCE_AGG_DATA | &quot;ADVANCE_AGG_DATA&quot; |
| ACCT_PROFILE | &quot;ACCT_PROFILE&quot; |
| DOCUMENT | &quot;DOCUMENT&quot; |



## Enum: UpdateEligibilityEnum

| Name | Value |
|---- | -----|
| ALLOW_UPDATE | &quot;ALLOW_UPDATE&quot; |
| ALLOW_UPDATE_WITH_CREDENTIALS | &quot;ALLOW_UPDATE_WITH_CREDENTIALS&quot; |
| DISALLOW_UPDATE | &quot;DISALLOW_UPDATE&quot; |



