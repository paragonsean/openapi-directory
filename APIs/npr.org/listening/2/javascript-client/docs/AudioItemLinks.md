# NprListeningService.AudioItemLinks

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | [**[OtherLink]**](OtherLink.md) | One or more links to be trigged by user actions, usually when a button is clicked | [optional] 
**audio** | [**[AudioLink]**](AudioLink.md) | One or more links to audio files for the item | [optional] 
**binge** | [**[OtherLink]**](OtherLink.md) | One or more links that start a flow-based experience focused on the aggregation | [optional] 
**image** | [**[ImageLink]**](ImageLink.md) | One or more links to an image, along with metadata for display | [optional] 
**onramps** | [**[OtherLink]**](OtherLink.md) | One or more shareable links for the item | [optional] 
**ratings** | [**[OtherLink]**](OtherLink.md) | This is an alternate URL to use to POST the ratings JSON. Difference between this and &#39;recommendations&#39; is that &#39;ratings&#39; will NOT return back recommendations of audio to play next. | [optional] 
**recommendations** | [**[OtherLink]**](OtherLink.md) | This is the URL that should be POSTed with the ratings JSON when this audio starts to play | [optional] 
**streamMetadata** | [**[OtherLink]**](OtherLink.md) | Links that can be polled to retreive current program metadata for a given stream | [optional] 
**up** | [**[OtherLink]**](OtherLink.md) | One or more links to more details about the program or podcast with which this item is associated | [optional] 
**web** | [**[OtherLink]**](OtherLink.md) | One or more links to a web page for the item | [optional] 


