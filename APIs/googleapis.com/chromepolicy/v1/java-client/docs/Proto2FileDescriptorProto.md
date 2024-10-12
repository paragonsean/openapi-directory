

# Proto2FileDescriptorProto

Describes a complete .proto file.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**editionDeprecated** | **String** | BEGIN GOOGLE-INTERNAL TODO(b/297898292) Deprecate and remove this field in favor of enums. END GOOGLE-INTERNAL |  [optional] |
|**enumType** | [**List&lt;Proto2EnumDescriptorProto&gt;**](Proto2EnumDescriptorProto.md) |  |  [optional] |
|**messageType** | [**List&lt;Proto2DescriptorProto&gt;**](Proto2DescriptorProto.md) | All top-level definitions in this file. |  [optional] |
|**name** | **String** | file name, relative to root of source tree |  [optional] |
|**_package** | **String** | e.g. \&quot;foo\&quot;, \&quot;foo.bar\&quot;, etc. |  [optional] |
|**syntax** | **String** | The syntax of the proto file. The supported values are \&quot;proto2\&quot;, \&quot;proto3\&quot;, and \&quot;editions\&quot;. If &#x60;edition&#x60; is present, this value must be \&quot;editions\&quot;. |  [optional] |



