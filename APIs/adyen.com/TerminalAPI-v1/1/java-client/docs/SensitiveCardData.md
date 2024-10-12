

# SensitiveCardData

This data structure could be CMS protected (EnvelopedData). In this case the data structure SensitiveCardData is replaced by the data structure ProtectedCardData of type ContentInformationType. When this data is protected, the exact content is unknown by the Sale System, and might include all the information which are required by an external backup POI Server to make a batch payment transaction in case of problem with the POI System. Sensitive information related to the payment card, entered or read by the Sale System.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**cardSeqNumb** | **Integer** | if EntryMode is File, Keyed or Manual. |  [optional] |
|**expiryDate** | **Integer** | if EntryMode is File. |  [optional] |
|**PAN** | **Integer** |  |  [optional] |
|**trackData** | [**List&lt;TrackData&gt;**](TrackData.md) |  |  [optional] |



