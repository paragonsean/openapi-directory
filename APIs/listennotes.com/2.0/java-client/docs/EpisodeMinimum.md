

# EpisodeMinimum


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**audio** | **String** | Audio url of this episode, which can be played directly. |  [optional] |
|**audioLengthSec** | **Integer** | Audio length of this episode. In seconds. |  [optional] |
|**description** | **String** | Html of this episode&#39;s full description |  [optional] |
|**explicitContent** | **Boolean** | Whether this podcast contains explicit language. |  [optional] |
|**id** | **String** | Episode id, which can be used to further fetch detailed episode metadata via &#x60;GET /episodes/{id}&#x60;. |  [optional] |
|**image** | **String** | Image url for this podcast&#39;s artwork. If you are using PRO/ENTERPRISE plan, then it&#39;s a high resolution image (1400x1400). If you are using FREE plan, then it&#39;s the same as **thumbnail**, low resolution image (300x300).  |  [optional] |
|**link** | **String** | Web link of this episode. |  [optional] |
|**listennotesEditUrl** | **String** | Edit url of this episode where you can update the audio url if you find the audio is broken. |  [optional] |
|**listennotesUrl** | **String** | The url of this episode on [ListenNotes.com](https://www.ListenNotes.com). |  [optional] |
|**maybeAudioInvalid** | **Boolean** | Whether or not this episode&#39;s audio is invalid. Podcasters may delete the original audio. |  [optional] |
|**pubDateMs** | **Integer** | Published date for this episode. In millisecond. |  [optional] |
|**thumbnail** | **String** | Thumbnail image url for this podcast&#39;s artwork (300x300). |  [optional] |
|**title** | **String** | Episode name. |  [optional] |



