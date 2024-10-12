

# ServiceEndpoint

The endpoint to which service requests can be submitted, including the actual URL prefix for sending requests and the Amazon Resource Name (ARN) so the endpoint can be referenced in other API calls such as <a>UpdateServiceAccessPolicies</a>.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**arn** | **String** | An Amazon Resource Name (ARN). See &lt;a href&#x3D;\&quot;http://docs.aws.amazon.com/IAM/latest/UserGuide/index.html?Using_Identifiers.html\&quot; target&#x3D;\&quot;_blank\&quot;&gt;Identifiers for IAM Entities&lt;/a&gt; in &lt;i&gt;Using AWS Identity and Access Management&lt;/i&gt; for more information. |  [optional] |
|**endpoint** | **String** | The URL (including /version/pathPrefix) to which service requests can be submitted. |  [optional] |



