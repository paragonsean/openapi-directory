

# ActivityHistory


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**createdAt** | **OffsetDateTime** | When this record was created |  [optional] |
|**dynamicData** | **Object** | Attributes from associated records. This is specific to the type of activity and may change over time. Not returned for create requests |  [optional] |
|**failedDynamicResources** | **Object** | A list of remote resource names that failed to load. This is specific to the type of activity and may change over time. Not returned for create requests |  [optional] |
|**id** | **Integer** | ID of this activity |  [optional] |
|**occurredAt** | **OffsetDateTime** | When this activity occurred |  [optional] |
|**pinnedAt** | **OffsetDateTime** | When this record was pinned |  [optional] |
|**resourceId** | **Integer** | ID of the resource this activity is for. It will be a string for the following resource types: crm_opportunity |  [optional] |
|**resourceType** | **Integer** | Type of the resource this activity is for. One of: account, person |  [optional] |
|**staticData** | **Object** | The static data for this activity |  [optional] |
|**type** | **String** | The type of activity |  [optional] |
|**updatedAt** | **OffsetDateTime** | When this record was updated |  [optional] |
|**userGuid** | **String** | UUID of the user this activity is for |  [optional] |



