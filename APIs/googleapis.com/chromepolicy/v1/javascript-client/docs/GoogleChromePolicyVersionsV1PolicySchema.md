# ChromePolicyApi.GoogleChromePolicyVersionsV1PolicySchema

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accessRestrictions** | **[String]** | Output only. Specific access restrictions related to this policy. | [optional] [readonly] 
**additionalTargetKeyNames** | [**[GoogleChromePolicyVersionsV1AdditionalTargetKeyName]**](GoogleChromePolicyVersionsV1AdditionalTargetKeyName.md) | Output only. Additional key names that will be used to identify the target of the policy value. When specifying a &#x60;policyTargetKey&#x60;, each of the additional keys specified here will have to be included in the &#x60;additionalTargetKeys&#x60; map. | [optional] [readonly] 
**categoryTitle** | **String** | Title of the category in which a setting belongs. | [optional] 
**definition** | [**Proto2FileDescriptorProto**](Proto2FileDescriptorProto.md) |  | [optional] 
**fieldDescriptions** | [**[GoogleChromePolicyVersionsV1PolicySchemaFieldDescription]**](GoogleChromePolicyVersionsV1PolicySchemaFieldDescription.md) | Output only. Detailed description of each field that is part of the schema. Fields are suggested to be displayed by the ordering in this list, not by field number. | [optional] [readonly] 
**name** | **String** | Format: name&#x3D;customers/{customer}/policySchemas/{schema_namespace} | [optional] 
**notices** | [**[GoogleChromePolicyVersionsV1PolicySchemaNoticeDescription]**](GoogleChromePolicyVersionsV1PolicySchemaNoticeDescription.md) | Output only. Special notice messages related to setting certain values in certain fields in the schema. | [optional] [readonly] 
**policyApiLifecycle** | [**GoogleChromePolicyVersionsV1PolicyApiLifecycle**](GoogleChromePolicyVersionsV1PolicyApiLifecycle.md) |  | [optional] 
**policyDescription** | **String** | Output only. Description about the policy schema for user consumption. | [optional] [readonly] 
**schemaName** | **String** | Output only. The fully qualified name of the policy schema. This value is used to fill the field &#x60;policy_schema&#x60; in PolicyValue when calling BatchInheritOrgUnitPolicies BatchModifyOrgUnitPolicies BatchModifyGroupPolicies or BatchDeleteGroupPolicies. | [optional] [readonly] 
**supportUri** | **String** | Output only. URI to related support article for this schema. | [optional] [readonly] 
**supportedPlatforms** | **[String]** | Output only. List indicates that the policy will only apply to devices/users on these platforms. | [optional] [readonly] 
**validTargetResources** | **[String]** | Output only. Information about applicable target resources for the policy. | [optional] [readonly] 



## Enum: [SupportedPlatformsEnum]


* `PLATFORM_UNSPECIFIED` (value: `"PLATFORM_UNSPECIFIED"`)

* `CHROME_OS` (value: `"CHROME_OS"`)

* `CHROME_BROWSER` (value: `"CHROME_BROWSER"`)

* `CHROME_BROWSER_FOR_ANDROID` (value: `"CHROME_BROWSER_FOR_ANDROID"`)

* `CHROME_BROWSER_FOR_IOS` (value: `"CHROME_BROWSER_FOR_IOS"`)





## Enum: [ValidTargetResourcesEnum]


* `TARGET_RESOURCE_UNSPECIFIED` (value: `"TARGET_RESOURCE_UNSPECIFIED"`)

* `ORG_UNIT` (value: `"ORG_UNIT"`)

* `GROUP` (value: `"GROUP"`)




