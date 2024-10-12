

# ListCertificateTemplatesResponse

Response message for CertificateAuthorityService.ListCertificateTemplates.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**certificateTemplates** | [**List&lt;CertificateTemplate&gt;**](CertificateTemplate.md) | The list of CertificateTemplates. |  [optional] |
|**nextPageToken** | **String** | A token to retrieve next page of results. Pass this value in ListCertificateTemplatesRequest.next_page_token to retrieve the next page of results. |  [optional] |
|**unreachable** | **List&lt;String&gt;** | A list of locations (e.g. \&quot;us-west1\&quot;) that could not be reached. |  [optional] |



