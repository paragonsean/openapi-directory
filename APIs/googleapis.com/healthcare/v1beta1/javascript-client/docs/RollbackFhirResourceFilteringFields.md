# CloudHealthcareApi.RollbackFhirResourceFilteringFields

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadataFilter** | **String** | Optional. A filter expression that matches data in the &#x60;Resource.meta&#x60; element. Supports all filters in [AIP-160](https://google.aip.dev/160) except the \&quot;has\&quot; (&#x60;:&#x60;) operator. Supports the following custom functions: * &#x60;tag(\&quot;\&quot;) &#x3D; \&quot;\&quot;&#x60; for tag filtering. * &#x60;extension_value_ts(\&quot;\&quot;) &#x3D; &#x60; for filtering extensions with a timestamp, where &#x60;&#x60; is a Unix timestamp. Supports the &#x60;&gt;&#x60;, &#x60;&lt;&#x60;, &#x60;&lt;&#x3D;&#x60;, &#x60;&gt;&#x3D;&#x60;, and &#x60;!&#x3D;&#x60; comparison operators. | [optional] 
**operationIds** | **[String]** | Optional. A list of operation IDs to roll back. Only changes made by these operations will be rolled back. | [optional] 


