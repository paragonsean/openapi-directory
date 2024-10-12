

# ListCertificateAuthoritiesResponse

Response message for CertificateAuthorityService.ListCertificateAuthorities.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**certificateAuthorities** | [**List&lt;CertificateAuthority&gt;**](CertificateAuthority.md) | The list of CertificateAuthorities. |  [optional] |
|**nextPageToken** | **String** | A token to retrieve next page of results. Pass this value in ListCertificateAuthoritiesRequest.next_page_token to retrieve the next page of results. |  [optional] |
|**unreachable** | **List&lt;String&gt;** | A list of locations (e.g. \&quot;us-west1\&quot;) that could not be reached. |  [optional] |



