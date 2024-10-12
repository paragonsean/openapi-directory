

# RegisterResourceRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**resourceArn** | **String** | The Amazon Resource Name (ARN) of the resource that you want to register. |  |
|**useServiceLinkedRole** | **Boolean** | &lt;p&gt;Designates an Identity and Access Management (IAM) service-linked role by registering this role with the Data Catalog. A service-linked role is a unique type of IAM role that is linked directly to Lake Formation.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/lake-formation/latest/dg/service-linked-roles.html\&quot;&gt;Using Service-Linked Roles for Lake Formation&lt;/a&gt;.&lt;/p&gt; |  [optional] |
|**roleArn** | **String** | The identifier for the role that registers the resource. |  [optional] |
|**withFederation** | **Boolean** | Whether or not the resource is a federated resource. |  [optional] |



