

# XmlNs0City

This class represents a city where Venues are located. Most of the original city data was taken from <a href=\"http://geonames.org/\">Geonames.org</a>.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**coords** | [**XmlNs0Coords**](XmlNs0Coords.md) |  |  [optional] |
|**country** | [**XmlNs0Country**](XmlNs0Country.md) |  |  [optional] |
|**id** | **String** | unique identifier |  [optional] |
|**name** | **String** | the city&#39;s name, depending on the language valid values are e.g. &lt;em&gt;&amp;quot;M&amp;uuml;chen&amp;quot;&lt;/em&gt; or &lt;em&gt;Munich&lt;/em&gt; |  [optional] |
|**state** | **String** | The name of city&#39;s state, e.g. &lt;em&gt;&amp;quot;Bavaria&amp;quot;&lt;/em&gt; or &lt;em&gt;&amp;quot;Florida&amp;quot;&lt;/em&gt; |  [optional] |
|**stateCode** | **String** | The code of the city&#39;s state. For most countries this is a two-digit numeric code, with which the state can be identified uniquely in the specific Country. The code can also be a String for other cities. Valid examples are &lt;em&gt;&amp;quot;CA&amp;quot;&lt;/em&gt; or &lt;em&gt;&amp;quot;02&amp;quot;&lt;/em&gt;  which in turn get uniquely identifiable when combined with the state&#39;s country:  &lt;em&gt;&amp;quot;US.CA&amp;quot;&lt;/em&gt; for California, United States or &lt;em&gt;&amp;quot;DE.02&amp;quot;&lt;/em&gt; for Bavaria, Germany  For a complete list of available states (that aren&#39;t necessarily used in this database) is available in &lt;a href&#x3D; \&quot;http://download.geonames.org/export/dump/admin1CodesASCII.txt\&quot;&gt;a textfile on geonames.org&lt;/a&gt;.  Note that this code is only unique combined with the city&#39;s Country. The code alone is &lt;strong&gt;not&lt;/strong&gt; unique. |  [optional] |



