

# TensorflowTensorProto

Protocol buffer representing a tensor.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**boolVal** | **List&lt;Boolean&gt;** |  |  [optional] |
|**dcomplexVal** | **List&lt;Double&gt;** | DT_COMPLEX128. dcomplex_val(2*i) and dcomplex_val(2*i+1) are real and imaginary parts of i-th double precision complex. |  [optional] |
|**doubleVal** | **List&lt;Double&gt;** | DT_DOUBLE. |  [optional] |
|**dtype** | **TensorflowDataType** |  |  [optional] |
|**floatVal** | **List&lt;Float&gt;** | DT_FLOAT. |  [optional] |
|**halfVal** | **List&lt;Integer&gt;** | DT_HALF, DT_BFLOAT16. Note that since protobuf has no int16 type, we&#39;ll have some pointless zero padding for each value here. |  [optional] |
|**int64Val** | **List&lt;String&gt;** |  |  [optional] |
|**intVal** | **List&lt;Integer&gt;** | DT_INT32, DT_INT16, DT_INT8, DT_UINT8. |  [optional] |
|**resourceHandleVal** | [**List&lt;TensorflowResourceHandleProto&gt;**](TensorflowResourceHandleProto.md) |  |  [optional] |
|**scomplexVal** | **List&lt;Float&gt;** | DT_COMPLEX64. scomplex_val(2*i) and scomplex_val(2*i+1) are real and imaginary parts of i-th single precision complex. |  [optional] |
|**stringVal** | **List&lt;byte[]&gt;** |  |  [optional] |
|**tensorContent** | **byte[]** | Serialized raw tensor content from either Tensor::AsProtoTensorContent or memcpy in tensorflow::grpc::EncodeTensorToByteBuffer. This representation can be used for all tensor types. The purpose of this representation is to reduce serialization overhead during RPC call by avoiding serialization of many repeated small items. |  [optional] |
|**tensorShape** | [**TensorflowTensorShapeProto**](TensorflowTensorShapeProto.md) |  |  [optional] |
|**uint32Val** | **List&lt;Long&gt;** |  |  [optional] |
|**uint64Val** | **List&lt;String&gt;** |  |  [optional] |
|**variantVal** | [**List&lt;TensorflowVariantTensorDataProto&gt;**](TensorflowVariantTensorDataProto.md) |  |  [optional] |
|**versionNumber** | **Integer** | Version number. In version 0, if the \&quot;repeated xxx\&quot; representations contain only one element, that element is repeated to fill the shape.  This makes it easy to represent a constant Tensor with a single value. |  [optional] |



