

# ListVerificationsResponse

Response message for Verifications.ListVerifications.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**nextPageToken** | **String** | If the number of verifications exceeded the requested page size, this field will be populated with a token to fetch the next page of verification on a subsequent call. If there are no more attributes, this field will not be present in the response. |  [optional] |
|**verifications** | [**List&lt;Verification&gt;**](Verification.md) | List of the verifications. |  [optional] |



