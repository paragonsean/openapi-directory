# AwsResourceAccessManager.GetPermissionRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**permissionArn** | **String** | Specifies the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\&quot;&gt;Amazon Resource Name (ARN)&lt;/a&gt; of the permission whose contents you want to retrieve. To find the ARN for a permission, use either the &lt;a&gt;ListPermissions&lt;/a&gt; operation or go to the &lt;a href&#x3D;\&quot;https://console.aws.amazon.com/ram/home#Permissions:\&quot;&gt;Permissions library&lt;/a&gt; page in the RAM console and then choose the name of the permission. The ARN is displayed on the detail page. | 
**permissionVersion** | **Number** | &lt;p&gt;Specifies the version number of the RAM permission to retrieve. If you don&#39;t specify this parameter, the operation retrieves the default version.&lt;/p&gt; &lt;p&gt;To see the list of available versions, use &lt;a&gt;ListPermissionVersions&lt;/a&gt;.&lt;/p&gt; | [optional] 


