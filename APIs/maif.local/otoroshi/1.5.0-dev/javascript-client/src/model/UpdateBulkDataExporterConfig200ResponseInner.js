/**
 * Otoroshi Admin API
 * Admin API of the Otoroshi reverse proxy
 *
 * The version of the OpenAPI document: 1.5.0-dev
 * Contact: oss@maif.fr
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';

/**
 * The UpdateBulkDataExporterConfig200ResponseInner model module.
 * @module model/UpdateBulkDataExporterConfig200ResponseInner
 * @version 1.5.0-dev
 */
class UpdateBulkDataExporterConfig200ResponseInner {
    /**
     * Constructs a new <code>UpdateBulkDataExporterConfig200ResponseInner</code>.
     * The bulk response
     * @alias module:model/UpdateBulkDataExporterConfig200ResponseInner
     */
    constructor() { 
        
        UpdateBulkDataExporterConfig200ResponseInner.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>UpdateBulkDataExporterConfig200ResponseInner</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/UpdateBulkDataExporterConfig200ResponseInner} obj Optional instance to populate.
     * @return {module:model/UpdateBulkDataExporterConfig200ResponseInner} The populated <code>UpdateBulkDataExporterConfig200ResponseInner</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new UpdateBulkDataExporterConfig200ResponseInner();

            if (data.hasOwnProperty('id')) {
                obj['id'] = ApiClient.convertToType(data['id'], 'Boolean');
            }
            if (data.hasOwnProperty('status')) {
                obj['status'] = ApiClient.convertToType(data['status'], 'String');
            }
            if (data.hasOwnProperty('updated')) {
                obj['updated'] = ApiClient.convertToType(data['updated'], 'Boolean');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>UpdateBulkDataExporterConfig200ResponseInner</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>UpdateBulkDataExporterConfig200ResponseInner</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['status'] && !(typeof data['status'] === 'string' || data['status'] instanceof String)) {
            throw new Error("Expected the field `status` to be a primitive type in the JSON string but got " + data['status']);
        }

        return true;
    }


}



/**
 * Data exporter id
 * @member {Boolean} id
 */
UpdateBulkDataExporterConfig200ResponseInner.prototype['id'] = undefined;

/**
 * Status
 * @member {module:model/UpdateBulkDataExporterConfig200ResponseInner.StatusEnum} status
 */
UpdateBulkDataExporterConfig200ResponseInner.prototype['status'] = undefined;

/**
 * Whether the action was carried out correctly or not
 * @member {Boolean} updated
 */
UpdateBulkDataExporterConfig200ResponseInner.prototype['updated'] = undefined;





/**
 * Allowed values for the <code>status</code> property.
 * @enum {String}
 * @readonly
 */
UpdateBulkDataExporterConfig200ResponseInner['StatusEnum'] = {

    /**
     * value: "200"
     * @const
     */
    "200": "200"
};



export default UpdateBulkDataExporterConfig200ResponseInner;

