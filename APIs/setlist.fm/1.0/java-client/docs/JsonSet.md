

# JsonSet

A setlist consists of different (at least one) sets. Sets can either be sets as defined in the <a href=\"https://www.setlist.fm/guidelines\">Guidelines</a> or encores.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**encore** | **BigDecimal** | if the set is an encore, this is the number of the encore, starting with 1 for the first encore, 2 for the second and so on. |  [optional] |
|**name** | **String** | the description/name of the set. E.g. &lt;em&gt;&amp;quot;Acoustic set&amp;quot;&lt;/em&gt; or &lt;em&gt;&amp;quot;Paul McCartney solo&amp;quot;&lt;/em&gt; |  [optional] |
|**song** | [**List&lt;JsonSong&gt;**](JsonSong.md) | this set&#39;s songs |  [optional] |



