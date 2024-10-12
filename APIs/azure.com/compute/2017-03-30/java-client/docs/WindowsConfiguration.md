

# WindowsConfiguration

Specifies Windows operating system settings on the virtual machine.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**additionalUnattendContent** | [**List&lt;AdditionalUnattendContent&gt;**](AdditionalUnattendContent.md) | Specifies additional base-64 encoded XML formatted information that can be included in the Unattend.xml file, which is used by Windows Setup. |  [optional] |
|**enableAutomaticUpdates** | **Boolean** | Indicates whether virtual machine is enabled for automatic updates. |  [optional] |
|**provisionVMAgent** | **Boolean** | Indicates whether virtual machine agent should be provisioned on the virtual machine. &lt;br&gt;&lt;br&gt; When this property is not specified in the request body, default behavior is to set it to true.  This will ensure that VM Agent is installed on the VM so that extensions can be added to the VM later. |  [optional] |
|**timeZone** | **String** | Specifies the time zone of the virtual machine. e.g. \&quot;Pacific Standard Time\&quot; |  [optional] |
|**winRM** | [**WinRMConfiguration**](WinRMConfiguration.md) |  |  [optional] |



