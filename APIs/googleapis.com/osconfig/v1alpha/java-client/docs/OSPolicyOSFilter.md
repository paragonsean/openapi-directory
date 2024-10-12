

# OSPolicyOSFilter

Filtering criteria to select VMs based on OS details.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**osShortName** | **String** | This should match OS short name emitted by the OS inventory agent. An empty value matches any OS. |  [optional] |
|**osVersion** | **String** | This value should match the version emitted by the OS inventory agent. Prefix matches are supported if asterisk(*) is provided as the last character. For example, to match all versions with a major version of &#x60;7&#x60;, specify the following value for this field &#x60;7.*&#x60; |  [optional] |



