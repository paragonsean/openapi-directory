

# UpdatePermissionGroupRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**name** | **String** | The name of the permission group. |  [optional] |
|**description** | **String** | A brief description for the permission group. |  [optional] |
|**applicationPermissions** | **List&lt;ApplicationPermission&gt;** | &lt;p&gt;The permissions that are granted to a specific group for accessing the FinSpace application.&lt;/p&gt; &lt;important&gt; &lt;p&gt;When assigning application permissions, be aware that the permission &lt;code&gt;ManageUsersAndGroups&lt;/code&gt; allows users to grant themselves or others access to any functionality in their FinSpace environment&#39;s application. It should only be granted to trusted users.&lt;/p&gt; &lt;/important&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;CreateDataset&lt;/code&gt; – Group members can create new datasets.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;ManageClusters&lt;/code&gt; – Group members can manage Apache Spark clusters from FinSpace notebooks.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;ManageUsersAndGroups&lt;/code&gt; – Group members can manage users and permission groups. This is a privileged permission that allows users to grant themselves or others access to any functionality in the application. It should only be granted to trusted users.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;ManageAttributeSets&lt;/code&gt; – Group members can manage attribute sets.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;ViewAuditData&lt;/code&gt; – Group members can view audit data.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;AccessNotebooks&lt;/code&gt; – Group members will have access to FinSpace notebooks.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;GetTemporaryCredentials&lt;/code&gt; – Group members can get temporary API credentials.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; |  [optional] |
|**clientToken** | **String** | Idempotence Token for API operations |  [optional] |



