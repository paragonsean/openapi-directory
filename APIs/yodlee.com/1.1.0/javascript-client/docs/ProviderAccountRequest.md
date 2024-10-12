# YodleeCoreApis.ProviderAccountRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aggregationSource** | **String** |  | [optional] 
**consentId** | **Number** | Consent Id generated for the request through POST Consent.&lt;br&gt;&lt;br&gt;&lt;b&gt;Endpoints&lt;/b&gt;:&lt;ul&gt;&lt;li&gt;POST Provider Account&lt;/li&gt;&lt;li&gt;PUT Provider Account&lt;/li&gt;&lt;/ul&gt; | [optional] 
**dataset** | [**[ProvidersDataset]**](ProvidersDataset.md) |  | [optional] 
**datasetName** | **[String]** |  | [optional] 
**field** | [**[Field]**](Field.md) |  | 
**preferences** | [**ProviderAccountPreferences**](ProviderAccountPreferences.md) |  | [optional] 



## Enum: AggregationSourceEnum


* `SYSTEM` (value: `"SYSTEM"`)

* `USER` (value: `"USER"`)





## Enum: [DatasetNameEnum]


* `BASIC_AGG_DATA` (value: `"BASIC_AGG_DATA"`)

* `ADVANCE_AGG_DATA` (value: `"ADVANCE_AGG_DATA"`)

* `ACCT_PROFILE` (value: `"ACCT_PROFILE"`)

* `DOCUMENT` (value: `"DOCUMENT"`)




