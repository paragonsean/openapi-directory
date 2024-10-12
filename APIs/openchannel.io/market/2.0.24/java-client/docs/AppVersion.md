

# AppVersion

An AppVersion

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**access** | **List&lt;String&gt;** | A custom defined list of access requirements |  [optional] |
|**allow** | [**Restrictions**](Restrictions.md) |  |  |
|**appId** | **String** | The id of this app |  |
|**attributes** | **Object** | A custom defined list of app attributes |  [optional] |
|**created** | **Long** | The date (in millis) that this app was created |  |
|**customData** | **Object** | A custom JSON object that you can create and attach to this record |  |
|**developerId** | **String** | The id of the developer that owns this app |  |
|**isLatestVersion** | **Boolean** | True if this is the latest version of this app |  |
|**isLive** | **Boolean** | True if this is the live version of the app |  |
|**lastUpdated** | **Long** | The date (in millis) that this app was last modified |  |
|**model** | [**List&lt;Model&gt;**](Model.md) | The models that describes the cost and pricing for this app |  |
|**name** | **String** | The name of this app |  |
|**parent** | [**Parent**](Parent.md) |  |  |
|**rating** | **Integer** | The average review rating for this app. Reviews are rated from 100 (one star) to 500 (five star) |  [optional] |
|**restrict** | [**Restrictions**](Restrictions.md) |  |  |
|**reviewCount** | **Integer** | The number of approved reviews for this app. |  [optional] |
|**safeName** | **List&lt;String&gt;** | URL safe aliases that can be used to identify this app even after name changes. The current alias is always at position 0. |  |
|**status** | [**Status**](Status.md) |  |  |
|**type** | **String** | The type for this app |  [optional] |
|**version** | **Integer** | The version number for this app |  |



