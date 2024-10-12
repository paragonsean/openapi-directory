

# Display

Contains the localized display information for this particular operation / action. These value will be used by several clients for (1) custom role definitions for RBAC; (2) complex query filters for the event service; and (3) audit history / records for management operations.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**description** | **String** | The description. The localized friendly description for the operation, as it should be shown to the user. It should be thorough, yet concise – it will be used in tool tips and detailed views. Prescriptive guidance for namespaces: Read any &#39;display.provider&#39; resource Create or Update any &#39;display.provider&#39; resource Delete any &#39;display.provider&#39; resource Perform any other action on any &#39;display.provider&#39; resource Prescriptive guidance for namespaces: Read any &#39;display.resource&#39; Create or Update any &#39;display.resource&#39; Delete any &#39;display.resource&#39; &#39;ActionName&#39; any &#39;display.resources&#39; |  [optional] |
|**operation** | **String** | The operation. The localized friendly name for the operation, as it should be shown to the user. It should be concise (to fit in drop downs) but clear (i.e. self-documenting). It should use Title Casing. Prescriptive guidance: Read Create or Update Delete &#39;ActionName&#39; |  [optional] |
|**provider** | **String** | The provider. The localized friendly form of the resource provider name – it is expected to also include the publisher/company responsible. It should use Title Casing and begin with \&quot;Microsoft\&quot; for 1st party services. e.g. \&quot;Microsoft Monitoring Insights\&quot; or \&quot;Microsoft Compute.\&quot; |  [optional] |
|**resource** | **String** | The resource. The localized friendly form of the resource related to this action/operation – it should match the public documentation for the resource provider. It should use Title Casing. This value should be unique for a particular URL type (e.g. nested types should *not* reuse their parent’s display.resource field). e.g. \&quot;Virtual Machines\&quot; or \&quot;Scheduler Job Collections\&quot;, or \&quot;Virtual Machine VM Sizes\&quot; or \&quot;Scheduler Jobs\&quot; |  [optional] |



