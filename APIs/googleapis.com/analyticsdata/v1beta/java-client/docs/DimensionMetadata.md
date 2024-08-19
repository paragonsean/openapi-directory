

# DimensionMetadata

Explains a dimension.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**apiName** | **String** | This dimension&#39;s name. Useable in [Dimension](#Dimension)&#39;s &#x60;name&#x60;. For example, &#x60;eventName&#x60;. |  [optional] |
|**category** | **String** | The display name of the category that this dimension belongs to. Similar dimensions and metrics are categorized together. |  [optional] |
|**customDefinition** | **Boolean** | True if the dimension is custom to this property. This includes user, event, &amp; item scoped custom dimensions; to learn more about custom dimensions, see https://support.google.com/analytics/answer/14240153. This also include custom channel groups; to learn more about custom channel groups, see https://support.google.com/analytics/answer/13051316. |  [optional] |
|**deprecatedApiNames** | **List&lt;String&gt;** | Still usable but deprecated names for this dimension. If populated, this dimension is available by either &#x60;apiName&#x60; or one of &#x60;deprecatedApiNames&#x60; for a period of time. After the deprecation period, the dimension will be available only by &#x60;apiName&#x60;. |  [optional] |
|**description** | **String** | Description of how this dimension is used and calculated. |  [optional] |
|**uiName** | **String** | This dimension&#39;s name within the Google Analytics user interface. For example, &#x60;Event name&#x60;. |  [optional] |



