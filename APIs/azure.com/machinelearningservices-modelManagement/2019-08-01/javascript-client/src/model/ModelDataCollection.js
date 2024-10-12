/**
 * Azure Machine Learning Model Management Service
 * These APIs allow end users to manage Azure Machine Learning Models, Images, Profiles, and Services.
 *
 * The version of the OpenAPI document: 2019-08-01
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';

/**
 * The ModelDataCollection model module.
 * @module model/ModelDataCollection
 * @version 2019-08-01
 */
class ModelDataCollection {
    /**
     * Constructs a new <code>ModelDataCollection</code>.
     * The Model data collection properties.
     * @alias module:model/ModelDataCollection
     */
    constructor() { 
        
        ModelDataCollection.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>ModelDataCollection</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/ModelDataCollection} obj Optional instance to populate.
     * @return {module:model/ModelDataCollection} The populated <code>ModelDataCollection</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new ModelDataCollection();

            if (data.hasOwnProperty('eventHubEnabled')) {
                obj['eventHubEnabled'] = ApiClient.convertToType(data['eventHubEnabled'], 'Boolean');
            }
            if (data.hasOwnProperty('storageEnabled')) {
                obj['storageEnabled'] = ApiClient.convertToType(data['storageEnabled'], 'Boolean');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>ModelDataCollection</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>ModelDataCollection</code>.
     */
    static validateJSON(data) {

        return true;
    }


}



/**
 * Option for enabling/disabling Event Hub.
 * @member {Boolean} eventHubEnabled
 */
ModelDataCollection.prototype['eventHubEnabled'] = undefined;

/**
 * Option for enabling/disabling storage.
 * @member {Boolean} storageEnabled
 */
ModelDataCollection.prototype['storageEnabled'] = undefined;






export default ModelDataCollection;

