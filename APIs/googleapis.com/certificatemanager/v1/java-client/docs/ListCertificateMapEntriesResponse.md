

# ListCertificateMapEntriesResponse

Response for the `ListCertificateMapEntries` method.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**certificateMapEntries** | [**List&lt;CertificateMapEntry&gt;**](CertificateMapEntry.md) | A list of certificate map entries for the parent resource. |  [optional] |
|**nextPageToken** | **String** | If there might be more results than those appearing in this response, then &#x60;next_page_token&#x60; is included. To get the next set of results, call this method again using the value of &#x60;next_page_token&#x60; as &#x60;page_token&#x60;. |  [optional] |
|**unreachable** | **List&lt;String&gt;** | Locations that could not be reached. |  [optional] |



