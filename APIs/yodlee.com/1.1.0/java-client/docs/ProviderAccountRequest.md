

# ProviderAccountRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**aggregationSource** | [**AggregationSourceEnum**](#AggregationSourceEnum) |  |  [optional] |
|**consentId** | **Long** | Consent Id generated for the request through POST Consent.&lt;br&gt;&lt;br&gt;&lt;b&gt;Endpoints&lt;/b&gt;:&lt;ul&gt;&lt;li&gt;POST Provider Account&lt;/li&gt;&lt;li&gt;PUT Provider Account&lt;/li&gt;&lt;/ul&gt; |  [optional] |
|**dataset** | [**List&lt;ProvidersDataset&gt;**](ProvidersDataset.md) |  |  [optional] |
|**datasetName** | [**List&lt;DatasetNameEnum&gt;**](#List&lt;DatasetNameEnum&gt;) |  |  [optional] |
|**field** | [**List&lt;Field&gt;**](Field.md) |  |  |
|**preferences** | [**ProviderAccountPreferences**](ProviderAccountPreferences.md) |  |  [optional] |



## Enum: AggregationSourceEnum

| Name | Value |
|---- | -----|
| SYSTEM | &quot;SYSTEM&quot; |
| USER | &quot;USER&quot; |



## Enum: List&lt;DatasetNameEnum&gt;

| Name | Value |
|---- | -----|
| BASIC_AGG_DATA | &quot;BASIC_AGG_DATA&quot; |
| ADVANCE_AGG_DATA | &quot;ADVANCE_AGG_DATA&quot; |
| ACCT_PROFILE | &quot;ACCT_PROFILE&quot; |
| DOCUMENT | &quot;DOCUMENT&quot; |



