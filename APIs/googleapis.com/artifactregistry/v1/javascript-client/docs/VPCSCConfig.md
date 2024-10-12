# ArtifactRegistryApi.VPCSCConfig

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **String** | The name of the project&#39;s VPC SC Config. Always of the form: projects/{projectID}/locations/{location}/vpcscConfig In update request: never set In response: always set | [optional] 
**vpcscPolicy** | **String** | The project per location VPC SC policy that defines the VPC SC behavior for the Remote Repository (Allow/Deny). | [optional] 



## Enum: VpcscPolicyEnum


* `VPCSC_POLICY_UNSPECIFIED` (value: `"VPCSC_POLICY_UNSPECIFIED"`)

* `DENY` (value: `"DENY"`)

* `ALLOW` (value: `"ALLOW"`)




