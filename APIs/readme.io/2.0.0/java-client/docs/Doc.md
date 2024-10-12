

# Doc


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**body** | **String** | Body content of the page, formatted in ReadMe or Github flavored Markdown. Accepts long page content, for example, greater than 100k characters |  [optional] |
|**category** | **String** | Category ID of the page, which you can get through https://docs.readme.com/developers/reference/categories#getcategory  |  |
|**hidden** | **Boolean** | Visibility of the page |  [optional] |
|**parentDoc** | **String** | For a subpage, specify the parent doc ID, which you can get through https://docs.readme.com/developers/reference/docs#getdoc |  [optional] |
|**title** | **String** | Title of the page |  |
|**type** | [**TypeEnum**](#TypeEnum) | Type of the page. The available types all show up under the /docs/ URL path of your docs project (also known as the \&quot;guides\&quot; section). Can be \&quot;basic\&quot; (most common), \&quot;error\&quot; (page desribing an API error), or \&quot;link\&quot; (page that redirects to an external link) |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| BASIC | &quot;basic&quot; |
| ERROR | &quot;error&quot; |
| LINK | &quot;link&quot; |



