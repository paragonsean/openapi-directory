# ApigeeRegistryApi.ApiDeployment

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accessGuidance** | **String** | Text briefly describing how to access the endpoint. Changes to this value will not affect the revision. | [optional] 
**annotations** | **{String: String}** | Annotations attach non-identifying metadata to resources. Annotation keys and values are less restricted than those of labels, but should be generally used for small values of broad interest. Larger, topic- specific metadata should be stored in Artifacts. | [optional] 
**apiSpecRevision** | **String** | The full resource name (including revision ID) of the spec of the API being served by the deployment. Changes to this value will update the revision. Format: &#x60;projects/{project}/locations/{location}/apis/{api}/versions/{version}/specs/{spec@revision}&#x60; | [optional] 
**createTime** | **String** | Output only. Creation timestamp; when the deployment resource was created. | [optional] [readonly] 
**description** | **String** | A detailed description. | [optional] 
**displayName** | **String** | Human-meaningful name. | [optional] 
**endpointUri** | **String** | The address where the deployment is serving. Changes to this value will update the revision. | [optional] 
**externalChannelUri** | **String** | The address of the external channel of the API (e.g., the Developer Portal). Changes to this value will not affect the revision. | [optional] 
**intendedAudience** | **String** | Text briefly identifying the intended audience of the API. Changes to this value will not affect the revision. | [optional] 
**labels** | **{String: String}** | Labels attach identifying metadata to resources. Identifying metadata can be used to filter list operations. Label keys and values can be no longer than 64 characters (Unicode codepoints), can only contain lowercase letters, numeric characters, underscores and dashes. International characters are allowed. No more than 64 user labels can be associated with one resource (System labels are excluded). See https://goo.gl/xmQnxf for more information and examples of labels. System reserved label keys are prefixed with &#x60;apigeeregistry.googleapis.com/&#x60; and cannot be changed. | [optional] 
**name** | **String** | Resource name. | [optional] 
**revisionCreateTime** | **String** | Output only. Revision creation timestamp; when the represented revision was created. | [optional] [readonly] 
**revisionId** | **String** | Output only. Immutable. The revision ID of the deployment. A new revision is committed whenever the deployment contents are changed. The format is an 8-character hexadecimal string. | [optional] [readonly] 
**revisionUpdateTime** | **String** | Output only. Last update timestamp: when the represented revision was last modified. | [optional] [readonly] 


