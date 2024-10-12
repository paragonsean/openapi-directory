

# GoogleCloudDataplexV1GovernanceEventEntity

Information about Entity resource that the log event is associated with.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**entity** | **String** | The Entity resource the log event is associated with. Format: projects/{project_number}/locations/{location_id}/lakes/{lake_id}/zones/{zone_id}/entities/{entity_id} |  [optional] |
|**entityType** | [**EntityTypeEnum**](#EntityTypeEnum) | Type of entity. |  [optional] |



## Enum: EntityTypeEnum

| Name | Value |
|---- | -----|
| ENTITY_TYPE_UNSPECIFIED | &quot;ENTITY_TYPE_UNSPECIFIED&quot; |
| TABLE | &quot;TABLE&quot; |
| FILESET | &quot;FILESET&quot; |



