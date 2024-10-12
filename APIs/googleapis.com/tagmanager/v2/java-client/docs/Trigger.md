

# Trigger

Represents a Google Tag Manager Trigger

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountId** | **String** | GTM Account ID. |  [optional] |
|**autoEventFilter** | [**List&lt;Condition&gt;**](Condition.md) | Used in the case of auto event tracking. @mutable tagmanager.accounts.containers.workspaces.triggers.create @mutable tagmanager.accounts.containers.workspaces.triggers.update |  [optional] |
|**checkValidation** | [**Parameter**](Parameter.md) |  |  [optional] |
|**containerId** | **String** | GTM Container ID. |  [optional] |
|**continuousTimeMinMilliseconds** | [**Parameter**](Parameter.md) |  |  [optional] |
|**customEventFilter** | [**List&lt;Condition&gt;**](Condition.md) | Used in the case of custom event, which is fired iff all Conditions are true. @mutable tagmanager.accounts.containers.workspaces.triggers.create @mutable tagmanager.accounts.containers.workspaces.triggers.update |  [optional] |
|**eventName** | [**Parameter**](Parameter.md) |  |  [optional] |
|**filter** | [**List&lt;Condition&gt;**](Condition.md) | The trigger will only fire iff all Conditions are true. @mutable tagmanager.accounts.containers.workspaces.triggers.create @mutable tagmanager.accounts.containers.workspaces.triggers.update |  [optional] |
|**fingerprint** | **String** | The fingerprint of the GTM Trigger as computed at storage time. This value is recomputed whenever the trigger is modified. |  [optional] |
|**horizontalScrollPercentageList** | [**Parameter**](Parameter.md) |  |  [optional] |
|**interval** | [**Parameter**](Parameter.md) |  |  [optional] |
|**intervalSeconds** | [**Parameter**](Parameter.md) |  |  [optional] |
|**limit** | [**Parameter**](Parameter.md) |  |  [optional] |
|**maxTimerLengthSeconds** | [**Parameter**](Parameter.md) |  |  [optional] |
|**name** | **String** | Trigger display name. @mutable tagmanager.accounts.containers.workspaces.triggers.create @mutable tagmanager.accounts.containers.workspaces.triggers.update |  [optional] |
|**notes** | **String** | User notes on how to apply this trigger in the container. @mutable tagmanager.accounts.containers.workspaces.triggers.create @mutable tagmanager.accounts.containers.workspaces.triggers.update |  [optional] |
|**parameter** | [**List&lt;Parameter&gt;**](Parameter.md) | Additional parameters. @mutable tagmanager.accounts.containers.workspaces.triggers.create @mutable tagmanager.accounts.containers.workspaces.triggers.update |  [optional] |
|**parentFolderId** | **String** | Parent folder id. |  [optional] |
|**path** | **String** | GTM Trigger&#39;s API relative path. |  [optional] |
|**selector** | [**Parameter**](Parameter.md) |  |  [optional] |
|**tagManagerUrl** | **String** | Auto generated link to the tag manager UI |  [optional] |
|**totalTimeMinMilliseconds** | [**Parameter**](Parameter.md) |  |  [optional] |
|**triggerId** | **String** | The Trigger ID uniquely identifies the GTM Trigger. |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | Defines the data layer event that causes this trigger. @mutable tagmanager.accounts.containers.workspaces.triggers.create @mutable tagmanager.accounts.containers.workspaces.triggers.update |  [optional] |
|**uniqueTriggerId** | [**Parameter**](Parameter.md) |  |  [optional] |
|**verticalScrollPercentageList** | [**Parameter**](Parameter.md) |  |  [optional] |
|**visibilitySelector** | [**Parameter**](Parameter.md) |  |  [optional] |
|**visiblePercentageMax** | [**Parameter**](Parameter.md) |  |  [optional] |
|**visiblePercentageMin** | [**Parameter**](Parameter.md) |  |  [optional] |
|**waitForTags** | [**Parameter**](Parameter.md) |  |  [optional] |
|**waitForTagsTimeout** | [**Parameter**](Parameter.md) |  |  [optional] |
|**workspaceId** | **String** | GTM Workspace ID. |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| EVENT_TYPE_UNSPECIFIED | &quot;eventTypeUnspecified&quot; |
| PAGEVIEW | &quot;pageview&quot; |
| DOM_READY | &quot;domReady&quot; |
| WINDOW_LOADED | &quot;windowLoaded&quot; |
| CUSTOM_EVENT | &quot;customEvent&quot; |
| TRIGGER_GROUP | &quot;triggerGroup&quot; |
| INIT | &quot;init&quot; |
| CONSENT_INIT | &quot;consentInit&quot; |
| SERVER_PAGEVIEW | &quot;serverPageview&quot; |
| ALWAYS | &quot;always&quot; |
| FIREBASE_APP_EXCEPTION | &quot;firebaseAppException&quot; |
| FIREBASE_APP_UPDATE | &quot;firebaseAppUpdate&quot; |
| FIREBASE_CAMPAIGN | &quot;firebaseCampaign&quot; |
| FIREBASE_FIRST_OPEN | &quot;firebaseFirstOpen&quot; |
| FIREBASE_IN_APP_PURCHASE | &quot;firebaseInAppPurchase&quot; |
| FIREBASE_NOTIFICATION_DISMISS | &quot;firebaseNotificationDismiss&quot; |
| FIREBASE_NOTIFICATION_FOREGROUND | &quot;firebaseNotificationForeground&quot; |
| FIREBASE_NOTIFICATION_OPEN | &quot;firebaseNotificationOpen&quot; |
| FIREBASE_NOTIFICATION_RECEIVE | &quot;firebaseNotificationReceive&quot; |
| FIREBASE_OS_UPDATE | &quot;firebaseOsUpdate&quot; |
| FIREBASE_SESSION_START | &quot;firebaseSessionStart&quot; |
| FIREBASE_USER_ENGAGEMENT | &quot;firebaseUserEngagement&quot; |
| FORM_SUBMISSION | &quot;formSubmission&quot; |
| CLICK | &quot;click&quot; |
| LINK_CLICK | &quot;linkClick&quot; |
| JS_ERROR | &quot;jsError&quot; |
| HISTORY_CHANGE | &quot;historyChange&quot; |
| TIMER | &quot;timer&quot; |
| AMP_CLICK | &quot;ampClick&quot; |
| AMP_TIMER | &quot;ampTimer&quot; |
| AMP_SCROLL | &quot;ampScroll&quot; |
| AMP_VISIBILITY | &quot;ampVisibility&quot; |
| YOU_TUBE_VIDEO | &quot;youTubeVideo&quot; |
| SCROLL_DEPTH | &quot;scrollDepth&quot; |
| ELEMENT_VISIBILITY | &quot;elementVisibility&quot; |



