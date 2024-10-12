/**
 * obono RKSV API
 * Provides a RESTful API for interacting with virtual cash registers and creating receipts that are conform with the Registrierkassensicherheitsverordnung (RKSV).  You may find our [automatically generated clients](./clients) for various programming languages and environments helpful... 
 *
 * The version of the OpenAPI document: 1.4.0.0
 * Contact: info@obono.at
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import ExportformatBelegeGruppeInner from './ExportformatBelegeGruppeInner';

/**
 * The Exportformat model module.
 * @module model/Exportformat
 * @version 1.4.0.0
 */
class Exportformat {
    /**
     * Constructs a new <code>Exportformat</code>.
     * @alias module:model/Exportformat
     */
    constructor() { 
        
        Exportformat.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>Exportformat</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/Exportformat} obj Optional instance to populate.
     * @return {module:model/Exportformat} The populated <code>Exportformat</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new Exportformat();

            if (data.hasOwnProperty('Belege-Gruppe')) {
                obj['Belege-Gruppe'] = ApiClient.convertToType(data['Belege-Gruppe'], [ExportformatBelegeGruppeInner]);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>Exportformat</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>Exportformat</code>.
     */
    static validateJSON(data) {
        if (data['Belege-Gruppe']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['Belege-Gruppe'])) {
                throw new Error("Expected the field `Belege-Gruppe` to be an array in the JSON data but got " + data['Belege-Gruppe']);
            }
            // validate the optional field `Belege-Gruppe` (array)
            for (const item of data['Belege-Gruppe']) {
                ExportformatBelegeGruppeInner.validateJSON(item);
            };
        }

        return true;
    }


}



/**
 * @member {Array.<module:model/ExportformatBelegeGruppeInner>} Belege-Gruppe
 */
Exportformat.prototype['Belege-Gruppe'] = undefined;






export default Exportformat;

