# EnterpriseLicenseManagerApi.LicenseAssignmentList

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**etag** | **String** | ETag of the resource. | [optional] 
**items** | [**[LicenseAssignment]**](LicenseAssignment.md) | The LicenseAssignments in this page of results. | [optional] 
**kind** | **String** | Identifies the resource as a collection of LicenseAssignments. | [optional] [default to &#39;licensing#licenseAssignmentList&#39;]
**nextPageToken** | **String** | The token that you must submit in a subsequent request to retrieve additional license results matching your query parameters. The &#x60;maxResults&#x60; query string is related to the &#x60;nextPageToken&#x60; since &#x60;maxResults&#x60; determines how many entries are returned on each next page. | [optional] 


