

# GoogleCloudDiscoveryengineV1alphaGcsSource

Cloud Storage location for input content.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**dataSchema** | **String** | The schema to use when parsing the data from the source. Supported values for document imports: * &#x60;document&#x60; (default): One JSON Document per line. Each document must have a valid Document.id. * &#x60;content&#x60;: Unstructured data (e.g. PDF, HTML). Each file matched by &#x60;input_uris&#x60; becomes a document, with the ID set to the first 128 bits of SHA256(URI) encoded as a hex string. * &#x60;custom&#x60;: One custom data JSON per row in arbitrary format that conforms to the defined Schema of the data store. This can only be used by Gen App Builder. * &#x60;csv&#x60;: A CSV file with header conforming to the defined Schema of the data store. Each entry after the header is imported as a Document. This can only be used by Gen App Builder. Supported values for user even imports: * &#x60;user_event&#x60; (default): One JSON UserEvent per line. |  [optional] |
|**inputUris** | **List&lt;String&gt;** | Required. Cloud Storage URIs to input files. URI can be up to 2000 characters long. URIs can match the full object path (for example, &#x60;gs://bucket/directory/object.json&#x60;) or a pattern matching one or more files, such as &#x60;gs://bucket/directory/_*.json&#x60;. A request can contain at most 100 files (or 100,000 files if &#x60;data_schema&#x60; is &#x60;content&#x60;). Each file can be up to 2 GB (or 100 MB if &#x60;data_schema&#x60; is &#x60;content&#x60;). |  [optional] |



