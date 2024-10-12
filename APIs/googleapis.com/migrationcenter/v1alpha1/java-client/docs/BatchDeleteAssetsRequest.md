

# BatchDeleteAssetsRequest

A request to delete a list of asset.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**allowMissing** | **Boolean** | Optional. When this value is set to &#x60;true&#x60; the request is a no-op for non-existing assets. See https://google.aip.dev/135#delete-if-existing for additional details. Default value is &#x60;false&#x60;. |  [optional] |
|**names** | **List&lt;String&gt;** | Required. The IDs of the assets to delete. A maximum of 1000 assets can be deleted in a batch. Format: projects/{project}/locations/{location}/assets/{name}. |  [optional] |



