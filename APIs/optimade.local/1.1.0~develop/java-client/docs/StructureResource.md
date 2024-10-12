

# StructureResource

Representing a structure.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**attributes** | [**StructureResourceAttributes**](StructureResourceAttributes.md) |  |  |
|**id** | **String** | An entry&#39;s ID as defined in section Definition of Terms.  - **Type**: string.  - **Requirements/Conventions**:     - **Support**: MUST be supported by all implementations, MUST NOT be &#x60;null&#x60;.     - **Query**: MUST be a queryable property with support for all mandatory filter features.     - **Response**: REQUIRED in the response.  - **Examples**:     - &#x60;\&quot;db/1234567\&quot;&#x60;     - &#x60;\&quot;cod/2000000\&quot;&#x60;     - &#x60;\&quot;cod/2000000@1234567\&quot;&#x60;     - &#x60;\&quot;nomad/L1234567890\&quot;&#x60;     - &#x60;\&quot;42\&quot;&#x60; |  |
|**links** | [**ResourceLinks**](ResourceLinks.md) | a links object containing links related to the resource. |  [optional] |
|**meta** | **Object** | a meta object containing non-standard meta-information about a resource that can not be represented as an attribute or relationship. |  [optional] |
|**relationships** | [**EntryRelationships**](EntryRelationships.md) | A dictionary containing references to other entries according to the description in section Relationships encoded as [JSON API Relationships](https://jsonapi.org/format/1.0/#document-resource-object-relationships). The OPTIONAL human-readable description of the relationship MAY be provided in the &#x60;description&#x60; field inside the &#x60;meta&#x60; dictionary of the JSON API resource identifier object. |  [optional] |
|**type** | **String** | The name of the type of an entry.  - **Type**: string.  - **Requirements/Conventions**:     - **Support**: MUST be supported by all implementations, MUST NOT be &#x60;null&#x60;.     - **Query**: MUST be a queryable property with support for all mandatory filter features.     - **Response**: REQUIRED in the response.     - MUST be an existing entry type.     - The entry of type &#x60;&lt;type&gt;&#x60; and ID &#x60;&lt;id&gt;&#x60; MUST be returned in response to a request for &#x60;/&lt;type&gt;/&lt;id&gt;&#x60; under the versioned base URL.  - **Examples**:     - &#x60;\&quot;structures\&quot;&#x60; |  |



