

# GeoFilter

Rules defining user's geo access within a CDN endpoint.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**action** | [**ActionEnum**](#ActionEnum) | Action of the geo filter, i.e. allow or block access. |  |
|**countryCodes** | **List&lt;String&gt;** | Two letter country codes defining user country access in a geo filter, e.g. AU, MX, US. |  |
|**relativePath** | **String** | Relative path applicable to geo filter. (e.g. &#39;/mypictures&#39;, &#39;/mypicture/kitty.jpg&#39;, and etc.) |  |



## Enum: ActionEnum

| Name | Value |
|---- | -----|
| BLOCK | &quot;Block&quot; |
| ALLOW | &quot;Allow&quot; |



