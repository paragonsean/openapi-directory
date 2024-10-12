

# TemplateArtifact

Blueprint artifact that deploys a Resource Manager template.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**properties** | [**TemplateArtifactProperties**](TemplateArtifactProperties.md) |  |  |
|**kind** | [**KindEnum**](#KindEnum) | Specifies the kind of blueprint artifact. |  |
|**id** | **String** | String Id used to locate any resource on Azure. |  [optional] [readonly] |
|**name** | **String** | Name of this resource. |  [optional] [readonly] |
|**type** | **String** | Type of this resource. |  [optional] [readonly] |



## Enum: KindEnum

| Name | Value |
|---- | -----|
| TEMPLATE | &quot;template&quot; |
| ROLE_ASSIGNMENT | &quot;roleAssignment&quot; |
| POLICY_ASSIGNMENT | &quot;policyAssignment&quot; |



