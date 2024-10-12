

# Event


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**address** | **String** | Address of the event&#39;s venue, if available. |  [optional] |
|**city** | **String** | City, town, village, etc. the event is located in. |  [optional] |
|**country** | **String** | Country the event is located in. |  [optional] |
|**district** | [**DistrictList**](DistrictList.md) |  |  [optional] |
|**divisionKeys** | **List&lt;String&gt;** | An array of event keys for the divisions at this event. |  [optional] |
|**endDate** | **LocalDate** | Event end date in &#x60;yyyy-mm-dd&#x60; format. |  |
|**eventCode** | **String** | Event short code, as provided by FIRST. |  |
|**eventType** | **Integer** | Event Type, as defined here: https://github.com/the-blue-alliance/the-blue-alliance/blob/master/consts/event_type.py#L2 |  |
|**eventTypeString** | **String** | Event Type, eg Regional, District, or Offseason. |  |
|**firstEventCode** | **String** | Public facing event code used by FIRST (on frc-events.firstinspires.org, for example) |  [optional] |
|**firstEventId** | **String** | The FIRST internal Event ID, used to link to the event on the FRC webpage. |  [optional] |
|**gmapsPlaceId** | **String** | Google Maps Place ID for the event address. |  [optional] |
|**gmapsUrl** | **String** | Link to address location on Google Maps. |  [optional] |
|**key** | **String** | TBA event key with the format yyyy[EVENT_CODE], where yyyy is the year, and EVENT_CODE is the event code of the event. |  |
|**lat** | **Double** | Latitude for the event address. |  [optional] |
|**lng** | **Double** | Longitude for the event address. |  [optional] |
|**locationName** | **String** | Name of the location at the address for the event, eg. Blue Alliance High School. |  [optional] |
|**name** | **String** | Official name of event on record either provided by FIRST or organizers of offseason event. |  |
|**parentEventKey** | **String** | The TBA Event key that represents the event&#39;s parent. Used to link back to the event from a division event. It is also the inverse relation of &#x60;divison_keys&#x60;. |  [optional] |
|**playoffType** | **Integer** | Playoff Type, as defined here: https://github.com/the-blue-alliance/the-blue-alliance/blob/master/consts/playoff_type.py#L4, or null. |  [optional] |
|**playoffTypeString** | **String** | String representation of the &#x60;playoff_type&#x60;, or null. |  [optional] |
|**postalCode** | **String** | Postal code from the event address. |  [optional] |
|**shortName** | **String** | Same as &#x60;name&#x60; but doesn&#39;t include event specifiers, such as &#39;Regional&#39; or &#39;District&#39;. May be null. |  [optional] |
|**startDate** | **LocalDate** | Event start date in &#x60;yyyy-mm-dd&#x60; format. |  |
|**stateProv** | **String** | State or Province the event is located in. |  [optional] |
|**timezone** | **String** | Timezone name. |  [optional] |
|**webcasts** | [**List&lt;Webcast&gt;**](Webcast.md) |  |  [optional] |
|**website** | **String** | The event&#39;s website, if any. |  [optional] |
|**week** | **Integer** | Week of the event relative to the first official season event, zero-indexed. Only valid for Regionals, Districts, and District Championships. Null otherwise. (Eg. A season with a week 0 &#39;preseason&#39; event does not count, and week 1 events will show 0 here. Seasons with a week 0.5 regional event will show week 0 for those event(s) and week 1 for week 1 events and so on.) |  [optional] |
|**year** | **Integer** | Year the event data is for. |  |



