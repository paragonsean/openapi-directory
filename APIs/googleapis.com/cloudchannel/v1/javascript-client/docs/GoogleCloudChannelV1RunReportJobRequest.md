# CloudChannelApi.GoogleCloudChannelV1RunReportJobRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dateRange** | [**GoogleCloudChannelV1DateRange**](GoogleCloudChannelV1DateRange.md) |  | [optional] 
**filter** | **String** | Optional. A structured string that defines conditions on dimension columns to restrict the report output. Filters support logical operators (AND, OR, NOT) and conditional operators (&#x3D;, !&#x3D;, &lt;, &gt;, &lt;&#x3D;, and &gt;&#x3D;) using &#x60;column_id&#x60; as keys. For example: &#x60;(customer:\&quot;accounts/C123abc/customers/S456def\&quot; OR customer:\&quot;accounts/C123abc/customers/S789ghi\&quot;) AND invoice_start_date.year &gt;&#x3D; 2022&#x60; | [optional] 
**languageCode** | **String** | Optional. The BCP-47 language code, such as \&quot;en-US\&quot;. If specified, the response is localized to the corresponding language code if the original data sources support it. Default is \&quot;en-US\&quot;. | [optional] 


