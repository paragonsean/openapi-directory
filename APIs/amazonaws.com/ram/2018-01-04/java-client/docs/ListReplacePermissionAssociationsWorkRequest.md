

# ListReplacePermissionAssociationsWorkRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**workIds** | **List&lt;String&gt;** | A list of IDs. These values come from the &lt;code&gt;id&lt;/code&gt;field of the &lt;code&gt;replacePermissionAssociationsWork&lt;/code&gt;structure returned by the &lt;a&gt;ReplacePermissionAssociations&lt;/a&gt; operation.  |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | Specifies that you want to see only the details about requests with a status that matches this value. |  [optional] |
|**nextToken** | **String** | Specifies that you want to receive the next page of results. Valid only if you received a &lt;code&gt;NextToken&lt;/code&gt; response in the previous request. If you did, it indicates that more output is available. Set this parameter to the value provided by the previous call&#39;s &lt;code&gt;NextToken&lt;/code&gt; response to request the next page of results. |  [optional] |
|**maxResults** | **Integer** | Specifies the total number of results that you want included on each page of the response. If you do not include this parameter, it defaults to a value that is specific to the operation. If additional items exist beyond the number you specify, the &lt;code&gt;NextToken&lt;/code&gt; response element is returned with a value (not null). Include the specified value as the &lt;code&gt;NextToken&lt;/code&gt; request parameter in the next call to the operation to get the next part of the results. Note that the service might return fewer results than the maximum even when there are more results available. You should check &lt;code&gt;NextToken&lt;/code&gt; after every operation to ensure that you receive all of the results. |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| IN_PROGRESS | &quot;IN_PROGRESS&quot; |
| COMPLETED | &quot;COMPLETED&quot; |
| FAILED | &quot;FAILED&quot; |



