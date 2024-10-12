/**
 * Musixmatch API
 * Musixmatch lyrics API is a robust service that permits you to search and retrieve lyrics in the simplest possible way. It just works.  Include millions of licensed lyrics on your website or in your application legally.  The fastest, most powerful and legal way to display lyrics on your website or in your application.  #### Read musixmatch API Terms & Conditions and the Privacy Policy: Before getting started, you must take a look at the [API Terms & Conditions](http://musixmatch.com/apiterms/) and the [Privacy Policy](https://developer.musixmatch.com/privacy). We’ve worked hard to make this service completely legal so that we are all protected from any foreseeable liability. Take the time to read this stuff.  #### Register for an API key: All you need to do is [register](https://developer.musixmatch.com/signup) in order to get your API key, a mandatory parameter for most of our API calls. It’s your personal identifier and should be kept secret:  ```   https://api.musixmatch.com/ws/v1.1/track.get?apikey=YOUR_API_KEY ``` #### Integrate the musixmatch service with your web site or application In the most common scenario you only need to implement two API calls:  The first call is to match your catalog to ours using the [track.search](#!/Track/get_track_search) function and the second is to get the lyrics using the [track.lyrics.get](#!/Lyrics/get_track_lyrics_get) api. That’s it!  ## API Methods What does the musiXmatch API do?  The musiXmatch API allows you to read objects from our huge 100% licensed lyrics database.  To make your life easier we are providing you with one or more examples to show you how it could work in the wild. You’ll find both the API request and API response in all the available output formats for each API call. Follow the links below for the details.  The current API version is 1.1, the root URL is located at https://api.musixmatch.com/ws/1.1/  Supported input parameters can be found on the page [Input Parameters](https://developer.musixmatch.com/documentation/input-parameters). Use UTF-8 to encode arguments when calling API methods.  Every response includes a status_code. A list of all status codes can be consulted at [Status Codes](https://developer.musixmatch.com/documentation/status-codes).  ## Music meta data The musiXmatch api is built around lyrics, but there are many other data we provide through the api that can be used to improve every existent music service.  ## Track Inside the track object you can get the following extra information:  ### TRACK RATING  The track rating is a score 0-100 identifying how popular is a song in musixmatch.  You can use this information to sort search results, like the most popular songs of an artist, of a music genre, of a lyrics language.  ### INSTRUMENTAL AND EXPLICIT FLAGS  The instrumental flag identifies songs with music only, no lyrics.  The explicit flag identifies songs with explicit lyrics or explicit title. We're able to identify explicit words and set the flag for the most common languages.  ### FAVOURITES  How many users have this song in their list of favourites.  Can be used to sort tracks by num favourite to identify more popular tracks within a set.  ### MUSIC GENRE  The music genere of the song.  Can be used to group songs by genre, as input for similarity alghorithms, artist genre identification, navigate songs by genere, etc.  ### SONG TITLES TRANSLATIONS  The track title, as translated in different lanauages, can be used to display the right writing for a given user, example:  LIES (Bigbang) becomes 在光化門 in chinese HALLELUJAH (Bigbang) becomes ハレルヤ in japanese   ## Artist Inside the artist object you can get the following nice extra information:  ### COMMENTS AND COUNTRY  An artist comment is a short snippet of text which can be mainly used for disambiguation.  The artist country is the born country of the artist/group  There are two perfect search result if you search by artist with the keyword \"U2\". Indeed there are two distinct music groups with this same name, one is the most known irish group of Bono Vox, the other is a less popular (world wide speaking) group from Japan.  Here's how you can made use of the artist comment in your search result page:  U2 (Irish rock band) U2 (あきやまうに) You can also show the artist country for even better disambiguation:  U2 (Irish rock band) from Ireland U2 (あきやまうに) from Japan ARTIST TRANSLATIONS  When you create a world wide music related service you have to take into consideration to display the artist name in the user's local language. These translation are also used as aliases to improve the search results.  Let's use PSY for this example.  Western people know him as PSY but korean want to see the original name 싸이.  Using the name translations provided by our api you can show to every user the writing they expect to see.  Furthermore, when you search for \"psy gangnam style\" or \"싸이 gangnam style\" with our search/match api you will still be able to find the song.  ### ARTIST RATING  The artist rating is a score 0-100 identifying how popular is an artist in musixmatch.  You can use this information to build charts, for suggestions, to sort search results. In the example above about U2, we use the artist rating to show the irish band before the japanese one in our serp.  ### ARTIST MUSIC GENRE  We provide one or more main artist genre, this information can be used to calculate similar artist, suggestions, or the filter a search by artist genre.    ## Album Inside the album object you can get the following nice extra information:  ### ALBUM RATING  The album rating is a score 0-100 identifying how popular is an album in musixmatch.  You can use this information to sort search results, like the most popular albums of an artist.  ### ALBUM RATING  The album rating is a score 0-100 identifying how popular is an album in musixmatch.  You can use this information to sort search results, like the most popular albums of an artist.  ### ALBUM COPYRIGHT AND LABEL  For most of our albums we can provide extra information like for example:  Label: Universal-Island Records Ltd. Copyright: (P) 2013 Rubyworks, under license to Columbia Records, a Division of Sony Music Entertainment. ALBUM TYPE AND RELEASE DATE  The album official release date can be used to sort an artist's albums view starting by the most recent one.  Album can also be filtered or grouped by type: Single, Album, Compilation, Remix, Live. This can help to build an artist page with a more organized structure.  ### ALBUM MUSIC GENRE  For most of the albums we provide two groups of music genres. Primary and secondary. This information can be used to help user navigate albums by genre.  An example could be:  Primary genere: POP Secondary genre: K-POP or Mandopop 
 *
 * The version of the OpenAPI document: 1.1.0
 * Contact: info@musixmatch.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */


