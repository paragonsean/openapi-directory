# OptimadeApi.ReferenceResourceAttributes

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **String** | Meaning of property matches the BiBTeX specification. | [optional] 
**annote** | **String** | Meaning of property matches the BiBTeX specification. | [optional] 
**authors** | [**[Person]**](Person.md) | List of person objects containing the authors of the reference. | [optional] 
**bibType** | **String** | Type of the reference, corresponding to the **type** property in the BiBTeX specification. | [optional] 
**booktitle** | **String** | Meaning of property matches the BiBTeX specification. | [optional] 
**chapter** | **String** | Meaning of property matches the BiBTeX specification. | [optional] 
**crossref** | **String** | Meaning of property matches the BiBTeX specification. | [optional] 
**doi** | **String** | The digital object identifier of the reference. | [optional] 
**edition** | **String** | Meaning of property matches the BiBTeX specification. | [optional] 
**editors** | [**[Person]**](Person.md) | List of person objects containing the editors of the reference. | [optional] 
**howpublished** | **String** | Meaning of property matches the BiBTeX specification. | [optional] 
**immutableId** | **String** | The entry&#39;s immutable ID (e.g., an UUID). This is important for databases having preferred IDs that point to \&quot;the latest version\&quot; of a record, but still offer access to older variants. This ID maps to the version-specific record, in case it changes in the future.  - **Type**: string.  - **Requirements/Conventions**:     - **Support**: OPTIONAL support in implementations, i.e., MAY be &#x60;null&#x60;.     - **Query**: MUST be a queryable property with support for all mandatory filter features.  - **Examples**:     - &#x60;\&quot;8bd3e750-b477-41a0-9b11-3a799f21b44f\&quot;&#x60;     - &#x60;\&quot;fjeiwoj,54;@&#x3D;%&lt;&gt;#32\&quot;&#x60; (Strings that are not URL-safe are allowed.) | [optional] 
**institution** | **String** | Meaning of property matches the BiBTeX specification. | [optional] 
**journal** | **String** | Meaning of property matches the BiBTeX specification. | [optional] 
**key** | **String** | Meaning of property matches the BiBTeX specification. | [optional] 
**lastModified** | **Date** | Date and time representing when the entry was last modified.  - **Type**: timestamp.  - **Requirements/Conventions**:     - **Support**: SHOULD be supported by all implementations, i.e., SHOULD NOT be &#x60;null&#x60;.     - **Query**: MUST be a queryable property with support for all mandatory filter features.     - **Response**: REQUIRED in the response unless the query parameter &#x60;response_fields&#x60; is present and does not include this property.  - **Example**:     - As part of JSON response format: &#x60;\&quot;2007-04-05T14:30:20Z\&quot;&#x60; (i.e., encoded as an [RFC 3339 Internet Date/Time Format](https://tools.ietf.org/html/rfc3339#section-5.6) string.) | 
**month** | **String** | Meaning of property matches the BiBTeX specification. | [optional] 
**note** | **String** | Meaning of property matches the BiBTeX specification. | [optional] 
**number** | **String** | Meaning of property matches the BiBTeX specification. | [optional] 
**organization** | **String** | Meaning of property matches the BiBTeX specification. | [optional] 
**pages** | **String** | Meaning of property matches the BiBTeX specification. | [optional] 
**publisher** | **String** | Meaning of property matches the BiBTeX specification. | [optional] 
**school** | **String** | Meaning of property matches the BiBTeX specification. | [optional] 
**series** | **String** | Meaning of property matches the BiBTeX specification. | [optional] 
**title** | **String** | Meaning of property matches the BiBTeX specification. | [optional] 
**url** | **String** | The URL of the reference. | [optional] 
**volume** | **String** | Meaning of property matches the BiBTeX specification. | [optional] 
**year** | **String** | Meaning of property matches the BiBTeX specification. | [optional] 


