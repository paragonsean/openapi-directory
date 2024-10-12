# YodleeCoreApis.Attribute

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**container** | **[String]** | Containers for which the attributes are supported.&lt;br&gt;&lt;br&gt;&lt;b&gt;Endpoints&lt;/b&gt;:&lt;ul&gt;&lt;li&gt;GET providers&lt;/li&gt;&lt;li&gt;GET providers/{providerId}&lt;/li&gt;&lt;/ul&gt; | [optional] 
**containerAttributes** | [**ContainerAttributes**](ContainerAttributes.md) |  | [optional] 
**fromDate** | **String** | Applicable only to EBILLS and STATEMENTS attributes of DOCUMENT dataset.&lt;br&gt;&lt;br&gt;&lt;b&gt;Endpoints&lt;/b&gt;:&lt;ul&gt;&lt;li&gt;POST providerAccounts&lt;/li&gt;&lt;li&gt;PUT providerAccounts&lt;/li&gt;&lt;/ul&gt; | [optional] [readonly] 
**fromFinYear** | **String** | Applicable only to TAX attribute of DOCUMENT dataset.&lt;br&gt;&lt;br&gt;&lt;b&gt;Endpoints&lt;/b&gt;:&lt;ul&gt;&lt;li&gt;POST providerAccounts&lt;/li&gt;&lt;li&gt;PUT providerAccounts&lt;/li&gt;&lt;/ul&gt; | [optional] [readonly] 
**name** | **String** | Attributes that are supported for a dataset.&lt;br&gt;&lt;br&gt;&lt;b&gt;Endpoints&lt;/b&gt;:&lt;ul&gt;&lt;li&gt;GET providers&lt;/li&gt;&lt;li&gt;GET providers/{providerId}&lt;/li&gt;&lt;/ul&gt; | [optional] 
**toDate** | **String** | Applicable only to EBILLS and STATEMENTS attributes of DOCUMENT dataset.&lt;br&gt;&lt;br&gt;&lt;b&gt;Endpoints&lt;/b&gt;:&lt;ul&gt;&lt;li&gt;POST providerAccounts&lt;/li&gt;&lt;li&gt;PUT providerAccounts&lt;/li&gt;&lt;/ul&gt; | [optional] [readonly] 
**toFinYear** | **String** | Applicable only to TAX attribute of DOCUMENT dataset.&lt;br&gt;&lt;br&gt;&lt;b&gt;Endpoints&lt;/b&gt;:&lt;ul&gt;&lt;li&gt;POST providerAccounts&lt;/li&gt;&lt;li&gt;PUT providerAccounts&lt;/li&gt;&lt;/ul&gt; | [optional] [readonly] 



## Enum: [ContainerEnum]


* `bank` (value: `"bank"`)

* `creditCard` (value: `"creditCard"`)

* `investment` (value: `"investment"`)

* `insurance` (value: `"insurance"`)

* `loan` (value: `"loan"`)

* `reward` (value: `"reward"`)

* `realEstate` (value: `"realEstate"`)

* `otherAssets` (value: `"otherAssets"`)

* `otherLiabilities` (value: `"otherLiabilities"`)





## Enum: NameEnum


* `BASIC_ACCOUNT_INFO` (value: `"BASIC_ACCOUNT_INFO"`)

* `TRANSACTIONS` (value: `"TRANSACTIONS"`)

* `STATEMENTS` (value: `"STATEMENTS"`)

* `HOLDINGS` (value: `"HOLDINGS"`)

* `ACCOUNT_DETAILS` (value: `"ACCOUNT_DETAILS"`)

* `TAX` (value: `"TAX"`)

* `EBILLS` (value: `"EBILLS"`)

* `FULL_ACCT_NUMBER` (value: `"FULL_ACCT_NUMBER"`)

* `BANK_TRANSFER_CODE` (value: `"BANK_TRANSFER_CODE"`)

* `HOLDER_NAME` (value: `"HOLDER_NAME"`)

* `HOLDER_DETAILS` (value: `"HOLDER_DETAILS"`)

* `PAYMENT_PROFILE` (value: `"PAYMENT_PROFILE"`)

* `PAYMENT_DETAILS` (value: `"PAYMENT_DETAILS"`)

* `INTEREST_DETAILS` (value: `"INTEREST_DETAILS"`)

* `COVERAGE` (value: `"COVERAGE"`)




