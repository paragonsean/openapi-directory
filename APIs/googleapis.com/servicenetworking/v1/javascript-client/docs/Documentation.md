# ServiceNetworkingApi.Documentation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**documentationRootUrl** | **String** | The URL to the root of documentation. | [optional] 
**overview** | **String** | Declares a single overview page. For example: documentation: summary: ... overview: (&#x3D;&#x3D; include overview.md &#x3D;&#x3D;) This is a shortcut for the following declaration (using pages style): documentation: summary: ... pages: - name: Overview content: (&#x3D;&#x3D; include overview.md &#x3D;&#x3D;) Note: you cannot specify both &#x60;overview&#x60; field and &#x60;pages&#x60; field. | [optional] 
**pages** | [**[Page]**](Page.md) | The top level pages for the documentation set. | [optional] 
**rules** | [**[DocumentationRule]**](DocumentationRule.md) | A list of documentation rules that apply to individual API elements. **NOTE:** All service configuration rules follow \&quot;last one wins\&quot; order. | [optional] 
**sectionOverrides** | [**[Page]**](Page.md) | Specifies section and content to override boilerplate content provided by go/api-docgen. Currently overrides following sections: 1. rest.service.client_libraries | [optional] 
**serviceRootUrl** | **String** | Specifies the service root url if the default one (the service name from the yaml file) is not suitable. This can be seen in any fully specified service urls as well as sections that show a base that other urls are relative to. | [optional] 
**summary** | **String** | A short description of what the service does. The summary must be plain text. It becomes the overview of the service displayed in Google Cloud Console. NOTE: This field is equivalent to the standard field &#x60;description&#x60;. | [optional] 


