

# Artifact

Represents a Blueprint artifact.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**kind** | [**KindEnum**](#KindEnum) | Specifies the kind of Blueprint artifact. |  |
|**id** | **String** | String Id used to locate any resource on Azure. |  [optional] [readonly] |
|**name** | **String** | Name of this resource. |  [optional] [readonly] |
|**type** | **String** | Type of this resource. |  [optional] [readonly] |



## Enum: KindEnum

| Name | Value |
|---- | -----|
| TEMPLATE | &quot;template&quot; |
| ROLE_ASSIGNMENT | &quot;roleAssignment&quot; |
| POLICY_ASSIGNMENT | &quot;policyAssignment&quot; |



