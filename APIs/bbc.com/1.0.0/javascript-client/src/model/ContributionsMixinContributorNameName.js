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
import ContributionsMixinContributorNameNameName from './ContributionsMixinContributorNameNameName';

/**
 * The ContributionsMixinContributorNameName model module.
 * @module model/ContributionsMixinContributorNameName
 * @version 1.0.0
 */
class ContributionsMixinContributorNameName {
    /**
     * Constructs a new <code>ContributionsMixinContributorNameName</code>.
     * @alias module:model/ContributionsMixinContributorNameName
     * @param name {module:model/ContributionsMixinContributorNameNameName} 
     */
    constructor(name) { 
        
        ContributionsMixinContributorNameName.initialize(this, name);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, name) { 
        obj['name'] = name;
    }

    /**
     * Constructs a <code>ContributionsMixinContributorNameName</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/ContributionsMixinContributorNameName} obj Optional instance to populate.
     * @return {module:model/ContributionsMixinContributorNameName} The populated <code>ContributionsMixinContributorNameName</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new ContributionsMixinContributorNameName();

            if (data.hasOwnProperty('family')) {
                obj['family'] = ApiClient.convertToType(data['family'], 'String');
            }
            if (data.hasOwnProperty('given')) {
                obj['given'] = ApiClient.convertToType(data['given'], 'String');
            }
            if (data.hasOwnProperty('name')) {
                obj['name'] = ContributionsMixinContributorNameNameName.constructFromObject(data['name']);
            }
            if (data.hasOwnProperty('presentation')) {
                obj['presentation'] = ApiClient.convertToType(data['presentation'], 'String');
            }
            if (data.hasOwnProperty('title')) {
                obj['title'] = ApiClient.convertToType(data['title'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>ContributionsMixinContributorNameName</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>ContributionsMixinContributorNameName</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of ContributionsMixinContributorNameName.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is a string
        if (data['family'] && !(typeof data['family'] === 'string' || data['family'] instanceof String)) {
            throw new Error("Expected the field `family` to be a primitive type in the JSON string but got " + data['family']);
        }
        // ensure the json data is a string
        if (data['given'] && !(typeof data['given'] === 'string' || data['given'] instanceof String)) {
            throw new Error("Expected the field `given` to be a primitive type in the JSON string but got " + data['given']);
        }
        // validate the optional field `name`
        if (data['name']) { // data not null
          ContributionsMixinContributorNameNameName.validateJSON(data['name']);
        }
        // ensure the json data is a string
        if (data['presentation'] && !(typeof data['presentation'] === 'string' || data['presentation'] instanceof String)) {
            throw new Error("Expected the field `presentation` to be a primitive type in the JSON string but got " + data['presentation']);
        }
        // ensure the json data is a string
        if (data['title'] && !(typeof data['title'] === 'string' || data['title'] instanceof String)) {
            throw new Error("Expected the field `title` to be a primitive type in the JSON string but got " + data['title']);
        }

        return true;
    }


}

ContributionsMixinContributorNameName.RequiredProperties = ["name"];

/**
 * @member {String} family
 */
ContributionsMixinContributorNameName.prototype['family'] = undefined;

/**
 * @member {String} given
 */
ContributionsMixinContributorNameName.prototype['given'] = undefined;

/**
 * @member {module:model/ContributionsMixinContributorNameNameName} name
 */
ContributionsMixinContributorNameName.prototype['name'] = undefined;

/**
 * @member {String} presentation
 */
ContributionsMixinContributorNameName.prototype['presentation'] = undefined;

/**
 * @member {String} title
 */
ContributionsMixinContributorNameName.prototype['title'] = undefined;






export default ContributionsMixinContributorNameName;

