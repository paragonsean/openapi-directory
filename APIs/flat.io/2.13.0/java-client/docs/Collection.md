

# Collection

Collection of scores

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**app** | **String** | If this directory is dedicated to an app, the unique idenfier of this app |  [optional] |
|**capabilities** | [**CollectionCapabilities**](CollectionCapabilities.md) |  |  [optional] |
|**collaborators** | [**List&lt;ResourceCollaborator&gt;**](ResourceCollaborator.md) | The list of the collaborators of the collection |  [optional] |
|**collections** | **List&lt;String&gt;** | The List of parent collections, which includes all the collections this score is included. Please note that you might not have access to all of them. |  [optional] |
|**creationDate** | **OffsetDateTime** | The date when the collection was created |  [optional] |
|**htmlUrl** | **String** | The url where the collection can be viewed in a web browser |  [optional] |
|**id** | **String** | Unique identifier of the collection |  [optional] |
|**privacy** | **CollectionPrivacy** |  |  [optional] |
|**rights** | [**ResourceRights**](ResourceRights.md) |  |  [optional] |
|**sharingKey** | **String** | The private sharing key of the collection (available when the &#x60;privacy&#x60; mode is set to &#x60;privateLink&#x60;) |  [optional] |
|**title** | **String** | The title of the collection |  [optional] |
|**type** | **CollectionType** |  |  [optional] |
|**user** | [**UserPublicSummary**](UserPublicSummary.md) |  |  [optional] |



