# AwsResourceGroups.CreateGroupRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **String** | The name of the group, which is the identifier of the group in other operations. You can&#39;t change the name of a resource group after you create it. A resource group name can consist of letters, numbers, hyphens, periods, and underscores. The name cannot start with &lt;code&gt;AWS&lt;/code&gt; or &lt;code&gt;aws&lt;/code&gt;; these are reserved. A resource group name must be unique within each Amazon Web Services Region in your Amazon Web Services account. | 
**description** | **String** | The description of the resource group. Descriptions can consist of letters, numbers, hyphens, underscores, periods, and spaces. | [optional] 
**resourceQuery** | [**CreateGroupRequestResourceQuery**](CreateGroupRequestResourceQuery.md) |  | [optional] 
**tags** | **{String: String}** | The tags to add to the group. A tag is key-value pair string. | [optional] 
**configuration** | [**[GroupConfigurationItem]**](GroupConfigurationItem.md) | &lt;p&gt;A configuration associates the resource group with an Amazon Web Services service and specifies how the service can interact with the resources in the group. A configuration is an array of &lt;a&gt;GroupConfigurationItem&lt;/a&gt; elements. For details about the syntax of service configurations, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/ARG/latest/APIReference/about-slg.html\&quot;&gt;Service configurations for Resource Groups&lt;/a&gt;.&lt;/p&gt; &lt;note&gt; &lt;p&gt;A resource group can contain either a &lt;code&gt;Configuration&lt;/code&gt; or a &lt;code&gt;ResourceQuery&lt;/code&gt;, but not both.&lt;/p&gt; &lt;/note&gt; | [optional] 


