

# WindowsUpdatePackage

Details related to a Windows Update package. Field data and names are taken from Windows Update API IUpdate Interface: https://docs.microsoft.com/en-us/windows/win32/api/_wua/ Descriptive fields like title, and description are localized based on the locale of the VM being updated.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**categories** | [**List&lt;WindowsUpdateCategory&gt;**](WindowsUpdateCategory.md) | The categories that are associated with this update package. |  [optional] |
|**description** | **String** | The localized description of the update package. |  [optional] |
|**kbArticleIds** | **List&lt;String&gt;** | A collection of Microsoft Knowledge Base article IDs that are associated with the update package. |  [optional] |
|**lastDeploymentChangeTime** | **String** | The last published date of the update, in (UTC) date and time. |  [optional] |
|**moreInfoUrls** | **List&lt;String&gt;** | A collection of URLs that provide more information about the update package. |  [optional] |
|**revisionNumber** | **Integer** | The revision number of this update package. |  [optional] |
|**supportUrl** | **String** | A hyperlink to the language-specific support information for the update. |  [optional] |
|**title** | **String** | The localized title of the update package. |  [optional] |
|**updateId** | **String** | Gets the identifier of an update package. Stays the same across revisions. |  [optional] |



