/**
 * The Blue Alliance API v3
 * # Overview    Information and statistics about FIRST Robotics Competition teams and events.   # Authentication   All endpoints require an Auth Key to be passed in the header `X-TBA-Auth-Key`. If you do not have an auth key yet, you can obtain one from your [Account Page](/account).
 *
 * The version of the OpenAPI document: 3.8.2
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import EliminationAllianceBackup from './EliminationAllianceBackup';
import EliminationAllianceStatus from './EliminationAllianceStatus';

/**
 * The EliminationAlliance model module.
 * @module model/EliminationAlliance
 * @version 3.8.2
 */
class EliminationAlliance {
    /**
     * Constructs a new <code>EliminationAlliance</code>.
     * @alias module:model/EliminationAlliance
     * @param picks {Array.<String>} List of team keys picked for the alliance. First pick is captain.
     */
    constructor(picks) { 
        
        EliminationAlliance.initialize(this, picks);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, picks) { 
        obj['picks'] = picks;
    }

    /**
     * Constructs a <code>EliminationAlliance</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/EliminationAlliance} obj Optional instance to populate.
     * @return {module:model/EliminationAlliance} The populated <code>EliminationAlliance</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new EliminationAlliance();

            if (data.hasOwnProperty('backup')) {
                obj['backup'] = EliminationAllianceBackup.constructFromObject(data['backup']);
            }
            if (data.hasOwnProperty('declines')) {
                obj['declines'] = ApiClient.convertToType(data['declines'], ['String']);
            }
            if (data.hasOwnProperty('name')) {
                obj['name'] = ApiClient.convertToType(data['name'], 'String');
            }
            if (data.hasOwnProperty('picks')) {
                obj['picks'] = ApiClient.convertToType(data['picks'], ['String']);
            }
            if (data.hasOwnProperty('status')) {
                obj['status'] = EliminationAllianceStatus.constructFromObject(data['status']);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>EliminationAlliance</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>EliminationAlliance</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of EliminationAlliance.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // validate the optional field `backup`
        if (data['backup']) { // data not null
          EliminationAllianceBackup.validateJSON(data['backup']);
        }
        // ensure the json data is an array
        if (!Array.isArray(data['declines'])) {
            throw new Error("Expected the field `declines` to be an array in the JSON data but got " + data['declines']);
        }
        // ensure the json data is a string
        if (data['name'] && !(typeof data['name'] === 'string' || data['name'] instanceof String)) {
            throw new Error("Expected the field `name` to be a primitive type in the JSON string but got " + data['name']);
        }
        // ensure the json data is an array
        if (!Array.isArray(data['picks'])) {
            throw new Error("Expected the field `picks` to be an array in the JSON data but got " + data['picks']);
        }
        // validate the optional field `status`
        if (data['status']) { // data not null
          EliminationAllianceStatus.validateJSON(data['status']);
        }

        return true;
    }


}

EliminationAlliance.RequiredProperties = ["picks"];

/**
 * @member {module:model/EliminationAllianceBackup} backup
 */
EliminationAlliance.prototype['backup'] = undefined;

/**
 * List of teams that declined the alliance.
 * @member {Array.<String>} declines
 */
EliminationAlliance.prototype['declines'] = undefined;

/**
 * Alliance name, may be null.
 * @member {String} name
 */
EliminationAlliance.prototype['name'] = undefined;

/**
 * List of team keys picked for the alliance. First pick is captain.
 * @member {Array.<String>} picks
 */
EliminationAlliance.prototype['picks'] = undefined;

/**
 * @member {module:model/EliminationAllianceStatus} status
 */
EliminationAlliance.prototype['status'] = undefined;






export default EliminationAlliance;

