

# WorkbookTemplateProperties

Properties that contain a workbook template.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**author** | **String** | Information about the author of the workbook template. |  [optional] |
|**galleries** | [**List&lt;WorkbookTemplateGallery&gt;**](WorkbookTemplateGallery.md) | Workbook galleries supported by the template. |  |
|**localized** | **Map&lt;String, List&lt;WorkbookTemplateLocalizedGallery&gt;&gt;** | Key value pair of localized gallery. Each key is the locale code of languages supported by the Azure portal. |  [optional] |
|**priority** | **Integer** | Priority of the template. Determines which template to open when a workbook gallery is opened in viewer mode. |  [optional] |
|**templateData** | **Object** | Valid JSON object containing workbook template payload. |  |



