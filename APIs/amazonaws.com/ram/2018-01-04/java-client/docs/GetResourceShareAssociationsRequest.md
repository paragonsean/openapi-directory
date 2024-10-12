

# GetResourceShareAssociationsRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**associationType** | [**AssociationTypeEnum**](#AssociationTypeEnum) | &lt;p&gt;Specifies whether you want to retrieve the associations that involve a specified resource or principal.&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;PRINCIPAL&lt;/code&gt; – list the principals whose associations you want to see.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;RESOURCE&lt;/code&gt; – list the resources whose associations you want to see.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; |  |
|**resourceShareArns** | **List&lt;String&gt;** | Specifies a list of &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\&quot;&gt;Amazon Resource Names (ARNs)&lt;/a&gt; of the resource share whose associations you want to retrieve. |  [optional] |
|**resourceArn** | **String** | &lt;p&gt;Specifies the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\&quot;&gt;Amazon Resource Name (ARN)&lt;/a&gt; of a resource whose resource shares you want to retrieve.&lt;/p&gt; &lt;p&gt;You cannot specify this parameter if the association type is &lt;code&gt;PRINCIPAL&lt;/code&gt;.&lt;/p&gt; |  [optional] |
|**principal** | **String** | &lt;p&gt;Specifies the ID of the principal whose resource shares you want to retrieve. This can be an Amazon Web Services account ID, an organization ID, an organizational unit ID, or the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\&quot;&gt;Amazon Resource Name (ARN)&lt;/a&gt; of an individual IAM role or user.&lt;/p&gt; &lt;p&gt;You cannot specify this parameter if the association type is &lt;code&gt;RESOURCE&lt;/code&gt;.&lt;/p&gt; |  [optional] |
|**associationStatus** | [**AssociationStatusEnum**](#AssociationStatusEnum) | Specifies that you want to retrieve only associations that have this status. |  [optional] |
|**nextToken** | **String** | Specifies that you want to receive the next page of results. Valid only if you received a &lt;code&gt;NextToken&lt;/code&gt; response in the previous request. If you did, it indicates that more output is available. Set this parameter to the value provided by the previous call&#39;s &lt;code&gt;NextToken&lt;/code&gt; response to request the next page of results. |  [optional] |
|**maxResults** | **Integer** | Specifies the total number of results that you want included on each page of the response. If you do not include this parameter, it defaults to a value that is specific to the operation. If additional items exist beyond the number you specify, the &lt;code&gt;NextToken&lt;/code&gt; response element is returned with a value (not null). Include the specified value as the &lt;code&gt;NextToken&lt;/code&gt; request parameter in the next call to the operation to get the next part of the results. Note that the service might return fewer results than the maximum even when there are more results available. You should check &lt;code&gt;NextToken&lt;/code&gt; after every operation to ensure that you receive all of the results. |  [optional] |



## Enum: AssociationTypeEnum

| Name | Value |
|---- | -----|
| PRINCIPAL | &quot;PRINCIPAL&quot; |
| RESOURCE | &quot;RESOURCE&quot; |



## Enum: AssociationStatusEnum

| Name | Value |
|---- | -----|
| ASSOCIATING | &quot;ASSOCIATING&quot; |
| ASSOCIATED | &quot;ASSOCIATED&quot; |
| FAILED | &quot;FAILED&quot; |
| DISASSOCIATING | &quot;DISASSOCIATING&quot; |
| DISASSOCIATED | &quot;DISASSOCIATED&quot; |



