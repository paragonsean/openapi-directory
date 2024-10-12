# ServiceNetworkingApi.Option

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **String** | The option&#39;s name. For protobuf built-in options (options defined in descriptor.proto), this is the short name. For example, &#x60;\&quot;map_entry\&quot;&#x60;. For custom options, it should be the fully-qualified name. For example, &#x60;\&quot;google.api.http\&quot;&#x60;. | [optional] 
**value** | **{String: Object}** | The option&#39;s value packed in an Any message. If the value is a primitive, the corresponding wrapper type defined in google/protobuf/wrappers.proto should be used. If the value is an enum, it should be stored as an int32 value using the google.protobuf.Int32Value type. | [optional] 


