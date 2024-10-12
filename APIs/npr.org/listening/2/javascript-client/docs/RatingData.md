# NprListeningService.RatingData

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**affiliations** | **[Object]** | An array of IDs &amp; other data about collections or podcasts the user has ratings for; produced by the server and should be sent back as received; used for tracking program and podcast suggestions | [optional] 
**channel** | **String** | The channel this media item was pulled from | [default to &#39;npr&#39;]
**cohort** | **String** | The primary cohort of the current logged-in user | 
**duration** | **Number** | Number of seconds this audio piece is expected to last | 
**elapsed** | **Number** | Number of seconds since the start of playback for this media item, as an integer | 
**mediaId** | **String** | The media id as given by the media object | 
**origin** | **String** | How the recommendation was generated | 
**rating** | **String** | String representing the rating | 
**timestamp** | **Date** | ISO-8601 formatted date/time; typically replaced by the client with the actual rating time | 


