# ServiceControlApi.CheckInfo

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apiKeyUid** | **String** | The unique id of the api key in the format of \&quot;apikey:\&quot;. This field will be populated when the consumer passed to Chemist is an API key and all the API key related validations are successful. | [optional] 
**consumerInfo** | [**ConsumerInfo**](ConsumerInfo.md) |  | [optional] 
**unusedArguments** | **[String]** | A list of fields and label keys that are ignored by the server. The client doesn&#39;t need to send them for following requests to improve performance and allow better aggregation. | [optional] 


