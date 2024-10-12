

# WindowsUpdate

Windows Update represents the metadata about the update for the Windows operating system. The fields in this message come from the Windows Update API documented at https://docs.microsoft.com/en-us/windows/win32/api/wuapi/nn-wuapi-iupdate.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**categories** | [**List&lt;Category&gt;**](Category.md) | The list of categories to which the update belongs. |  [optional] |
|**description** | **String** | The localized description of the update. |  [optional] |
|**identity** | [**Identity**](Identity.md) |  |  [optional] |
|**kbArticleIds** | **List&lt;String&gt;** | The Microsoft Knowledge Base article IDs that are associated with the update. |  [optional] |
|**lastPublishedTimestamp** | **String** | The last published timestamp of the update. |  [optional] |
|**supportUrl** | **String** | The hyperlink to the support information for the update. |  [optional] |
|**title** | **String** | The localized title of the update. |  [optional] |



