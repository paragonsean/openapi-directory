

# ListCaPoolsResponse

Response message for CertificateAuthorityService.ListCaPools.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**caPools** | [**List&lt;CaPool&gt;**](CaPool.md) | The list of CaPools. |  [optional] |
|**nextPageToken** | **String** | A token to retrieve next page of results. Pass this value in ListCertificateAuthoritiesRequest.next_page_token to retrieve the next page of results. |  [optional] |
|**unreachable** | **List&lt;String&gt;** | A list of locations (e.g. \&quot;us-west1\&quot;) that could not be reached. |  [optional] |



