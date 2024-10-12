

# GenerateConfigReportResponse

Response message for GenerateConfigReport method.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**changeReports** | [**List&lt;ChangeReport&gt;**](ChangeReport.md) | list of ChangeReport, each corresponding to comparison between two service configurations. |  [optional] |
|**diagnostics** | [**List&lt;Diagnostic&gt;**](Diagnostic.md) | Errors / Linter warnings associated with the service definition this report belongs to. |  [optional] |
|**id** | **String** | ID of the service configuration this report belongs to. |  [optional] |
|**serviceName** | **String** | Name of the service this report belongs to. |  [optional] |



