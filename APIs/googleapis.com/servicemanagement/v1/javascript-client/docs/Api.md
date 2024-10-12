# ServiceManagementApi.Api

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**methods** | [**[Method]**](Method.md) | The methods of this interface, in unspecified order. | [optional] 
**mixins** | [**[Mixin]**](Mixin.md) | Included interfaces. See Mixin. | [optional] 
**name** | **String** | The fully qualified name of this interface, including package name followed by the interface&#39;s simple name. | [optional] 
**options** | [**[Option]**](Option.md) | Any metadata attached to the interface. | [optional] 
**sourceContext** | [**SourceContext**](SourceContext.md) |  | [optional] 
**syntax** | **String** | The source syntax of the service. | [optional] 
**version** | **String** | A version string for this interface. If specified, must have the form &#x60;major-version.minor-version&#x60;, as in &#x60;1.10&#x60;. If the minor version is omitted, it defaults to zero. If the entire version field is empty, the major version is derived from the package name, as outlined below. If the field is not empty, the version in the package name will be verified to be consistent with what is provided here. The versioning schema uses [semantic versioning](http://semver.org) where the major version number indicates a breaking change and the minor version an additive, non-breaking change. Both version numbers are signals to users what to expect from different versions, and should be carefully chosen based on the product plan. The major version is also reflected in the package name of the interface, which must end in &#x60;v&#x60;, as in &#x60;google.feature.v1&#x60;. For major versions 0 and 1, the suffix can be omitted. Zero major versions must only be used for experimental, non-GA interfaces.  | [optional] 



## Enum: SyntaxEnum


* `PROTO2` (value: `"SYNTAX_PROTO2"`)

* `PROTO3` (value: `"SYNTAX_PROTO3"`)

* `EDITIONS` (value: `"SYNTAX_EDITIONS"`)




