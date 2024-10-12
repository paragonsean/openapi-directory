# Vimeo.EditAlbumAlt1Request

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**brandColor** | **String** | The hexadecimal code for the color of the player buttons. | [optional] 
**description** | **String** | The description of the album. | [optional] 
**domain** | **String** | The custom domain a user has selected for their album. | [optional] 
**hideNav** | **Boolean** | Whether to hide Vimeo navigation when displaying the album. | [optional] 
**layout** | **String** | The type of layout for presenting the album. | [optional] 
**name** | **String** | The name of the album. | [optional] 
**password** | **String** | The album&#39;s password. Required only if **privacy** is &#x60;password&#x60;. | [optional] 
**privacy** | **String** | The privacy level of the album. | [optional] 
**reviewMode** | **Boolean** | Whether album videos should use the review mode URL. | [optional] 
**sort** | **String** | The default sort order of the album&#39;s videos. | [optional] 
**theme** | **String** | The color theme of the album. | [optional] 
**url** | **String** | The custom Vimeo URL a user has selected for their album. | [optional] 
**useCustomDomain** | **Boolean** | Whether the user has opted in to use a custom domain for their album. | [optional] 



## Enum: LayoutEnum


* `grid` (value: `"grid"`)

* `player` (value: `"player"`)





## Enum: PrivacyEnum


* `anybody` (value: `"anybody"`)

* `embed_only` (value: `"embed_only"`)

* `password` (value: `"password"`)





## Enum: SortEnum


* `added_first` (value: `"added_first"`)

* `added_last` (value: `"added_last"`)

* `alphabetical` (value: `"alphabetical"`)

* `arranged` (value: `"arranged"`)

* `comments` (value: `"comments"`)

* `likes` (value: `"likes"`)

* `newest` (value: `"newest"`)

* `oldest` (value: `"oldest"`)

* `plays` (value: `"plays"`)





## Enum: ThemeEnum


* `dark` (value: `"dark"`)

* `standard` (value: `"standard"`)




