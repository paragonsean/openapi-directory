

# AccountHolder


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**gender** | **String** | Identifiers of the account holder.&lt;br&gt;&lt;br&gt;&lt;b&gt;Aggregated / Manual&lt;/b&gt;: Aggregated &lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;: bank&lt;br&gt;&lt;b&gt;Endpoints&lt;/b&gt;:&lt;ul&gt;&lt;li&gt;GET accounts&lt;/li&gt;&lt;li&gt;GET accounts/{accountId}&lt;/li&gt;&lt;/ul&gt; |  [optional] [readonly] |
|**identifier** | [**List&lt;Identifier&gt;**](Identifier.md) | Identifiers of the account holder.&lt;br&gt;&lt;br&gt;&lt;b&gt;Aggregated / Manual&lt;/b&gt;: Aggregated &lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;: bank&lt;br&gt;&lt;b&gt;Endpoints&lt;/b&gt;:&lt;ul&gt;&lt;li&gt;GET accounts&lt;/li&gt;&lt;li&gt;GET accounts/{accountId}&lt;/li&gt;&lt;/ul&gt; |  [optional] [readonly] |
|**name** | [**Name**](Name.md) |  |  [optional] |
|**ownership** | [**OwnershipEnum**](#OwnershipEnum) | Indicates the ownership of the account.&lt;br&gt;&lt;br&gt;&lt;b&gt;Aggregated / Manual&lt;/b&gt;: Aggregated &lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;: bank&lt;br&gt;&lt;b&gt;Endpoints&lt;/b&gt;:&lt;ul&gt;&lt;li&gt;GET accounts&lt;/li&gt;&lt;li&gt;GET accounts/{accountId}&lt;/li&gt;&lt;/ul&gt;&lt;b&gt;Applicable Values&lt;/b&gt;&lt;br&gt; |  [optional] [readonly] |



## Enum: OwnershipEnum

| Name | Value |
|---- | -----|
| PRIMARY | &quot;PRIMARY&quot; |
| SECONDARY | &quot;SECONDARY&quot; |
| CUSTODIAN | &quot;CUSTODIAN&quot; |
| OTHERS | &quot;OTHERS&quot; |
| POWER_OF_ATTORNEY | &quot;POWER_OF_ATTORNEY&quot; |
| TRUSTEE | &quot;TRUSTEE&quot; |
| JOINT_OWNER | &quot;JOINT_OWNER&quot; |
| BENEFICIARY | &quot;BENEFICIARY&quot; |
| AAS | &quot;AAS&quot; |
| BUSINESS | &quot;BUSINESS&quot; |
| DBA | &quot;DBA&quot; |
| TRUST | &quot;TRUST&quot; |



