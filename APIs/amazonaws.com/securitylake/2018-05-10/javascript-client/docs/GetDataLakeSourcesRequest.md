# AmazonSecurityLake.GetDataLakeSourcesRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accounts** | **[String]** | The Amazon Web Services account ID for which a static snapshot of the current Amazon Web Services Region, including enabled accounts and log sources, is retrieved. | [optional] 
**maxResults** | **Number** | The maximum limit of accounts for which the static snapshot of the current Region, including enabled accounts and log sources, is retrieved. | [optional] 
**nextToken** | **String** | &lt;p&gt;Lists if there are more results available. The value of nextToken is a unique pagination token for each page. Repeat the call using the returned token to retrieve the next page. Keep all other arguments unchanged.&lt;/p&gt; &lt;p&gt;Each pagination token expires after 24 hours. Using an expired pagination token will return an HTTP 400 InvalidToken error.&lt;/p&gt; | [optional] 


