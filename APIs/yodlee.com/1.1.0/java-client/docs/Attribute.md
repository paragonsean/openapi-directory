

# Attribute


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**container** | [**List&lt;ContainerEnum&gt;**](#List&lt;ContainerEnum&gt;) | Containers for which the attributes are supported.&lt;br&gt;&lt;br&gt;&lt;b&gt;Endpoints&lt;/b&gt;:&lt;ul&gt;&lt;li&gt;GET providers&lt;/li&gt;&lt;li&gt;GET providers/{providerId}&lt;/li&gt;&lt;/ul&gt; |  [optional] |
|**containerAttributes** | [**ContainerAttributes**](ContainerAttributes.md) |  |  [optional] |
|**fromDate** | **String** | Applicable only to EBILLS and STATEMENTS attributes of DOCUMENT dataset.&lt;br&gt;&lt;br&gt;&lt;b&gt;Endpoints&lt;/b&gt;:&lt;ul&gt;&lt;li&gt;POST providerAccounts&lt;/li&gt;&lt;li&gt;PUT providerAccounts&lt;/li&gt;&lt;/ul&gt; |  [optional] [readonly] |
|**fromFinYear** | **String** | Applicable only to TAX attribute of DOCUMENT dataset.&lt;br&gt;&lt;br&gt;&lt;b&gt;Endpoints&lt;/b&gt;:&lt;ul&gt;&lt;li&gt;POST providerAccounts&lt;/li&gt;&lt;li&gt;PUT providerAccounts&lt;/li&gt;&lt;/ul&gt; |  [optional] [readonly] |
|**name** | [**NameEnum**](#NameEnum) | Attributes that are supported for a dataset.&lt;br&gt;&lt;br&gt;&lt;b&gt;Endpoints&lt;/b&gt;:&lt;ul&gt;&lt;li&gt;GET providers&lt;/li&gt;&lt;li&gt;GET providers/{providerId}&lt;/li&gt;&lt;/ul&gt; |  [optional] |
|**toDate** | **String** | Applicable only to EBILLS and STATEMENTS attributes of DOCUMENT dataset.&lt;br&gt;&lt;br&gt;&lt;b&gt;Endpoints&lt;/b&gt;:&lt;ul&gt;&lt;li&gt;POST providerAccounts&lt;/li&gt;&lt;li&gt;PUT providerAccounts&lt;/li&gt;&lt;/ul&gt; |  [optional] [readonly] |
|**toFinYear** | **String** | Applicable only to TAX attribute of DOCUMENT dataset.&lt;br&gt;&lt;br&gt;&lt;b&gt;Endpoints&lt;/b&gt;:&lt;ul&gt;&lt;li&gt;POST providerAccounts&lt;/li&gt;&lt;li&gt;PUT providerAccounts&lt;/li&gt;&lt;/ul&gt; |  [optional] [readonly] |



## Enum: List&lt;ContainerEnum&gt;

| Name | Value |
|---- | -----|
| BANK | &quot;bank&quot; |
| CREDIT_CARD | &quot;creditCard&quot; |
| INVESTMENT | &quot;investment&quot; |
| INSURANCE | &quot;insurance&quot; |
| LOAN | &quot;loan&quot; |
| REWARD | &quot;reward&quot; |
| REAL_ESTATE | &quot;realEstate&quot; |
| OTHER_ASSETS | &quot;otherAssets&quot; |
| OTHER_LIABILITIES | &quot;otherLiabilities&quot; |



## Enum: NameEnum

| Name | Value |
|---- | -----|
| BASIC_ACCOUNT_INFO | &quot;BASIC_ACCOUNT_INFO&quot; |
| TRANSACTIONS | &quot;TRANSACTIONS&quot; |
| STATEMENTS | &quot;STATEMENTS&quot; |
| HOLDINGS | &quot;HOLDINGS&quot; |
| ACCOUNT_DETAILS | &quot;ACCOUNT_DETAILS&quot; |
| TAX | &quot;TAX&quot; |
| EBILLS | &quot;EBILLS&quot; |
| FULL_ACCT_NUMBER | &quot;FULL_ACCT_NUMBER&quot; |
| BANK_TRANSFER_CODE | &quot;BANK_TRANSFER_CODE&quot; |
| HOLDER_NAME | &quot;HOLDER_NAME&quot; |
| HOLDER_DETAILS | &quot;HOLDER_DETAILS&quot; |
| PAYMENT_PROFILE | &quot;PAYMENT_PROFILE&quot; |
| PAYMENT_DETAILS | &quot;PAYMENT_DETAILS&quot; |
| INTEREST_DETAILS | &quot;INTEREST_DETAILS&quot; |
| COVERAGE | &quot;COVERAGE&quot; |



