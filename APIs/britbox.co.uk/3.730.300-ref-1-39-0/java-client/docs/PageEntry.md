

# PageEntry

Represents an entry of a Page. Defines what specific piece of content should be presented e.g. an Item or ItemList. Also defines what visual template should be used to render that content. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**customFields** | **Map&lt;String, Object&gt;** | A map of custom fields defined by a curator for a page entry. |  [optional] |
|**id** | **String** | The unique identifier for a page entry. |  |
|**images** | **Map&lt;String, URI&gt;** | The images for the page entry if any.  For example the images of an &#x60;ImageEntry&#x60;.  |  [optional] |
|**item** | [**ItemSummary**](ItemSummary.md) |  |  [optional] |
|**_list** | [**ItemList**](ItemList.md) |  |  [optional] |
|**people** | [**List&lt;Person&gt;**](Person.md) | If &#39;type&#39; is &#39;PeopleEntry&#39; then this is the array of people to present. |  [optional] |
|**template** | **String** | Template type used to present the content of the PageEntry. |  |
|**text** | **String** | If &#39;type&#39; is &#39;TextEntry&#39; then this is the text to be represented. |  [optional] |
|**title** | **String** | The name of the Page Entry. |  |
|**type** | [**TypeEnum**](#TypeEnum) | The type of PageEntry. Used to help identify what type of content will be presented. |  |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| ITEM_ENTRY | &quot;ItemEntry&quot; |
| ITEM_DETAIL_ENTRY | &quot;ItemDetailEntry&quot; |
| LIST_ENTRY | &quot;ListEntry&quot; |
| LIST_DETAIL_ENTRY | &quot;ListDetailEntry&quot; |
| USER_ENTRY | &quot;UserEntry&quot; |
| TEXT_ENTRY | &quot;TextEntry&quot; |
| IMAGE_ENTRY | &quot;ImageEntry&quot; |
| CUSTOM_ENTRY | &quot;CustomEntry&quot; |
| PEOPLE_ENTRY | &quot;PeopleEntry&quot; |



