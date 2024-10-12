

# EventOccurenceDetail

Event Occurrence Detail limited to requested fieldset.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**atId** | **String** | Unique event id |  [optional] |
|**atType** | [**AtTypeEnum**](#AtTypeEnum) | Type of occurrence. You will usually see Organized as the type for most events. While Virtual events will get their own Virtual type. |  [optional] |
|**activity** | [**List&lt;FeatureReference&gt;**](FeatureReference.md) | Associated ActivityType entries |  [optional] |
|**ambience** | [**List&lt;FeatureReference&gt;**](FeatureReference.md) | expected mood and feel of the event |  [optional] |
|**at** | [**PlaceReference**](PlaceReference.md) |  |  [optional] |
|**awayTeam** | [**FeatureReference**](FeatureReference.md) |  |  [optional] |
|**category** | [**List&lt;FeatureReference&gt;**](FeatureReference.md) | Associated EventCategory. May be multiple, such as Charity Music event |  [optional] |
|**contactPoint** | [**ContactDetail**](ContactDetail.md) |  |  [optional] |
|**description** | **String** | Full description in plain text |  [optional] |
|**doorTime** | **OffsetDateTime** | Time when the admission starts |  [optional] |
|**duration** | **String** | Duration of the event in ISO-8601 format (PT45M) - 45 minutes |  [optional] |
|**endApprox** | **Boolean** | endDate is approximated based on historical data |  [optional] |
|**endDate** | **OffsetDateTime** | Time when the event ends, if known |  [optional] |
|**extTaxonomy** | [**List&lt;FeatureReference&gt;**](FeatureReference.md) | extended taxonomy such as IAB and Google AdWords |  [optional] |
|**genre** | [**List&lt;FeatureReference&gt;**](FeatureReference.md) | applicable Genres. (Tier 2 taxonomy). May include related genres from categories, not deemed as primary |  [optional] |
|**headline** | **String** | Optional short description in plain text |  [optional] |
|**homeTeam** | [**FeatureReference**](FeatureReference.md) |  |  [optional] |
|**htmlDescription** | **String** | Full description with HTML formatting, where available |  [optional] |
|**image** | [**ImageMeta**](ImageMeta.md) |  |  [optional] |
|**inLanguage** | [**FeatureReference**](FeatureReference.md) |  |  [optional] |
|**name** | **String** | Name of the event in plain text |  [optional] |
|**noTime** | **Boolean** | Specific time of the event is unknown. (shown only when true) |  [optional] |
|**offers** | [**List&lt;TicketOffer&gt;**](TicketOffer.md) | Ticketing options |  [optional] |
|**onDemand** | **Boolean** | This event can start at any time during specified window |  [optional] |
|**performer** | [**List&lt;FeatureReference&gt;**](FeatureReference.md) | List of Personas significant for this event |  [optional] |
|**photo** | [**List&lt;ImageMeta&gt;**](ImageMeta.md) | Primary image |  [optional] |
|**startDate** | **OffsetDateTime** | Time when the event starts |  [optional] |
|**superEvent** | [**OccurrenceReference**](OccurrenceReference.md) |  |  [optional] |
|**updated** | **OffsetDateTime** | Timestamp of last modification (UTC) |  [optional] |
|**url** | **String** | Primary url for published event |  [optional] |
|**workPerformed** | [**List&lt;FeatureReference&gt;**](FeatureReference.md) | Subject matter of the event |  [optional] |



## Enum: AtTypeEnum

| Name | Value |
|---- | -----|
| ORGANIZED | &quot;Organized&quot; |
| SCREENING | &quot;Screening&quot; |
| ENVIRONMENTAL | &quot;Environmental&quot; |
| VIRTUAL | &quot;Virtual&quot; |



