# MesheryApi.ManagedFieldsEntry

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apiVersion** | **String** | APIVersion defines the version of this resource that this field set applies to. The format is \&quot;group/version\&quot; just like the top-level APIVersion field. It is necessary to track the version of a field set because it cannot be automatically converted. | [optional] 
**fieldsType** | **String** | FieldsType is the discriminator for the different fields format and version. There is currently only one possible value: \&quot;FieldsV1\&quot; | [optional] 
**fieldsV1** | **Object** | Each key is either a &#39;.&#39; representing the field itself, and will always map to an empty set, or a string representing a sub-field or item. The string will follow one of these four formats: &#39;f:&lt;name&gt;&#39;, where &lt;name&gt; is the name of a field in a struct, or key in a map &#39;v:&lt;value&gt;&#39;, where &lt;value&gt; is the exact json formatted value of a list item &#39;i:&lt;index&gt;&#39;, where &lt;index&gt; is position of a item in a list &#39;k:&lt;keys&gt;&#39;, where &lt;keys&gt; is a map of  a list item&#39;s key fields to their unique values If a key maps to an empty Fields value, the field that key represents is part of the set.  The exact format is defined in sigs.k8s.io/structured-merge-diff | [optional] 
**manager** | **String** | Manager is an identifier of the workflow managing these fields. | [optional] 
**operation** | **String** |  | [optional] 
**time** | **Object** | +protobuf.options.marshal&#x3D;false +protobuf.as&#x3D;Timestamp +protobuf.options.(gogoproto.goproto_stringer)&#x3D;false | [optional] 


