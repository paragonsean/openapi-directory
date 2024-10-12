# WowzaStreamingCloudRestApiReferenceDocumentation.TheNameOfTheRendition

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**countries** | [**[CountryObject]**](CountryObject.md) |  | [optional] 
**name** | **String** | The name of the rendition. | [optional] 
**percentageViewers** | **Number** | Total percentage of viewers (&lt;strong&gt;100&lt;/strong&gt;). | [optional] 
**percentageViewingTime** | **Number** | The percentage of total viewing time that the protocol or rendition was viewed. Always &lt;strong&gt;100&lt;/strong&gt; for &lt;em&gt;stream_target&lt;/em&gt;. | [optional] 
**protocols** | [**[ProtocolObject]**](ProtocolObject.md) |  | [optional] 
**secondsAvgViewingTime** | **Number** | The average length of time, in seconds, that viewers played the stream at the target. | [optional] 
**secondsTotalViewingTime** | **Number** | The total length of time, in seconds, that all viewers played the stream at the target. &lt;em&gt;seconds_total_viewing_time&lt;/em&gt; may be longer than the duration of the stream. | [optional] 
**totalUniqueViewers** | **Number** | The total number of unique viewers that downloaded at least one chunk of the stream at the target (for HTTP streams) or connected to and viewed the stream (for ultra low latency streams). A unique viewer is a single IP address; multiple users that share the same IP address are counted once. | [optional] 


