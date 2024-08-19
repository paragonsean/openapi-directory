

# PutFileSystemPolicyRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**policy** | **String** | The &lt;code&gt;FileSystemPolicy&lt;/code&gt; that you&#39;re creating. Accepts a JSON formatted policy definition. EFS file system policies have a 20,000 character limit. To find out more about the elements that make up a file system policy, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/efs/latest/ug/access-control-overview.html#access-control-manage-access-intro-resource-policies\&quot;&gt;EFS Resource-based Policies&lt;/a&gt;.  |  |
|**bypassPolicyLockoutSafetyCheck** | **Boolean** | (Optional) A boolean that specifies whether or not to bypass the &lt;code&gt;FileSystemPolicy&lt;/code&gt; lockout safety check. The lockout safety check determines whether the policy in the request will lock out, or prevent, the IAM principal that is making the request from making future &lt;code&gt;PutFileSystemPolicy&lt;/code&gt; requests on this file system. Set &lt;code&gt;BypassPolicyLockoutSafetyCheck&lt;/code&gt; to &lt;code&gt;True&lt;/code&gt; only when you intend to prevent the IAM principal that is making the request from making subsequent &lt;code&gt;PutFileSystemPolicy&lt;/code&gt; requests on this file system. The default value is &lt;code&gt;False&lt;/code&gt;.  |  [optional] |



