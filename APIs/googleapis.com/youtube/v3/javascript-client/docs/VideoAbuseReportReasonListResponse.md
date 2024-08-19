# YouTubeDataApiV3.VideoAbuseReportReasonListResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**etag** | **String** | Etag of this resource. | [optional] 
**eventId** | **String** | Serialized EventId of the request which produced this response. | [optional] 
**items** | [**[VideoAbuseReportReason]**](VideoAbuseReportReason.md) | A list of valid abuse reasons that are used with &#x60;video.ReportAbuse&#x60;. | [optional] 
**kind** | **String** | Identifies what kind of resource this is. Value: the fixed string &#x60;\&quot;youtube#videoAbuseReportReasonListResponse\&quot;&#x60;. | [optional] [default to &#39;youtube#videoAbuseReportReasonListResponse&#39;]
**visitorId** | **String** | The &#x60;visitorId&#x60; identifies the visitor. | [optional] 


