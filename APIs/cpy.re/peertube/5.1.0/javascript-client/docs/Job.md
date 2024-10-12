# PeerTube.Job

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**createdAt** | **Date** |  | [optional] 
**data** | **{String: Object}** |  | [optional] 
**error** | **{String: Object}** |  | [optional] 
**finishedOn** | **Date** |  | [optional] 
**id** | **Number** |  | [optional] 
**processedOn** | **Date** |  | [optional] 
**state** | **String** |  | [optional] 
**type** | **String** |  | [optional] 



## Enum: StateEnum


* `active` (value: `"active"`)

* `completed` (value: `"completed"`)

* `failed` (value: `"failed"`)

* `waiting` (value: `"waiting"`)

* `delayed` (value: `"delayed"`)





## Enum: TypeEnum


* `activitypub-http-unicast` (value: `"activitypub-http-unicast"`)

* `activitypub-http-broadcast` (value: `"activitypub-http-broadcast"`)

* `activitypub-http-fetcher` (value: `"activitypub-http-fetcher"`)

* `activitypub-follow` (value: `"activitypub-follow"`)

* `video-file-import` (value: `"video-file-import"`)

* `video-transcoding` (value: `"video-transcoding"`)

* `email` (value: `"email"`)

* `video-import` (value: `"video-import"`)

* `videos-views-stats` (value: `"videos-views-stats"`)

* `activitypub-refresher` (value: `"activitypub-refresher"`)

* `video-redundancy` (value: `"video-redundancy"`)

* `video-channel-import` (value: `"video-channel-import"`)




