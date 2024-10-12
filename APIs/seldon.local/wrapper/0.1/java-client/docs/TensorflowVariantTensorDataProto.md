

# TensorflowVariantTensorDataProto

Protocol buffer representing the serialization format of DT_VARIANT tensors.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**metadata** | **byte[]** | Portions of the object that are not Tensors. |  [optional] |
|**tensors** | [**List&lt;TensorflowTensorProto&gt;**](TensorflowTensorProto.md) | Tensors contained within objects being serialized. |  [optional] |
|**typeName** | **String** | Name of the type of objects being serialized. |  [optional] |



