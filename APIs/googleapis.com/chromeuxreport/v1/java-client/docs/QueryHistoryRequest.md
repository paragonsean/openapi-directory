

# QueryHistoryRequest

Request payload sent by a physical web client. This request includes all necessary context to load a particular user experience history record.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**formFactor** | [**FormFactorEnum**](#FormFactorEnum) | The form factor is a query dimension that specifies the device class that the record&#39;s data should belong to. Note: If no form factor is specified, then a special record with aggregated data over all form factors will be returned. |  [optional] |
|**metrics** | **List&lt;String&gt;** | The metrics that should be included in the response. If none are specified then any metrics found will be returned. Allowed values: [\&quot;first_contentful_paint\&quot;, \&quot;first_input_delay\&quot;, \&quot;largest_contentful_paint\&quot;, \&quot;cumulative_layout_shift\&quot;, \&quot;experimental_time_to_first_byte\&quot;, \&quot;experimental_interaction_to_next_paint\&quot;] |  [optional] |
|**origin** | **String** | The url pattern \&quot;origin\&quot; refers to a url pattern that is the origin of a website. Examples: \&quot;https://example.com\&quot;, \&quot;https://cloud.google.com\&quot; |  [optional] |
|**url** | **String** | The url pattern \&quot;url\&quot; refers to a url pattern that is any arbitrary url. Examples: \&quot;https://example.com/\&quot;, \&quot;https://cloud.google.com/why-google-cloud/\&quot; |  [optional] |



## Enum: FormFactorEnum

| Name | Value |
|---- | -----|
| ALL_FORM_FACTORS | &quot;ALL_FORM_FACTORS&quot; |
| PHONE | &quot;PHONE&quot; |
| DESKTOP | &quot;DESKTOP&quot; |
| TABLET | &quot;TABLET&quot; |



