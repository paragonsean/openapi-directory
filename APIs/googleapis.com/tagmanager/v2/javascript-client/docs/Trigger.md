# TagManagerApi.Trigger

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accountId** | **String** | GTM Account ID. | [optional] 
**autoEventFilter** | [**[Condition]**](Condition.md) | Used in the case of auto event tracking. @mutable tagmanager.accounts.containers.workspaces.triggers.create @mutable tagmanager.accounts.containers.workspaces.triggers.update | [optional] 
**checkValidation** | [**Parameter**](Parameter.md) |  | [optional] 
**containerId** | **String** | GTM Container ID. | [optional] 
**continuousTimeMinMilliseconds** | [**Parameter**](Parameter.md) |  | [optional] 
**customEventFilter** | [**[Condition]**](Condition.md) | Used in the case of custom event, which is fired iff all Conditions are true. @mutable tagmanager.accounts.containers.workspaces.triggers.create @mutable tagmanager.accounts.containers.workspaces.triggers.update | [optional] 
**eventName** | [**Parameter**](Parameter.md) |  | [optional] 
**filter** | [**[Condition]**](Condition.md) | The trigger will only fire iff all Conditions are true. @mutable tagmanager.accounts.containers.workspaces.triggers.create @mutable tagmanager.accounts.containers.workspaces.triggers.update | [optional] 
**fingerprint** | **String** | The fingerprint of the GTM Trigger as computed at storage time. This value is recomputed whenever the trigger is modified. | [optional] 
**horizontalScrollPercentageList** | [**Parameter**](Parameter.md) |  | [optional] 
**interval** | [**Parameter**](Parameter.md) |  | [optional] 
**intervalSeconds** | [**Parameter**](Parameter.md) |  | [optional] 
**limit** | [**Parameter**](Parameter.md) |  | [optional] 
**maxTimerLengthSeconds** | [**Parameter**](Parameter.md) |  | [optional] 
**name** | **String** | Trigger display name. @mutable tagmanager.accounts.containers.workspaces.triggers.create @mutable tagmanager.accounts.containers.workspaces.triggers.update | [optional] 
**notes** | **String** | User notes on how to apply this trigger in the container. @mutable tagmanager.accounts.containers.workspaces.triggers.create @mutable tagmanager.accounts.containers.workspaces.triggers.update | [optional] 
**parameter** | [**[Parameter]**](Parameter.md) | Additional parameters. @mutable tagmanager.accounts.containers.workspaces.triggers.create @mutable tagmanager.accounts.containers.workspaces.triggers.update | [optional] 
**parentFolderId** | **String** | Parent folder id. | [optional] 
**path** | **String** | GTM Trigger&#39;s API relative path. | [optional] 
**selector** | [**Parameter**](Parameter.md) |  | [optional] 
**tagManagerUrl** | **String** | Auto generated link to the tag manager UI | [optional] 
**totalTimeMinMilliseconds** | [**Parameter**](Parameter.md) |  | [optional] 
**triggerId** | **String** | The Trigger ID uniquely identifies the GTM Trigger. | [optional] 
**type** | **String** | Defines the data layer event that causes this trigger. @mutable tagmanager.accounts.containers.workspaces.triggers.create @mutable tagmanager.accounts.containers.workspaces.triggers.update | [optional] 
**uniqueTriggerId** | [**Parameter**](Parameter.md) |  | [optional] 
**verticalScrollPercentageList** | [**Parameter**](Parameter.md) |  | [optional] 
**visibilitySelector** | [**Parameter**](Parameter.md) |  | [optional] 
**visiblePercentageMax** | [**Parameter**](Parameter.md) |  | [optional] 
**visiblePercentageMin** | [**Parameter**](Parameter.md) |  | [optional] 
**waitForTags** | [**Parameter**](Parameter.md) |  | [optional] 
**waitForTagsTimeout** | [**Parameter**](Parameter.md) |  | [optional] 
**workspaceId** | **String** | GTM Workspace ID. | [optional] 



## Enum: TypeEnum


* `eventTypeUnspecified` (value: `"eventTypeUnspecified"`)

* `pageview` (value: `"pageview"`)

* `domReady` (value: `"domReady"`)

* `windowLoaded` (value: `"windowLoaded"`)

* `customEvent` (value: `"customEvent"`)

* `triggerGroup` (value: `"triggerGroup"`)

* `init` (value: `"init"`)

* `consentInit` (value: `"consentInit"`)

* `serverPageview` (value: `"serverPageview"`)

* `always` (value: `"always"`)

* `firebaseAppException` (value: `"firebaseAppException"`)

* `firebaseAppUpdate` (value: `"firebaseAppUpdate"`)

* `firebaseCampaign` (value: `"firebaseCampaign"`)

* `firebaseFirstOpen` (value: `"firebaseFirstOpen"`)

* `firebaseInAppPurchase` (value: `"firebaseInAppPurchase"`)

* `firebaseNotificationDismiss` (value: `"firebaseNotificationDismiss"`)

* `firebaseNotificationForeground` (value: `"firebaseNotificationForeground"`)

* `firebaseNotificationOpen` (value: `"firebaseNotificationOpen"`)

* `firebaseNotificationReceive` (value: `"firebaseNotificationReceive"`)

* `firebaseOsUpdate` (value: `"firebaseOsUpdate"`)

* `firebaseSessionStart` (value: `"firebaseSessionStart"`)

* `firebaseUserEngagement` (value: `"firebaseUserEngagement"`)

* `formSubmission` (value: `"formSubmission"`)

* `click` (value: `"click"`)

* `linkClick` (value: `"linkClick"`)

* `jsError` (value: `"jsError"`)

* `historyChange` (value: `"historyChange"`)

* `timer` (value: `"timer"`)

* `ampClick` (value: `"ampClick"`)

* `ampTimer` (value: `"ampTimer"`)

* `ampScroll` (value: `"ampScroll"`)

* `ampVisibility` (value: `"ampVisibility"`)

* `youTubeVideo` (value: `"youTubeVideo"`)

* `scrollDepth` (value: `"scrollDepth"`)

* `elementVisibility` (value: `"elementVisibility"`)




