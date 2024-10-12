# Vimeo.Album

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allowContinuousPlay** | **Boolean** | Whether an album should allow continuous play. | 
**allowDownloads** | **Boolean** | Whether an album should allow downloads. | 
**allowShare** | **Boolean** | Whether an album should allow sharing. | 
**brandColor** | **String** | Hexadecimal color code for the decorative color. For example, album videos use this color for player buttons. | 
**createdTime** | **String** | The time in ISO 8601 format that the album was created. | 
**customLogo** | [**Picture**](Picture.md) | The custom logo for this album. | 
**description** | **String** | A brief description of the album&#39;s content. | 
**domain** | **String** | The custom domain a user has selected for their album. | 
**duration** | **Number** | The total duration in seconds of all the videos in the album. | 
**embed** | [**AlbumEmbed**](AlbumEmbed.md) |  | 
**embedBrandColor** | **Boolean** | Whether to show the album&#39;s custom brand color in the player of the album&#39;s embedded playlist. | 
**embedCustomLogo** | **Boolean** | Whether to show the album&#39;s custom logo in the player of the album&#39;s embedded playlist. | 
**hideNav** | **Boolean** | Whether to hide the Vimeo navigation when viewing the album. | 
**hideVimeoLogo** | **Boolean** | Whether to hide the Vimeo logo in the player of the album&#39;s embedded playlist. | 
**layout** | **String** | The album&#39;s layout preference | 
**link** | **String** | The URL to access the album. | 
**metadata** | [**AlbumMetadata**](AlbumMetadata.md) |  | 
**modifiedTime** | **String** | The time in ISO 8601 format when the album was last modified. | 
**name** | **String** | The album&#39;s display name. | 
**pictures** | [**Picture**](Picture.md) | The active image for the album; defaults to the thumbnail of the last video added to the album. | 
**privacy** | [**AlbumPrivacy**](AlbumPrivacy.md) |  | 
**resourceKey** | **String** | The album resource key. | 
**reviewMode** | **Boolean** | Whether album videos should use the review mode URL. | 
**sort** | **String** | Sort type of the album. | 
**theme** | **String** | The album&#39;s color theme preference | 
**uri** | **String** | The album&#39;s URI. | 
**url** | **String** | The custom Vimeo URL a user has selected for their album. | 
**useCustomDomain** | **Boolean** | Whether the user has opted in to use a custom domain for their album. | 
**user** | [**User**](User.md) | The owner of the album. | 
**webBrandColor** | **Boolean** | Whether an album should show the brand color in the web layout. | 
**webCustomLogo** | **Boolean** | Whether an album&#39;s custom logo should be shown in the web layout. | 



## Enum: LayoutEnum


* `grid` (value: `"grid"`)

* `player` (value: `"player"`)





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




