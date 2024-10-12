# ServiceUsageApi.DocumentationRule

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deprecationDescription** | **String** | Deprecation description of the selected element(s). It can be provided if an element is marked as &#x60;deprecated&#x60;. | [optional] 
**description** | **String** | Description of the selected proto element (e.g. a message, a method, a &#39;service&#39; definition, or a field). Defaults to leading &amp; trailing comments taken from the proto source definition of the proto element. | [optional] 
**disableReplacementWords** | **String** | String of comma or space separated case-sensitive words for which method/field name replacement will be disabled by go/api-docgen. | [optional] 
**selector** | **String** | The selector is a comma-separated list of patterns for any element such as a method, a field, an enum value. Each pattern is a qualified name of the element which may end in \&quot;*\&quot;, indicating a wildcard. Wildcards are only allowed at the end and for a whole component of the qualified name, i.e. \&quot;foo.*\&quot; is ok, but not \&quot;foo.b*\&quot; or \&quot;foo.*.bar\&quot;. A wildcard will match one or more components. To specify a default for all applicable elements, the whole pattern \&quot;*\&quot; is used. | [optional] 


