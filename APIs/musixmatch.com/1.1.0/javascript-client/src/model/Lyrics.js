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

/**
 * The Lyrics model module.
 * @module model/Lyrics
 * @version 1.1.0
 */
class Lyrics {
    /**
     * Constructs a new <code>Lyrics</code>.
     * a Lyrics in the Musixmatch database.
     * @alias module:model/Lyrics
     */
    constructor() { 
        
        Lyrics.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>Lyrics</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/Lyrics} obj Optional instance to populate.
     * @return {module:model/Lyrics} The populated <code>Lyrics</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new Lyrics();

            if (data.hasOwnProperty('action_requested')) {
                obj['action_requested'] = ApiClient.convertToType(data['action_requested'], 'String');
            }
            if (data.hasOwnProperty('can_edit')) {
                obj['can_edit'] = ApiClient.convertToType(data['can_edit'], 'Number');
            }
            if (data.hasOwnProperty('explicit')) {
                obj['explicit'] = ApiClient.convertToType(data['explicit'], 'Number');
            }
            if (data.hasOwnProperty('html_tracking_url')) {
                obj['html_tracking_url'] = ApiClient.convertToType(data['html_tracking_url'], 'String');
            }
            if (data.hasOwnProperty('instrumental')) {
                obj['instrumental'] = ApiClient.convertToType(data['instrumental'], 'Number');
            }
            if (data.hasOwnProperty('locked')) {
                obj['locked'] = ApiClient.convertToType(data['locked'], 'Number');
            }
            if (data.hasOwnProperty('lyrics_body')) {
                obj['lyrics_body'] = ApiClient.convertToType(data['lyrics_body'], 'String');
            }
            if (data.hasOwnProperty('lyrics_copyright')) {
                obj['lyrics_copyright'] = ApiClient.convertToType(data['lyrics_copyright'], 'String');
            }
            if (data.hasOwnProperty('lyrics_id')) {
                obj['lyrics_id'] = ApiClient.convertToType(data['lyrics_id'], 'Number');
            }
            if (data.hasOwnProperty('lyrics_language')) {
                obj['lyrics_language'] = ApiClient.convertToType(data['lyrics_language'], 'String');
            }
            if (data.hasOwnProperty('lyrics_language_description')) {
                obj['lyrics_language_description'] = ApiClient.convertToType(data['lyrics_language_description'], 'String');
            }
            if (data.hasOwnProperty('pixel_tracking_url')) {
                obj['pixel_tracking_url'] = ApiClient.convertToType(data['pixel_tracking_url'], 'String');
            }
            if (data.hasOwnProperty('publisher_list')) {
                obj['publisher_list'] = ApiClient.convertToType(data['publisher_list'], ['String']);
            }
            if (data.hasOwnProperty('restricted')) {
                obj['restricted'] = ApiClient.convertToType(data['restricted'], 'Number');
            }
            if (data.hasOwnProperty('script_tracking_url')) {
                obj['script_tracking_url'] = ApiClient.convertToType(data['script_tracking_url'], 'String');
            }
            if (data.hasOwnProperty('updated_time')) {
                obj['updated_time'] = ApiClient.convertToType(data['updated_time'], 'String');
            }
            if (data.hasOwnProperty('verified')) {
                obj['verified'] = ApiClient.convertToType(data['verified'], 'Number');
            }
            if (data.hasOwnProperty('writer_list')) {
                obj['writer_list'] = ApiClient.convertToType(data['writer_list'], ['String']);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>Lyrics</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>Lyrics</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['action_requested'] && !(typeof data['action_requested'] === 'string' || data['action_requested'] instanceof String)) {
            throw new Error("Expected the field `action_requested` to be a primitive type in the JSON string but got " + data['action_requested']);
        }
        // ensure the json data is a string
        if (data['html_tracking_url'] && !(typeof data['html_tracking_url'] === 'string' || data['html_tracking_url'] instanceof String)) {
            throw new Error("Expected the field `html_tracking_url` to be a primitive type in the JSON string but got " + data['html_tracking_url']);
        }
        // ensure the json data is a string
        if (data['lyrics_body'] && !(typeof data['lyrics_body'] === 'string' || data['lyrics_body'] instanceof String)) {
            throw new Error("Expected the field `lyrics_body` to be a primitive type in the JSON string but got " + data['lyrics_body']);
        }
        // ensure the json data is a string
        if (data['lyrics_copyright'] && !(typeof data['lyrics_copyright'] === 'string' || data['lyrics_copyright'] instanceof String)) {
            throw new Error("Expected the field `lyrics_copyright` to be a primitive type in the JSON string but got " + data['lyrics_copyright']);
        }
        // ensure the json data is a string
        if (data['lyrics_language'] && !(typeof data['lyrics_language'] === 'string' || data['lyrics_language'] instanceof String)) {
            throw new Error("Expected the field `lyrics_language` to be a primitive type in the JSON string but got " + data['lyrics_language']);
        }
        // ensure the json data is a string
        if (data['lyrics_language_description'] && !(typeof data['lyrics_language_description'] === 'string' || data['lyrics_language_description'] instanceof String)) {
            throw new Error("Expected the field `lyrics_language_description` to be a primitive type in the JSON string but got " + data['lyrics_language_description']);
        }
        // ensure the json data is a string
        if (data['pixel_tracking_url'] && !(typeof data['pixel_tracking_url'] === 'string' || data['pixel_tracking_url'] instanceof String)) {
            throw new Error("Expected the field `pixel_tracking_url` to be a primitive type in the JSON string but got " + data['pixel_tracking_url']);
        }
        // ensure the json data is an array
        if (!Array.isArray(data['publisher_list'])) {
            throw new Error("Expected the field `publisher_list` to be an array in the JSON data but got " + data['publisher_list']);
        }
        // ensure the json data is a string
        if (data['script_tracking_url'] && !(typeof data['script_tracking_url'] === 'string' || data['script_tracking_url'] instanceof String)) {
            throw new Error("Expected the field `script_tracking_url` to be a primitive type in the JSON string but got " + data['script_tracking_url']);
        }
        // ensure the json data is a string
        if (data['updated_time'] && !(typeof data['updated_time'] === 'string' || data['updated_time'] instanceof String)) {
            throw new Error("Expected the field `updated_time` to be a primitive type in the JSON string but got " + data['updated_time']);
        }
        // ensure the json data is an array
        if (!Array.isArray(data['writer_list'])) {
            throw new Error("Expected the field `writer_list` to be an array in the JSON data but got " + data['writer_list']);
        }

