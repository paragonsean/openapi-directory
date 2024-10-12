/**
 * PeerTube
 * The PeerTube API is built on HTTP(S) and is RESTful. You can use your favorite HTTP/REST library for your programming language to use PeerTube. The spec API is fully compatible with [openapi-generator](https://github.com/OpenAPITools/openapi-generator/wiki/API-client-generator-HOWTO) which generates a client SDK in the language of your choice - we generate some client SDKs automatically:  - [Python](https://framagit.org/framasoft/peertube/clients/python) - [Go](https://framagit.org/framasoft/peertube/clients/go) - [Kotlin](https://framagit.org/framasoft/peertube/clients/kotlin)  See the [REST API quick start](https://docs.joinpeertube.org/api/rest-getting-started) for a few examples of using the PeerTube API.  # Authentication  When you sign up for an account on a PeerTube instance, you are given the possibility to generate sessions on it, and authenticate there using an access token. Only __one access token can currently be used at a time__.  ## Roles  Accounts are given permissions based on their role. There are three roles on PeerTube: Administrator, Moderator, and User. See the [roles guide](https://docs.joinpeertube.org/admin/managing-users#roles) for a detail of their permissions.  # Errors  The API uses standard HTTP status codes to indicate the success or failure of the API call, completed by a [RFC7807-compliant](https://tools.ietf.org/html/rfc7807) response body.  ``` HTTP 1.1 404 Not Found Content-Type: application/problem+json; charset=utf-8  {   \"detail\": \"Video not found\",   \"docs\": \"https://docs.joinpeertube.org/api/rest-reference.html#operation/getVideo\",   \"status\": 404,   \"title\": \"Not Found\",   \"type\": \"about:blank\" } ```  We provide error `type` values for [a growing number of cases](https://github.com/Chocobozzz/PeerTube/blob/develop/shared/models/server/server-error-code.enum.ts), but it is still optional. Types are used to disambiguate errors that bear the same status code and are non-obvious:  ``` HTTP 1.1 403 Forbidden Content-Type: application/problem+json; charset=utf-8  {   \"detail\": \"Cannot get this video regarding follow constraints\",   \"docs\": \"https://docs.joinpeertube.org/api/rest-reference.html#operation/getVideo\",   \"status\": 403,   \"title\": \"Forbidden\",   \"type\": \"https://docs.joinpeertube.org/api/rest-reference.html#section/Errors/does_not_respect_follow_constraints\" } ```  Here a 403 error could otherwise mean that the video is private or blocklisted.  ### Validation errors  Each parameter is evaluated on its own against a set of rules before the route validator proceeds with potential testing involving parameter combinations. Errors coming from validation errors appear earlier and benefit from a more detailed error description:  ``` HTTP 1.1 400 Bad Request Content-Type: application/problem+json; charset=utf-8  {   \"detail\": \"Incorrect request parameters: id\",   \"docs\": \"https://docs.joinpeertube.org/api/rest-reference.html#operation/getVideo\",   \"instance\": \"/api/v1/videos/9c9de5e8-0a1e-484a-b099-e80766180\",   \"invalid-params\": {     \"id\": {       \"location\": \"params\",       \"msg\": \"Invalid value\",       \"param\": \"id\",       \"value\": \"9c9de5e8-0a1e-484a-b099-e80766180\"     }   },   \"status\": 400,   \"title\": \"Bad Request\",   \"type\": \"about:blank\" } ```  Where `id` is the name of the field concerned by the error, within the route definition. `invalid-params.<field>.location` can be either 'params', 'body', 'header', 'query' or 'cookies', and `invalid-params.<field>.value` reports the value that didn't pass validation whose `invalid-params.<field>.msg` is about.  ### Deprecated error fields  Some fields could be included with previous versions. They are still included but their use is deprecated: - `error`: superseded by `detail` - `code`: superseded by `type` (which is now an URI)  # Rate limits  We are rate-limiting all endpoints of PeerTube's API. Custom values can be set by administrators:  | Endpoint (prefix: `/api/v1`) | Calls         | Time frame   | |------------------------------|---------------|--------------| | `/_*`                         | 50            | 10 seconds   | | `POST /users/token`          | 15            | 5 minutes    | | `POST /users/register`       | 2<sup>*</sup> | 5 minutes    | | `POST /users/ask-send-verify-email` | 3      | 5 minutes    |  Depending on the endpoint, <sup>*</sup>failed requests are not taken into account. A service limit is announced by a `429 Too Many Requests` status code.  You can get details about the current state of your rate limit by reading the following headers:  | Header                  | Description                                                | |-------------------------|------------------------------------------------------------| | `X-RateLimit-Limit`     | Number of max requests allowed in the current time period  | | `X-RateLimit-Remaining` | Number of remaining requests in the current time period    | | `X-RateLimit-Reset`     | Timestamp of end of current time period as UNIX timestamp  | | `Retry-After`           | Seconds to delay after the first `429` is received         |  # CORS  This API features [Cross-Origin Resource Sharing (CORS)](https://fetch.spec.whatwg.org/), allowing cross-domain communication from the browser for some routes:  | Endpoint                    | |------------------------- ---| | `/api/_*`                    | | `/download/_*`               | | `/lazy-static/_*`            | | `/.well-known/webfinger`    |  In addition, all routes serving ActivityPub are CORS-enabled for all origins. 
 *
 * The version of the OpenAPI document: 5.1.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import VideosForXMLInnerEnclosure from './VideosForXMLInnerEnclosure';
import VideosForXMLInnerMediaCommunity from './VideosForXMLInnerMediaCommunity';
import VideosForXMLInnerMediaEmbed from './VideosForXMLInnerMediaEmbed';
import VideosForXMLInnerMediaGroupInner from './VideosForXMLInnerMediaGroupInner';
import VideosForXMLInnerMediaPlayer from './VideosForXMLInnerMediaPlayer';
import VideosForXMLInnerMediaThumbnail from './VideosForXMLInnerMediaThumbnail';

/**
 * The VideosForXMLInner model module.
 * @module model/VideosForXMLInner
 * @version 5.1.0
 */
