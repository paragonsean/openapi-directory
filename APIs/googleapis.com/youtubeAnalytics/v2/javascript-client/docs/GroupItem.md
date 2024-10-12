# YouTubeAnalyticsApi.GroupItem

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**errors** | [**Errors**](Errors.md) |  | [optional] 
**etag** | **String** | The Etag of this resource. | [optional] 
**groupId** | **String** | The ID that YouTube uses to uniquely identify the group that contains the item. | [optional] 
**id** | **String** | The ID that YouTube uses to uniquely identify the &#x60;channel&#x60;, &#x60;video&#x60;, &#x60;playlist&#x60;, or &#x60;asset&#x60; resource that is included in the group. Note that this ID refers specifically to the inclusion of that resource in a particular group and is different than the channel ID, video ID, playlist ID, or asset ID that uniquely identifies the resource itself. The &#x60;resource.id&#x60; property&#39;s value specifies the unique channel, video, playlist, or asset ID. | [optional] 
**kind** | **String** | Identifies the API resource&#39;s type. The value will be &#x60;youtube#groupItem&#x60;. | [optional] 
**resource** | [**GroupItemResource**](GroupItemResource.md) |  | [optional] 


