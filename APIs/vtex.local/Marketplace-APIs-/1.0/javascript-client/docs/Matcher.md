# Suggestions.Matcher

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **String** | Insert in this field any notes about the approval. This field is optional. | [optional] 
**isActive** | **Boolean** | Whether the matcher is active in the account (&#x60;true&#x60;), or not (&#x60;false&#x60;). | [default to true]
**matcherId** | **String** | Identifies the matching entity. It can be either VTEX&#39;s matcher, or an external matcher developed by partners, for example. The &#x60;matcherId&#x60;&#39;s value can be obtained through the [Get SKU Suggestion by ID](https://developers.vtex.com/vtex-rest-api/reference/getsuggestion) endpoint. | [default to &#39;vtex-matcher&#39;]
**updatesNotificationEndpoint** | **String** | The Received SKUs module uses this endpoint to send updates about a suggestion, to the chosen Matcher. | 
**hookBaseAddress** | **String** | The chosen Matcher&#39;s url. It is the endpoint that the Received SKUs module calls, to send new suggestions for the Matcher&#39;s review. | [default to &#39;http://simple-suggestion-matcher.vtex.com.br&#39;]


