# FirebaseRulesApi.GetReleaseExecutableResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**executable** | **Blob** | Executable view of the &#x60;Ruleset&#x60; referenced by the &#x60;Release&#x60;. | [optional] 
**executableVersion** | **String** | The Rules runtime version of the executable. | [optional] 
**language** | **String** | &#x60;Language&#x60; used to generate the executable bytes. | [optional] 
**rulesetName** | **String** | &#x60;Ruleset&#x60; name associated with the &#x60;Release&#x60; executable. | [optional] 
**syncTime** | **String** | Optional, indicates the freshness of the result. The response is guaranteed to be the latest within an interval up to the sync_time (inclusive). | [optional] 
**updateTime** | **String** | Timestamp for the most recent &#x60;Release.update_time&#x60;. | [optional] 



## Enum: ExecutableVersionEnum


* `RELEASE_EXECUTABLE_VERSION_UNSPECIFIED` (value: `"RELEASE_EXECUTABLE_VERSION_UNSPECIFIED"`)

* `FIREBASE_RULES_EXECUTABLE_V1` (value: `"FIREBASE_RULES_EXECUTABLE_V1"`)

* `FIREBASE_RULES_EXECUTABLE_V2` (value: `"FIREBASE_RULES_EXECUTABLE_V2"`)





## Enum: LanguageEnum


* `LANGUAGE_UNSPECIFIED` (value: `"LANGUAGE_UNSPECIFIED"`)

* `FIREBASE_RULES` (value: `"FIREBASE_RULES"`)

* `EVENT_FLOW_TRIGGERS` (value: `"EVENT_FLOW_TRIGGERS"`)




