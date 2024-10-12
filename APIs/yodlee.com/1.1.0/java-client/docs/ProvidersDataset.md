

# ProvidersDataset


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**attribute** | [**List&lt;Attribute&gt;**](Attribute.md) | The name of the dataset attribute suported by the provider.&lt;br&gt;&lt;br&gt;&lt;b&gt;Endpoints&lt;/b&gt;:&lt;ul&gt;&lt;li&gt;GET providers/{providerId}&lt;/li&gt;&lt;li&gt;GET providers&lt;/li&gt;&lt;/ul&gt; |  [optional] |
|**name** | [**NameEnum**](#NameEnum) | The name of the dataset requested from the provider site&lt;br&gt;&lt;br&gt;&lt;b&gt;Account Type&lt;/b&gt;: Manual&lt;br&gt;&lt;b&gt;Endpoints&lt;/b&gt;:&lt;ul&gt;&lt;li&gt;GET accounts&lt;/li&gt;&lt;li&gt;GET accounts/{accountId}&lt;/li&gt;&lt;li&gt;GET providerAccounts&lt;/li&gt;&lt;li&gt;POST providerAccounts&lt;/li&gt;&lt;li&gt;PUT providerAccounts/{providerAccountId}&lt;/li&gt;&lt;li&gt;GET providerAccounts/{providerAccountId}&lt;/li&gt;&lt;li&gt;GET providers/{providerId}&lt;/li&gt;&lt;li&gt;GET providers&lt;/li&gt;&lt;/ul&gt;&lt;b&gt;Applicable Values&lt;/b&gt;&lt;br&gt; |  [optional] |



## Enum: NameEnum

| Name | Value |
|---- | -----|
| BASIC_AGG_DATA | &quot;BASIC_AGG_DATA&quot; |
| ADVANCE_AGG_DATA | &quot;ADVANCE_AGG_DATA&quot; |
| ACCT_PROFILE | &quot;ACCT_PROFILE&quot; |
| DOCUMENT | &quot;DOCUMENT&quot; |



