

# GoogleChromeManagementV1CountPrintJobsByUserResponse

Response containing a summary printing report for each user that has initiated a print job with a printer from the specified organizational unit during the requested time interval.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**nextPageToken** | **String** | Pagination token for requesting the next page. |  [optional] |
|**totalSize** | **String** | Total number of users matching request. |  [optional] |
|**userPrintReports** | [**List&lt;GoogleChromeManagementV1UserPrintReport&gt;**](GoogleChromeManagementV1UserPrintReport.md) | List of UserPrintReports matching request. |  [optional] |



