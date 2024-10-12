# YodleeCoreApis.AccountHolder

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gender** | **String** | Identifiers of the account holder.&lt;br&gt;&lt;br&gt;&lt;b&gt;Aggregated / Manual&lt;/b&gt;: Aggregated &lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;: bank&lt;br&gt;&lt;b&gt;Endpoints&lt;/b&gt;:&lt;ul&gt;&lt;li&gt;GET accounts&lt;/li&gt;&lt;li&gt;GET accounts/{accountId}&lt;/li&gt;&lt;/ul&gt; | [optional] [readonly] 
**identifier** | [**[Identifier]**](Identifier.md) | Identifiers of the account holder.&lt;br&gt;&lt;br&gt;&lt;b&gt;Aggregated / Manual&lt;/b&gt;: Aggregated &lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;: bank&lt;br&gt;&lt;b&gt;Endpoints&lt;/b&gt;:&lt;ul&gt;&lt;li&gt;GET accounts&lt;/li&gt;&lt;li&gt;GET accounts/{accountId}&lt;/li&gt;&lt;/ul&gt; | [optional] [readonly] 
**name** | [**Name**](Name.md) |  | [optional] 
**ownership** | **String** | Indicates the ownership of the account.&lt;br&gt;&lt;br&gt;&lt;b&gt;Aggregated / Manual&lt;/b&gt;: Aggregated &lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;: bank&lt;br&gt;&lt;b&gt;Endpoints&lt;/b&gt;:&lt;ul&gt;&lt;li&gt;GET accounts&lt;/li&gt;&lt;li&gt;GET accounts/{accountId}&lt;/li&gt;&lt;/ul&gt;&lt;b&gt;Applicable Values&lt;/b&gt;&lt;br&gt; | [optional] [readonly] 



## Enum: OwnershipEnum


* `PRIMARY` (value: `"PRIMARY"`)

* `SECONDARY` (value: `"SECONDARY"`)

* `CUSTODIAN` (value: `"CUSTODIAN"`)

* `OTHERS` (value: `"OTHERS"`)

* `POWER_OF_ATTORNEY` (value: `"POWER_OF_ATTORNEY"`)

* `TRUSTEE` (value: `"TRUSTEE"`)

* `JOINT_OWNER` (value: `"JOINT_OWNER"`)

* `BENEFICIARY` (value: `"BENEFICIARY"`)

* `AAS` (value: `"AAS"`)

* `BUSINESS` (value: `"BUSINESS"`)

* `DBA` (value: `"DBA"`)

* `TRUST` (value: `"TRUST"`)




