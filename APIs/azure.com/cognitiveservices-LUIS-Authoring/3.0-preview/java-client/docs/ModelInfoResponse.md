

# ModelInfoResponse

An application model info.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **UUID** | The ID of the Entity Model. |  |
|**name** | **String** | Name of the Entity Model. |  [optional] |
|**readableType** | **ReadableType** |  |  |
|**typeId** | **Integer** | The type ID of the Entity Model. |  [optional] |
|**children** | [**List&lt;ChildEntity&gt;**](ChildEntity.md) |  |  [optional] |
|**roles** | [**List&lt;EntityRole&gt;**](EntityRole.md) | List of Pattern.Any Entity Extractors. |  [optional] |
|**subLists** | [**List&lt;SubClosedListResponse&gt;**](SubClosedListResponse.md) | List of sublists. |  [optional] |
|**customPrebuiltDomainName** | **String** | The domain name. |  [optional] |
|**customPrebuiltModelName** | **String** | The intent name or entity name. |  [optional] |
|**regexPattern** | **String** | The Regular Expression entity pattern. |  [optional] |
|**explicitList** | [**List&lt;ExplicitListItem&gt;**](ExplicitListItem.md) | List of explicit (exception) list items |  [optional] |



