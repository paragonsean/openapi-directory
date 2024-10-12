# ApigeeApi.GoogleCloudApigeeV1ListSecurityReportsResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**nextPageToken** | **String** | If the number of security reports exceeded the page size requested, the token can be used to fetch the next page in a subsequent call. If the response is the last page and there are no more reports to return this field is left empty. | [optional] 
**securityReports** | [**[GoogleCloudApigeeV1SecurityReport]**](GoogleCloudApigeeV1SecurityReport.md) | The security reports belong to requested resource name. | [optional] 


