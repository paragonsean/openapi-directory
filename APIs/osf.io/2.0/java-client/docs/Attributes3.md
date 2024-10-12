

# Attributes3

The properties of the comment entity.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**canEdit** | **Boolean** | Whether or not the current user has permission to edit this comment |  [optional] [readonly] |
|**content** | **String** | The content of the comment. |  [optional] |
|**dateCreated** | **OffsetDateTime** | The time at which the comment was created, as an iso8601 formatted timestamp. |  [optional] [readonly] |
|**dateModified** | **OffsetDateTime** | The time at which the comment was last modified, as an iso8601 formatted timestamp. |  [optional] [readonly] |
|**deleted** | **Boolean** | Whether or not the comment is deleted. |  [optional] [readonly] |
|**hasChildren** | **Boolean** | Whether or not the comment has replies. |  [optional] [readonly] |
|**hasReport** | **Boolean** | Whether or not the comment the current user reported this as spam. |  [optional] [readonly] |
|**isAbuse** | **Boolean** | Whether or not the comment is flagged or confirmed spam. |  [optional] [readonly] |
|**isHam** | **Boolean** | Whether or not an admin checked the legitimacy of this comment. |  [optional] [readonly] |
|**modified** | **Boolean** | Whether or not the comment has been edited. |  [optional] [readonly] |
|**page** | **String** | The page type the comment is on, e.g. &#x60;node&#x60;, &#x60;registration&#x60;, &#x60;wiki&#x60;, &#x60;files&#x60;. |  [optional] [readonly] |



