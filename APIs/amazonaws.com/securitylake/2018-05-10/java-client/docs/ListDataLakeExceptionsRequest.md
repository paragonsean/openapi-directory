

# ListDataLakeExceptionsRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**maxResults** | **Integer** | List the maximum number of failures in Security Lake. |  [optional] |
|**nextToken** | **String** | &lt;p&gt;List if there are more results available. The value of nextToken is a unique pagination token for each page. Repeat the call using the returned token to retrieve the next page. Keep all other arguments unchanged.&lt;/p&gt; &lt;p&gt;Each pagination token expires after 24 hours. Using an expired pagination token will return an HTTP 400 InvalidToken error.&lt;/p&gt; |  [optional] |
|**regions** | **List&lt;String&gt;** | List the Amazon Web Services Regions from which exceptions are retrieved. |  [optional] |



