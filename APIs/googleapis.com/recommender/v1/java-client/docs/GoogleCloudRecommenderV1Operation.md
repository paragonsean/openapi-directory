

# GoogleCloudRecommenderV1Operation

Contains an operation for a resource loosely based on the JSON-PATCH format with support for: * Custom filters for describing partial array patch. * Extended path values for describing nested arrays. * Custom fields for describing the resource for which the operation is being described. * Allows extension to custom operations not natively supported by RFC6902. See https://tools.ietf.org/html/rfc6902 for details on the original RFC.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**action** | **String** | Type of this operation. Contains one of &#39;add&#39;, &#39;remove&#39;, &#39;replace&#39;, &#39;move&#39;, &#39;copy&#39;, &#39;test&#39; and custom operations. This field is case-insensitive and always populated. |  [optional] |
|**path** | **String** | Path to the target field being operated on. If the operation is at the resource level, then path should be \&quot;/\&quot;. This field is always populated. |  [optional] |
|**pathFilters** | **Map&lt;String, Object&gt;** | Set of filters to apply if &#x60;path&#x60; refers to array elements or nested array elements in order to narrow down to a single unique element that is being tested/modified. This is intended to be an exact match per filter. To perform advanced matching, use path_value_matchers. * Example: &#x60;&#x60;&#x60; { \&quot;/versions/_*_/name\&quot; : \&quot;it-123\&quot; \&quot;/versions/_*_/targetSize/percent\&quot;: 20 } &#x60;&#x60;&#x60; * Example: &#x60;&#x60;&#x60; { \&quot;/bindings/_*_/role\&quot;: \&quot;roles/owner\&quot; \&quot;/bindings/_*_/condition\&quot; : null } &#x60;&#x60;&#x60; * Example: &#x60;&#x60;&#x60; { \&quot;/bindings/_*_/role\&quot;: \&quot;roles/owner\&quot; \&quot;/bindings/_*_/members/_*\&quot; : [\&quot;x@example.com\&quot;, \&quot;y@example.com\&quot;] } &#x60;&#x60;&#x60; When both path_filters and path_value_matchers are set, an implicit AND must be performed. |  [optional] |
|**pathValueMatchers** | [**Map&lt;String, GoogleCloudRecommenderV1ValueMatcher&gt;**](GoogleCloudRecommenderV1ValueMatcher.md) | Similar to path_filters, this contains set of filters to apply if &#x60;path&#x60; field refers to array elements. This is meant to support value matching beyond exact match. To perform exact match, use path_filters. When both path_filters and path_value_matchers are set, an implicit AND must be performed. |  [optional] |
|**resource** | **String** | Contains the fully qualified resource name. This field is always populated. ex: //cloudresourcemanager.googleapis.com/projects/foo. |  [optional] |
|**resourceType** | **String** | Type of GCP resource being modified/tested. This field is always populated. Example: cloudresourcemanager.googleapis.com/Project, compute.googleapis.com/Instance |  [optional] |
|**sourcePath** | **String** | Can be set with action &#39;copy&#39; or &#39;move&#39; to indicate the source field within resource or source_resource, ignored if provided for other operation types. |  [optional] |
|**sourceResource** | **String** | Can be set with action &#39;copy&#39; to copy resource configuration across different resources of the same type. Example: A resource clone can be done via action &#x3D; &#39;copy&#39;, path &#x3D; \&quot;/\&quot;, from &#x3D; \&quot;/\&quot;, source_resource &#x3D; and resource_name &#x3D; . This field is empty for all other values of &#x60;action&#x60;. |  [optional] |
|**value** | **Object** | Value for the &#x60;path&#x60; field. Will be set for actions:&#39;add&#39;/&#39;replace&#39;. Maybe set for action: &#39;test&#39;. Either this or &#x60;value_matcher&#x60; will be set for &#39;test&#39; operation. An exact match must be performed. |  [optional] |
|**valueMatcher** | [**GoogleCloudRecommenderV1ValueMatcher**](GoogleCloudRecommenderV1ValueMatcher.md) |  |  [optional] |



