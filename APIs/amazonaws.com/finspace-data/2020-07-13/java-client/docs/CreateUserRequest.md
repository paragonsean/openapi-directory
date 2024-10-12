

# CreateUserRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**emailAddress** | **String** | The email address of the user that you want to register. The email address serves as a uniquer identifier for each user and cannot be changed after it&#39;s created. |  |
|**type** | [**TypeEnum**](#TypeEnum) | &lt;p&gt;The option to indicate the type of user. Use one of the following options to specify this parameter:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;SUPER_USER&lt;/code&gt; – A user with permission to all the functionality and data in FinSpace.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;APP_USER&lt;/code&gt; – A user with specific permissions in FinSpace. The users are assigned permissions by adding them to a permission group.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; |  |
|**firstName** | **String** | The first name of the user that you want to register. |  [optional] |
|**lastName** | **String** | The last name of the user that you want to register. |  [optional] |
|**apiAccess** | [**ApiAccessEnum**](#ApiAccessEnum) | &lt;p&gt;The option to indicate whether the user can use the &lt;code&gt;GetProgrammaticAccessCredentials&lt;/code&gt; API to obtain credentials that can then be used to access other FinSpace Data API operations.&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;ENABLED&lt;/code&gt; – The user has permissions to use the APIs.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;DISABLED&lt;/code&gt; – The user does not have permissions to use any APIs.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; |  [optional] |
|**apiAccessPrincipalArn** | **String** | The ARN identifier of an AWS user or role that is allowed to call the &lt;code&gt;GetProgrammaticAccessCredentials&lt;/code&gt; API to obtain a credentials token for a specific FinSpace user. This must be an IAM role within your FinSpace account. |  [optional] |
|**clientToken** | **String** | Idempotence Token for API operations |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| SUPER_USER | &quot;SUPER_USER&quot; |
| APP_USER | &quot;APP_USER&quot; |



## Enum: ApiAccessEnum

| Name | Value |
|---- | -----|
| ENABLED | &quot;ENABLED&quot; |
| DISABLED | &quot;DISABLED&quot; |



