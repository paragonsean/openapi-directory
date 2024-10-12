

# GoogleCloudMlV1SuggestTrialsRequest

The request message for the SuggestTrial service method.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**clientId** | **String** | Required. The identifier of the client that is requesting the suggestion. If multiple SuggestTrialsRequests have the same &#x60;client_id&#x60;, the service will return the identical suggested trial if the trial is pending, and provide a new trial if the last suggested trial was completed. |  [optional] |
|**suggestionCount** | **Integer** | Required. The number of suggestions requested. |  [optional] |



