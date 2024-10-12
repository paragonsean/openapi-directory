

# StoreLayout

General setting for the managed Google Play store layout, currently only specifying the page to display the first time the store is opened.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**homepageId** | **String** | The ID of the store page to be used as the homepage. The homepage is the first page shown in the managed Google Play Store. Not specifying a homepage is equivalent to setting the store layout type to \&quot;basic\&quot;. |  [optional] |
|**storeLayoutType** | [**StoreLayoutTypeEnum**](#StoreLayoutTypeEnum) | The store layout type. By default, this value is set to \&quot;basic\&quot; if the homepageId field is not set, and to \&quot;custom\&quot; otherwise. If set to \&quot;basic\&quot;, the layout will consist of all approved apps that have been whitelisted for the user. |  [optional] |



## Enum: StoreLayoutTypeEnum

| Name | Value |
|---- | -----|
| UNKNOWN | &quot;unknown&quot; |
| BASIC | &quot;basic&quot; |
| CUSTOM | &quot;custom&quot; |



