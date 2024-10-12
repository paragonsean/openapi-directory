

# CollectionStatus

The collectionstatus message.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**collectionLevelIssuses** | [**List&lt;CollectionStatusItemLevelIssue&gt;**](CollectionStatusItemLevelIssue.md) | A list of all issues associated with the collection. |  [optional] |
|**creationDate** | **String** | Date on which the collection has been created in [ISO 8601](http://en.wikipedia.org/wiki/ISO_8601) format: Date, time, and offset, for example \&quot;2020-01-02T09:00:00+01:00\&quot; or \&quot;2020-01-02T09:00:00Z\&quot; |  [optional] |
|**destinationStatuses** | [**List&lt;CollectionStatusDestinationStatus&gt;**](CollectionStatusDestinationStatus.md) | The intended destinations for the collection. |  [optional] |
|**id** | **String** | Required. The ID of the collection for which status is reported. |  [optional] |
|**lastUpdateDate** | **String** | Date on which the collection has been last updated in [ISO 8601](http://en.wikipedia.org/wiki/ISO_8601) format: Date, time, and offset, for example \&quot;2020-01-02T09:00:00+01:00\&quot; or \&quot;2020-01-02T09:00:00Z\&quot; |  [optional] |



