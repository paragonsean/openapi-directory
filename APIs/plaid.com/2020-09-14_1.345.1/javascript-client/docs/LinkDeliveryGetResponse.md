# ThePlaidApi.LinkDeliveryGetResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accessTokens** | **[String]** | An array of access tokens associated with the Link Delivery session. | [optional] 
**completedAt** | **Date** | Timestamp in [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format (&#x60;YYYY-MM-DDTHH:mm:ssZ&#x60;) indicating the time the given Link Delivery Session was completed at. | [optional] 
**createdAt** | **Date** | Timestamp in [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format (&#x60;YYYY-MM-DDTHH:mm:ssZ&#x60;) indicating the time the given Link Delivery Session was created at. | 
**itemIds** | **[String]** | An array of &#x60;item_id&#x60;s associated with the Link Delivery session. | [optional] 
**requestId** | **String** | A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid identifiers, is case sensitive. | 
**status** | [**LinkDeliverySessionStatus**](LinkDeliverySessionStatus.md) |  | 


