# GoToMeeting.MeetingReqUpdate

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conferencecallinfo** | **String** | A required string. Can be one of the following options: &lt;br&gt;PSTN (PSTN only), &lt;br&gt;Free (PSTN and VoIP), &lt;br&gt;Hybrid, (PSTN and VoIP), &lt;br&gt;Private (you provide numbers and access code), or &lt;br&gt;VoIP (VoIP only). &lt;br&gt;You may also enter plain text for numbers and access codes with a limit of 255 characters | 
**endtime** | **Date** | The ending time of the meeting. A required ISO8601 UTC string, e.g. 2015-07-01T22:00:00Z | 
**meetingtype** | [**MeetingType**](MeetingType.md) |  | 
**passwordrequired** | **Boolean** | Indicates whether a password is required to join the meeting. Required parameter | 
**starttime** | **Date** | The starting time of the meeting. A required ISO8601 UTC string, e.g. 2015-07-01T22:00:00Z | 
**subject** | **String** | A description of the meeting. 100 characters maximum. The characters &#39;&amp;gt;&#39; and &#39;&amp;lt;&#39; have to be replaced with the corresponding html character code (&amp;amp;gt; for &amp;#39;&amp;gt;&amp;#39; and &amp;amp;lt; for &amp;#39;&amp;lt;&amp;#39;) | 
**timezonekey** | **String** | DEPRECATED. Must be provided and set to empty string &#39;&#39; | 


