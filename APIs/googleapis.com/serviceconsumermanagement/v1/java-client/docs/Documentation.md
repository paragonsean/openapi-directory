

# Documentation

`Documentation` provides the information for describing a service. Example: documentation: summary: > The Google Calendar API gives access to most calendar features. pages: - name: Overview content: (== include google/foo/overview.md ==) - name: Tutorial content: (== include google/foo/tutorial.md ==) subpages: - name: Java content: (== include google/foo/tutorial_java.md ==) rules: - selector: google.calendar.Calendar.Get description: > ... - selector: google.calendar.Calendar.Put description: > ... Documentation is provided in markdown syntax. In addition to standard markdown features, definition lists, tables and fenced code blocks are supported. Section headers can be provided and are interpreted relative to the section nesting of the context where a documentation fragment is embedded. Documentation from the IDL is merged with documentation defined via the config at normalization time, where documentation provided by config rules overrides IDL provided. A number of constructs specific to the API platform are supported in documentation text. In order to reference a proto element, the following notation can be used: [fully.qualified.proto.name][] To override the display text used for the link, this can be used: [display text][fully.qualified.proto.name] Text can be excluded from doc using the following notation: (-- internal comment --) A few directives are available in documentation. Note that directives must appear on a single line to be properly identified. The `include` directive includes a markdown file from an external source: (== include path/to/file ==) The `resource_for` directive marks a message to be the resource of a collection in REST view. If it is not specified, tools attempt to infer the resource from the operations in a collection: (== resource_for v1.shelves.books ==) The directive `suppress_warning` does not directly affect documentation and is documented together with service config validation.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**documentationRootUrl** | **String** | The URL to the root of documentation. |  [optional] |
|**overview** | **String** | Declares a single overview page. For example: documentation: summary: ... overview: (&#x3D;&#x3D; include overview.md &#x3D;&#x3D;) This is a shortcut for the following declaration (using pages style): documentation: summary: ... pages: - name: Overview content: (&#x3D;&#x3D; include overview.md &#x3D;&#x3D;) Note: you cannot specify both &#x60;overview&#x60; field and &#x60;pages&#x60; field. |  [optional] |
|**pages** | [**List&lt;Page&gt;**](Page.md) | The top level pages for the documentation set. |  [optional] |
|**rules** | [**List&lt;DocumentationRule&gt;**](DocumentationRule.md) | A list of documentation rules that apply to individual API elements. **NOTE:** All service configuration rules follow \&quot;last one wins\&quot; order. |  [optional] |
|**sectionOverrides** | [**List&lt;Page&gt;**](Page.md) | Specifies section and content to override boilerplate content provided by go/api-docgen. Currently overrides following sections: 1. rest.service.client_libraries |  [optional] |
|**serviceRootUrl** | **String** | Specifies the service root url if the default one (the service name from the yaml file) is not suitable. This can be seen in any fully specified service urls as well as sections that show a base that other urls are relative to. |  [optional] |
|**summary** | **String** | A short description of what the service does. The summary must be plain text. It becomes the overview of the service displayed in Google Cloud Console. NOTE: This field is equivalent to the standard field &#x60;description&#x60;. |  [optional] |



