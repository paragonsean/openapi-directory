

# AdTrackingData

All the information needed for the Sponsorship Service to send back tracking information to our external sponsorship provider

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**adId** | **String** | The VAST Ad node &#x60;id&#x60; attribute value, (e.g. AdswizzAd12345) |  |
|**event** | [**EventEnum**](#EventEnum) | The user-interaction event to submit tracking for |  |



## Enum: EventEnum

| Name | Value |
|---- | -----|
| START | &quot;start&quot; |
| FIRST_QUARTILE | &quot;firstQuartile&quot; |
| MIDPOINT | &quot;midpoint&quot; |
| THIRD_QUARTILE | &quot;thirdQuartile&quot; |
| COMPLETE | &quot;complete&quot; |



