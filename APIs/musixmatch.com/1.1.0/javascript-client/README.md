# musixmatch_api

MusixmatchApi - JavaScript client for musixmatch_api
Musixmatch lyrics API is a robust service that permits you to search and retrieve lyrics in the simplest possible way. It just works.

Include millions of licensed lyrics on your website or in your application legally.

The fastest, most powerful and legal way to display lyrics on your website or in your application.

#### Read musixmatch API Terms & Conditions and the Privacy Policy:
Before getting started, you must take a look at the [API Terms & Conditions](http://musixmatch.com/apiterms/) and the [Privacy Policy](https://developer.musixmatch.com/privacy). We’ve worked hard to make this service completely legal so that we are all protected from any foreseeable liability. Take the time to read this stuff.

#### Register for an API key:
All you need to do is [register](https://developer.musixmatch.com/signup) in order to get your API key, a mandatory parameter for most of our API calls. It’s your personal identifier and should be kept secret:

```
  https://api.musixmatch.com/ws/v1.1/track.get?apikey=YOUR_API_KEY
```
#### Integrate the musixmatch service with your web site or application
In the most common scenario you only need to implement two API calls: 
The first call is to match your catalog to ours using the [track.search](#!/Track/get_track_search) function and the second is to get the lyrics using the [track.lyrics.get](#!/Lyrics/get_track_lyrics_get) api. That’s it!

## API Methods
What does the musiXmatch API do?

The musiXmatch API allows you to read objects from our huge 100% licensed lyrics database.

To make your life easier we are providing you with one or more examples to show you how it could work in the wild. You’ll find both the API request and API response in all the available output formats for each API call. Follow the links below for the details.

The current API version is 1.1, the root URL is located at https://api.musixmatch.com/ws/1.1/

Supported input parameters can be found on the page [Input Parameters](https://developer.musixmatch.com/documentation/input-parameters). Use UTF-8 to encode arguments when calling API methods.

Every response includes a status_code. A list of all status codes can be consulted at [Status Codes](https://developer.musixmatch.com/documentation/status-codes).

## Music meta data
The musiXmatch api is built around lyrics, but there are many other data we provide through the api that can be used to improve every existent music service.

## Track
Inside the track object you can get the following extra information:

### TRACK RATING

The track rating is a score 0-100 identifying how popular is a song in musixmatch.

You can use this information to sort search results, like the most popular songs of an artist, of a music genre, of a lyrics language.

### INSTRUMENTAL AND EXPLICIT FLAGS

The instrumental flag identifies songs with music only, no lyrics.

The explicit flag identifies songs with explicit lyrics or explicit title. We're able to identify explicit words and set the flag for the most common languages.

### FAVOURITES

How many users have this song in their list of favourites.

Can be used to sort tracks by num favourite to identify more popular tracks within a set.

### MUSIC GENRE

The music genere of the song.

Can be used to group songs by genre, as input for similarity alghorithms, artist genre identification, navigate songs by genere, etc.

### SONG TITLES TRANSLATIONS

The track title, as translated in different lanauages, can be used to display the right writing for a given user, example:

LIES (Bigbang) becomes 在光化門 in chinese
HALLELUJAH (Bigbang) becomes ハレルヤ in japanese


## Artist
Inside the artist object you can get the following nice extra information:

### COMMENTS AND COUNTRY

An artist comment is a short snippet of text which can be mainly used for disambiguation.

The artist country is the born country of the artist/group

There are two perfect search result if you search by artist with the keyword \"U2\". Indeed there are two distinct music groups with this same name, one is the most known irish group of Bono Vox, the other is a less popular (world wide speaking) group from Japan.

Here's how you can made use of the artist comment in your search result page:

U2 (Irish rock band)
U2 (あきやまうに)
You can also show the artist country for even better disambiguation:

U2 (Irish rock band) from Ireland
U2 (あきやまうに) from Japan
ARTIST TRANSLATIONS

When you create a world wide music related service you have to take into consideration to display the artist name in the user's local language. These translation are also used as aliases to improve the search results.

Let's use PSY for this example.

Western people know him as PSY but korean want to see the original name 싸이.

Using the name translations provided by our api you can show to every user the writing they expect to see.

Furthermore, when you search for \"psy gangnam style\" or \"싸이 gangnam style\" with our search/match api you will still be able to find the song.

### ARTIST RATING

The artist rating is a score 0-100 identifying how popular is an artist in musixmatch.

You can use this information to build charts, for suggestions, to sort search results. In the example above about U2, we use the artist rating to show the irish band before the japanese one in our serp.

### ARTIST MUSIC GENRE

We provide one or more main artist genre, this information can be used to calculate similar artist, suggestions, or the filter a search by artist genre.



## Album
Inside the album object you can get the following nice extra information:

### ALBUM RATING

The album rating is a score 0-100 identifying how popular is an album in musixmatch.

You can use this information to sort search results, like the most popular albums of an artist.

### ALBUM RATING

The album rating is a score 0-100 identifying how popular is an album in musixmatch.

You can use this information to sort search results, like the most popular albums of an artist.

### ALBUM COPYRIGHT AND LABEL

For most of our albums we can provide extra information like for example:

Label: Universal-Island Records Ltd.
Copyright: (P) 2013 Rubyworks, under license to Columbia Records, a Division of Sony Music Entertainment.
ALBUM TYPE AND RELEASE DATE

The album official release date can be used to sort an artist's albums view starting by the most recent one.

Album can also be filtered or grouped by type: Single, Album, Compilation, Remix, Live. This can help to build an artist page with a more organized structure.

### ALBUM MUSIC GENRE

For most of the albums we provide two groups of music genres. Primary and secondary. This information can be used to help user navigate albums by genre.

An example could be:

Primary genere: POP
Secondary genre: K-POP or Mandopop

This SDK is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 1.1.0
- Package version: 1.1.0
- Generator version: 7.9.0
- Build package: org.openapitools.codegen.languages.JavascriptClientCodegen
For more information, please visit [https://musixmatch.com](https://musixmatch.com)

## Installation

### For [Node.js](https://nodejs.org/)

#### npm

To publish the library as a [npm](https://www.npmjs.com/), please follow the procedure in ["Publishing npm packages"](https://docs.npmjs.com/getting-started/publishing-npm-packages).

Then install it via:

```shell
npm install musixmatch_api --save
```

Finally, you need to build the module:

```shell
npm run build
```

##### Local development

To use the library locally without publishing to a remote npm registry, first install the dependencies by changing into the directory containing `package.json` (and this README). Let's call this `JAVASCRIPT_CLIENT_DIR`. Then run:

```shell
npm install
```

Next, [link](https://docs.npmjs.com/cli/link) it globally in npm with the following, also from `JAVASCRIPT_CLIENT_DIR`:

```shell
npm link
```

To use the link you just defined in your project, switch to the directory you want to use your musixmatch_api from, and run:

```shell
npm link /path/to/<JAVASCRIPT_CLIENT_DIR>
```

Finally, you need to build the module:

```shell
npm run build
```

#### git

If the library is hosted at a git repository, e.g.https://github.com/GIT_USER_ID/GIT_REPO_ID
then install it via:

```shell
    npm install GIT_USER_ID/GIT_REPO_ID --save
```

### For browser

The library also works in the browser environment via npm and [browserify](http://browserify.org/). After following
the above steps with Node.js and installing browserify with `npm install -g browserify`,
perform the following (assuming *main.js* is your entry file):

```shell
browserify main.js > bundle.js
```

Then include *bundle.js* in the HTML pages.

### Webpack Configuration

Using Webpack you may encounter the following error: "Module not found: Error:
Cannot resolve module", most certainly you should disable AMD loader. Add/merge
the following section to your webpack config:

```javascript
module: {
  rules: [
    {
      parser: {
        amd: false
      }
    }
  ]
}
```

## Getting Started

Please follow the [installation](#installation) instruction and execute the following JS code:

```javascript
var MusixmatchApi = require('musixmatch_api');

var defaultClient = MusixmatchApi.ApiClient.instance;
// Configure API key authorization: key
var key = defaultClient.authentications['key'];
key.apiKey = "YOUR API KEY"
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//key.apiKeyPrefix['apikey'] = "Token"

var api = new MusixmatchApi.AlbumApi()
var albumId = "albumId_example"; // {String} The musiXmatch album id
var opts = {
  'format': "'json'", // {String} output format: json, jsonp, xml.
  'callback': "callback_example" // {String} jsonp callback
};
var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
};
api.albumGetGet(albumId, opts, callback);

```

## Documentation for API Endpoints

All URIs are relative to *https://api.musixmatch.com/ws/1.1*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*MusixmatchApi.AlbumApi* | [**albumGetGet**](docs/AlbumApi.md#albumGetGet) | **GET** /album.get | 
*MusixmatchApi.AlbumApi* | [**artistAlbumsGetGet**](docs/AlbumApi.md#artistAlbumsGetGet) | **GET** /artist.albums.get | 
*MusixmatchApi.ArtistApi* | [**artistGetGet**](docs/ArtistApi.md#artistGetGet) | **GET** /artist.get | 
*MusixmatchApi.ArtistApi* | [**artistRelatedGetGet**](docs/ArtistApi.md#artistRelatedGetGet) | **GET** /artist.related.get | 
*MusixmatchApi.ArtistApi* | [**artistSearchGet**](docs/ArtistApi.md#artistSearchGet) | **GET** /artist.search | 
*MusixmatchApi.ArtistApi* | [**chartArtistsGetGet**](docs/ArtistApi.md#chartArtistsGetGet) | **GET** /chart.artists.get | 
*MusixmatchApi.LyricsApi* | [**matcherLyricsGetGet**](docs/LyricsApi.md#matcherLyricsGetGet) | **GET** /matcher.lyrics.get | 
*MusixmatchApi.LyricsApi* | [**trackLyricsGetGet**](docs/LyricsApi.md#trackLyricsGetGet) | **GET** /track.lyrics.get | 
*MusixmatchApi.SnippetApi* | [**trackSnippetGetGet**](docs/SnippetApi.md#trackSnippetGetGet) | **GET** /track.snippet.get | 
*MusixmatchApi.SubtitleApi* | [**matcherSubtitleGetGet**](docs/SubtitleApi.md#matcherSubtitleGetGet) | **GET** /matcher.subtitle.get | 
*MusixmatchApi.SubtitleApi* | [**trackSubtitleGetGet**](docs/SubtitleApi.md#trackSubtitleGetGet) | **GET** /track.subtitle.get | 
*MusixmatchApi.TrackApi* | [**albumTracksGetGet**](docs/TrackApi.md#albumTracksGetGet) | **GET** /album.tracks.get | 
*MusixmatchApi.TrackApi* | [**chartTracksGetGet**](docs/TrackApi.md#chartTracksGetGet) | **GET** /chart.tracks.get | 
*MusixmatchApi.TrackApi* | [**matcherTrackGetGet**](docs/TrackApi.md#matcherTrackGetGet) | **GET** /matcher.track.get | 
*MusixmatchApi.TrackApi* | [**trackGetGet**](docs/TrackApi.md#trackGetGet) | **GET** /track.get | 
*MusixmatchApi.TrackApi* | [**trackSearchGet**](docs/TrackApi.md#trackSearchGet) | **GET** /track.search | 


## Documentation for Models

 - [MusixmatchApi.Album](docs/Album.md)
 - [MusixmatchApi.AlbumGetGet200Response](docs/AlbumGetGet200Response.md)
 - [MusixmatchApi.AlbumGetGet200ResponseMessage](docs/AlbumGetGet200ResponseMessage.md)
 - [MusixmatchApi.AlbumGetGet200ResponseMessageBody](docs/AlbumGetGet200ResponseMessageBody.md)
 - [MusixmatchApi.AlbumGetGet200ResponseMessageHeader](docs/AlbumGetGet200ResponseMessageHeader.md)
 - [MusixmatchApi.AlbumPrimaryGenres](docs/AlbumPrimaryGenres.md)
 - [MusixmatchApi.AlbumPrimaryGenresMusicGenreListInner](docs/AlbumPrimaryGenresMusicGenreListInner.md)
 - [MusixmatchApi.AlbumPrimaryGenresMusicGenreListInnerMusicGenre](docs/AlbumPrimaryGenresMusicGenreListInnerMusicGenre.md)
 - [MusixmatchApi.AlbumSecondaryGenres](docs/AlbumSecondaryGenres.md)
 - [MusixmatchApi.AlbumTracksGetGet200Response](docs/AlbumTracksGetGet200Response.md)
 - [MusixmatchApi.AlbumTracksGetGet200ResponseMessage](docs/AlbumTracksGetGet200ResponseMessage.md)
 - [MusixmatchApi.AlbumTracksGetGet200ResponseMessageBody](docs/AlbumTracksGetGet200ResponseMessageBody.md)
 - [MusixmatchApi.AlbumTracksGetGet200ResponseMessageHeader](docs/AlbumTracksGetGet200ResponseMessageHeader.md)
 - [MusixmatchApi.Artist](docs/Artist.md)
 - [MusixmatchApi.ArtistAlbumsGetGet200Response](docs/ArtistAlbumsGetGet200Response.md)
 - [MusixmatchApi.ArtistAlbumsGetGet200ResponseMessage](docs/ArtistAlbumsGetGet200ResponseMessage.md)
 - [MusixmatchApi.ArtistAlbumsGetGet200ResponseMessageBody](docs/ArtistAlbumsGetGet200ResponseMessageBody.md)
 - [MusixmatchApi.ArtistArtistAliasListInner](docs/ArtistArtistAliasListInner.md)
 - [MusixmatchApi.ArtistArtistCredits](docs/ArtistArtistCredits.md)
 - [MusixmatchApi.ArtistArtistNameTranslationListInner](docs/ArtistArtistNameTranslationListInner.md)
 - [MusixmatchApi.ArtistArtistNameTranslationListInnerArtistNameTranslation](docs/ArtistArtistNameTranslationListInnerArtistNameTranslation.md)
 - [MusixmatchApi.ArtistGetGet200Response](docs/ArtistGetGet200Response.md)
 - [MusixmatchApi.ArtistGetGet200ResponseMessage](docs/ArtistGetGet200ResponseMessage.md)
 - [MusixmatchApi.ArtistGetGet200ResponseMessageBody](docs/ArtistGetGet200ResponseMessageBody.md)
 - [MusixmatchApi.ArtistRelatedGetGet200Response](docs/ArtistRelatedGetGet200Response.md)
 - [MusixmatchApi.ArtistRelatedGetGet200ResponseMessage](docs/ArtistRelatedGetGet200ResponseMessage.md)
 - [MusixmatchApi.ArtistRelatedGetGet200ResponseMessageBody](docs/ArtistRelatedGetGet200ResponseMessageBody.md)
 - [MusixmatchApi.ChartArtistsGetGet200Response](docs/ChartArtistsGetGet200Response.md)
 - [MusixmatchApi.ChartArtistsGetGet200ResponseMessage](docs/ChartArtistsGetGet200ResponseMessage.md)
 - [MusixmatchApi.ChartArtistsGetGet200ResponseMessageHeader](docs/ChartArtistsGetGet200ResponseMessageHeader.md)
 - [MusixmatchApi.ChartTracksGetGet200Response](docs/ChartTracksGetGet200Response.md)
 - [MusixmatchApi.ChartTracksGetGet200ResponseMessage](docs/ChartTracksGetGet200ResponseMessage.md)
 - [MusixmatchApi.ChartTracksGetGet200ResponseMessageBody](docs/ChartTracksGetGet200ResponseMessageBody.md)
 - [MusixmatchApi.ChartTracksGetGet200ResponseMessageBodyTrackListInner](docs/ChartTracksGetGet200ResponseMessageBodyTrackListInner.md)
 - [MusixmatchApi.Lyrics](docs/Lyrics.md)
 - [MusixmatchApi.MatcherLyricsGetGet200Response](docs/MatcherLyricsGetGet200Response.md)
 - [MusixmatchApi.MatcherLyricsGetGet200ResponseMessage](docs/MatcherLyricsGetGet200ResponseMessage.md)
 - [MusixmatchApi.MatcherLyricsGetGet200ResponseMessageBody](docs/MatcherLyricsGetGet200ResponseMessageBody.md)
 - [MusixmatchApi.MatcherSubtitleGetGet200Response](docs/MatcherSubtitleGetGet200Response.md)
 - [MusixmatchApi.MatcherSubtitleGetGet200ResponseMessage](docs/MatcherSubtitleGetGet200ResponseMessage.md)
 - [MusixmatchApi.MatcherSubtitleGetGet200ResponseMessageBody](docs/MatcherSubtitleGetGet200ResponseMessageBody.md)
 - [MusixmatchApi.MatcherTrackGetGet200Response](docs/MatcherTrackGetGet200Response.md)
 - [MusixmatchApi.MatcherTrackGetGet200ResponseMessage](docs/MatcherTrackGetGet200ResponseMessage.md)
 - [MusixmatchApi.Snippet](docs/Snippet.md)
 - [MusixmatchApi.Subtitle](docs/Subtitle.md)
 - [MusixmatchApi.Track](docs/Track.md)
 - [MusixmatchApi.TrackSnippetGetGet200Response](docs/TrackSnippetGetGet200Response.md)
 - [MusixmatchApi.TrackSnippetGetGet200ResponseMessage](docs/TrackSnippetGetGet200ResponseMessage.md)
 - [MusixmatchApi.TrackSnippetGetGet200ResponseMessageBody](docs/TrackSnippetGetGet200ResponseMessageBody.md)


## Documentation for Authorization


Authentication schemes defined for the API:
### key


- **Type**: API key
- **API key parameter name**: apikey
- **Location**: URL query string

