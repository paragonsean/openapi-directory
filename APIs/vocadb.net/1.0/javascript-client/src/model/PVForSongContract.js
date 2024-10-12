/**
 * VocaDbWeb
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 1.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import PVExtendedMetadata from './PVExtendedMetadata';
import PVService from './PVService';
import PVType from './PVType';
import SongContract from './SongContract';

/**
 * The PVForSongContract model module.
 * @module model/PVForSongContract
 * @version 1.0
 */
class PVForSongContract {
    /**
     * Constructs a new <code>PVForSongContract</code>.
     * @alias module:model/PVForSongContract
     */
    constructor() { 
        
        PVForSongContract.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>PVForSongContract</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/PVForSongContract} obj Optional instance to populate.
     * @return {module:model/PVForSongContract} The populated <code>PVForSongContract</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new PVForSongContract();

            if (data.hasOwnProperty('author')) {
                obj['author'] = ApiClient.convertToType(data['author'], 'String');
            }
            if (data.hasOwnProperty('createdBy')) {
                obj['createdBy'] = ApiClient.convertToType(data['createdBy'], 'Number');
            }
            if (data.hasOwnProperty('disabled')) {
                obj['disabled'] = ApiClient.convertToType(data['disabled'], 'Boolean');
            }
            if (data.hasOwnProperty('extendedMetadata')) {
                obj['extendedMetadata'] = PVExtendedMetadata.constructFromObject(data['extendedMetadata']);
            }
            if (data.hasOwnProperty('id')) {
                obj['id'] = ApiClient.convertToType(data['id'], 'Number');
            }
            if (data.hasOwnProperty('length')) {
                obj['length'] = ApiClient.convertToType(data['length'], 'Number');
            }
            if (data.hasOwnProperty('name')) {
                obj['name'] = ApiClient.convertToType(data['name'], 'String');
            }
            if (data.hasOwnProperty('publishDate')) {
                obj['publishDate'] = ApiClient.convertToType(data['publishDate'], 'Date');
            }
            if (data.hasOwnProperty('pvId')) {
                obj['pvId'] = ApiClient.convertToType(data['pvId'], 'String');
            }
            if (data.hasOwnProperty('pvType')) {
                obj['pvType'] = PVType.constructFromObject(data['pvType']);
            }
            if (data.hasOwnProperty('service')) {
                obj['service'] = PVService.constructFromObject(data['service']);
            }
            if (data.hasOwnProperty('song')) {
                obj['song'] = SongContract.constructFromObject(data['song']);
            }
            if (data.hasOwnProperty('thumbUrl')) {
                obj['thumbUrl'] = ApiClient.convertToType(data['thumbUrl'], 'String');
            }
            if (data.hasOwnProperty('url')) {
                obj['url'] = ApiClient.convertToType(data['url'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>PVForSongContract</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>PVForSongContract</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['author'] && !(typeof data['author'] === 'string' || data['author'] instanceof String)) {
            throw new Error("Expected the field `author` to be a primitive type in the JSON string but got " + data['author']);
        }
        // validate the optional field `extendedMetadata`
        if (data['extendedMetadata']) { // data not null
          PVExtendedMetadata.validateJSON(data['extendedMetadata']);
        }
        // ensure the json data is a string
        if (data['name'] && !(typeof data['name'] === 'string' || data['name'] instanceof String)) {
            throw new Error("Expected the field `name` to be a primitive type in the JSON string but got " + data['name']);
        }
        // ensure the json data is a string
        if (data['pvId'] && !(typeof data['pvId'] === 'string' || data['pvId'] instanceof String)) {
            throw new Error("Expected the field `pvId` to be a primitive type in the JSON string but got " + data['pvId']);
        }
        // validate the optional field `song`
        if (data['song']) { // data not null
          SongContract.validateJSON(data['song']);
        }
        // ensure the json data is a string
        if (data['thumbUrl'] && !(typeof data['thumbUrl'] === 'string' || data['thumbUrl'] instanceof String)) {
            throw new Error("Expected the field `thumbUrl` to be a primitive type in the JSON string but got " + data['thumbUrl']);
        }
        // ensure the json data is a string
        if (data['url'] && !(typeof data['url'] === 'string' || data['url'] instanceof String)) {
            throw new Error("Expected the field `url` to be a primitive type in the JSON string but got " + data['url']);
        }

        return true;
    }


}



/**
 * @member {String} author
 */
PVForSongContract.prototype['author'] = undefined;

/**
 * @member {Number} createdBy
 */
PVForSongContract.prototype['createdBy'] = undefined;

/**
 * @member {Boolean} disabled
 */
PVForSongContract.prototype['disabled'] = undefined;

/**
 * @member {module:model/PVExtendedMetadata} extendedMetadata
 */
PVForSongContract.prototype['extendedMetadata'] = undefined;

/**
 * @member {Number} id
 */
PVForSongContract.prototype['id'] = undefined;

/**
 * @member {Number} length
 */
PVForSongContract.prototype['length'] = undefined;

/**
 * @member {String} name
 */
PVForSongContract.prototype['name'] = undefined;

/**
 * @member {Date} publishDate
 */
PVForSongContract.prototype['publishDate'] = undefined;

/**
 * @member {String} pvId
 */
PVForSongContract.prototype['pvId'] = undefined;

/**
 * @member {module:model/PVType} pvType
 */
PVForSongContract.prototype['pvType'] = undefined;

/**
 * @member {module:model/PVService} service
 */
PVForSongContract.prototype['service'] = undefined;

/**
 * @member {module:model/SongContract} song
 */
PVForSongContract.prototype['song'] = undefined;

/**
 * @member {String} thumbUrl
 */
PVForSongContract.prototype['thumbUrl'] = undefined;

/**
 * @member {String} url
 */
PVForSongContract.prototype['url'] = undefined;






export default PVForSongContract;

