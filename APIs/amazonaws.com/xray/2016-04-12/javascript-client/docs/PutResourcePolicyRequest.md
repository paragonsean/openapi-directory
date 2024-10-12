# AwsXRay.PutResourcePolicyRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**policyName** | **String** | The name of the resource policy. Must be unique within a specific Amazon Web Services account. | 
**policyDocument** | **String** | The resource policy document, which can be up to 5kb in size. | 
**policyRevisionId** | **String** | &lt;p&gt;Specifies a specific policy revision, to ensure an atomic create operation. By default the resource policy is created if it does not exist, or updated with an incremented revision id. The revision id is unique to each policy in the account.&lt;/p&gt; &lt;p&gt;If the policy revision id does not match the latest revision id, the operation will fail with an &lt;code&gt;InvalidPolicyRevisionIdException&lt;/code&gt; exception. You can also provide a &lt;code&gt;PolicyRevisionId&lt;/code&gt; of 0. In this case, the operation will fail with an &lt;code&gt;InvalidPolicyRevisionIdException&lt;/code&gt; exception if a resource policy with the same name already exists. &lt;/p&gt; | [optional] 
**bypassPolicyLockoutCheck** | **Boolean** | &lt;p&gt;A flag to indicate whether to bypass the resource policy lockout safety check.&lt;/p&gt; &lt;important&gt; &lt;p&gt;Setting this value to true increases the risk that the policy becomes unmanageable. Do not set this value to true indiscriminately.&lt;/p&gt; &lt;/important&gt; &lt;p&gt;Use this parameter only when you include a policy in the request and you intend to prevent the principal that is making the request from making a subsequent &lt;code&gt;PutResourcePolicy&lt;/code&gt; request.&lt;/p&gt; &lt;p&gt;The default value is false.&lt;/p&gt; | [optional] 


