

# Datafeed

Datafeed configuration data.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**attributeLanguage** | **String** | The two-letter ISO 639-1 language in which the attributes are defined in the data feed. |  [optional] |
|**contentLanguage** | **String** | [DEPRECATED] Please use targets[].language instead. The two-letter ISO 639-1 language of the items in the feed. Must be a valid language for &#x60;targetCountry&#x60;. |  [optional] |
|**contentType** | **String** | Required. The type of data feed. For product inventory feeds, only feeds for local stores, not online stores, are supported. Acceptable values are: - \&quot;&#x60;local products&#x60;\&quot; - \&quot;&#x60;product inventory&#x60;\&quot; - \&quot;&#x60;products&#x60;\&quot;  |  [optional] |
|**fetchSchedule** | [**DatafeedFetchSchedule**](DatafeedFetchSchedule.md) |  |  [optional] |
|**fileName** | **String** | Required. The filename of the feed. All feeds must have a unique file name. |  [optional] |
|**format** | [**DatafeedFormat**](DatafeedFormat.md) |  |  [optional] |
|**id** | **String** | Required for update. The ID of the data feed. |  [optional] |
|**intendedDestinations** | **List&lt;String&gt;** | [DEPRECATED] Please use targets[].includedDestinations instead. The list of intended destinations (corresponds to checked check boxes in Merchant Center). |  [optional] |
|**kind** | **String** | Identifies what kind of resource this is. Value: the fixed string \&quot;&#x60;content#datafeed&#x60;\&quot; |  [optional] |
|**name** | **String** | Required for insert. A descriptive name of the data feed. |  [optional] |
|**targetCountry** | **String** | [DEPRECATED] Please use targets[].country instead. The country where the items in the feed will be included in the search index, represented as a CLDR territory code. |  [optional] |
|**targets** | [**List&lt;DatafeedTarget&gt;**](DatafeedTarget.md) | The targets this feed should apply to (country, language, destinations). |  [optional] |



