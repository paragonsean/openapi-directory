

# RetrieveCardResponse

Defines the fields that are included in the response body of a request to the [RetrieveCard](#endpoint-cards-retrievecard) endpoint.  Note: if there are errors processing the request, the card field will not be present.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**card** | [**Card**](Card.md) |  |  [optional] |
|**errors** | [**List&lt;Error&gt;**](Error.md) | Information on errors encountered during the request. |  [optional] |



