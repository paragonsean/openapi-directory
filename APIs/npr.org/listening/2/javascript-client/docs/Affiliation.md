# NprListeningService.Affiliation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**daysSinceLastListen** | **Number** | The number of days since a user last listened to a story from this aggregation. Absent if user never listened to the aggregation. | [optional] 
**following** | **Boolean** | Whether or not the user is following the aggregation. When changing affiliation status, the client is expected to toggle this value and then send the entire object back. | [default to false]
**href** | **String** | A link to more details about the program from the NPR Story API | 
**id** | **Number** | A unique identifier for the aggregation (program) | 
**notifFollowing** | **[String]** | The topic in Firebase Cloud Messaging to which the device should subscribe if it supports notifications and the user wants notifications about the podcasts they follow. | [optional] 
**notifRated** | **[String]** | The topic in Firebase Cloud Messaging to which the device should subscribe if it supports notifications and the user wants notifications about the podcasts they have highly rated. | [optional] 
**rating** | **Number** | The user&#39;s average rating for this affiliation on a scale of 0-1. Absent if user never listened to the aggregation. | [optional] 
**title** | **String** | The title for the aggregation (program) | [optional] 


