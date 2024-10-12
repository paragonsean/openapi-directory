# RocketServices.PageEntry

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customFields** | **{String: Object}** | A map of custom fields defined by a curator for a page entry. | [optional] 
**id** | **String** | The unique identifier for a page entry. | 
**images** | **{String: String}** | The images for the page entry if any.  For example the images of an &#x60;ImageEntry&#x60;.  | [optional] 
**item** | [**ItemSummary**](ItemSummary.md) |  | [optional] 
**list** | [**ItemList**](ItemList.md) |  | [optional] 
**people** | [**[Person]**](Person.md) | If &#39;type&#39; is &#39;PeopleEntry&#39; then this is the array of people to present. | [optional] 
**template** | **String** | Template type used to present the content of the PageEntry. | 
**text** | **String** | If &#39;type&#39; is &#39;TextEntry&#39; then this is the text to be represented. | [optional] 
**title** | **String** | The name of the Page Entry. | 
**type** | **String** | The type of PageEntry. Used to help identify what type of content will be presented. | 



## Enum: TypeEnum


* `ItemEntry` (value: `"ItemEntry"`)

* `ItemDetailEntry` (value: `"ItemDetailEntry"`)

* `ListEntry` (value: `"ListEntry"`)

* `ListDetailEntry` (value: `"ListDetailEntry"`)

* `UserEntry` (value: `"UserEntry"`)

* `TextEntry` (value: `"TextEntry"`)

* `ImageEntry` (value: `"ImageEntry"`)

* `CustomEntry` (value: `"CustomEntry"`)

* `PeopleEntry` (value: `"PeopleEntry"`)




