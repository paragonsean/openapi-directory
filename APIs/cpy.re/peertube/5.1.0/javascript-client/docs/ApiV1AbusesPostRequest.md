# PeerTube.ApiV1AbusesPostRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account** | [**ApiV1AbusesPostRequestAccount**](ApiV1AbusesPostRequestAccount.md) |  | [optional] 
**comment** | [**ApiV1AbusesPostRequestComment**](ApiV1AbusesPostRequestComment.md) |  | [optional] 
**predefinedReasons** | **[String]** | Reason categories that help triage reports | [optional] 
**reason** | **String** | Reason why the user reports this video | 
**video** | [**ApiV1AbusesPostRequestVideo**](ApiV1AbusesPostRequestVideo.md) |  | [optional] 



## Enum: [PredefinedReasonsEnum]


* `violentOrAbusive` (value: `"violentOrAbusive"`)

* `hatefulOrAbusive` (value: `"hatefulOrAbusive"`)

* `spamOrMisleading` (value: `"spamOrMisleading"`)

* `privacy` (value: `"privacy"`)

* `rights` (value: `"rights"`)

* `serverRules` (value: `"serverRules"`)

* `thumbnails` (value: `"thumbnails"`)

* `captions` (value: `"captions"`)




