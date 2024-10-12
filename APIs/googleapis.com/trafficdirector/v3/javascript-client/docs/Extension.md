# TrafficDirectorApi.Extension

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category** | **String** | Category of the extension. Extension category names use reverse DNS notation. For instance \&quot;envoy.filters.listener\&quot; for Envoy&#39;s built-in listener filters or \&quot;com.acme.filters.http\&quot; for HTTP filters from acme.com vendor. [#comment: | [optional] 
**disabled** | **Boolean** | Indicates that the extension is present but was disabled via dynamic configuration. | [optional] 
**name** | **String** | This is the name of the Envoy filter as specified in the Envoy configuration, e.g. envoy.filters.http.router, com.acme.widget. | [optional] 
**typeDescriptor** | **String** | [#not-implemented-hide:] Type descriptor of extension configuration proto. [#comment: | [optional] 
**typeUrls** | **[String]** | Type URLs of extension configuration protos. | [optional] 
**version** | [**BuildVersion**](BuildVersion.md) |  | [optional] 


