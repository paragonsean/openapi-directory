

# Entitlement

This class defines an entitlement data on the Publish API

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**data** | **Object** | The actual entitlements information to add to the entity |  |
|**relatedEntityId** | **String** | Id of the entity to add this extionsion to. If the relatedEntityId is Null, a relatedEntitySource MUST be provided |  [optional] |
|**relatedEntitySource** | [**Source**](Source.md) |  |  [optional] |
|**relatedEntityType** | [**RelatedEntityTypeEnum**](#RelatedEntityTypeEnum) | The type of the entity to add this entitlement to |  |
|**source** | [**SourceEnum**](#SourceEnum) | Source of the extension, where it came from |  |
|**versionNumber** | **Long** | Version of the entitlements. Version is to prevent to override an entitlements with an older one |  [optional] |



## Enum: RelatedEntityTypeEnum

| Name | Value |
|---- | -----|
| EVENT | &quot;event&quot; |
| VENUE | &quot;venue&quot; |
| ATTRACTION | &quot;attraction&quot; |



## Enum: SourceEnum

| Name | Value |
|---- | -----|
| TICKETMASTER | &quot;ticketmaster&quot; |



