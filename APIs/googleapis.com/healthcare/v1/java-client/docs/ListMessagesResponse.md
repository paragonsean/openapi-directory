

# ListMessagesResponse

Lists the messages in the specified HL7v2 store.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**hl7V2Messages** | [**List&lt;Message&gt;**](Message.md) | The returned Messages. Won&#39;t be more Messages than the value of page_size in the request. See view for populated fields. |  [optional] |
|**nextPageToken** | **String** | Token to retrieve the next page of results or empty if there are no more results in the list. |  [optional] |



