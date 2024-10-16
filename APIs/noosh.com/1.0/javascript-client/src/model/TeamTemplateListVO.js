/**
 * Noosh API application
 * Full description of Noosh API
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
import TeamTemplateSimpleVO from './TeamTemplateSimpleVO';

/**
 * The TeamTemplateListVO model module.
 * @module model/TeamTemplateListVO
 * @version 1.0
 */
class TeamTemplateListVO {
    /**
     * Constructs a new <code>TeamTemplateListVO</code>.
     * Java type: com.noosh.nooshapi.vo.TeamTemplateListVO
     * @alias module:model/TeamTemplateListVO
     */
    constructor() { 
        
        TeamTemplateListVO.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>TeamTemplateListVO</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/TeamTemplateListVO} obj Optional instance to populate.
     * @return {module:model/TeamTemplateListVO} The populated <code>TeamTemplateListVO</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new TeamTemplateListVO();

            if (data.hasOwnProperty('results')) {
                obj['results'] = ApiClient.convertToType(data['results'], [TeamTemplateSimpleVO]);
            }
            if (data.hasOwnProperty('status_code')) {
                obj['status_code'] = ApiClient.convertToType(data['status_code'], 'Number');
            }
            if (data.hasOwnProperty('status_reason')) {
                obj['status_reason'] = ApiClient.convertToType(data['status_reason'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>TeamTemplateListVO</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>TeamTemplateListVO</code>.
     */
    static validateJSON(data) {
        if (data['results']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['results'])) {
                throw new Error("Expected the field `results` to be an array in the JSON data but got " + data['results']);
            }
            // validate the optional field `results` (array)
            for (const item of data['results']) {
                TeamTemplateSimpleVO.validateJSON(item);
            };
        }
        // ensure the json data is a string
        if (data['status_reason'] && !(typeof data['status_reason'] === 'string' || data['status_reason'] instanceof String)) {
            throw new Error("Expected the field `status_reason` to be a primitive type in the JSON string but got " + data['status_reason']);
        }

        return true;
    }


}



/**
 * 
 * @member {Array.<module:model/TeamTemplateSimpleVO>} results
 */
TeamTemplateListVO.prototype['results'] = undefined;

/**
 * 
 * @member {Number} status_code
 */
TeamTemplateListVO.prototype['status_code'] = undefined;

/**
 * 
 * @member {String} status_reason
 */
TeamTemplateListVO.prototype['status_reason'] = undefined;






export default TeamTemplateListVO;

