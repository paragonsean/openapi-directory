

# GoogleAnalyticsAdminV1alphaConversionValues

Conversion value settings for a postback window for SKAdNetwork conversion value schema.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**coarseValue** | [**CoarseValueEnum**](#CoarseValueEnum) | Required. A coarse grained conversion value. This value is not guaranteed to be unique. |  [optional] |
|**displayName** | **String** | Display name of the SKAdNetwork conversion value. The max allowed display name length is 50 UTF-16 code units. |  [optional] |
|**eventMappings** | [**List&lt;GoogleAnalyticsAdminV1alphaEventMapping&gt;**](GoogleAnalyticsAdminV1alphaEventMapping.md) | Event conditions that must be met for this Conversion Value to be achieved. The conditions in this list are ANDed together. It must have minimum of 1 entry and maximum of 3 entries, if the postback window is enabled. |  [optional] |
|**fineValue** | **Integer** | The fine-grained conversion value. This is applicable only to the first postback window. Its valid values are [0,63], both inclusive. It must be set for postback window 1, and must not be set for postback window 2 &amp; 3. This value is not guaranteed to be unique. If the configuration for the first postback window is re-used for second or third postback windows this field has no effect. |  [optional] |
|**lockEnabled** | **Boolean** | If true, the SDK should lock to this conversion value for the current postback window. |  [optional] |



## Enum: CoarseValueEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;COARSE_VALUE_UNSPECIFIED&quot; |
| LOW | &quot;COARSE_VALUE_LOW&quot; |
| MEDIUM | &quot;COARSE_VALUE_MEDIUM&quot; |
| HIGH | &quot;COARSE_VALUE_HIGH&quot; |



