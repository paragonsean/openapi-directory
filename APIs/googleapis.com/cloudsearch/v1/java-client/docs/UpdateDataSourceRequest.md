

# UpdateDataSourceRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**debugOptions** | [**DebugOptions**](DebugOptions.md) |  |  [optional] |
|**source** | [**DataSource**](DataSource.md) |  |  [optional] |
|**updateMask** | **String** | Only applies to [&#x60;settings.datasources.patch&#x60;](https://developers.google.com/cloud-search/docs/reference/rest/v1/settings.datasources/patch). Update mask to control which fields to update. Example field paths: &#x60;name&#x60;, &#x60;displayName&#x60;. * If &#x60;update_mask&#x60; is non-empty, then only the fields specified in the &#x60;update_mask&#x60; are updated. * If you specify a field in the &#x60;update_mask&#x60;, but don&#39;t specify its value in the source, that field is cleared. * If the &#x60;update_mask&#x60; is not present or empty or has the value &#x60;*&#x60;, then all fields are updated. |  [optional] |



