

# DestinyEntitiesCharactersDestinyCharacterActivitiesComponent

This component holds activity data for a character. It will tell you about the character's current activity status, as well as activities that are available to the user.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**availableActivities** | [**List&lt;DestinyDestinyActivity&gt;**](DestinyDestinyActivity.md) | The list of activities that the user can play. |  [optional] |
|**currentActivityHash** | **Integer** | If the user is in an activity, this will be the hash of the Activity being played. Note that you must combine this info with currentActivityModeHash to get a real picture of what the user is doing right now. For instance, PVP \&quot;Activities\&quot; are just maps: it&#39;s the ActivityMode that determines what type of PVP game they&#39;re playing. |  [optional] |
|**currentActivityModeHash** | **Integer** | If the user is in an activity, this will be the hash of the activity mode being played. Combine with currentActivityHash to give a person a full picture of what they&#39;re doing right now. |  [optional] |
|**currentActivityModeHashes** | **List&lt;Integer&gt;** | If the user is in an activity, this will be the hashes of the DestinyActivityModeDefinition being played. Combine with currentActivityHash to give a person a full picture of what they&#39;re doing right now. |  [optional] |
|**currentActivityModeType** | [**CurrentActivityModeTypeEnum**](#CurrentActivityModeTypeEnum) | And the current activity&#39;s most specific mode type, if it can be found. |  [optional] |
|**currentActivityModeTypes** | **List&lt;Integer&gt;** | All Activity Modes that apply to the current activity being played, in enum form. |  [optional] |
|**currentPlaylistActivityHash** | **Integer** | If the user is in a playlist, this is the hash identifier for the playlist that they chose. |  [optional] |
|**dateActivityStarted** | **OffsetDateTime** | The last date that the user started playing an activity. |  [optional] |
|**lastCompletedStoryHash** | **Integer** | This will have the activity hash of the last completed story/campaign mission, in case you care about that. |  [optional] |



## Enum: CurrentActivityModeTypeEnum

| Name | Value |
|---- | -----|
| NUMBER_0 | 0 |
| NUMBER_2 | 2 |
| NUMBER_3 | 3 |
| NUMBER_4 | 4 |
| NUMBER_5 | 5 |
| NUMBER_6 | 6 |
| NUMBER_7 | 7 |
| NUMBER_9 | 9 |
| NUMBER_10 | 10 |
| NUMBER_11 | 11 |
| NUMBER_12 | 12 |
| NUMBER_13 | 13 |
| NUMBER_15 | 15 |
| NUMBER_16 | 16 |
| NUMBER_17 | 17 |
| NUMBER_18 | 18 |
| NUMBER_19 | 19 |
| NUMBER_20 | 20 |
| NUMBER_21 | 21 |
| NUMBER_22 | 22 |
| NUMBER_24 | 24 |
| NUMBER_25 | 25 |
| NUMBER_26 | 26 |
| NUMBER_27 | 27 |
| NUMBER_28 | 28 |
| NUMBER_29 | 29 |
| NUMBER_30 | 30 |
| NUMBER_31 | 31 |
| NUMBER_32 | 32 |
| NUMBER_37 | 37 |
| NUMBER_38 | 38 |
| NUMBER_39 | 39 |
| NUMBER_40 | 40 |
| NUMBER_41 | 41 |
| NUMBER_42 | 42 |
| NUMBER_43 | 43 |
| NUMBER_44 | 44 |
| NUMBER_45 | 45 |
| NUMBER_46 | 46 |
| NUMBER_47 | 47 |
| NUMBER_48 | 48 |
| NUMBER_49 | 49 |
| NUMBER_50 | 50 |
| NUMBER_51 | 51 |
| NUMBER_52 | 52 |
| NUMBER_53 | 53 |
| NUMBER_54 | 54 |
| NUMBER_55 | 55 |
| NUMBER_56 | 56 |
| NUMBER_57 | 57 |
| NUMBER_58 | 58 |
| NUMBER_59 | 59 |
| NUMBER_60 | 60 |
| NUMBER_61 | 61 |
| NUMBER_62 | 62 |
| NUMBER_63 | 63 |
| NUMBER_64 | 64 |
| NUMBER_65 | 65 |
| NUMBER_66 | 66 |
| NUMBER_67 | 67 |
| NUMBER_68 | 68 |
| NUMBER_69 | 69 |
| NUMBER_70 | 70 |
| NUMBER_71 | 71 |
| NUMBER_72 | 72 |
| NUMBER_73 | 73 |
| NUMBER_74 | 74 |
| NUMBER_75 | 75 |
| NUMBER_76 | 76 |
| NUMBER_77 | 77 |
| NUMBER_78 | 78 |
| NUMBER_79 | 79 |
| NUMBER_80 | 80 |
| NUMBER_81 | 81 |
| NUMBER_82 | 82 |
| NUMBER_83 | 83 |
| NUMBER_84 | 84 |
| NUMBER_85 | 85 |
| NUMBER_86 | 86 |
| NUMBER_87 | 87 |
| NUMBER_88 | 88 |
| NUMBER_89 | 89 |
| NUMBER_90 | 90 |
| NUMBER_91 | 91 |