class VideosForXMLInner {
    /**
     * Constructs a new <code>VideosForXMLInner</code>.
     * @alias module:model/VideosForXMLInner
     */
    constructor() { 
        
        VideosForXMLInner.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>VideosForXMLInner</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/VideosForXMLInner} obj Optional instance to populate.
     * @return {module:model/VideosForXMLInner} The populated <code>VideosForXMLInner</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new VideosForXMLInner();

            if (data.hasOwnProperty('content:encoded')) {
                obj['content:encoded'] = ApiClient.convertToType(data['content:encoded'], 'String');
            }
            if (data.hasOwnProperty('dc:creator')) {
                obj['dc:creator'] = ApiClient.convertToType(data['dc:creator'], 'String');
            }
            if (data.hasOwnProperty('description')) {
                obj['description'] = ApiClient.convertToType(data['description'], 'String');
            }
            if (data.hasOwnProperty('enclosure')) {
                obj['enclosure'] = VideosForXMLInnerEnclosure.constructFromObject(data['enclosure']);
            }
            if (data.hasOwnProperty('guid')) {
                obj['guid'] = ApiClient.convertToType(data['guid'], 'String');
            }
            if (data.hasOwnProperty('link')) {
                obj['link'] = ApiClient.convertToType(data['link'], 'String');
            }
            if (data.hasOwnProperty('media:category')) {
                obj['media:category'] = ApiClient.convertToType(data['media:category'], 'Number');
            }
            if (data.hasOwnProperty('media:community')) {
                obj['media:community'] = VideosForXMLInnerMediaCommunity.constructFromObject(data['media:community']);
            }
            if (data.hasOwnProperty('media:description')) {
                obj['media:description'] = ApiClient.convertToType(data['media:description'], 'String');
            }
            if (data.hasOwnProperty('media:embed')) {
                obj['media:embed'] = VideosForXMLInnerMediaEmbed.constructFromObject(data['media:embed']);
            }
            if (data.hasOwnProperty('media:group')) {
                obj['media:group'] = ApiClient.convertToType(data['media:group'], [VideosForXMLInnerMediaGroupInner]);
            }
            if (data.hasOwnProperty('media:player')) {
                obj['media:player'] = VideosForXMLInnerMediaPlayer.constructFromObject(data['media:player']);
            }
            if (data.hasOwnProperty('media:rating')) {
                obj['media:rating'] = ApiClient.convertToType(data['media:rating'], 'String');
            }
            if (data.hasOwnProperty('media:thumbnail')) {
                obj['media:thumbnail'] = VideosForXMLInnerMediaThumbnail.constructFromObject(data['media:thumbnail']);
            }
            if (data.hasOwnProperty('media:title')) {
                obj['media:title'] = ApiClient.convertToType(data['media:title'], 'String');
            }
            if (data.hasOwnProperty('pubDate')) {
                obj['pubDate'] = ApiClient.convertToType(data['pubDate'], 'Date');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>VideosForXMLInner</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>VideosForXMLInner</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['content:encoded'] && !(typeof data['content:encoded'] === 'string' || data['content:encoded'] instanceof String)) {
            throw new Error("Expected the field `content:encoded` to be a primitive type in the JSON string but got " + data['content:encoded']);
        }
        // ensure the json data is a string
        if (data['dc:creator'] && !(typeof data['dc:creator'] === 'string' || data['dc:creator'] instanceof String)) {
            throw new Error("Expected the field `dc:creator` to be a primitive type in the JSON string but got " + data['dc:creator']);
        }
        // ensure the json data is a string
        if (data['description'] && !(typeof data['description'] === 'string' || data['description'] instanceof String)) {
            throw new Error("Expected the field `description` to be a primitive type in the JSON string but got " + data['description']);
        }
        // validate the optional field `enclosure`
        if (data['enclosure']) { // data not null
          VideosForXMLInnerEnclosure.validateJSON(data['enclosure']);
        }
        // ensure the json data is a string
        if (data['guid'] && !(typeof data['guid'] === 'string' || data['guid'] instanceof String)) {
            throw new Error("Expected the field `guid` to be a primitive type in the JSON string but got " + data['guid']);
        }
        // ensure the json data is a string
        if (data['link'] && !(typeof data['link'] === 'string' || data['link'] instanceof String)) {
            throw new Error("Expected the field `link` to be a primitive type in the JSON string but got " + data['link']);
        }
        // validate the optional field `media:community`
        if (data['media:community']) { // data not null
          VideosForXMLInnerMediaCommunity.validateJSON(data['media:community']);
        }
        // ensure the json data is a string
        if (data['media:description'] && !(typeof data['media:description'] === 'string' || data['media:description'] instanceof String)) {
            throw new Error("Expected the field `media:description` to be a primitive type in the JSON string but got " + data['media:description']);
        }
        // validate the optional field `media:embed`
        if (data['media:embed']) { // data not null
          VideosForXMLInnerMediaEmbed.validateJSON(data['media:embed']);
        }
        if (data['media:group']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['media:group'])) {
                throw new Error("Expected the field `media:group` to be an array in the JSON data but got " + data['media:group']);
            }
            // validate the optional field `media:group` (array)
            for (const item of data['media:group']) {
                VideosForXMLInnerMediaGroupInner.validateJSON(item);
            };
        }
        // validate the optional field `media:player`
        if (data['media:player']) { // data not null
          VideosForXMLInnerMediaPlayer.validateJSON(data['media:player']);
        }
        // ensure the json data is a string
        if (data['media:rating'] && !(typeof data['media:rating'] === 'string' || data['media:rating'] instanceof String)) {
            throw new Error("Expected the field `media:rating` to be a primitive type in the JSON string but got " + data['media:rating']);
        }
        // validate the optional field `media:thumbnail`
        if (data['media:thumbnail']) { // data not null
          VideosForXMLInnerMediaThumbnail.validateJSON(data['media:thumbnail']);
        }
        // ensure the json data is a string
        if (data['media:title'] && !(typeof data['media:title'] === 'string' || data['media:title'] instanceof String)) {
            throw new Error("Expected the field `media:title` to be a primitive type in the JSON string but got " + data['media:title']);
        }

        return true;
    }


}



