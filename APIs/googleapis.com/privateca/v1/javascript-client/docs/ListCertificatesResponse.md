# CertificateAuthorityApi.ListCertificatesResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**certificates** | [**[Certificate]**](Certificate.md) | The list of Certificates. | [optional] 
**nextPageToken** | **String** | A token to retrieve next page of results. Pass this value in ListCertificatesRequest.next_page_token to retrieve the next page of results. | [optional] 
**unreachable** | **[String]** | A list of locations (e.g. \&quot;us-west1\&quot;) that could not be reached. | [optional] 


