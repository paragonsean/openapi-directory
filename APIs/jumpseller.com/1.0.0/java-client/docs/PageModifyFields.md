

# PageModifyFields


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**body** | **String** | Body of the Page |  [optional] |
|**categories** | [**List&lt;PageCategory&gt;**](PageCategory.md) | Page categories to which the Page belongs to |  [optional] |
|**image** | [**PageFieldsImage**](PageFieldsImage.md) |  |  [optional] |
|**metaDescription** | **String** | Meta description of the Page |  [optional] |
|**pageTitle** | **String** | Meta title of the Page |  [optional] |
|**permalink** | **String** | URL of the Page |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | Status of the Page |  [optional] |
|**template** | **Integer** | ID of the Page template. Use null for the blank layout (&#39;None&#39;) |  [optional] |
|**title** | **String** | Title of the Page |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| PUBLIC | &quot;public&quot; |
| DRAFT | &quot;draft&quot; |
| HIDDEN | &quot;hidden&quot; |



