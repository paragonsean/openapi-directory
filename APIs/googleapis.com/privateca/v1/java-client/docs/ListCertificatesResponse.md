

# ListCertificatesResponse

Response message for CertificateAuthorityService.ListCertificates.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**certificates** | [**List&lt;Certificate&gt;**](Certificate.md) | The list of Certificates. |  [optional] |
|**nextPageToken** | **String** | A token to retrieve next page of results. Pass this value in ListCertificatesRequest.next_page_token to retrieve the next page of results. |  [optional] |
|**unreachable** | **List&lt;String&gt;** | A list of locations (e.g. \&quot;us-west1\&quot;) that could not be reached. |  [optional] |



