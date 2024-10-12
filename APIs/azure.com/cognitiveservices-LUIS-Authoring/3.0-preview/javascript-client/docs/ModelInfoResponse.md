# LuisAuthoringClient.ModelInfoResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **String** | The ID of the Entity Model. | 
**name** | **String** | Name of the Entity Model. | [optional] 
**readableType** | [**ReadableType**](ReadableType.md) |  | 
**typeId** | **Number** | The type ID of the Entity Model. | [optional] 
**children** | [**[ChildEntity]**](ChildEntity.md) |  | [optional] 
**roles** | [**[EntityRole]**](EntityRole.md) | List of Pattern.Any Entity Extractors. | [optional] 
**subLists** | [**[SubClosedListResponse]**](SubClosedListResponse.md) | List of sublists. | [optional] 
**customPrebuiltDomainName** | **String** | The domain name. | [optional] 
**customPrebuiltModelName** | **String** | The intent name or entity name. | [optional] 
**regexPattern** | **String** | The Regular Expression entity pattern. | [optional] 
**explicitList** | [**[ExplicitListItem]**](ExplicitListItem.md) | List of explicit (exception) list items | [optional] 


