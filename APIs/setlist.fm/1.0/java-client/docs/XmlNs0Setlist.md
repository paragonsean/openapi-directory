

# XmlNs0Setlist

Setlists, that's what it's all about. So if you're trying to use this API without knowing what a setlist is then you're kinda wrong on this page ;-).  A setlist can be distinguished from other setlists by its unique id. But as <a href=\"https://www.setlist.fm/\">setlist.fm</a> works the wiki way, there can be different versions of one setlist (each time a user updates a setlist a new version gets created). These different versions have a unique id on its own. So setlists can have the same id although they differ as far as the content is concerned - thus the best way to check if two setlists are the same is to compare their versionIds.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**artist** | [**XmlNs0Artist**](XmlNs0Artist.md) |  |  [optional] |
|**eventDate** | **String** | date of the concert in the format &amp;quot;dd-MM-yyyy&amp;quot; |  [optional] |
|**id** | **String** | unique identifier |  [optional] |
|**info** | **String** | additional information on the concert - see the &lt;a href&#x3D;\&quot;https://www.setlist.fm/guidelines\&quot;&gt;setlist.fm guidelines&lt;/a&gt; for a complete list of allowed content. |  [optional] |
|**lastFmEventId** | **BigDecimal** | the id this event has on &lt;a href&#x3D;\&quot;http://last.fm/\&quot;&gt;last.fm&lt;/a&gt; (deprecated) |  [optional] |
|**lastUpdated** | **String** | date, time and time zone of the last update to this setlist in the format &amp;quot;yyyy-MM-dd&#39;T&#39;HH:mm:ss.SSSZZZZZ&amp;quot; |  [optional] |
|**set** | [**XmlNs0Set**](XmlNs0Set.md) |  |  [optional] |
|**tour** | [**XmlNs0Tour**](XmlNs0Tour.md) |  |  [optional] |
|**url** | **String** | the attribution url to which you have to link to wherever you use data from this setlist in your application |  [optional] |
|**venue** | [**XmlNs0Venue**](XmlNs0Venue.md) |  |  [optional] |
|**versionId** | **String** | unique identifier of the version |  [optional] |



