# LotaData.EventOccurenceDetail

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **String** | Unique event id | [optional] 
**type** | **String** | Type of occurrence. You will usually see Organized as the type for most events. While Virtual events will get their own Virtual type. | [optional] 
**activity** | [**[FeatureReference]**](FeatureReference.md) | Associated ActivityType entries | [optional] 
**ambience** | [**[FeatureReference]**](FeatureReference.md) | expected mood and feel of the event | [optional] 
**at** | [**PlaceReference**](PlaceReference.md) |  | [optional] 
**awayTeam** | [**FeatureReference**](FeatureReference.md) |  | [optional] 
**category** | [**[FeatureReference]**](FeatureReference.md) | Associated EventCategory. May be multiple, such as Charity Music event | [optional] 
**contactPoint** | [**ContactDetail**](ContactDetail.md) |  | [optional] 
**description** | **String** | Full description in plain text | [optional] 
**doorTime** | **Date** | Time when the admission starts | [optional] 
**duration** | **String** | Duration of the event in ISO-8601 format (PT45M) - 45 minutes | [optional] 
**endApprox** | **Boolean** | endDate is approximated based on historical data | [optional] 
**endDate** | **Date** | Time when the event ends, if known | [optional] 
**extTaxonomy** | [**[FeatureReference]**](FeatureReference.md) | extended taxonomy such as IAB and Google AdWords | [optional] 
**genre** | [**[FeatureReference]**](FeatureReference.md) | applicable Genres. (Tier 2 taxonomy). May include related genres from categories, not deemed as primary | [optional] 
**headline** | **String** | Optional short description in plain text | [optional] 
**homeTeam** | [**FeatureReference**](FeatureReference.md) |  | [optional] 
**htmlDescription** | **String** | Full description with HTML formatting, where available | [optional] 
**image** | [**ImageMeta**](ImageMeta.md) |  | [optional] 
**inLanguage** | [**FeatureReference**](FeatureReference.md) |  | [optional] 
**name** | **String** | Name of the event in plain text | [optional] 
**noTime** | **Boolean** | Specific time of the event is unknown. (shown only when true) | [optional] 
**offers** | [**[TicketOffer]**](TicketOffer.md) | Ticketing options | [optional] 
**onDemand** | **Boolean** | This event can start at any time during specified window | [optional] 
**performer** | [**[FeatureReference]**](FeatureReference.md) | List of Personas significant for this event | [optional] 
**photo** | [**[ImageMeta]**](ImageMeta.md) | Primary image | [optional] 
**startDate** | **Date** | Time when the event starts | [optional] 
**superEvent** | [**OccurrenceReference**](OccurrenceReference.md) |  | [optional] 
**updated** | **Date** | Timestamp of last modification (UTC) | [optional] 
**url** | **String** | Primary url for published event | [optional] 
**workPerformed** | [**[FeatureReference]**](FeatureReference.md) | Subject matter of the event | [optional] 



## Enum: TypeEnum


* `Organized` (value: `"Organized"`)

* `Screening` (value: `"Screening"`)

* `Environmental` (value: `"Environmental"`)

* `Virtual` (value: `"Virtual"`)




