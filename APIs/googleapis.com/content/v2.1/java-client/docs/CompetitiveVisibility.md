

# CompetitiveVisibility

Fields related to [competitive visibility reports] (https://support.google.com/merchants/answer/11366442).

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**adsOrganicRatio** | **Double** | [Ads / organic ratio] (https://support.google.com/merchants/answer/11366442#zippy&#x3D;%2Cadsfree-ratio) shows how often a merchant receives impressions from Shopping ads compared to organic traffic. The number is rounded and bucketed. Available only in &#x60;CompetitiveVisibilityTopMerchantView&#x60; and &#x60;CompetitiveVisibilityCompetitorView&#x60;. Cannot be filtered on in the &#39;WHERE&#39; clause. |  [optional] |
|**categoryBenchmarkVisibilityTrend** | **Double** | Change in visibility based on impressions with respect to the start of the selected time range (or first day with non-zero impressions) for a combined set of merchants with highest visibility approximating the market. Available only in &#x60;CompetitiveVisibilityBenchmarkView&#x60;. Cannot be filtered on in the &#39;WHERE&#39; clause. |  [optional] |
|**categoryId** | **String** | Google product category ID to calculate the report for, represented in [Google&#39;s product taxonomy](https://support.google.com/merchants/answer/6324436). Required in the &#x60;SELECT&#x60; clause. A &#x60;WHERE&#x60; condition on &#x60;competitive_visibility.category_id&#x60; is required in the query. |  [optional] |
|**countryCode** | **String** | The country where impression appeared. Required in the &#x60;SELECT&#x60; clause. A &#x60;WHERE&#x60; condition on &#x60;competitive_visibility.country_code&#x60; is required in the query. |  [optional] |
|**date** | [**Date**](Date.md) |  |  [optional] |
|**domain** | **String** | Domain of your competitor or your domain, if &#39;is_your_domain&#39; is true. Available only in &#x60;CompetitiveVisibilityTopMerchantView&#x60; and &#x60;CompetitiveVisibilityCompetitorView&#x60;. Required in the &#x60;SELECT&#x60; clause for &#x60;CompetitiveVisibilityTopMerchantView&#x60; and &#x60;CompetitiveVisibilityCompetitorView&#x60;. Cannot be filtered on in the &#39;WHERE&#39; clause. |  [optional] |
|**higherPositionRate** | **Double** | Higher position rate shows how often a competitor’s offer got placed in a higher position on the page than your offer. Available only in &#x60;CompetitiveVisibilityTopMerchantView&#x60; and &#x60;CompetitiveVisibilityCompetitorView&#x60;. Cannot be filtered on in the &#39;WHERE&#39; clause. |  [optional] |
|**isYourDomain** | **Boolean** | True if this row contains data for your domain. Available only in &#x60;CompetitiveVisibilityTopMerchantView&#x60; and &#x60;CompetitiveVisibilityCompetitorView&#x60;. Cannot be filtered on in the &#39;WHERE&#39; clause. |  [optional] |
|**pageOverlapRate** | **Double** | Page overlap rate describes how frequently competing retailers’ offers are shown together with your offers on the same page. Available only in &#x60;CompetitiveVisibilityTopMerchantView&#x60; and &#x60;CompetitiveVisibilityCompetitorView&#x60;. Cannot be filtered on in the &#39;WHERE&#39; clause. |  [optional] |
|**rank** | **String** | Position of the domain in the top merchants ranking for the selected keys (&#x60;date&#x60;, &#x60;category_id&#x60;, &#x60;country_code&#x60;, &#x60;listing_type&#x60;) based on impressions. 1 is the highest. Available only in &#x60;CompetitiveVisibilityTopMerchantView&#x60; and &#x60;CompetitiveVisibilityCompetitorView&#x60;. Cannot be filtered on in the &#39;WHERE&#39; clause. |  [optional] |
|**relativeVisibility** | **Double** | Relative visibility shows how often your competitors’ offers are shown compared to your offers. In other words, this is the number of displayed impressions of a competitor retailer divided by the number of your displayed impressions during a selected time range for a selected product category and country. Available only in &#x60;CompetitiveVisibilityCompetitorView&#x60;. Cannot be filtered on in the &#39;WHERE&#39; clause. |  [optional] |
|**trafficSource** | [**TrafficSourceEnum**](#TrafficSourceEnum) | Type of impression listing. Required in the &#x60;SELECT&#x60; clause. Cannot be filtered on in the &#39;WHERE&#39; clause. |  [optional] |
|**yourDomainVisibilityTrend** | **Double** | Change in visibility based on impressions for your domain with respect to the start of the selected time range (or first day with non-zero impressions). Available only in &#x60;CompetitiveVisibilityBenchmarkView&#x60;. Cannot be filtered on in the &#39;WHERE&#39; clause. |  [optional] |



## Enum: TrafficSourceEnum

| Name | Value |
|---- | -----|
| UNKNOWN | &quot;UNKNOWN&quot; |
| ORGANIC | &quot;ORGANIC&quot; |
| ADS | &quot;ADS&quot; |
| ALL | &quot;ALL&quot; |



