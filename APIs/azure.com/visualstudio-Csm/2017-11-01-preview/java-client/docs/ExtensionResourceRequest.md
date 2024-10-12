

# ExtensionResourceRequest

The body of an extension resource PUT request.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**location** | **String** | The Azure region of the Visual Studio account associated with this request (i.e &#39;southcentralus&#39;.) |  [optional] |
|**plan** | [**ExtensionResourcePlan**](ExtensionResourcePlan.md) |  |  [optional] |
|**properties** | **Map&lt;String, String&gt;** | A dictionary of extended properties. This property is currently unused. |  [optional] |
|**tags** | **Map&lt;String, String&gt;** | A dictionary of user-defined tags to be stored with the extension resource. |  [optional] |



