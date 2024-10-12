

# Authorization


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**authorizationUuid** | **String** | Identifier of the Authorization |  |
|**clientUuid** | **String** | The UUID of the client owning the Dataset to which the product is authorized |  |
|**createTimestamp** | **Integer** | Creation timestamp for the Authorization |  |
|**isActive** | **Boolean** | If false, the the authorization is revoked and data access authorizations fail |  |
|**order** | **String** | Optional UUID of the Order that created the Authorization |  [optional] |
|**productUuid** | **String** | Identifier of the Product to be authorized |  |
|**reportCredentials** | [**List&lt;ReportCredentials&gt;**](ReportCredentials.md) |  |  [optional] |
|**reportFiles** | [**List&lt;ReportFile&gt;**](ReportFile.md) |  |  [optional] |
|**scopes** | [**AccessScope**](AccessScope.md) |  |  |
|**sequenceNumber** | **Integer** | The sequence number of the Authorization. Used as a filter when fetching new Authorizations |  [optional] |
|**state** | **String** | The authorization state. One of : [&#39;authorization_state_pending_dataset&#39;, &#39;authorization_state_fulfillable&#39;, &#39;authorization_state_result_available&#39;, &#39;authorization_state_not_fulfillable&#39;] |  |



