

# VPCSCConfig

The Artifact Registry VPC SC config that apply to a Project.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**name** | **String** | The name of the project&#39;s VPC SC Config. Always of the form: projects/{projectID}/locations/{location}/vpcscConfig In update request: never set In response: always set |  [optional] |
|**vpcscPolicy** | [**VpcscPolicyEnum**](#VpcscPolicyEnum) | The project per location VPC SC policy that defines the VPC SC behavior for the Remote Repository (Allow/Deny). |  [optional] |



## Enum: VpcscPolicyEnum

| Name | Value |
|---- | -----|
| VPCSC_POLICY_UNSPECIFIED | &quot;VPCSC_POLICY_UNSPECIFIED&quot; |
| DENY | &quot;DENY&quot; |
| ALLOW | &quot;ALLOW&quot; |



