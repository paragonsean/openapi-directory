

# AudioItemLinks


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**action** | [**List&lt;OtherLink&gt;**](OtherLink.md) | One or more links to be trigged by user actions, usually when a button is clicked |  [optional] |
|**audio** | [**List&lt;AudioLink&gt;**](AudioLink.md) | One or more links to audio files for the item |  [optional] |
|**binge** | [**List&lt;OtherLink&gt;**](OtherLink.md) | One or more links that start a flow-based experience focused on the aggregation |  [optional] |
|**image** | [**List&lt;ImageLink&gt;**](ImageLink.md) | One or more links to an image, along with metadata for display |  [optional] |
|**onramps** | [**List&lt;OtherLink&gt;**](OtherLink.md) | One or more shareable links for the item |  [optional] |
|**ratings** | [**List&lt;OtherLink&gt;**](OtherLink.md) | This is an alternate URL to use to POST the ratings JSON. Difference between this and &#39;recommendations&#39; is that &#39;ratings&#39; will NOT return back recommendations of audio to play next. |  [optional] |
|**recommendations** | [**List&lt;OtherLink&gt;**](OtherLink.md) | This is the URL that should be POSTed with the ratings JSON when this audio starts to play |  [optional] |
|**streamMetadata** | [**List&lt;OtherLink&gt;**](OtherLink.md) | Links that can be polled to retreive current program metadata for a given stream |  [optional] |
|**up** | [**List&lt;OtherLink&gt;**](OtherLink.md) | One or more links to more details about the program or podcast with which this item is associated |  [optional] |
|**web** | [**List&lt;OtherLink&gt;**](OtherLink.md) | One or more links to a web page for the item |  [optional] |



