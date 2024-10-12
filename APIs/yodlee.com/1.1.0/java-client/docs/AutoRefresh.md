

# AutoRefresh


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**additionalStatus** | [**AdditionalStatusEnum**](#AdditionalStatusEnum) | Indicates the reason for the status.&lt;br&gt;&lt;br&gt;&lt;b&gt;Endpoints&lt;/b&gt;:&lt;ul&gt;&lt;li&gt;GET accounts&lt;/li&gt;&lt;li&gt;GET accounts/{accountId}&lt;/li&gt;&lt;/ul&gt;&lt;b&gt;Applicable Values&lt;/b&gt;&lt;br&gt; |  [optional] [readonly] |
|**asOfDate** | **String** | Date on which the auto refresh status is determined.&lt;br&gt;&lt;br&gt;&lt;b&gt;Endpoints&lt;/b&gt;:&lt;ul&gt;&lt;li&gt;GET accounts&lt;/li&gt;&lt;li&gt;GET accounts/{accountId}&lt;/li&gt;&lt;/ul&gt; |  [optional] [readonly] |
|**status** | [**StatusEnum**](#StatusEnum) | Indicates whether auto refresh is enabled or disabled.&lt;br&gt;&lt;br&gt;&lt;b&gt;Endpoints&lt;/b&gt;:&lt;ul&gt;&lt;li&gt;GET accounts&lt;/li&gt;&lt;li&gt;GET accounts/{accountId}&lt;/li&gt;&lt;/ul&gt;&lt;b&gt;Applicable Values&lt;/b&gt;&lt;br&gt; |  [optional] [readonly] |



## Enum: AdditionalStatusEnum

| Name | Value |
|---- | -----|
| SCHEDULED | &quot;SCHEDULED&quot; |
| TEMP_ERROR | &quot;TEMP_ERROR&quot; |
| SITE_BLOCKING | &quot;SITE_BLOCKING&quot; |
| SITE_NOT_SUPPORTED | &quot;SITE_NOT_SUPPORTED&quot; |
| REAL_TIME_MFA_REQUIRED | &quot;REAL_TIME_MFA_REQUIRED&quot; |
| USER_ACTION_REQUIRED | &quot;USER_ACTION_REQUIRED&quot; |
| UNSUBSCRIBED | &quot;UNSUBSCRIBED&quot; |
| MANUAL_ACCOUNT | &quot;MANUAL_ACCOUNT&quot; |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| ENABLED | &quot;ENABLED&quot; |
| DISABLED | &quot;DISABLED&quot; |



