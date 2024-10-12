# Vimeo.Category

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**icon** | [**Picture**](Picture.md) | The active icon for the category. | [optional] 
**lastVideoFeaturedTime** | **String** | The last time, in ISO 8601 format, that a video was featured. | 
**link** | **String** | The URL to access the category in a browser. | 
**metadata** | [**CategoryMetadata**](CategoryMetadata.md) |  | 
**name** | **String** | The display name that identifies the category. | 
**parent** | [**CategoryParent**](CategoryParent.md) |  | 
**pictures** | [**Picture**](Picture.md) | The active picture for this category; defaults to vertical color bars. | 
**resourceKey** | **String** | The resource key of the category. | 
**subcategories** | [**[CategorySubcategoriesInner]**](CategorySubcategoriesInner.md) | All the subcategories that belong to this category, if the current category is a top-level parent. | [optional] 
**topLevel** | **Boolean** | Whether the category isn&#39;t a subcategory of another category. | 
**uri** | **String** | The unique identifier to access the category resource. | 


