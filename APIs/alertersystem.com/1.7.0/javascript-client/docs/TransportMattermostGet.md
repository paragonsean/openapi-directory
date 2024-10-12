# AlerterSystemApi.TransportMattermostGet

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**createdAt** | **Date** | When the resource instance was created. This date-time is in the UTC timezone. | [optional] 
**dataSegmentCode** | **String** | User-provided string on which to segment and filter data. Max 50 characters. | [optional] 
**id** | **String** | The unique identifier of the resource instance. | [optional] [readonly] 
**mattermostAccessToken** | **String** | The access token for the Mattermost service. Stored in encrypted format. | 
**mattermostChannel** | **String** | The default channel ID for the Mattermost service. | 
**mattermostHost** | **String** | The host for the Mattermost service. | 
**mattermostPath** | **String** | The optional path for the Mattermost service. | [optional] 
**partition** | **String** | The partition that contains this resource instance. The resource cannot be moved to another partition. | 
**resourceOwner** | **String** | The name of the person who owns this resource. | [optional] 
**transportName** | **String** | The name of the transport. | 