/**
 * video description
 * @member {String} content:encoded
 */
VideosForXMLInner.prototype['content:encoded'] = undefined;

/**
 * publisher user name
 * @member {String} dc:creator
 */
VideosForXMLInner.prototype['dc:creator'] = undefined;

/**
 * video description
 * @member {String} description
 */
VideosForXMLInner.prototype['description'] = undefined;

/**
 * @member {module:model/VideosForXMLInnerEnclosure} enclosure
 */
VideosForXMLInner.prototype['enclosure'] = undefined;

/**
 * video canonical URL
 * @member {String} guid
 */
VideosForXMLInner.prototype['guid'] = undefined;

/**
 * video watch page URL
 * @member {String} link
 */
VideosForXMLInner.prototype['link'] = undefined;

/**
 * video category (MRSS)
 * @member {Number} media:category
 */
VideosForXMLInner.prototype['media:category'] = undefined;

/**
 * @member {module:model/VideosForXMLInnerMediaCommunity} media:community
 */
VideosForXMLInner.prototype['media:community'] = undefined;

/**
 * @member {String} media:description
 */
VideosForXMLInner.prototype['media:description'] = undefined;

/**
 * @member {module:model/VideosForXMLInnerMediaEmbed} media:embed
 */
VideosForXMLInner.prototype['media:embed'] = undefined;

/**
 * list of streamable files for the video. see [media:peerLink](https://www.rssboard.org/media-rss#media-peerlink) and [media:content](https://www.rssboard.org/media-rss#media-content) or  (MRSS)
 * @member {Array.<module:model/VideosForXMLInnerMediaGroupInner>} media:group
 */
VideosForXMLInner.prototype['media:group'] = undefined;

/**
 * @member {module:model/VideosForXMLInnerMediaPlayer} media:player
 */
VideosForXMLInner.prototype['media:player'] = undefined;

/**
 * see [media:rating](https://www.rssboard.org/media-rss#media-rating) (MRSS)
 * @member {module:model/VideosForXMLInner.MediaratingEnum} media:rating
 */
VideosForXMLInner.prototype['media:rating'] = undefined;

/**
 * @member {module:model/VideosForXMLInnerMediaThumbnail} media:thumbnail
 */
VideosForXMLInner.prototype['media:thumbnail'] = undefined;

/**
 * see [media:title](https://www.rssboard.org/media-rss#media-title) (MRSS). We only use `plain` titles.
 * @member {String} media:title
 */
VideosForXMLInner.prototype['media:title'] = undefined;

/**
 * video publication date
 * @member {Date} pubDate
 */
VideosForXMLInner.prototype['pubDate'] = undefined;





/**
 * Allowed values for the <code>media:rating</code> property.
 * @enum {String}
 * @readonly
 */
VideosForXMLInner['MediaratingEnum'] = {

    /**
     * value: "nonadult"
     * @const
     */
    "nonadult": "nonadult",

    /**
     * value: "adult"
     * @const
     */
    "adult": "adult"
};



export default VideosForXMLInner;

