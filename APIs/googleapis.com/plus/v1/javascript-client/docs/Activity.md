# GoogleApi.Activity

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access** | [**Acl**](Acl.md) |  | [optional] 
**actor** | [**ActivityActor**](ActivityActor.md) |  | [optional] 
**address** | **String** | Street address where this activity occurred. | [optional] 
**annotation** | **String** | Additional content added by the person who shared this activity, applicable only when resharing an activity. | [optional] 
**crosspostSource** | **String** | If this activity is a crosspost from another system, this property specifies the ID of the original activity. | [optional] 
**etag** | **String** | ETag of this response for caching purposes. | [optional] 
**geocode** | **String** | Latitude and longitude where this activity occurred. Format is latitude followed by longitude, space separated. | [optional] 
**id** | **String** | The ID of this activity. | [optional] 
**kind** | **String** | Identifies this resource as an activity. Value: \&quot;plus#activity\&quot;. | [optional] [default to &#39;plus#activity&#39;]
**location** | [**Place**](Place.md) |  | [optional] 
**object** | [**ActivityObject**](ActivityObject.md) |  | [optional] 
**placeId** | **String** | ID of the place where this activity occurred. | [optional] 
**placeName** | **String** | Name of the place where this activity occurred. | [optional] 
**provider** | [**ActivityProvider**](ActivityProvider.md) |  | [optional] 
**published** | **Date** | The time at which this activity was initially published. Formatted as an RFC 3339 timestamp. | [optional] 
**radius** | **String** | Radius, in meters, of the region where this activity occurred, centered at the latitude and longitude identified in geocode. | [optional] 
**title** | **String** | Title of this activity. | [optional] 
**updated** | **Date** | The time at which this activity was last updated. Formatted as an RFC 3339 timestamp. | [optional] 
**url** | **String** | The link to this activity. | [optional] 
**verb** | **String** | This activity&#39;s verb, which indicates the action that was performed. Possible values include, but are not limited to, the following values:   - \&quot;post\&quot; - Publish content to the stream.  - \&quot;share\&quot; - Reshare an activity. | [optional] 