        return true;
    }


}



/**
 * 
 * @member {String} action_requested
 */
Lyrics.prototype['action_requested'] = undefined;

/**
 * 
 * @member {Number} can_edit
 */
Lyrics.prototype['can_edit'] = undefined;

/**
 * 
 * @member {Number} explicit
 */
Lyrics.prototype['explicit'] = undefined;

/**
 * 
 * @member {String} html_tracking_url
 */
Lyrics.prototype['html_tracking_url'] = undefined;

/**
 * 
 * @member {Number} instrumental
 */
Lyrics.prototype['instrumental'] = undefined;

/**
 * 
 * @member {Number} locked
 */
Lyrics.prototype['locked'] = undefined;

/**
 * 
 * @member {String} lyrics_body
 */
Lyrics.prototype['lyrics_body'] = undefined;

/**
 * 
 * @member {String} lyrics_copyright
 */
Lyrics.prototype['lyrics_copyright'] = undefined;

/**
 * 
 * @member {Number} lyrics_id
 */
Lyrics.prototype['lyrics_id'] = undefined;

/**
 * 
 * @member {String} lyrics_language
 */
Lyrics.prototype['lyrics_language'] = undefined;

/**
 * 
 * @member {String} lyrics_language_description
 */
Lyrics.prototype['lyrics_language_description'] = undefined;

/**
 * 
 * @member {String} pixel_tracking_url
 */
Lyrics.prototype['pixel_tracking_url'] = undefined;

/**
 * @member {Array.<String>} publisher_list
 */
Lyrics.prototype['publisher_list'] = undefined;

/**
 * 
 * @member {Number} restricted
 */
Lyrics.prototype['restricted'] = undefined;

/**
 * 
 * @member {String} script_tracking_url
 */
Lyrics.prototype['script_tracking_url'] = undefined;

/**
 * 
 * @member {String} updated_time
 */
Lyrics.prototype['updated_time'] = undefined;

/**
 * 
 * @member {Number} verified
 */
Lyrics.prototype['verified'] = undefined;

/**
 * @member {Array.<String>} writer_list
 */
Lyrics.prototype['writer_list'] = undefined;






export default Lyrics;

