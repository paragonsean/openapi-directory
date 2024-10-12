# ApplicationInsightsManagementClient.WorkbookTemplateProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**author** | **String** | Information about the author of the workbook template. | [optional] 
**galleries** | [**[WorkbookTemplateGallery]**](WorkbookTemplateGallery.md) | Workbook galleries supported by the template. | 
**localized** | **{String: [WorkbookTemplateLocalizedGallery]}** | Key value pair of localized gallery. Each key is the locale code of languages supported by the Azure portal. | [optional] 
**priority** | **Number** | Priority of the template. Determines which template to open when a workbook gallery is opened in viewer mode. | [optional] 
**templateData** | **Object** | Valid JSON object containing workbook template payload. | 


