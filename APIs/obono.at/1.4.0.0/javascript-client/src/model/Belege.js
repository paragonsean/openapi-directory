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
import Beleg from './Beleg';
import Belegformat from './Belegformat';
import Exportformat from './Exportformat';
import ExportformatBelegeGruppeInner from './ExportformatBelegeGruppeInner';

/**
 * The Belege model module.
 * @module model/Belege
 * @version 1.4.0.0
 */
class Belege {
    /**
     * Constructs a new <code>Belege</code>.
     * @alias module:model/Belege
     * @implements module:model/Belegformat
     * @implements module:model/Exportformat
     */
    constructor() { 
        Belegformat.initialize(this);Exportformat.initialize(this);
        Belege.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>Belege</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/Belege} obj Optional instance to populate.
     * @return {module:model/Belege} The populated <code>Belege</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new Belege();
            Belegformat.constructFromObject(data, obj);
            Exportformat.constructFromObject(data, obj);

            if (data.hasOwnProperty('Belege')) {
                obj['Belege'] = ApiClient.convertToType(data['Belege'], [Beleg]);
            }
            if (data.hasOwnProperty('Belege-Gruppe')) {
                obj['Belege-Gruppe'] = ApiClient.convertToType(data['Belege-Gruppe'], [ExportformatBelegeGruppeInner]);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>Belege</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>Belege</code>.
     */
    static validateJSON(data) {
        if (data['Belege']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['Belege'])) {
                throw new Error("Expected the field `Belege` to be an array in the JSON data but got " + data['Belege']);
            }
            // validate the optional field `Belege` (array)
            for (const item of data['Belege']) {
                Beleg.validateJSON(item);
            };
        }
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
 * @member {Array.<module:model/Beleg>} Belege
 */
Belege.prototype['Belege'] = undefined;

/**
 * @member {Array.<module:model/ExportformatBelegeGruppeInner>} Belege-Gruppe
 */
Belege.prototype['Belege-Gruppe'] = undefined;


// Implement Belegformat interface:
/**
 * @member {Array.<module:model/Beleg>} Belege
 */
Belegformat.prototype['Belege'] = undefined;
// Implement Exportformat interface:
/**
 * @member {Array.<module:model/ExportformatBelegeGruppeInner>} Belege-Gruppe
 */
Exportformat.prototype['Belege-Gruppe'] = undefined;




export default Belege;

