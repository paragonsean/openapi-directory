

# MatchTimeseries2018

Timeseries data for the 2018 game *FIRST* POWER UP. *WARNING:* This is *not* official data, and is subject to a significant possibility of error, or missing data. Do not rely on this data for any purpose. In fact, pretend we made it up. *WARNING:* This model is currently under active development and may change at any time, including in breaking ways.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**blueAutoQuest** | **Integer** | 1 if the blue alliance is credited with the AUTO QUEST, 0 if not. |  [optional] |
|**blueBoostCount** | **Integer** | Number of POWER CUBES in the BOOST section of the blue alliance VAULT. |  [optional] |
|**blueBoostPlayed** | **Integer** | Returns 1 if the blue alliance BOOST was played, or 0 if not played. |  [optional] |
|**blueCurrentPowerup** | **String** | Name of the current blue alliance POWER UP being played, or &#x60;null&#x60;. |  [optional] |
|**blueFaceTheBoss** | **Integer** | 1 if the blue alliance is credited with FACING THE BOSS, 0 if not. |  [optional] |
|**blueForceCount** | **Integer** | Number of POWER CUBES in the FORCE section of the blue alliance VAULT. |  [optional] |
|**blueForcePlayed** | **Integer** | Returns 1 if the blue alliance FORCE was played, or 0 if not played. |  [optional] |
|**blueLevitateCount** | **Integer** | Number of POWER CUBES in the LEVITATE section of the blue alliance VAULT. |  [optional] |
|**blueLevitatePlayed** | **Integer** | Returns 1 if the blue alliance LEVITATE was played, or 0 if not played. |  [optional] |
|**bluePowerupTimeRemaining** | **String** | Number of seconds remaining in the blue alliance POWER UP time, or 0 if none is active. |  [optional] |
|**blueScaleOwned** | **Integer** | 1 if the blue alliance owns the SCALE, 0 if not. |  [optional] |
|**blueScore** | **Integer** | Current score for the blue alliance. |  [optional] |
|**blueSwitchOwned** | **Integer** | 1 if the blue alliance owns their SWITCH, 0 if not. |  [optional] |
|**eventKey** | **String** | TBA event key with the format yyyy[EVENT_CODE], where yyyy is the year, and EVENT_CODE is the event code of the event. |  [optional] |
|**matchId** | **String** | Match ID consisting of the level, match number, and set number, eg &#x60;qm45&#x60; or &#x60;f1m1&#x60;. |  [optional] |
|**mode** | **String** | Current mode of play, can be &#x60;pre_match&#x60;, &#x60;auto&#x60;, &#x60;telop&#x60;, or &#x60;post_match&#x60;. |  [optional] |
|**play** | **Integer** |  |  [optional] |
|**redAutoQuest** | **Integer** | 1 if the red alliance is credited with the AUTO QUEST, 0 if not. |  [optional] |
|**redBoostCount** | **Integer** | Number of POWER CUBES in the BOOST section of the red alliance VAULT. |  [optional] |
|**redBoostPlayed** | **Integer** | Returns 1 if the red alliance BOOST was played, or 0 if not played. |  [optional] |
|**redCurrentPowerup** | **String** | Name of the current red alliance POWER UP being played, or &#x60;null&#x60;. |  [optional] |
|**redFaceTheBoss** | **Integer** | 1 if the red alliance is credited with FACING THE BOSS, 0 if not. |  [optional] |
|**redForceCount** | **Integer** | Number of POWER CUBES in the FORCE section of the red alliance VAULT. |  [optional] |
|**redForcePlayed** | **Integer** | Returns 1 if the red alliance FORCE was played, or 0 if not played. |  [optional] |
|**redLevitateCount** | **Integer** | Number of POWER CUBES in the LEVITATE section of the red alliance VAULT. |  [optional] |
|**redLevitatePlayed** | **Integer** | Returns 1 if the red alliance LEVITATE was played, or 0 if not played. |  [optional] |
|**redPowerupTimeRemaining** | **String** | Number of seconds remaining in the red alliance POWER UP time, or 0 if none is active. |  [optional] |
|**redScaleOwned** | **Integer** | 1 if the red alliance owns the SCALE, 0 if not. |  [optional] |
|**redScore** | **Integer** | Current score for the red alliance. |  [optional] |
|**redSwitchOwned** | **Integer** | 1 if the red alliance owns their SWITCH, 0 if not. |  [optional] |
|**timeRemaining** | **Integer** | Amount of time remaining in the match, only valid during &#x60;auto&#x60; and &#x60;teleop&#x60; modes. |  [optional] |



