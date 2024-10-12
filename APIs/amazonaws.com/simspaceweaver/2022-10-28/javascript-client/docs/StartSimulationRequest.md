# AwsSimSpaceWeaver.StartSimulationRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**clientToken** | **String** | A value that you provide to ensure that repeated calls to this API operation using the same parameters complete only once. A &lt;code&gt;ClientToken&lt;/code&gt; is also known as an &lt;i&gt;idempotency token&lt;/i&gt;. A &lt;code&gt;ClientToken&lt;/code&gt; expires after 24 hours. | [optional] 
**description** | **String** | The description of the simulation. | [optional] 
**maximumDuration** | **String** | The maximum running time of the simulation, specified as a number of minutes (m or M), hours (h or H), or days (d or D). The simulation stops when it reaches this limit. The maximum value is &lt;code&gt;14D&lt;/code&gt;, or its equivalent in the other units. The default value is &lt;code&gt;14D&lt;/code&gt;. A value equivalent to &lt;code&gt;0&lt;/code&gt; makes the simulation immediately transition to &lt;code&gt;Stopping&lt;/code&gt; as soon as it reaches &lt;code&gt;Started&lt;/code&gt;. | [optional] 
**name** | **String** | The name of the simulation. | 
**roleArn** | **String** | The Amazon Resource Name (ARN) of the Identity and Access Management (IAM) role that the simulation assumes to perform actions. For more information about ARNs, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\&quot;&gt;Amazon Resource Names (ARNs)&lt;/a&gt; in the &lt;i&gt;Amazon Web Services General Reference&lt;/i&gt;. For more information about IAM roles, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html\&quot;&gt;IAM roles&lt;/a&gt; in the &lt;i&gt;Identity and Access Management User Guide&lt;/i&gt;. | 
**schemaS3Location** | [**StartSimulationRequestSchemaS3Location**](StartSimulationRequestSchemaS3Location.md) |  | [optional] 
**snapshotS3Location** | [**StartSimulationRequestSchemaS3Location**](StartSimulationRequestSchemaS3Location.md) |  | [optional] 
**tags** | **{String: String}** | A list of tags for the simulation. For more information about tags, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html\&quot;&gt;Tagging Amazon Web Services resources&lt;/a&gt; in the &lt;i&gt;Amazon Web Services General Reference&lt;/i&gt;. | [optional] 


