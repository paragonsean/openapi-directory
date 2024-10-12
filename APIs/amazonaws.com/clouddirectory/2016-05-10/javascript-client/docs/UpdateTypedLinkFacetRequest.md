# AmazonCloudDirectory.UpdateTypedLinkFacetRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **String** | The unique name of the typed link facet. | 
**attributeUpdates** | [**[TypedLinkFacetAttributeUpdate]**](TypedLinkFacetAttributeUpdate.md) | Attributes update structure. | 
**identityAttributeOrder** | **[String]** | The order of identity attributes for the facet, from most significant to least significant. The ability to filter typed links considers the order that the attributes are defined on the typed link facet. When providing ranges to a typed link selection, any inexact ranges must be specified at the end. Any attributes that do not have a range specified are presumed to match the entire range. Filters are interpreted in the order of the attributes on the typed link facet, not the order in which they are supplied to any API calls. For more information about identity attributes, see &lt;a href&#x3D;\&quot;http://docs.aws.amazon.com/directoryservice/latest/admin-guide/objectsandlinks.html#typedlink\&quot;&gt;Typed link&lt;/a&gt;. | 


