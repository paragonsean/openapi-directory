

# EventSimple


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**city** | **String** | City, town, village, etc. the event is located in. |  [optional] |
|**country** | **String** | Country the event is located in. |  [optional] |
|**district** | [**DistrictList**](DistrictList.md) |  |  [optional] |
|**endDate** | **LocalDate** | Event end date in &#x60;yyyy-mm-dd&#x60; format. |  |
|**eventCode** | **String** | Event short code, as provided by FIRST. |  |
|**eventType** | **Integer** | Event Type, as defined here: https://github.com/the-blue-alliance/the-blue-alliance/blob/master/consts/event_type.py#L2 |  |
|**key** | **String** | TBA event key with the format yyyy[EVENT_CODE], where yyyy is the year, and EVENT_CODE is the event code of the event. |  |
|**name** | **String** | Official name of event on record either provided by FIRST or organizers of offseason event. |  |
|**startDate** | **LocalDate** | Event start date in &#x60;yyyy-mm-dd&#x60; format. |  |
|**stateProv** | **String** | State or Province the event is located in. |  [optional] |
|**year** | **Integer** | Year the event data is for. |  |



