

# Api

Api is a light-weight descriptor for an API Interface. Interfaces are also described as \"protocol buffer services\" in some contexts, such as by the \"service\" keyword in a .proto file, but they are different from API Services, which represent a concrete implementation of an interface as opposed to simply a description of methods and bindings. They are also sometimes simply referred to as \"APIs\" in other contexts, such as the name of this message itself. See https://cloud.google.com/apis/design/glossary for detailed terminology.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**methods** | [**List&lt;Method&gt;**](Method.md) | The methods of this interface, in unspecified order. |  [optional] |
|**mixins** | [**List&lt;Mixin&gt;**](Mixin.md) | Included interfaces. See Mixin. |  [optional] |
|**name** | **String** | The fully qualified name of this interface, including package name followed by the interface&#39;s simple name. |  [optional] |
|**options** | [**List&lt;Option&gt;**](Option.md) | Any metadata attached to the interface. |  [optional] |
|**sourceContext** | [**SourceContext**](SourceContext.md) |  |  [optional] |
|**syntax** | [**SyntaxEnum**](#SyntaxEnum) | The source syntax of the service. |  [optional] |
|**version** | **String** | A version string for this interface. If specified, must have the form &#x60;major-version.minor-version&#x60;, as in &#x60;1.10&#x60;. If the minor version is omitted, it defaults to zero. If the entire version field is empty, the major version is derived from the package name, as outlined below. If the field is not empty, the version in the package name will be verified to be consistent with what is provided here. The versioning schema uses [semantic versioning](http://semver.org) where the major version number indicates a breaking change and the minor version an additive, non-breaking change. Both version numbers are signals to users what to expect from different versions, and should be carefully chosen based on the product plan. The major version is also reflected in the package name of the interface, which must end in &#x60;v&#x60;, as in &#x60;google.feature.v1&#x60;. For major versions 0 and 1, the suffix can be omitted. Zero major versions must only be used for experimental, non-GA interfaces.  |  [optional] |



## Enum: SyntaxEnum

| Name | Value |
|---- | -----|
| PROTO2 | &quot;SYNTAX_PROTO2&quot; |
| PROTO3 | &quot;SYNTAX_PROTO3&quot; |
| EDITIONS | &quot;SYNTAX_EDITIONS&quot; |



