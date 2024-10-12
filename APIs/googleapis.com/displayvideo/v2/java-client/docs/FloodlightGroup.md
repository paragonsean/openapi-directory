

# FloodlightGroup

A single Floodlight group.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**activeViewConfig** | [**ActiveViewVideoViewabilityMetricConfig**](ActiveViewVideoViewabilityMetricConfig.md) |  |  [optional] |
|**customVariables** | **Map&lt;String, Object&gt;** | User-defined custom variables owned by the Floodlight group. Use custom Floodlight variables to create reporting data that is tailored to your unique business needs. Custom Floodlight variables use the keys &#x60;U1&#x3D;&#x60;, &#x60;U2&#x3D;&#x60;, and so on, and can take any values that you choose to pass to them. You can use them to track virtually any type of data that you collect about your customers, such as the genre of movie that a customer purchases, the country to which the item is shipped, and so on. Custom Floodlight variables may not be used to pass any data that could be used or recognized as personally identifiable information (PII). Example: &#x60;custom_variables { fields { \&quot;U1\&quot;: value { number_value: 123.4 }, \&quot;U2\&quot;: value { string_value: \&quot;MyVariable2\&quot; }, \&quot;U3\&quot;: value { string_value: \&quot;MyVariable3\&quot; } } }&#x60; Acceptable values for keys are \&quot;U1\&quot; through \&quot;U100\&quot;, inclusive. String values must be less than 64 characters long, and cannot contain the following characters: &#x60;\&quot;&lt;&gt;&#x60;. |  [optional] |
|**displayName** | **String** | Required. The display name of the Floodlight group. |  [optional] |
|**floodlightGroupId** | **String** | Output only. The unique ID of the Floodlight group. Assigned by the system. |  [optional] [readonly] |
|**lookbackWindow** | [**LookbackWindow**](LookbackWindow.md) |  |  [optional] |
|**name** | **String** | Output only. The resource name of the Floodlight group. |  [optional] [readonly] |
|**webTagType** | [**WebTagTypeEnum**](#WebTagTypeEnum) | Required. The web tag type enabled for the Floodlight group. |  [optional] |



## Enum: WebTagTypeEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;WEB_TAG_TYPE_UNSPECIFIED&quot; |
| NONE | &quot;WEB_TAG_TYPE_NONE&quot; |
| IMAGE | &quot;WEB_TAG_TYPE_IMAGE&quot; |
| DYNAMIC | &quot;WEB_TAG_TYPE_DYNAMIC&quot; |



