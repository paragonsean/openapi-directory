

# GoogleCloudDatacatalogV1TaggedEntry

Wrapper containing Entry and information about Tags that should and should not be attached to it.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**absentTags** | [**List&lt;GoogleCloudDatacatalogV1Tag&gt;**](GoogleCloudDatacatalogV1Tag.md) | Optional. Tags that should be deleted from the Data Catalog. Caller should populate template name and column only. |  [optional] |
|**presentTags** | [**List&lt;GoogleCloudDatacatalogV1Tag&gt;**](GoogleCloudDatacatalogV1Tag.md) | Optional. Tags that should be ingested into the Data Catalog. Caller should populate template name, column and fields. |  [optional] |
|**v1Entry** | [**GoogleCloudDatacatalogV1Entry**](GoogleCloudDatacatalogV1Entry.md) |  |  [optional] |



