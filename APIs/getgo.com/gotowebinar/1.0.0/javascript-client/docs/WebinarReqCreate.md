# GoToWebinar.WebinarReqCreate

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **String** | A short description of the webinar (2048 characters maximum) | [optional] 
**isPasswordProtected** | **Boolean** | A boolean flag indicating if the webinar is password protected or not. | [optional] [default to false]
**subject** | **String** | The name/subject of the webinar (128 characters maximum) | 
**timeZone** | **String** | The time zone where the webinar is taking place (must be a valid time zone ID, see https://goto-developer.logmein.com/time-zones). If this parameter is not passed, the timezone of the organizer&#39;s profile will be used | [optional] 
**times** | [**[DateTimeRange]**](DateTimeRange.md) | Array with startTime and endTime for webinar. Since this call creates single session webinars, the array can only contain a single pair of startTime and endTime | 
**type** | **String** | Specifies the webinar type. The default type value is \&quot;single_session\&quot;, which is used to create a single webinar session. The possible values are \&quot;single_session\&quot;, \&quot;series\&quot;, \&quot;sequence\&quot;. If type is set to \&quot;single_session\&quot;, a single webinar session is created. If type is set to \&quot;series\&quot;, a webinar series is created. In this case 2 or more timeframes must be specified for each webinar. Example: \&quot;times\&quot;: [{\&quot;startTime\&quot;: \&quot;...\&quot;, \&quot;endTime\&quot;: \&quot;...\&quot;},{\&quot;startTime\&quot;: \&quot;...\&quot;, \&quot;endTime\&quot;: \&quot;...\&quot;},{\&quot;startTime\&quot;: \&quot;...\&quot;, \&quot;endTime\&quot;: \&quot;...\&quot;}. If type is set to \&quot;sequence\&quot; a sequence of webinars is created. The times object in the body must be replaced by the \&quot;recurrenceStart\&quot; object. Example: \&quot;recurrenceStart\&quot;: {\&quot;startTime\&quot;:\&quot;2012-06-12T16:00:00Z\&quot;, \&quot;endTime\&quot;: \&quot;2012-06-12T17:00:00Z\&quot; }.  The \&quot;recurrenceEnd\&quot; and \&quot;recurrencePattern\&quot; body parameter must be specified. Example: , \&quot;recurrenceEnd\&quot;: \&quot;2012-07-10\&quot;, \&quot;recurrencePattern\&quot;: \&quot;daily\&quot;. | [optional] [default to &#39;single_session&#39;]


