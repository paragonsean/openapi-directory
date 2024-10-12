# MigrationCenterApi.AddAssetsToGroupRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allowExisting** | **Boolean** | Optional. When this value is set to &#x60;false&#x60; and one of the given assets is already an existing member of the group, the operation fails with an &#x60;Already Exists&#x60; error. When set to &#x60;true&#x60; this situation is silently ignored by the server. Default value is &#x60;false&#x60;. | [optional] 
**assets** | [**AssetList**](AssetList.md) |  | [optional] 
**requestId** | **String** | Optional. An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server will guarantee that for at least 60 minutes after the first request. For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments. The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000). | [optional] 


