

# Audio

Describes the audio/conferencing information for a webinar.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**confCallNumbers** | [**Map&lt;String, CallNumbers&gt;**](CallNumbers.md) | The conference call numbers and access codes per country. This will be returned only, if &#39;type&#39; is not set to &#39;Private&#39;. Example for this object: \&quot;confCallNumbers\&quot;:{\&quot;CA\&quot;:{\&quot;accessCodes\&quot;:{\&quot;attendee\&quot;:\&quot;159-309-045\&quot;,\&quot;organizer\&quot;:\&quot;791-426-085\&quot;,\&quot;panelist\&quot;:\&quot;690-270-339\&quot;},\&quot;tollFree\&quot;:\&quot;1 888 455 4198\&quot;},\&quot;FI\&quot;:{\&quot;accessCodes\&quot;:{\&quot;attendee\&quot;:\&quot;159-309-045\&quot;,\&quot;organizer\&quot;:\&quot;791-426-085\&quot;,\&quot;panelist\&quot;:\&quot;690-270-339\&quot;},\&quot;toll\&quot;:\&quot;+358 (0) 338 79 4198\&quot;},\&quot;US\&quot;:{\&quot;accessCodes\&quot;:{\&quot;attendee\&quot;:\&quot;159-309-045\&quot;,\&quot;organizer\&quot;:\&quot;791-426-085\&quot;,\&quot;panelist\&quot;:\&quot;690-270-339\&quot;},\&quot;toll\&quot;:\&quot;+1 (805) 879-4198\&quot;,\&quot;tollFree\&quot;:\&quot;1 888 455 4198\&quot;}} |  [optional] |
|**privateInfo** | [**PrivateInfo**](PrivateInfo.md) |  |  [optional] |
|**type** | **AudioType** |  |  |



