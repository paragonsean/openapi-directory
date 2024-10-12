# SeldonExternalApi.TensorflowTensorShapeProto

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dim** | [**[TensorShapeProtoDim]**](TensorShapeProtoDim.md) | Dimensions of the tensor, such as {\&quot;input\&quot;, 30}, {\&quot;output\&quot;, 40} for a 30 x 40 2D tensor.  If an entry has size -1, this corresponds to a dimension of unknown size. The names are optional. The order of entries in \&quot;dim\&quot; matters: It indicates the layout of the values in the tensor in-memory representation. The first entry in \&quot;dim\&quot; is the outermost dimension used to layout the values, the last entry is the innermost dimension.  This matches the in-memory layout of RowMajor Eigen tensors. If \&quot;dim.size()\&quot; &gt; 0, \&quot;unknown_rank\&quot; must be false. | [optional] 
**unknownRank** | **Boolean** | If true, the number of dimensions in the shape is unknown. If true, \&quot;dim.size()\&quot; must be 0. | [optional] 


