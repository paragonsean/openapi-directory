/**
 * BBC Nitro API
 * BBC Nitro is the BBC's application programming interface (API) for BBC Programmes Metadata.
 *
 * The version of the OpenAPI document: 1.0.0
 * Contact: nitro@bbc.co.uk
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import Identifiers from './Identifiers';
import ImageLink from './ImageLink';
import ImagesMixin from './ImagesMixin';
import MasterBrandCompetitionWarning from './MasterBrandCompetitionWarning';
import MasterBrandMasterBrandDateRange from './MasterBrandMasterBrandDateRange';
import MasterBrandSynopses from './MasterBrandSynopses';

/**
 * The MasterBrand model module.
 * @module model/MasterBrand
 * @version 1.0.0
 */
class MasterBrand {
    /**
     * Constructs a new <code>MasterBrand</code>.
     * @alias module:model/MasterBrand
     * @param mid {String} 
     * @param partner {String} 
     */
    constructor(mid, partner) { 
        
        MasterBrand.initialize(this, mid, partner);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, mid, partner) { 
        obj['mid'] = mid;
        obj['partner'] = partner;
    }

    /**
     * Constructs a <code>MasterBrand</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/MasterBrand} obj Optional instance to populate.
     * @return {module:model/MasterBrand} The populated <code>MasterBrand</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new MasterBrand();

            if (data.hasOwnProperty('colour')) {
                obj['colour'] = ApiClient.convertToType(data['colour'], 'String');
            }
            if (data.hasOwnProperty('competition_warning')) {
                obj['competition_warning'] = MasterBrandCompetitionWarning.constructFromObject(data['competition_warning']);
            }
            if (data.hasOwnProperty('ident')) {
                obj['ident'] = ApiClient.convertToType(data['ident'], 'String');
            }
            if (data.hasOwnProperty('identifiers')) {
                obj['identifiers'] = Identifiers.constructFromObject(data['identifiers']);
            }
            if (data.hasOwnProperty('image_link')) {
                obj['image_link'] = ImageLink.constructFromObject(data['image_link']);
            }
            if (data.hasOwnProperty('images_mixin')) {
                obj['images_mixin'] = ImagesMixin.constructFromObject(data['images_mixin']);
            }
            if (data.hasOwnProperty('master_brand_date_range')) {
                obj['master_brand_date_range'] = MasterBrandMasterBrandDateRange.constructFromObject(data['master_brand_date_range']);
            }
            if (data.hasOwnProperty('mid')) {
                obj['mid'] = ApiClient.convertToType(data['mid'], 'String');
            }
            if (data.hasOwnProperty('name')) {
                obj['name'] = ApiClient.convertToType(data['name'], 'String');
            }
            if (data.hasOwnProperty('partner')) {
                obj['partner'] = ApiClient.convertToType(data['partner'], 'String');
            }
            if (data.hasOwnProperty('position')) {
                obj['position'] = ApiClient.convertToType(data['position'], 'Number');
            }
            if (data.hasOwnProperty('synopses')) {
                obj['synopses'] = MasterBrandSynopses.constructFromObject(data['synopses']);
            }
            if (data.hasOwnProperty('title')) {
                obj['title'] = ApiClient.convertToType(data['title'], 'String');
            }
            if (data.hasOwnProperty('url_key')) {
                obj['url_key'] = ApiClient.convertToType(data['url_key'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>MasterBrand</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>MasterBrand</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of MasterBrand.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is a string
        if (data['colour'] && !(typeof data['colour'] === 'string' || data['colour'] instanceof String)) {
            throw new Error("Expected the field `colour` to be a primitive type in the JSON string but got " + data['colour']);
        }
        // validate the optional field `competition_warning`
        if (data['competition_warning']) { // data not null
          MasterBrandCompetitionWarning.validateJSON(data['competition_warning']);
        }
        // ensure the json data is a string
        if (data['ident'] && !(typeof data['ident'] === 'string' || data['ident'] instanceof String)) {
            throw new Error("Expected the field `ident` to be a primitive type in the JSON string but got " + data['ident']);
        }
        // validate the optional field `identifiers`
        if (data['identifiers']) { // data not null
          Identifiers.validateJSON(data['identifiers']);
        }
        // validate the optional field `image_link`
        if (data['image_link']) { // data not null
          ImageLink.validateJSON(data['image_link']);
        }
        // validate the optional field `images_mixin`
        if (data['images_mixin']) { // data not null
          ImagesMixin.validateJSON(data['images_mixin']);
        }
        // validate the optional field `master_brand_date_range`
        if (data['master_brand_date_range']) { // data not null
          MasterBrandMasterBrandDateRange.validateJSON(data['master_brand_date_range']);
        }
        // ensure the json data is a string
        if (data['mid'] && !(typeof data['mid'] === 'string' || data['mid'] instanceof String)) {
            throw new Error("Expected the field `mid` to be a primitive type in the JSON string but got " + data['mid']);
        }
        // ensure the json data is a string
        if (data['name'] && !(typeof data['name'] === 'string' || data['name'] instanceof String)) {
            throw new Error("Expected the field `name` to be a primitive type in the JSON string but got " + data['name']);
        }
        // ensure the json data is a string
        if (data['partner'] && !(typeof data['partner'] === 'string' || data['partner'] instanceof String)) {
            throw new Error("Expected the field `partner` to be a primitive type in the JSON string but got " + data['partner']);
        }
        // validate the optional field `synopses`
        if (data['synopses']) { // data not null
          MasterBrandSynopses.validateJSON(data['synopses']);
        }
        // ensure the json data is a string
        if (data['title'] && !(typeof data['title'] === 'string' || data['title'] instanceof String)) {
            throw new Error("Expected the field `title` to be a primitive type in the JSON string but got " + data['title']);
        }
        // ensure the json data is a string
        if (data['url_key'] && !(typeof data['url_key'] === 'string' || data['url_key'] instanceof String)) {
            throw new Error("Expected the field `url_key` to be a primitive type in the JSON string but got " + data['url_key']);
        }

        return true;
    }


}

MasterBrand.RequiredProperties = ["mid", "partner"];

/**
 * @member {String} colour
 */
MasterBrand.prototype['colour'] = undefined;

/**
 * @member {module:model/MasterBrandCompetitionWarning} competition_warning
 */
MasterBrand.prototype['competition_warning'] = undefined;

/**
 * @member {String} ident
 */
MasterBrand.prototype['ident'] = undefined;

/**
 * @member {module:model/Identifiers} identifiers
 */
MasterBrand.prototype['identifiers'] = undefined;

/**
 * @member {module:model/ImageLink} image_link
 */
MasterBrand.prototype['image_link'] = undefined;

/**
 * @member {module:model/ImagesMixin} images_mixin
 */
MasterBrand.prototype['images_mixin'] = undefined;

/**
 * @member {module:model/MasterBrandMasterBrandDateRange} master_brand_date_range
 */
MasterBrand.prototype['master_brand_date_range'] = undefined;

/**
 * @member {String} mid
 */
MasterBrand.prototype['mid'] = undefined;

/**
 * @member {String} name
 */
MasterBrand.prototype['name'] = undefined;

/**
 * @member {String} partner
 */
MasterBrand.prototype['partner'] = undefined;

/**
 * @member {Number} position
 */
MasterBrand.prototype['position'] = undefined;

/**
 * @member {module:model/MasterBrandSynopses} synopses
 */
MasterBrand.prototype['synopses'] = undefined;

/**
 * @member {String} title
 */
MasterBrand.prototype['title'] = undefined;

/**
 * @member {String} url_key
 */
MasterBrand.prototype['url_key'] = undefined;






export default MasterBrand;

