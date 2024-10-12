

# GenericClass

Generic Class

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**callbackOptions** | [**CallbackOptions**](CallbackOptions.md) |  |  [optional] |
|**classTemplateInfo** | [**ClassTemplateInfo**](ClassTemplateInfo.md) |  |  [optional] |
|**enableSmartTap** | **Boolean** | Available only to Smart Tap enabled partners. Contact support for additional guidance. |  [optional] |
|**id** | **String** | Required. The unique identifier for the class. This ID must be unique across all from an issuer. This value needs to follow the format &#x60;issuerID.identifier&#x60; where &#x60;issuerID&#x60; is issued by Google and &#x60;identifier&#x60; is chosen by you. The unique identifier can only include alphanumeric characters, &#x60;.&#x60;, &#x60;_&#x60;, or &#x60;-&#x60;. |  [optional] |
|**imageModulesData** | [**List&lt;ImageModuleData&gt;**](ImageModuleData.md) | Image module data. If &#x60;imageModulesData&#x60; is also defined on the object, both will be displayed. Only one of the image from class and one from object level will be rendered when both set. |  [optional] |
|**linksModuleData** | [**LinksModuleData**](LinksModuleData.md) |  |  [optional] |
|**multipleDevicesAndHoldersAllowedStatus** | [**MultipleDevicesAndHoldersAllowedStatusEnum**](#MultipleDevicesAndHoldersAllowedStatusEnum) | Identifies whether multiple users and devices will save the same object referencing this class. |  [optional] |
|**redemptionIssuers** | **List&lt;String&gt;** | Identifies which redemption issuers can redeem the pass over Smart Tap. Redemption issuers are identified by their issuer ID. Redemption issuers must have at least one Smart Tap key configured. The &#x60;enableSmartTap&#x60; and object level &#x60;smartTapRedemptionLevel&#x60; fields must also be set up correctly in order for a pass to support Smart Tap. |  [optional] |
|**securityAnimation** | [**SecurityAnimation**](SecurityAnimation.md) |  |  [optional] |
|**textModulesData** | [**List&lt;TextModuleData&gt;**](TextModuleData.md) | Text module data. If &#x60;textModulesData&#x60; is also defined on the object, both will be displayed. The maximum number of these fields displayed is 10 from class and 10 from object. |  [optional] |
|**viewUnlockRequirement** | [**ViewUnlockRequirementEnum**](#ViewUnlockRequirementEnum) | View Unlock Requirement options for the generic pass. |  [optional] |



## Enum: MultipleDevicesAndHoldersAllowedStatusEnum

| Name | Value |
|---- | -----|
| STATUS_UNSPECIFIED | &quot;STATUS_UNSPECIFIED&quot; |
| MULTIPLE_HOLDERS | &quot;MULTIPLE_HOLDERS&quot; |
| MULTIPLE_HOLDERS2 | &quot;multipleHolders&quot; |
| ONE_USER_ALL_DEVICES | &quot;ONE_USER_ALL_DEVICES&quot; |
| ONE_USER_ALL_DEVICES2 | &quot;oneUserAllDevices&quot; |
| ONE_USER_ONE_DEVICE | &quot;ONE_USER_ONE_DEVICE&quot; |
| ONE_USER_ONE_DEVICE2 | &quot;oneUserOneDevice&quot; |



## Enum: ViewUnlockRequirementEnum

| Name | Value |
|---- | -----|
| VIEW_UNLOCK_REQUIREMENT_UNSPECIFIED | &quot;VIEW_UNLOCK_REQUIREMENT_UNSPECIFIED&quot; |
| UNLOCK_NOT_REQUIRED | &quot;UNLOCK_NOT_REQUIRED&quot; |
| UNLOCK_REQUIRED_TO_VIEW | &quot;UNLOCK_REQUIRED_TO_VIEW&quot; |



