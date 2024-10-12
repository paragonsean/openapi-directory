

# CloudBuildMembershipSpec

**Cloud Build**: Configurations for each Cloud Build enabled cluster.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**securityPolicy** | [**SecurityPolicyEnum**](#SecurityPolicyEnum) | Whether it is allowed to run the privileged builds on the cluster or not. |  [optional] |
|**version** | **String** | Version of the cloud build software on the cluster. |  [optional] |



## Enum: SecurityPolicyEnum

| Name | Value |
|---- | -----|
| SECURITY_POLICY_UNSPECIFIED | &quot;SECURITY_POLICY_UNSPECIFIED&quot; |
| NON_PRIVILEGED | &quot;NON_PRIVILEGED&quot; |
| PRIVILEGED | &quot;PRIVILEGED&quot; |



