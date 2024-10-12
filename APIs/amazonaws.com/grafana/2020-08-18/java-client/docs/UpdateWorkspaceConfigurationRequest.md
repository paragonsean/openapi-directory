

# UpdateWorkspaceConfigurationRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**_configuration** | **String** | The new configuration string for the workspace. For more information about the format and configuration options available, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/grafana/latest/userguide/AMG-configure-workspace.html\&quot;&gt;Working in your Grafana workspace&lt;/a&gt;. |  |
|**grafanaVersion** | **String** | &lt;p&gt;Specifies the version of Grafana to support in the new workspace.&lt;/p&gt; &lt;p&gt;Can only be used to upgrade (for example, from 8.4 to 9.4), not downgrade (for example, from 9.4 to 8.4).&lt;/p&gt; &lt;p&gt;To know what versions are available to upgrade to for a specific workspace, see the &lt;code&gt;ListVersions&lt;/code&gt; operation.&lt;/p&gt; |  [optional] |



