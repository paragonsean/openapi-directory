/**
 * TrainingApi
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 2.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import BoundingBox from './BoundingBox';

/**
 * The RegionProposal model module.
 * @module model/RegionProposal
 * @version 2.0
 */
class RegionProposal {
    /**
     * Constructs a new <code>RegionProposal</code>.
     * @alias module:model/RegionProposal
     */
    constructor() { 
        
        RegionProposal.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>RegionProposal</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/RegionProposal} obj Optional instance to populate.
     * @return {module:model/RegionProposal} The populated <code>RegionProposal</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new RegionProposal();

            if (data.hasOwnProperty('boundingBox')) {
                obj['boundingBox'] = BoundingBox.constructFromObject(data['boundingBox']);
            }
            if (data.hasOwnProperty('confidence')) {
                obj['confidence'] = ApiClient.convertToType(data['confidence'], 'Number');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>RegionProposal</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>RegionProposal</code>.
     */
    static validateJSON(data) {
        // validate the optional field `boundingBox`
        if (data['boundingBox']) { // data not null
          BoundingBox.validateJSON(data['boundingBox']);
        }

        return true;
    }


}



/**
 * @member {module:model/BoundingBox} boundingBox
 */
RegionProposal.prototype['boundingBox'] = undefined;

/**
 * @member {Number} confidence
 */
RegionProposal.prototype['confidence'] = undefined;






export default RegionProposal;

