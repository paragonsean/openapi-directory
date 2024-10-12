# AmazonInteractiveVideoServiceRealTime.ListParticipantsRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filterByPublished** | **Boolean** | Filters the response list to only show participants who published during the stage session. Only one of &lt;code&gt;filterByUserId&lt;/code&gt;, &lt;code&gt;filterByPublished&lt;/code&gt;, or &lt;code&gt;filterByState&lt;/code&gt; can be provided per request. | [optional] 
**filterByState** | **String** | Filters the response list to only show participants in the specified state. Only one of &lt;code&gt;filterByUserId&lt;/code&gt;, &lt;code&gt;filterByPublished&lt;/code&gt;, or &lt;code&gt;filterByState&lt;/code&gt; can be provided per request. | [optional] 
**filterByUserId** | **String** | Filters the response list to match the specified user ID. Only one of &lt;code&gt;filterByUserId&lt;/code&gt;, &lt;code&gt;filterByPublished&lt;/code&gt;, or &lt;code&gt;filterByState&lt;/code&gt; can be provided per request. A &lt;code&gt;userId&lt;/code&gt; is a customer-assigned name to help identify the token; this can be used to link a participant to a user in the customer’s own systems. | [optional] 
**maxResults** | **Number** | Maximum number of results to return. Default: 50. | [optional] 
**nextToken** | **String** | The first participant to retrieve. This is used for pagination; see the &lt;code&gt;nextToken&lt;/code&gt; response field. | [optional] 
**sessionId** | **String** | ID of the session within the stage. | 
**stageArn** | **String** | Stage ARN. | 



## Enum: FilterByStateEnum


* `CONNECTED` (value: `"CONNECTED"`)

* `DISCONNECTED` (value: `"DISCONNECTED"`)




