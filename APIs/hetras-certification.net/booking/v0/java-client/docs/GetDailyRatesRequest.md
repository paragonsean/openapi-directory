

# GetDailyRatesRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**channelCode** | **String** | Define the channel code in order to look up the rates for. |  |
|**expand** | [**List&lt;ExpandEnum&gt;**](#List&lt;ExpandEnum&gt;) | Define the sections you want to expand and get informed about rates for. |  [optional] |
|**from** | **OffsetDateTime** | Define the first business day you would like to get availability numbers for. The day should not be in the past. |  |
|**hotelId** | **Integer** | Define the hotel id to request the availability for. |  |
|**ratePlanCodes** | **List&lt;String&gt;** | Define the codes of rate plans to show in the response. A list of comma &#39;,&#39; separated rate plan codes. |  [optional] |
|**to** | **OffsetDateTime** | Define the last business day you would like to get rates for (inclusive). The maximum time span between &lt;i&gt;&#39;From&#39;&lt;/i&gt; and &lt;i&gt;&#39;To&#39;&lt;/i&gt;              is limited to 365 days. This can&#39;t be less than the &#39;From&#39; date. |  |



## Enum: List&lt;ExpandEnum&gt;

| Name | Value |
|---- | -----|
| NONE | &quot;None&quot; |
| POLICIES | &quot;Policies&quot; |
| RATE_PLANS | &quot;RatePlans&quot; |



