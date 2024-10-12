# AmazonElasticKubernetesService.UpdateAddonRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**addonVersion** | **String** | The version of the add-on. The version must match one of the versions returned by &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/eks/latest/APIReference/API_DescribeAddonVersions.html\&quot;&gt; &lt;code&gt;DescribeAddonVersions&lt;/code&gt; &lt;/a&gt;. | [optional] 
**serviceAccountRoleArn** | **String** | &lt;p&gt;The Amazon Resource Name (ARN) of an existing IAM role to bind to the add-on&#39;s service account. The role must be assigned the IAM permissions required by the add-on. If you don&#39;t specify an existing IAM role, then the add-on uses the permissions assigned to the node IAM role. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/eks/latest/userguide/create-node-role.html\&quot;&gt;Amazon EKS node IAM role&lt;/a&gt; in the &lt;i&gt;Amazon EKS User Guide&lt;/i&gt;.&lt;/p&gt; &lt;note&gt; &lt;p&gt;To specify an existing IAM role, you must have an IAM OpenID Connect (OIDC) provider created for your cluster. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/eks/latest/userguide/enable-iam-roles-for-service-accounts.html\&quot;&gt;Enabling IAM roles for service accounts on your cluster&lt;/a&gt; in the &lt;i&gt;Amazon EKS User Guide&lt;/i&gt;.&lt;/p&gt; &lt;/note&gt; | [optional] 
**resolveConflicts** | **String** | &lt;p&gt;How to resolve field value conflicts for an Amazon EKS add-on if you&#39;ve changed a value from the Amazon EKS default value. Conflicts are handled based on the option you choose:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;b&gt;None&lt;/b&gt; – Amazon EKS doesn&#39;t change the value. The update might fail.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;b&gt;Overwrite&lt;/b&gt; – Amazon EKS overwrites the changed value back to the Amazon EKS default value.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;b&gt;Preserve&lt;/b&gt; – Amazon EKS preserves the value. If you choose this option, we recommend that you test any field and value changes on a non-production cluster before updating the add-on on your production cluster.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; | [optional] 
**clientRequestToken** | **String** | Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. | [optional] 
**configurationValues** | **String** | The set of configuration values for the add-on that&#39;s created. The values that you provide are validated against the schema in &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/eks/latest/APIReference/API_DescribeAddonConfiguration.html\&quot;&gt;DescribeAddonConfiguration&lt;/a&gt;. | [optional] 



## Enum: ResolveConflictsEnum


* `OVERWRITE` (value: `"OVERWRITE"`)

* `NONE` (value: `"NONE"`)

* `PRESERVE` (value: `"PRESERVE"`)