import ApiClient from './ApiClient';
import Album from './model/Album';
import AlbumGetGet200Response from './model/AlbumGetGet200Response';
import AlbumGetGet200ResponseMessage from './model/AlbumGetGet200ResponseMessage';
import AlbumGetGet200ResponseMessageBody from './model/AlbumGetGet200ResponseMessageBody';
import AlbumGetGet200ResponseMessageHeader from './model/AlbumGetGet200ResponseMessageHeader';
import AlbumPrimaryGenres from './model/AlbumPrimaryGenres';
import AlbumPrimaryGenresMusicGenreListInner from './model/AlbumPrimaryGenresMusicGenreListInner';
import AlbumPrimaryGenresMusicGenreListInnerMusicGenre from './model/AlbumPrimaryGenresMusicGenreListInnerMusicGenre';
import AlbumSecondaryGenres from './model/AlbumSecondaryGenres';
import AlbumTracksGetGet200Response from './model/AlbumTracksGetGet200Response';
import AlbumTracksGetGet200ResponseMessage from './model/AlbumTracksGetGet200ResponseMessage';
import AlbumTracksGetGet200ResponseMessageBody from './model/AlbumTracksGetGet200ResponseMessageBody';
import AlbumTracksGetGet200ResponseMessageHeader from './model/AlbumTracksGetGet200ResponseMessageHeader';
import Artist from './model/Artist';
import ArtistAlbumsGetGet200Response from './model/ArtistAlbumsGetGet200Response';
import ArtistAlbumsGetGet200ResponseMessage from './model/ArtistAlbumsGetGet200ResponseMessage';
import ArtistAlbumsGetGet200ResponseMessageBody from './model/ArtistAlbumsGetGet200ResponseMessageBody';
import ArtistArtistAliasListInner from './model/ArtistArtistAliasListInner';
import ArtistArtistCredits from './model/ArtistArtistCredits';
import ArtistArtistNameTranslationListInner from './model/ArtistArtistNameTranslationListInner';
import ArtistArtistNameTranslationListInnerArtistNameTranslation from './model/ArtistArtistNameTranslationListInnerArtistNameTranslation';
import ArtistGetGet200Response from './model/ArtistGetGet200Response';
import ArtistGetGet200ResponseMessage from './model/ArtistGetGet200ResponseMessage';
import ArtistGetGet200ResponseMessageBody from './model/ArtistGetGet200ResponseMessageBody';
import ArtistRelatedGetGet200Response from './model/ArtistRelatedGetGet200Response';
import ArtistRelatedGetGet200ResponseMessage from './model/ArtistRelatedGetGet200ResponseMessage';
import ArtistRelatedGetGet200ResponseMessageBody from './model/ArtistRelatedGetGet200ResponseMessageBody';
import ChartArtistsGetGet200Response from './model/ChartArtistsGetGet200Response';
import ChartArtistsGetGet200ResponseMessage from './model/ChartArtistsGetGet200ResponseMessage';
import ChartArtistsGetGet200ResponseMessageHeader from './model/ChartArtistsGetGet200ResponseMessageHeader';
import ChartTracksGetGet200Response from './model/ChartTracksGetGet200Response';
import ChartTracksGetGet200ResponseMessage from './model/ChartTracksGetGet200ResponseMessage';
import ChartTracksGetGet200ResponseMessageBody from './model/ChartTracksGetGet200ResponseMessageBody';
import ChartTracksGetGet200ResponseMessageBodyTrackListInner from './model/ChartTracksGetGet200ResponseMessageBodyTrackListInner';
import Lyrics from './model/Lyrics';
import MatcherLyricsGetGet200Response from './model/MatcherLyricsGetGet200Response';
import MatcherLyricsGetGet200ResponseMessage from './model/MatcherLyricsGetGet200ResponseMessage';
import MatcherLyricsGetGet200ResponseMessageBody from './model/MatcherLyricsGetGet200ResponseMessageBody';
import MatcherSubtitleGetGet200Response from './model/MatcherSubtitleGetGet200Response';
import MatcherSubtitleGetGet200ResponseMessage from './model/MatcherSubtitleGetGet200ResponseMessage';
import MatcherSubtitleGetGet200ResponseMessageBody from './model/MatcherSubtitleGetGet200ResponseMessageBody';
import MatcherTrackGetGet200Response from './model/MatcherTrackGetGet200Response';
import MatcherTrackGetGet200ResponseMessage from './model/MatcherTrackGetGet200ResponseMessage';
import Snippet from './model/Snippet';
import Subtitle from './model/Subtitle';
import Track from './model/Track';
import TrackSnippetGetGet200Response from './model/TrackSnippetGetGet200Response';
import TrackSnippetGetGet200ResponseMessage from './model/TrackSnippetGetGet200ResponseMessage';
import TrackSnippetGetGet200ResponseMessageBody from './model/TrackSnippetGetGet200ResponseMessageBody';
import AlbumApi from './api/AlbumApi';
import ArtistApi from './api/ArtistApi';
import LyricsApi from './api/LyricsApi';
import SnippetApi from './api/SnippetApi';
import SubtitleApi from './api/SubtitleApi';
import TrackApi from './api/TrackApi';


