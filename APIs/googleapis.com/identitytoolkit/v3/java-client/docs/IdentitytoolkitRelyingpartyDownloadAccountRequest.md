

# IdentitytoolkitRelyingpartyDownloadAccountRequest

Request to download user account in batch.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**delegatedProjectNumber** | **String** | GCP project number of the requesting delegated app. Currently only intended for Firebase V1 migration. |  [optional] |
|**maxResults** | **Integer** | The max number of results to return in the response. |  [optional] |
|**nextPageToken** | **String** | The token for the next page. This should be taken from the previous response. |  [optional] |
|**targetProjectId** | **String** | Specify which project (field value is actually project id) to operate. Only used when provided credential. |  [optional] |



