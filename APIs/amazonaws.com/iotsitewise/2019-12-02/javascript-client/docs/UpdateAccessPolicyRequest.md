# AwsIoTSiteWise.UpdateAccessPolicyRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accessPolicyIdentity** | [**CreateAccessPolicyRequestAccessPolicyIdentity**](CreateAccessPolicyRequestAccessPolicyIdentity.md) |  | 
**accessPolicyResource** | [**CreateAccessPolicyRequestAccessPolicyResource**](CreateAccessPolicyRequestAccessPolicyResource.md) |  | 
**accessPolicyPermission** | **String** | The permission level for this access policy. Note that a project &lt;code&gt;ADMINISTRATOR&lt;/code&gt; is also known as a project owner. | 
**clientToken** | **String** | A unique case-sensitive identifier that you can provide to ensure the idempotency of the request. Don&#39;t reuse this client token if a new idempotent request is required. | [optional] 



## Enum: AccessPolicyPermissionEnum


* `ADMINISTRATOR` (value: `"ADMINISTRATOR"`)

* `VIEWER` (value: `"VIEWER"`)




