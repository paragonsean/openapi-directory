

# ListCertificateRevocationListsResponse

Response message for CertificateAuthorityService.ListCertificateRevocationLists.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**certificateRevocationLists** | [**List&lt;CertificateRevocationList&gt;**](CertificateRevocationList.md) | The list of CertificateRevocationLists. |  [optional] |
|**nextPageToken** | **String** | A token to retrieve next page of results. Pass this value in ListCertificateRevocationListsRequest.next_page_token to retrieve the next page of results. |  [optional] |
|**unreachable** | **List&lt;String&gt;** | A list of locations (e.g. \&quot;us-west1\&quot;) that could not be reached. |  [optional] |



