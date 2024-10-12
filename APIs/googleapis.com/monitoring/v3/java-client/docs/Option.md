

# Option

A protocol buffer option, which can be attached to a message, field, enumeration, etc.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**name** | **String** | The option&#39;s name. For protobuf built-in options (options defined in descriptor.proto), this is the short name. For example, \&quot;map_entry\&quot;. For custom options, it should be the fully-qualified name. For example, \&quot;google.api.http\&quot;. |  [optional] |
|**value** | **Map&lt;String, Object&gt;** | The option&#39;s value packed in an Any message. If the value is a primitive, the corresponding wrapper type defined in google/protobuf/wrappers.proto should be used. If the value is an enum, it should be stored as an int32 value using the google.protobuf.Int32Value type. |  [optional] |



