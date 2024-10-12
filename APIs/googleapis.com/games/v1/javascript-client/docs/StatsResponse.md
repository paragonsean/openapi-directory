# GooglePlayGameServices.StatsResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**avgSessionLengthMinutes** | **Number** | Average session length in minutes of the player. E.g., 1, 30, 60, ... . Not populated if there is not enough information. | [optional] 
**churnProbability** | **Number** | The probability of the player not returning to play the game in the next day. E.g., 0, 0.1, 0.5, ..., 1.0. Not populated if there is not enough information. | [optional] 
**daysSinceLastPlayed** | **Number** | Number of days since the player last played this game. E.g., 0, 1, 5, 10, ... . Not populated if there is not enough information. | [optional] 
**highSpenderProbability** | **Number** | The probability of the player going to spend beyond a threshold amount of money. E.g., 0, 0.25, 0.50, 0.75. Not populated if there is not enough information. | [optional] 
**kind** | **String** | Uniquely identifies the type of this resource. Value is always the fixed string &#x60;games#statsResponse&#x60;. | [optional] 
**numPurchases** | **Number** | Number of in-app purchases made by the player in this game. E.g., 0, 1, 5, 10, ... . Not populated if there is not enough information. | [optional] 
**numSessions** | **Number** | The approximate number of sessions of the player within the last 28 days, where a session begins when the player is connected to Play Games Services and ends when they are disconnected. E.g., 0, 1, 5, 10, ... . Not populated if there is not enough information. | [optional] 
**numSessionsPercentile** | **Number** | The approximation of the sessions percentile of the player within the last 30 days, where a session begins when the player is connected to Play Games Services and ends when they are disconnected. E.g., 0, 0.25, 0.5, 0.75. Not populated if there is not enough information. | [optional] 
**spendPercentile** | **Number** | The approximate spend percentile of the player in this game. E.g., 0, 0.25, 0.5, 0.75. Not populated if there is not enough information. | [optional] 
**spendProbability** | **Number** | The probability of the player going to spend the game in the next seven days. E.g., 0, 0.25, 0.50, 0.75. Not populated if there is not enough information. | [optional] 
**totalSpendNext28Days** | **Number** | The predicted amount of money that the player going to spend in the next 28 days. E.g., 1, 30, 60, ... . Not populated if there is not enough information. | [optional] 


