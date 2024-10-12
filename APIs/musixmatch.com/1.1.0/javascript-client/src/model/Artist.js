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

import ApiClient from '../ApiClient';
import AlbumPrimaryGenres from './AlbumPrimaryGenres';
import AlbumSecondaryGenres from './AlbumSecondaryGenres';
import ArtistArtistAliasListInner from './ArtistArtistAliasListInner';
import ArtistArtistCredits from './ArtistArtistCredits';
import ArtistArtistNameTranslationListInner from './ArtistArtistNameTranslationListInner';

/**
 * The Artist model module.
 * @module model/Artist
 * @version 1.1.0
 */
class Artist {
    /**
     * Constructs a new <code>Artist</code>.
     * a artist in the Musixmatch database.
     * @alias module:model/Artist
     */
    constructor() { 
        
        Artist.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>Artist</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/Artist} obj Optional instance to populate.
     * @return {module:model/Artist} The populated <code>Artist</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new Artist();

            if (data.hasOwnProperty('artist_alias_list')) {
                obj['artist_alias_list'] = ApiClient.convertToType(data['artist_alias_list'], [ArtistArtistAliasListInner]);
            }
            if (data.hasOwnProperty('artist_comment')) {
                obj['artist_comment'] = ApiClient.convertToType(data['artist_comment'], 'String');
            }
            if (data.hasOwnProperty('artist_country')) {
                obj['artist_country'] = ApiClient.convertToType(data['artist_country'], 'String');
            }
            if (data.hasOwnProperty('artist_credits')) {
                obj['artist_credits'] = ArtistArtistCredits.constructFromObject(data['artist_credits']);
            }
            if (data.hasOwnProperty('artist_edit_url')) {
                obj['artist_edit_url'] = ApiClient.convertToType(data['artist_edit_url'], 'String');
            }
            if (data.hasOwnProperty('artist_id')) {
                obj['artist_id'] = ApiClient.convertToType(data['artist_id'], 'Number');
            }
            if (data.hasOwnProperty('artist_mbid')) {
                obj['artist_mbid'] = ApiClient.convertToType(data['artist_mbid'], 'String');
            }
            if (data.hasOwnProperty('artist_name')) {
                obj['artist_name'] = ApiClient.convertToType(data['artist_name'], 'String');
            }
            if (data.hasOwnProperty('artist_name_translation_list')) {
                obj['artist_name_translation_list'] = ApiClient.convertToType(data['artist_name_translation_list'], [ArtistArtistNameTranslationListInner]);
            }
            if (data.hasOwnProperty('artist_rating')) {
                obj['artist_rating'] = ApiClient.convertToType(data['artist_rating'], 'Number');
            }
            if (data.hasOwnProperty('artist_share_url')) {
                obj['artist_share_url'] = ApiClient.convertToType(data['artist_share_url'], 'String');
            }
            if (data.hasOwnProperty('artist_twitter_url')) {
                obj['artist_twitter_url'] = ApiClient.convertToType(data['artist_twitter_url'], 'String');
            }
            if (data.hasOwnProperty('artist_vanity_id')) {
                obj['artist_vanity_id'] = ApiClient.convertToType(data['artist_vanity_id'], 'String');
            }
            if (data.hasOwnProperty('managed')) {
                obj['managed'] = ApiClient.convertToType(data['managed'], 'Number');
            }
            if (data.hasOwnProperty('primary_genres')) {
                obj['primary_genres'] = AlbumPrimaryGenres.constructFromObject(data['primary_genres']);
            }
            if (data.hasOwnProperty('restricted')) {
                obj['restricted'] = ApiClient.convertToType(data['restricted'], 'Number');
            }
            if (data.hasOwnProperty('secondary_genres')) {
                obj['secondary_genres'] = AlbumSecondaryGenres.constructFromObject(data['secondary_genres']);
            }
            if (data.hasOwnProperty('updated_time')) {
                obj['updated_time'] = ApiClient.convertToType(data['updated_time'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>Artist</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>Artist</code>.
     */
    static validateJSON(data) {
        if (data['artist_alias_list']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['artist_alias_list'])) {
                throw new Error("Expected the field `artist_alias_list` to be an array in the JSON data but got " + data['artist_alias_list']);
            }
            // validate the optional field `artist_alias_list` (array)
            for (const item of data['artist_alias_list']) {
                ArtistArtistAliasListInner.validateJSON(item);
            };
        }
        // ensure the json data is a string
        if (data['artist_comment'] && !(typeof data['artist_comment'] === 'string' || data['artist_comment'] instanceof String)) {
            throw new Error("Expected the field `artist_comment` to be a primitive type in the JSON string but got " + data['artist_comment']);
        }
        // ensure the json data is a string
        if (data['artist_country'] && !(typeof data['artist_country'] === 'string' || data['artist_country'] instanceof String)) {
            throw new Error("Expected the field `artist_country` to be a primitive type in the JSON string but got " + data['artist_country']);
        }
        // validate the optional field `artist_credits`
        if (data['artist_credits']) { // data not null
          ArtistArtistCredits.validateJSON(data['artist_credits']);
        }
        // ensure the json data is a string
        if (data['artist_edit_url'] && !(typeof data['artist_edit_url'] === 'string' || data['artist_edit_url'] instanceof String)) {
            throw new Error("Expected the field `artist_edit_url` to be a primitive type in the JSON string but got " + data['artist_edit_url']);
        }
        // ensure the json data is a string
        if (data['artist_mbid'] && !(typeof data['artist_mbid'] === 'string' || data['artist_mbid'] instanceof String)) {
            throw new Error("Expected the field `artist_mbid` to be a primitive type in the JSON string but got " + data['artist_mbid']);
        }
        // ensure the json data is a string
        if (data['artist_name'] && !(typeof data['artist_name'] === 'string' || data['artist_name'] instanceof String)) {
            throw new Error("Expected the field `artist_name` to be a primitive type in the JSON string but got " + data['artist_name']);
        }
        if (data['artist_name_translation_list']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['artist_name_translation_list'])) {
                throw new Error("Expected the field `artist_name_translation_list` to be an array in the JSON data but got " + data['artist_name_translation_list']);
            }
            // validate the optional field `artist_name_translation_list` (array)
            for (const item of data['artist_name_translation_list']) {
                ArtistArtistNameTranslationListInner.validateJSON(item);
            };
        }
        // ensure the json data is a string
        if (data['artist_share_url'] && !(typeof data['artist_share_url'] === 'string' || data['artist_share_url'] instanceof String)) {
            throw new Error("Expected the field `artist_share_url` to be a primitive type in the JSON string but got " + data['artist_share_url']);
        }
        // ensure the json data is a string
        if (data['artist_twitter_url'] && !(typeof data['artist_twitter_url'] === 'string' || data['artist_twitter_url'] instanceof String)) {
            throw new Error("Expected the field `artist_twitter_url` to be a primitive type in the JSON string but got " + data['artist_twitter_url']);
        }
        // ensure the json data is a string
        if (data['artist_vanity_id'] && !(typeof data['artist_vanity_id'] === 'string' || data['artist_vanity_id'] instanceof String)) {
            throw new Error("Expected the field `artist_vanity_id` to be a primitive type in the JSON string but got " + data['artist_vanity_id']);
        }
        // validate the optional field `primary_genres`
        if (data['primary_genres']) { // data not null
          AlbumPrimaryGenres.validateJSON(data['primary_genres']);
        }
        // validate the optional field `secondary_genres`
        if (data['secondary_genres']) { // data not null
          AlbumSecondaryGenres.validateJSON(data['secondary_genres']);
        }
        // ensure the json data is a string
        if (data['updated_time'] && !(typeof data['updated_time'] === 'string' || data['updated_time'] instanceof String)) {
            throw new Error("Expected the field `updated_time` to be a primitive type in the JSON string but got " + data['updated_time']);
        }