/**
* Musixmatch lyrics API is a robust service that permits you to search and retrieve lyrics in the simplest possible way. It just works.  Include millions of licensed lyrics on your website or in your application legally.  The fastest, most powerful and legal way to display lyrics on your website or in your application.  #### Read musixmatch API Terms &amp; Conditions and the Privacy Policy: Before getting started, you must take a look at the [API Terms &amp; Conditions](http://musixmatch.com/apiterms/) and the [Privacy Policy](https://developer.musixmatch.com/privacy). We’ve worked hard to make this service completely legal so that we are all protected from any foreseeable liability. Take the time to read this stuff.  #### Register for an API key: All you need to do is [register](https://developer.musixmatch.com/signup) in order to get your API key, a mandatory parameter for most of our API calls. It’s your personal identifier and should be kept secret:  &#x60;&#x60;&#x60;   https://api.musixmatch.com/ws/v1.1/track.get?apikey&#x3D;YOUR_API_KEY &#x60;&#x60;&#x60; #### Integrate the musixmatch service with your web site or application In the most common scenario you only need to implement two API calls:  The first call is to match your catalog to ours using the [track.search](#!/Track/get_track_search) function and the second is to get the lyrics using the [track.lyrics.get](#!/Lyrics/get_track_lyrics_get) api. That’s it!  ## API Methods What does the musiXmatch API do?  The musiXmatch API allows you to read objects from our huge 100% licensed lyrics database.  To make your life easier we are providing you with one or more examples to show you how it could work in the wild. You’ll find both the API request and API response in all the available output formats for each API call. Follow the links below for the details.  The current API version is 1.1, the root URL is located at https://api.musixmatch.com/ws/1.1/  Supported input parameters can be found on the page [Input Parameters](https://developer.musixmatch.com/documentation/input-parameters). Use UTF-8 to encode arguments when calling API methods.  Every response includes a status_code. A list of all status codes can be consulted at [Status Codes](https://developer.musixmatch.com/documentation/status-codes).  ## Music meta data The musiXmatch api is built around lyrics, but there are many other data we provide through the api that can be used to improve every existent music service.  ## Track Inside the track object you can get the following extra information:  ### TRACK RATING  The track rating is a score 0-100 identifying how popular is a song in musixmatch.  You can use this information to sort search results, like the most popular songs of an artist, of a music genre, of a lyrics language.  ### INSTRUMENTAL AND EXPLICIT FLAGS  The instrumental flag identifies songs with music only, no lyrics.  The explicit flag identifies songs with explicit lyrics or explicit title. We&#39;re able to identify explicit words and set the flag for the most common languages.  ### FAVOURITES  How many users have this song in their list of favourites.  Can be used to sort tracks by num favourite to identify more popular tracks within a set.  ### MUSIC GENRE  The music genere of the song.  Can be used to group songs by genre, as input for similarity alghorithms, artist genre identification, navigate songs by genere, etc.  ### SONG TITLES TRANSLATIONS  The track title, as translated in different lanauages, can be used to display the right writing for a given user, example:  LIES (Bigbang) becomes 在光化門 in chinese HALLELUJAH (Bigbang) becomes ハレルヤ in japanese   ## Artist Inside the artist object you can get the following nice extra information:  ### COMMENTS AND COUNTRY  An artist comment is a short snippet of text which can be mainly used for disambiguation.  The artist country is the born country of the artist/group  There are two perfect search result if you search by artist with the keyword \&quot;U2\&quot;. Indeed there are two distinct music groups with this same name, one is the most known irish group of Bono Vox, the other is a less popular (world wide speaking) group from Japan.  Here&#39;s how you can made use of the artist comment in your search result page:  U2 (Irish rock band) U2 (あきやまうに) You can also show the artist country for even better disambiguation:  U2 (Irish rock band) from Ireland U2 (あきやまうに) from Japan ARTIST TRANSLATIONS  When you create a world wide music related service you have to take into consideration to display the artist name in the user&#39;s local language. These translation are also used as aliases to improve the search results.  Let&#39;s use PSY for this example.  Western people know him as PSY but korean want to see the original name 싸이.  Using the name translations provided by our api you can show to every user the writing they expect to see.  Furthermore, when you search for \&quot;psy gangnam style\&quot; or \&quot;싸이 gangnam style\&quot; with our search/match api you will still be able to find the song.  ### ARTIST RATING  The artist rating is a score 0-100 identifying how popular is an artist in musixmatch.  You can use this information to build charts, for suggestions, to sort search results. In the example above about U2, we use the artist rating to show the irish band before the japanese one in our serp.  ### ARTIST MUSIC GENRE  We provide one or more main artist genre, this information can be used to calculate similar artist, suggestions, or the filter a search by artist genre.    ## Album Inside the album object you can get the following nice extra information:  ### ALBUM RATING  The album rating is a score 0-100 identifying how popular is an album in musixmatch.  You can use this information to sort search results, like the most popular albums of an artist.  ### ALBUM RATING  The album rating is a score 0-100 identifying how popular is an album in musixmatch.  You can use this information to sort search results, like the most popular albums of an artist.  ### ALBUM COPYRIGHT AND LABEL  For most of our albums we can provide extra information like for example:  Label: Universal-Island Records Ltd. Copyright: (P) 2013 Rubyworks, under license to Columbia Records, a Division of Sony Music Entertainment. ALBUM TYPE AND RELEASE DATE  The album official release date can be used to sort an artist&#39;s albums view starting by the most recent one.  Album can also be filtered or grouped by type: Single, Album, Compilation, Remix, Live. This can help to build an artist page with a more organized structure.  ### ALBUM MUSIC GENRE  For most of the albums we provide two groups of music genres. Primary and secondary. This information can be used to help user navigate albums by genre.  An example could be:  Primary genere: POP Secondary genre: K-POP or Mandopop .<br>
* The <code>index</code> module provides access to constructors for all the classes which comprise the public API.
* <p>
* An AMD (recommended!) or CommonJS application will generally do something equivalent to the following:
* <pre>
* var MusixmatchApi = require('index'); // See note below*.
* var xxxSvc = new MusixmatchApi.XxxApi(); // Allocate the API class we're going to use.
* var yyyModel = new MusixmatchApi.Yyy(); // Construct a model instance.
* yyyModel.someProperty = 'someValue';
* ...
* var zzz = xxxSvc.doSomething(yyyModel); // Invoke the service.
* ...
* </pre>
* <em>*NOTE: For a top-level AMD script, use require(['index'], function(){...})
* and put the application logic within the callback function.</em>
* </p>
* <p>
* A non-AMD browser application (discouraged) might do something like this:
* <pre>
* var xxxSvc = new MusixmatchApi.XxxApi(); // Allocate the API class we're going to use.
* var yyy = new MusixmatchApi.Yyy(); // Construct a model instance.
* yyyModel.someProperty = 'someValue';
* ...
* var zzz = xxxSvc.doSomething(yyyModel); // Invoke the service.
* ...
* </pre>
* </p>
* @module index
* @version 1.1.0
*/
export {
    /**
     * The ApiClient constructor.
     * @property {module:ApiClient}
     */
    ApiClient,

    /**
     * The Album model constructor.
     * @property {module:model/Album}
     */
    Album,

    /**
     * The AlbumGetGet200Response model constructor.
     * @property {module:model/AlbumGetGet200Response}
     */
    AlbumGetGet200Response,

    /**
     * The AlbumGetGet200ResponseMessage model constructor.
     * @property {module:model/AlbumGetGet200ResponseMessage}
     */
    AlbumGetGet200ResponseMessage,

    /**
     * The AlbumGetGet200ResponseMessageBody model constructor.
     * @property {module:model/AlbumGetGet200ResponseMessageBody}
     */
    AlbumGetGet200ResponseMessageBody,

    /**
     * The AlbumGetGet200ResponseMessageHeader model constructor.
     * @property {module:model/AlbumGetGet200ResponseMessageHeader}
     */
    AlbumGetGet200ResponseMessageHeader,

    /**
     * The AlbumPrimaryGenres model constructor.
     * @property {module:model/AlbumPrimaryGenres}
     */
    AlbumPrimaryGenres,

    /**
     * The AlbumPrimaryGenresMusicGenreListInner model constructor.
     * @property {module:model/AlbumPrimaryGenresMusicGenreListInner}
     */
    AlbumPrimaryGenresMusicGenreListInner,

    /**
     * The AlbumPrimaryGenresMusicGenreListInnerMusicGenre model constructor.
     * @property {module:model/AlbumPrimaryGenresMusicGenreListInnerMusicGenre}
     */
    AlbumPrimaryGenresMusicGenreListInnerMusicGenre,

    /**
     * The AlbumSecondaryGenres model constructor.
     * @property {module:model/AlbumSecondaryGenres}
     */
    AlbumSecondaryGenres,

    /**
     * The AlbumTracksGetGet200Response model constructor.
     * @property {module:model/AlbumTracksGetGet200Response}
     */
    AlbumTracksGetGet200Response,

    /**
     * The AlbumTracksGetGet200ResponseMessage model constructor.
     * @property {module:model/AlbumTracksGetGet200ResponseMessage}
     */
    AlbumTracksGetGet200ResponseMessage,

    /**
     * The AlbumTracksGetGet200ResponseMessageBody model constructor.
     * @property {module:model/AlbumTracksGetGet200ResponseMessageBody}
     */
    AlbumTracksGetGet200ResponseMessageBody,

    /**
     * The AlbumTracksGetGet200ResponseMessageHeader model constructor.
     * @property {module:model/AlbumTracksGetGet200ResponseMessageHeader}
     */
    AlbumTracksGetGet200ResponseMessageHeader,

    /**
     * The Artist model constructor.
     * @property {module:model/Artist}
     */
    Artist,

    /**
     * The ArtistAlbumsGetGet200Response model constructor.
     * @property {module:model/ArtistAlbumsGetGet200Response}
     */
    ArtistAlbumsGetGet200Response,

    /**
     * The ArtistAlbumsGetGet200ResponseMessage model constructor.
     * @property {module:model/ArtistAlbumsGetGet200ResponseMessage}
     */
    ArtistAlbumsGetGet200ResponseMessage,

    /**
     * The ArtistAlbumsGetGet200ResponseMessageBody model constructor.
     * @property {module:model/ArtistAlbumsGetGet200ResponseMessageBody}
     */
    ArtistAlbumsGetGet200ResponseMessageBody,

    /**
     * The ArtistArtistAliasListInner model constructor.
     * @property {module:model/ArtistArtistAliasListInner}
     */
    ArtistArtistAliasListInner,

    /**
     * The ArtistArtistCredits model constructor.
     * @property {module:model/ArtistArtistCredits}
     */
    ArtistArtistCredits,

    /**
     * The ArtistArtistNameTranslationListInner model constructor.
     * @property {module:model/ArtistArtistNameTranslationListInner}
     */
    ArtistArtistNameTranslationListInner,

    /**
     * The ArtistArtistNameTranslationListInnerArtistNameTranslation model constructor.
     * @property {module:model/ArtistArtistNameTranslationListInnerArtistNameTranslation}
     */
    ArtistArtistNameTranslationListInnerArtistNameTranslation,

    /**
     * The ArtistGetGet200Response model constructor.
     * @property {module:model/ArtistGetGet200Response}
     */
    ArtistGetGet200Response,

    /**
     * The ArtistGetGet200ResponseMessage model constructor.
     * @property {module:model/ArtistGetGet200ResponseMessage}
     */
    ArtistGetGet200ResponseMessage,

    /**
     * The ArtistGetGet200ResponseMessageBody model constructor.
     * @property {module:model/ArtistGetGet200ResponseMessageBody}
     */
    ArtistGetGet200ResponseMessageBody,

    /**
     * The ArtistRelatedGetGet200Response model constructor.
     * @property {module:model/ArtistRelatedGetGet200Response}
     */
    ArtistRelatedGetGet200Response,

    /**
     * The ArtistRelatedGetGet200ResponseMessage model constructor.
     * @property {module:model/ArtistRelatedGetGet200ResponseMessage}
     */
    ArtistRelatedGetGet200ResponseMessage,

    /**
     * The ArtistRelatedGetGet200ResponseMessageBody model constructor.
     * @property {module:model/ArtistRelatedGetGet200ResponseMessageBody}
     */
    ArtistRelatedGetGet200ResponseMessageBody,

    /**
     * The ChartArtistsGetGet200Response model constructor.
     * @property {module:model/ChartArtistsGetGet200Response}
     */
    ChartArtistsGetGet200Response,

    /**
     * The ChartArtistsGetGet200ResponseMessage model constructor.
     * @property {module:model/ChartArtistsGetGet200ResponseMessage}
     */
    ChartArtistsGetGet200ResponseMessage,

    /**
     * The ChartArtistsGetGet200ResponseMessageHeader model constructor.
     * @property {module:model/ChartArtistsGetGet200ResponseMessageHeader}
     */
    ChartArtistsGetGet200ResponseMessageHeader,

    /**
     * The ChartTracksGetGet200Response model constructor.
     * @property {module:model/ChartTracksGetGet200Response}
     */
    ChartTracksGetGet200Response,

    /**
     * The ChartTracksGetGet200ResponseMessage model constructor.
     * @property {module:model/ChartTracksGetGet200ResponseMessage}
     */
    ChartTracksGetGet200ResponseMessage,

    /**
     * The ChartTracksGetGet200ResponseMessageBody model constructor.
     * @property {module:model/ChartTracksGetGet200ResponseMessageBody}
     */
    ChartTracksGetGet200ResponseMessageBody,

    /**
     * The ChartTracksGetGet200ResponseMessageBodyTrackListInner model constructor.
     * @property {module:model/ChartTracksGetGet200ResponseMessageBodyTrackListInner}
     */
    ChartTracksGetGet200ResponseMessageBodyTrackListInner,

    /**
     * The Lyrics model constructor.
     * @property {module:model/Lyrics}
     */
    Lyrics,

    /**
     * The MatcherLyricsGetGet200Response model constructor.
     * @property {module:model/MatcherLyricsGetGet200Response}
     */
    MatcherLyricsGetGet200Response,

    /**
     * The MatcherLyricsGetGet200ResponseMessage model constructor.
     * @property {module:model/MatcherLyricsGetGet200ResponseMessage}
     */
    MatcherLyricsGetGet200ResponseMessage,

    /**
     * The MatcherLyricsGetGet200ResponseMessageBody model constructor.
     * @property {module:model/MatcherLyricsGetGet200ResponseMessageBody}
     */
    MatcherLyricsGetGet200ResponseMessageBody,

    /**
     * The MatcherSubtitleGetGet200Response model constructor.
     * @property {module:model/MatcherSubtitleGetGet200Response}
     */
    MatcherSubtitleGetGet200Response,

    /**
     * The MatcherSubtitleGetGet200ResponseMessage model constructor.
     * @property {module:model/MatcherSubtitleGetGet200ResponseMessage}
     */
    MatcherSubtitleGetGet200ResponseMessage,

    /**
     * The MatcherSubtitleGetGet200ResponseMessageBody model constructor.
     * @property {module:model/MatcherSubtitleGetGet200ResponseMessageBody}
     */
    MatcherSubtitleGetGet200ResponseMessageBody,

    /**
     * The MatcherTrackGetGet200Response model constructor.
     * @property {module:model/MatcherTrackGetGet200Response}
     */
    MatcherTrackGetGet200Response,

    /**
     * The MatcherTrackGetGet200ResponseMessage model constructor.
     * @property {module:model/MatcherTrackGetGet200ResponseMessage}
     */
    MatcherTrackGetGet200ResponseMessage,

    /**
     * The Snippet model constructor.
     * @property {module:model/Snippet}
     */
    Snippet,

    /**
     * The Subtitle model constructor.
     * @property {module:model/Subtitle}
     */
    Subtitle,

    /**
     * The Track model constructor.
     * @property {module:model/Track}
     */
    Track,

    /**
     * The TrackSnippetGetGet200Response model constructor.
     * @property {module:model/TrackSnippetGetGet200Response}
     */
    TrackSnippetGetGet200Response,

    /**
     * The TrackSnippetGetGet200ResponseMessage model constructor.
     * @property {module:model/TrackSnippetGetGet200ResponseMessage}
     */
    TrackSnippetGetGet200ResponseMessage,

    /**
     * The TrackSnippetGetGet200ResponseMessageBody model constructor.
     * @property {module:model/TrackSnippetGetGet200ResponseMessageBody}
     */
    TrackSnippetGetGet200ResponseMessageBody,

    /**
    * The AlbumApi service constructor.
    * @property {module:api/AlbumApi}
    */
    AlbumApi,

    /**
    * The ArtistApi service constructor.
    * @property {module:api/ArtistApi}
    */
    ArtistApi,

    /**
    * The LyricsApi service constructor.
    * @property {module:api/LyricsApi}
    */
    LyricsApi,

    /**
    * The SnippetApi service constructor.
    * @property {module:api/SnippetApi}
    */
    SnippetApi,

    /**
    * The SubtitleApi service constructor.
    * @property {module:api/SubtitleApi}
    */
    SubtitleApi,

    /**
    * The TrackApi service constructor.
    * @property {module:api/TrackApi}
    */
    TrackApi
};
