# AmazonPersonalizeEvents.Event

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**eventId** | **String** |  | [optional] 
**eventType** | **String** |  | 
**eventValue** | **Number** |  | [optional] 
**itemId** | **String** |  | [optional] 
**properties** | **Object** | &lt;p&gt;A string map of event-specific data that you might choose to record. For example, if a user rates a movie on your site, other than movie ID (&lt;code&gt;itemId&lt;/code&gt;) and rating (&lt;code&gt;eventValue&lt;/code&gt;) , you might also send the number of movie ratings made by the user.&lt;/p&gt; &lt;p&gt;Each item in the map consists of a key-value pair. For example,&lt;/p&gt; &lt;p&gt; &lt;code&gt;{\&quot;numberOfRatings\&quot;: \&quot;12\&quot;}&lt;/code&gt; &lt;/p&gt; &lt;p&gt;The keys use camel case names that match the fields in the Interactions schema. In the above example, the &lt;code&gt;numberOfRatings&lt;/code&gt; would match the &#39;NUMBER_OF_RATINGS&#39; field defined in the Interactions schema.&lt;/p&gt; | [optional] 
**sentAt** | **Date** |  | 
**recommendationId** | **String** |  | [optional] 
**impression** | **Array** |  | [optional] 
**metricAttribution** | [**EventMetricAttribution**](EventMetricAttribution.md) |  | [optional] 


