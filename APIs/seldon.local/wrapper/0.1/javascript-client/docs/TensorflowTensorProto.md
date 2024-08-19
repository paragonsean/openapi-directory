# SeldonExternalApi.TensorflowTensorProto

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**boolVal** | **[Boolean]** |  | [optional] 
**dcomplexVal** | **[Number]** | DT_COMPLEX128. dcomplex_val(2*i) and dcomplex_val(2*i+1) are real and imaginary parts of i-th double precision complex. | [optional] 
**doubleVal** | **[Number]** | DT_DOUBLE. | [optional] 
**dtype** | [**TensorflowDataType**](TensorflowDataType.md) |  | [optional] 
**floatVal** | **[Number]** | DT_FLOAT. | [optional] 
**halfVal** | **[Number]** | DT_HALF, DT_BFLOAT16. Note that since protobuf has no int16 type, we&#39;ll have some pointless zero padding for each value here. | [optional] 
**int64Val** | **[String]** |  | [optional] 
**intVal** | **[Number]** | DT_INT32, DT_INT16, DT_INT8, DT_UINT8. | [optional] 
**resourceHandleVal** | [**[TensorflowResourceHandleProto]**](TensorflowResourceHandleProto.md) |  | [optional] 
**scomplexVal** | **[Number]** | DT_COMPLEX64. scomplex_val(2*i) and scomplex_val(2*i+1) are real and imaginary parts of i-th single precision complex. | [optional] 
**stringVal** | **[Blob]** |  | [optional] 
**tensorContent** | **Blob** | Serialized raw tensor content from either Tensor::AsProtoTensorContent or memcpy in tensorflow::grpc::EncodeTensorToByteBuffer. This representation can be used for all tensor types. The purpose of this representation is to reduce serialization overhead during RPC call by avoiding serialization of many repeated small items. | [optional] 
**tensorShape** | [**TensorflowTensorShapeProto**](TensorflowTensorShapeProto.md) |  | [optional] 
**uint32Val** | **[Number]** |  | [optional] 
**uint64Val** | **[String]** |  | [optional] 
**variantVal** | [**[TensorflowVariantTensorDataProto]**](TensorflowVariantTensorDataProto.md) |  | [optional] 
**versionNumber** | **Number** | Version number.  In version 0, if the \&quot;repeated xxx\&quot; representations contain only one element, that element is repeated to fill the shape.  This makes it easy to represent a constant Tensor with a single value. | [optional] 


