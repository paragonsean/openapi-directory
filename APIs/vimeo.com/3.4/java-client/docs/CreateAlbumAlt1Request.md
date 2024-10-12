

# CreateAlbumAlt1Request


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**brandColor** | **String** | The hexadecimal code for the color of the player buttons. |  [optional] |
|**description** | **String** | The description of the album. |  [optional] |
|**hideNav** | **Boolean** | Whether to hide Vimeo navigation when displaying the album. |  [optional] |
|**layout** | [**LayoutEnum**](#LayoutEnum) | The type of layout for presenting the album. |  [optional] |
|**name** | **String** | The name of the album. |  |
|**password** | **String** | The album&#39;s password. Required only if **privacy** is &#x60;password&#x60;. |  [optional] |
|**privacy** | [**PrivacyEnum**](#PrivacyEnum) | The privacy level of the album. |  [optional] |
|**reviewMode** | **Boolean** | Whether album videos should use the review mode URL. |  [optional] |
|**sort** | [**SortEnum**](#SortEnum) | The default sort order of the album&#39;s videos. |  [optional] |
|**theme** | [**ThemeEnum**](#ThemeEnum) | The color theme of the album. |  [optional] |



## Enum: LayoutEnum

| Name | Value |
|---- | -----|
| GRID | &quot;grid&quot; |
| PLAYER | &quot;player&quot; |



## Enum: PrivacyEnum

| Name | Value |
|---- | -----|
| ANYBODY | &quot;anybody&quot; |
| EMBED_ONLY | &quot;embed_only&quot; |
| PASSWORD | &quot;password&quot; |



## Enum: SortEnum

| Name | Value |
|---- | -----|
| ADDED_FIRST | &quot;added_first&quot; |
| ADDED_LAST | &quot;added_last&quot; |
| ALPHABETICAL | &quot;alphabetical&quot; |
| ARRANGED | &quot;arranged&quot; |
| COMMENTS | &quot;comments&quot; |
| LIKES | &quot;likes&quot; |
| NEWEST | &quot;newest&quot; |
| OLDEST | &quot;oldest&quot; |
| PLAYS | &quot;plays&quot; |



## Enum: ThemeEnum

| Name | Value |
|---- | -----|
| DARK | &quot;dark&quot; |
| STANDARD | &quot;standard&quot; |



