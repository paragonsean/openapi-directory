# SeldonExternalApi.TensorShapeProtoDim

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **String** | Optional name of the tensor dimension. | [optional] 
**size** | **String** | Size of the tensor in that dimension. This value must be &gt;&#x3D; -1, but values of -1 are reserved for \&quot;unknown\&quot; shapes (values of -1 mean \&quot;unknown\&quot; dimension).  Certain wrappers that work with TensorShapeProto may fail at runtime when deserializing a TensorShapeProto containing a dim value of -1. | [optional] 


