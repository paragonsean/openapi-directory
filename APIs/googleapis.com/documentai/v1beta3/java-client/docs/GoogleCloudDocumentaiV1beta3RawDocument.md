

# GoogleCloudDocumentaiV1beta3RawDocument

Payload message of raw document content (bytes).

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**content** | **byte[]** | Inline document content. |  [optional] |
|**displayName** | **String** | The display name of the document, it supports all Unicode characters except the following: &#x60;*&#x60;, &#x60;?&#x60;, &#x60;[&#x60;, &#x60;]&#x60;, &#x60;%&#x60;, &#x60;{&#x60;, &#x60;}&#x60;,&#x60;&#39;&#x60;, &#x60;\\\&quot;&#x60;, &#x60;,&#x60; &#x60;~&#x60;, &#x60;&#x3D;&#x60; and &#x60;:&#x60; are reserved. If not specified, a default ID is generated. |  [optional] |
|**mimeType** | **String** | An IANA MIME type (RFC6838) indicating the nature and format of the content. |  [optional] |



