

# FeedMetadata

Metadata on a single feed based on what the engine finds from querying the endpoints

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**createdAt** | **OffsetDateTime** | Date the metadata record was created in engine (first seen on source) |  [optional] |
|**groups** | [**List&lt;FeedGroupMetadata&gt;**](FeedGroupMetadata.md) |  |  [optional] |
|**lastFullSync** | **OffsetDateTime** |  |  [optional] |
|**name** | **String** | name of the feed |  [optional] |
|**updatedAt** | **OffsetDateTime** | Date the metadata was last updated |  [optional] |



