

# TflApiPresentationEntitiesRoadDisruption


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**category** | **String** | Describes the nature of disruption e.g. Traffic Incidents, Works |  [optional] |
|**comments** | **String** | Full text of comments describing the disruption, including details of any road closures and diversions, where appropriate. |  [optional] |
|**corridorIds** | **List&lt;String&gt;** | The Ids of affected corridors, if any. |  [optional] |
|**currentUpdate** | **String** | Text of the most recent update from the LSTCC on the state of the               disruption, including the current traffic impact and any advice to               road users. |  [optional] |
|**currentUpdateDateTime** | **OffsetDateTime** | The time when the last CurrentUpdate description was recorded,               or null if no CurrentUpdate has been applied. |  [optional] |
|**endDateTime** | **OffsetDateTime** | The date and time on which the disruption ended. For planned disruptions, this date will have a valid value. For unplanned               disruptions in progress, this field will be omitted. |  [optional] |
|**geography** | [**SystemDataSpatialDbGeography**](SystemDataSpatialDbGeography.md) |  |  [optional] |
|**geometry** | [**SystemDataSpatialDbGeography**](SystemDataSpatialDbGeography.md) |  |  [optional] |
|**hasClosures** | **Boolean** | True if any of the affected Streets have a \&quot;Full Closure\&quot; status, false otherwise. A RoadDisruption that has HasClosures is considered a               Severe or Serious disruption for severity filtering purposes. |  [optional] |
|**id** | **String** | Unique identifier for the road disruption |  [optional] |
|**isProvisional** | **Boolean** | True if the disruption is planned on a future date that is open to change |  [optional] |
|**lastModifiedTime** | **OffsetDateTime** | The date and time on which the disruption was last modified in the system. This information can reliably be used by a developer to quickly              compare two instances of the same disruption to determine if it has been changed. |  [optional] |
|**levelOfInterest** | **String** | This describes the level of potential impact on traffic operations of the disruption.               High &#x3D; e.g. a one-off disruption on a major or high profile route which will require a high level of operational attention               Medium &#x3D; This is the default value               Low &#x3D; e.g. a frequently occurring disruption which is well known |  [optional] |
|**linkText** | **String** | The text of any associated link |  [optional] |
|**linkUrl** | **String** | The url of any associated link |  [optional] |
|**location** | **String** | Main road name / number (borough) or preset area name where the disruption is located. This might be useful for a map popup where space is limited. |  [optional] |
|**ordinal** | **Integer** | An ordinal of the disruption based on severity, level of interest and corridor. |  [optional] |
|**point** | **String** | Latitude and longitude (WGS84) of the centroid of the disruption, stored in a geoJSON-formatted string. |  [optional] |
|**publishEndDate** | **OffsetDateTime** |  |  [optional] |
|**publishStartDate** | **OffsetDateTime** | TDM Additional properties |  [optional] |
|**recurringSchedules** | [**List&lt;TflApiPresentationEntitiesRoadDisruptionSchedule&gt;**](TflApiPresentationEntitiesRoadDisruptionSchedule.md) |  |  [optional] |
|**roadDisruptionImpactAreas** | [**List&lt;TflApiPresentationEntitiesRoadDisruptionImpactArea&gt;**](TflApiPresentationEntitiesRoadDisruptionImpactArea.md) |  |  [optional] |
|**roadDisruptionLines** | [**List&lt;TflApiPresentationEntitiesRoadDisruptionLine&gt;**](TflApiPresentationEntitiesRoadDisruptionLine.md) |  |  [optional] |
|**roadProject** | [**TflApiPresentationEntitiesRoadProject**](TflApiPresentationEntitiesRoadProject.md) |  |  [optional] |
|**severity** | **String** | A description of the severity of the disruption. |  [optional] |
|**startDateTime** | **OffsetDateTime** | The date and time which the disruption started. For a planned disruption (i.e. planned road works) this date will be in the future.              For unplanned disruptions, this will default to the date on which the disruption was first recorded, but may be adjusted by the operator. |  [optional] |
|**status** | **String** | This describes the status of the disruption.                Active &#x3D; currently in progress               Active Long Term &#x3D; currently in progress and long term              Scheduled &#x3D; scheduled to start within the next 180 days              Recurring Works &#x3D; planned maintenance works that follow a regular routine or pattern and whose next occurrence is to start within the next 180 days.              Recently Cleared &#x3D; recently cleared in the last 24 hours              Note that the status of Scheduled or Recurring Works disruptions will change to Active when they start, and will change status again when they end. |  [optional] |
|**streets** | [**List&lt;TflApiPresentationEntitiesStreet&gt;**](TflApiPresentationEntitiesStreet.md) | A collection of zero or more streets affected by the disruption. |  [optional] |
|**subCategory** | **String** | Describes the sub-category of disruption e.g. Collapsed Manhole, Abnormal Load |  [optional] |
|**timeFrame** | **String** |  |  [optional] |
|**url** | **String** | URL to retrieve this road disruption |  [optional] |



