

# Event

Represents user interaction event information sent using the <code>PutEvents</code> API.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**eventId** | [**String**](String.md) |  |  [optional] |
|**eventType** | [**String**](String.md) |  |  |
|**eventValue** | [**Float**](Float.md) |  |  [optional] |
|**itemId** | [**String**](String.md) |  |  [optional] |
|**properties** | **Object** | &lt;p&gt;A string map of event-specific data that you might choose to record. For example, if a user rates a movie on your site, other than movie ID (&lt;code&gt;itemId&lt;/code&gt;) and rating (&lt;code&gt;eventValue&lt;/code&gt;) , you might also send the number of movie ratings made by the user.&lt;/p&gt; &lt;p&gt;Each item in the map consists of a key-value pair. For example,&lt;/p&gt; &lt;p&gt; &lt;code&gt;{\&quot;numberOfRatings\&quot;: \&quot;12\&quot;}&lt;/code&gt; &lt;/p&gt; &lt;p&gt;The keys use camel case names that match the fields in the Interactions schema. In the above example, the &lt;code&gt;numberOfRatings&lt;/code&gt; would match the &#39;NUMBER_OF_RATINGS&#39; field defined in the Interactions schema.&lt;/p&gt; |  [optional] |
|**sentAt** | [**OffsetDateTime**](OffsetDateTime.md) |  |  |
|**recommendationId** | [**String**](String.md) |  |  [optional] |
|**impression** | [**List**](List.md) |  |  [optional] |
|**metricAttribution** | [**EventMetricAttribution**](EventMetricAttribution.md) |  |  [optional] |



