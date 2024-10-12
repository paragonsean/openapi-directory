

# QuotaTicketDetails

Additional set of information required for quota increase support ticket for certain quota types, e.g.: Virtual machine cores. Get complete details about Quota payload support request along with examples at <a target='' href='https://aka.ms/supportrpquotarequestpayload'>Support quota request</a>.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**quotaChangeRequestSubType** | **String** | Required for certain quota types when there is a sub type that you are requesting quota increase for. Example: Batch |  [optional] |
|**quotaChangeRequestVersion** | **String** | Quota change request version |  [optional] |
|**quotaChangeRequests** | [**List&lt;QuotaChangeRequest&gt;**](QuotaChangeRequest.md) | This property is required for providing the region and new quota limits. |  [optional] |



