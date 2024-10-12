# OpenChannelMarketApi.App

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access** | **[String]** | A custom defined list of access requirements | [optional] 
**allow** | [**Restrictions**](Restrictions.md) |  | 
**appId** | **String** | The id of this app | 
**attributes** | **Object** | A custom defined list of app attributes | 
**created** | **Number** | The date (in millis) that this app was created | 
**customData** | **Object** | A custom JSON object that you can create and attach to this record | 
**developerId** | **String** | The id of the developer that owns this app | 
**isLive** | **Boolean** | True if this is the live version of the app | 
**lastUpdated** | **Number** | The date (in millis) that this app was last modified | 
**model** | [**[Model]**](Model.md) | The models that describes the cost and pricing for this app | 
**name** | **String** | The name of this app | 
**ownership** | [**Ownership**](Ownership.md) |  | [optional] 
**randomize** | **Number** | A random number that changes hourly and is used for achieving a random sort order when displaying apps | 
**rating** | **Number** | The average review rating for this app. Reviews are rated from 100 (one star) to 500 (five star) | 
**restrict** | [**Restrictions**](Restrictions.md) |  | 
**reviewCount** | **Number** | The number of approved reviews for this app. | [optional] 
**safeName** | **[String]** | URL safe aliases that can be used to identify this app even after name changes. The current alias is always at position 0. | 
**statistics** | **Object** | A field containing summary stats about the app and is specially designed to allow apps to be sorted by popularity | [optional] 
**status** | [**Status**](Status.md) |  | 
**submittedDate** | **Number** | The date (in millis) that this app was submitted for approval | [optional] 
**type** | **String** | The type for this app | [optional] 
**version** | **Number** | The version number for this app | 


