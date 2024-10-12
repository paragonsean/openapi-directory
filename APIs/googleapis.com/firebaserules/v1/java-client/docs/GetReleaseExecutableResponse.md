

# GetReleaseExecutableResponse

The response for FirebaseRulesService.GetReleaseExecutable

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**executable** | **byte[]** | Executable view of the &#x60;Ruleset&#x60; referenced by the &#x60;Release&#x60;. |  [optional] |
|**executableVersion** | [**ExecutableVersionEnum**](#ExecutableVersionEnum) | The Rules runtime version of the executable. |  [optional] |
|**language** | [**LanguageEnum**](#LanguageEnum) | &#x60;Language&#x60; used to generate the executable bytes. |  [optional] |
|**rulesetName** | **String** | &#x60;Ruleset&#x60; name associated with the &#x60;Release&#x60; executable. |  [optional] |
|**syncTime** | **String** | Optional, indicates the freshness of the result. The response is guaranteed to be the latest within an interval up to the sync_time (inclusive). |  [optional] |
|**updateTime** | **String** | Timestamp for the most recent &#x60;Release.update_time&#x60;. |  [optional] |



## Enum: ExecutableVersionEnum

| Name | Value |
|---- | -----|
| RELEASE_EXECUTABLE_VERSION_UNSPECIFIED | &quot;RELEASE_EXECUTABLE_VERSION_UNSPECIFIED&quot; |
| FIREBASE_RULES_EXECUTABLE_V1 | &quot;FIREBASE_RULES_EXECUTABLE_V1&quot; |
| FIREBASE_RULES_EXECUTABLE_V2 | &quot;FIREBASE_RULES_EXECUTABLE_V2&quot; |



## Enum: LanguageEnum

| Name | Value |
|---- | -----|
| LANGUAGE_UNSPECIFIED | &quot;LANGUAGE_UNSPECIFIED&quot; |
| FIREBASE_RULES | &quot;FIREBASE_RULES&quot; |
| EVENT_FLOW_TRIGGERS | &quot;EVENT_FLOW_TRIGGERS&quot; |



