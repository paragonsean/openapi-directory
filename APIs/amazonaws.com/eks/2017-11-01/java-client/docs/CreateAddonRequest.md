

# CreateAddonRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**addonName** | **String** | The name of the add-on. The name must match one of the names that &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/eks/latest/APIReference/API_DescribeAddonVersions.html\&quot;&gt; &lt;code&gt;DescribeAddonVersions&lt;/code&gt; &lt;/a&gt; returns. |  |
|**addonVersion** | **String** | The version of the add-on. The version must match one of the versions returned by &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/eks/latest/APIReference/API_DescribeAddonVersions.html\&quot;&gt; &lt;code&gt;DescribeAddonVersions&lt;/code&gt; &lt;/a&gt;. |  [optional] |
|**serviceAccountRoleArn** | **String** | &lt;p&gt;The Amazon Resource Name (ARN) of an existing IAM role to bind to the add-on&#39;s service account. The role must be assigned the IAM permissions required by the add-on. If you don&#39;t specify an existing IAM role, then the add-on uses the permissions assigned to the node IAM role. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/eks/latest/userguide/create-node-role.html\&quot;&gt;Amazon EKS node IAM role&lt;/a&gt; in the &lt;i&gt;Amazon EKS User Guide&lt;/i&gt;.&lt;/p&gt; &lt;note&gt; &lt;p&gt;To specify an existing IAM role, you must have an IAM OpenID Connect (OIDC) provider created for your cluster. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/eks/latest/userguide/enable-iam-roles-for-service-accounts.html\&quot;&gt;Enabling IAM roles for service accounts on your cluster&lt;/a&gt; in the &lt;i&gt;Amazon EKS User Guide&lt;/i&gt;.&lt;/p&gt; &lt;/note&gt; |  [optional] |
|**resolveConflicts** | [**ResolveConflictsEnum**](#ResolveConflictsEnum) | &lt;p&gt;How to resolve field value conflicts for an Amazon EKS add-on. Conflicts are handled based on the value you choose:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;b&gt;None&lt;/b&gt; – If the self-managed version of the add-on is installed on your cluster, Amazon EKS doesn&#39;t change the value. Creation of the add-on might fail.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;b&gt;Overwrite&lt;/b&gt; – If the self-managed version of the add-on is installed on your cluster and the Amazon EKS default value is different than the existing value, Amazon EKS changes the value to the Amazon EKS default value.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;b&gt;Preserve&lt;/b&gt; – Not supported. You can set this value when updating an add-on though. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/eks/latest/APIReference/API_UpdateAddon.html\&quot;&gt;UpdateAddon&lt;/a&gt;.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;If you don&#39;t currently have the self-managed version of the add-on installed on your cluster, the Amazon EKS add-on is installed. Amazon EKS sets all values to default values, regardless of the option that you specify.&lt;/p&gt; |  [optional] |
|**clientRequestToken** | **String** | A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. |  [optional] |
|**tags** | **Map&lt;String, String&gt;** | The metadata to apply to the cluster to assist with categorization and organization. Each tag consists of a key and an optional value. You define both. |  [optional] |
|**configurationValues** | **String** | The set of configuration values for the add-on that&#39;s created. The values that you provide are validated against the schema in &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/eks/latest/APIReference/API_DescribeAddonConfiguration.html\&quot;&gt; &lt;code&gt;DescribeAddonConfiguration&lt;/code&gt; &lt;/a&gt;. |  [optional] |



## Enum: ResolveConflictsEnum

| Name | Value |
|---- | -----|
| OVERWRITE | &quot;OVERWRITE&quot; |
| NONE | &quot;NONE&quot; |
| PRESERVE | &quot;PRESERVE&quot; |