        return true;
    }


}



/**
 * @member {Array.<module:model/ArtistArtistAliasListInner>} artist_alias_list
 */
Artist.prototype['artist_alias_list'] = undefined;

/**
 * 
 * @member {String} artist_comment
 */
Artist.prototype['artist_comment'] = undefined;

/**
 * 
 * @member {String} artist_country
 */
Artist.prototype['artist_country'] = undefined;

/**
 * @member {module:model/ArtistArtistCredits} artist_credits
 */
Artist.prototype['artist_credits'] = undefined;

/**
 * 
 * @member {String} artist_edit_url
 */
Artist.prototype['artist_edit_url'] = undefined;

/**
 * 
 * @member {Number} artist_id
 */
Artist.prototype['artist_id'] = undefined;

/**
 * 
 * @member {String} artist_mbid
 */
Artist.prototype['artist_mbid'] = undefined;

/**
 * 
 * @member {String} artist_name
 */
Artist.prototype['artist_name'] = undefined;

/**
 * @member {Array.<module:model/ArtistArtistNameTranslationListInner>} artist_name_translation_list
 */
Artist.prototype['artist_name_translation_list'] = undefined;

/**
 * 
 * @member {Number} artist_rating
 */
Artist.prototype['artist_rating'] = undefined;

/**
 * 
 * @member {String} artist_share_url
 */
Artist.prototype['artist_share_url'] = undefined;

/**
 * 
 * @member {String} artist_twitter_url
 */
Artist.prototype['artist_twitter_url'] = undefined;

/**
 * 
 * @member {String} artist_vanity_id
 */
Artist.prototype['artist_vanity_id'] = undefined;

/**
 * 
 * @member {Number} managed
 */
Artist.prototype['managed'] = undefined;

/**
 * @member {module:model/AlbumPrimaryGenres} primary_genres
 */
Artist.prototype['primary_genres'] = undefined;

/**
 * 
 * @member {Number} restricted
 */
Artist.prototype['restricted'] = undefined;

/**
 * @member {module:model/AlbumSecondaryGenres} secondary_genres
 */
Artist.prototype['secondary_genres'] = undefined;

/**
 * 
 * @member {String} updated_time
 */
Artist.prototype['updated_time'] = undefined;






export default Artist;

