

# DescribeOrganizationResourceCollectionHealthRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**organizationResourceCollectionType** | [**OrganizationResourceCollectionTypeEnum**](#OrganizationResourceCollectionTypeEnum) |  An Amazon Web Services resource collection type. This type specifies how analyzed Amazon Web Services resources are defined. The two types of Amazon Web Services resource collections supported are Amazon Web Services CloudFormation stacks and Amazon Web Services resources that contain the same Amazon Web Services tag. DevOps Guru can be configured to analyze the Amazon Web Services resources that are defined in the stacks or that are tagged using the same tag &lt;i&gt;key&lt;/i&gt;. You can specify up to 500 Amazon Web Services CloudFormation stacks.  |  |
|**accountIds** | **List&lt;String&gt;** | The ID of the Amazon Web Services account. |  [optional] |
|**organizationalUnitIds** | **List&lt;String&gt;** | The ID of the organizational unit. |  [optional] |
|**nextToken** | **String** | The pagination token to use to retrieve the next page of results for this operation. If this value is null, it retrieves the first page. |  [optional] |
|**maxResults** | **Integer** | The maximum number of results to return with a single call. To retrieve the remaining results, make another call with the returned &lt;code&gt;nextToken&lt;/code&gt; value. |  [optional] |



## Enum: OrganizationResourceCollectionTypeEnum

| Name | Value |
|---- | -----|
| CLOUD_FORMATION | &quot;AWS_CLOUD_FORMATION&quot; |
| SERVICE | &quot;AWS_SERVICE&quot; |
| ACCOUNT | &quot;AWS_ACCOUNT&quot; |
| TAGS | &quot;AWS_TAGS&quot; |



