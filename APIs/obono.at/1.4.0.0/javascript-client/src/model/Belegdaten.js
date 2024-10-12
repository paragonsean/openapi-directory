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
import Posten from './Posten';
import Rabatt from './Rabatt';
import Zahlung from './Zahlung';

/**
 * The Belegdaten model module.
 * @module model/Belegdaten
 * @version 1.4.0.0
 */
class Belegdaten {
    /**
     * Constructs a new <code>Belegdaten</code>.
     * The &#x60;Beleg&#x60; to be signed by the \&quot;Signaturerstellungseinheit\&quot; and stored in the \&quot;Datenerfassungsprotokoll\&quot;.
     * @alias module:model/Belegdaten
     */
    constructor() { 
        
        Belegdaten.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>Belegdaten</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/Belegdaten} obj Optional instance to populate.
     * @return {module:model/Belegdaten} The populated <code>Belegdaten</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new Belegdaten();

            if (data.hasOwnProperty('Externer-Beleg-Belegkreis')) {
                obj['Externer-Beleg-Belegkreis'] = ApiClient.convertToType(data['Externer-Beleg-Belegkreis'], 'String');
            }
            if (data.hasOwnProperty('Externer-Beleg-Bezeichnung')) {
                obj['Externer-Beleg-Bezeichnung'] = ApiClient.convertToType(data['Externer-Beleg-Bezeichnung'], 'String');
            }
            if (data.hasOwnProperty('Externer-Beleg-Referenz')) {
                obj['Externer-Beleg-Referenz'] = ApiClient.convertToType(data['Externer-Beleg-Referenz'], 'String');
            }
            if (data.hasOwnProperty('Kunde')) {
                obj['Kunde'] = ApiClient.convertToType(data['Kunde'], 'String');
            }
            if (data.hasOwnProperty('Notizen')) {
                obj['Notizen'] = ApiClient.convertToType(data['Notizen'], ['String']);
            }
            if (data.hasOwnProperty('Posten')) {
                obj['Posten'] = ApiClient.convertToType(data['Posten'], [Posten]);
            }
            if (data.hasOwnProperty('Rabatte')) {
                obj['Rabatte'] = ApiClient.convertToType(data['Rabatte'], [Rabatt]);
            }
            if (data.hasOwnProperty('Storno')) {
                obj['Storno'] = ApiClient.convertToType(data['Storno'], 'Boolean');
            }
            if (data.hasOwnProperty('Storno-Beleg-UUID')) {
                obj['Storno-Beleg-UUID'] = ApiClient.convertToType(data['Storno-Beleg-UUID'], 'String');
            }
            if (data.hasOwnProperty('Storno-Text')) {
                obj['Storno-Text'] = ApiClient.convertToType(data['Storno-Text'], 'String');
            }
            if (data.hasOwnProperty('Training')) {
                obj['Training'] = ApiClient.convertToType(data['Training'], 'Boolean');
            }
            if (data.hasOwnProperty('Unternehmen-Adresse1')) {
                obj['Unternehmen-Adresse1'] = ApiClient.convertToType(data['Unternehmen-Adresse1'], 'String');
            }
            if (data.hasOwnProperty('Unternehmen-Adresse2')) {
                obj['Unternehmen-Adresse2'] = ApiClient.convertToType(data['Unternehmen-Adresse2'], 'String');
            }
            if (data.hasOwnProperty('Unternehmen-Fusszeile')) {
                obj['Unternehmen-Fusszeile'] = ApiClient.convertToType(data['Unternehmen-Fusszeile'], 'String');
            }
            if (data.hasOwnProperty('Unternehmen-ID')) {
                obj['Unternehmen-ID'] = ApiClient.convertToType(data['Unternehmen-ID'], 'String');
            }
            if (data.hasOwnProperty('Unternehmen-ID-Typ')) {
                obj['Unternehmen-ID-Typ'] = ApiClient.convertToType(data['Unternehmen-ID-Typ'], 'String');
            }
            if (data.hasOwnProperty('Unternehmen-Kopfzeile')) {
                obj['Unternehmen-Kopfzeile'] = ApiClient.convertToType(data['Unternehmen-Kopfzeile'], 'String');
            }
            if (data.hasOwnProperty('Unternehmen-Name')) {
                obj['Unternehmen-Name'] = ApiClient.convertToType(data['Unternehmen-Name'], 'String');
            }
            if (data.hasOwnProperty('Unternehmen-Ort')) {
                obj['Unternehmen-Ort'] = ApiClient.convertToType(data['Unternehmen-Ort'], 'String');
            }
            if (data.hasOwnProperty('Unternehmen-PLZ')) {
                obj['Unternehmen-PLZ'] = ApiClient.convertToType(data['Unternehmen-PLZ'], 'String');
            }
            if (data.hasOwnProperty('Zahlungen')) {
                obj['Zahlungen'] = ApiClient.convertToType(data['Zahlungen'], [Zahlung]);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>Belegdaten</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>Belegdaten</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['Externer-Beleg-Belegkreis'] && !(typeof data['Externer-Beleg-Belegkreis'] === 'string' || data['Externer-Beleg-Belegkreis'] instanceof String)) {
            throw new Error("Expected the field `Externer-Beleg-Belegkreis` to be a primitive type in the JSON string but got " + data['Externer-Beleg-Belegkreis']);
        }
        // ensure the json data is a string
        if (data['Externer-Beleg-Bezeichnung'] && !(typeof data['Externer-Beleg-Bezeichnung'] === 'string' || data['Externer-Beleg-Bezeichnung'] instanceof String)) {
            throw new Error("Expected the field `Externer-Beleg-Bezeichnung` to be a primitive type in the JSON string but got " + data['Externer-Beleg-Bezeichnung']);
        }
        // ensure the json data is a string
        if (data['Externer-Beleg-Referenz'] && !(typeof data['Externer-Beleg-Referenz'] === 'string' || data['Externer-Beleg-Referenz'] instanceof String)) {
            throw new Error("Expected the field `Externer-Beleg-Referenz` to be a primitive type in the JSON string but got " + data['Externer-Beleg-Referenz']);
        }
        // ensure the json data is a string
        if (data['Kunde'] && !(typeof data['Kunde'] === 'string' || data['Kunde'] instanceof String)) {
            throw new Error("Expected the field `Kunde` to be a primitive type in the JSON string but got " + data['Kunde']);
        }
        // ensure the json data is an array
        if (!Array.isArray(data['Notizen'])) {
            throw new Error("Expected the field `Notizen` to be an array in the JSON data but got " + data['Notizen']);
        }
        if (data['Posten']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['Posten'])) {
                throw new Error("Expected the field `Posten` to be an array in the JSON data but got " + data['Posten']);
            }
            // validate the optional field `Posten` (array)
            for (const item of data['Posten']) {
                Posten.validateJSON(item);
            };
        }
        if (data['Rabatte']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['Rabatte'])) {
                throw new Error("Expected the field `Rabatte` to be an array in the JSON data but got " + data['Rabatte']);
            }
            // validate the optional field `Rabatte` (array)
            for (const item of data['Rabatte']) {
                Rabatt.validateJSON(item);
            };
        }
        // ensure the json data is a string
        if (data['Storno-Beleg-UUID'] && !(typeof data['Storno-Beleg-UUID'] === 'string' || data['Storno-Beleg-UUID'] instanceof String)) {
            throw new Error("Expected the field `Storno-Beleg-UUID` to be a primitive type in the JSON string but got " + data['Storno-Beleg-UUID']);
        }
        // ensure the json data is a string
        if (data['Storno-Text'] && !(typeof data['Storno-Text'] === 'string' || data['Storno-Text'] instanceof String)) {
            throw new Error("Expected the field `Storno-Text` to be a primitive type in the JSON string but got " + data['Storno-Text']);
        }
        // ensure the json data is a string
        if (data['Unternehmen-Adresse1'] && !(typeof data['Unternehmen-Adresse1'] === 'string' || data['Unternehmen-Adresse1'] instanceof String)) {
            throw new Error("Expected the field `Unternehmen-Adresse1` to be a primitive type in the JSON string but got " + data['Unternehmen-Adresse1']);
        }
        // ensure the json data is a string
        if (data['Unternehmen-Adresse2'] && !(typeof data['Unternehmen-Adresse2'] === 'string' || data['Unternehmen-Adresse2'] instanceof String)) {
            throw new Error("Expected the field `Unternehmen-Adresse2` to be a primitive type in the JSON string but got " + data['Unternehmen-Adresse2']);
        }
        // ensure the json data is a string
        if (data['Unternehmen-Fusszeile'] && !(typeof data['Unternehmen-Fusszeile'] === 'string' || data['Unternehmen-Fusszeile'] instanceof String)) {
            throw new Error("Expected the field `Unternehmen-Fusszeile` to be a primitive type in the JSON string but got " + data['Unternehmen-Fusszeile']);
        }
        // ensure the json data is a string
        if (data['Unternehmen-ID'] && !(typeof data['Unternehmen-ID'] === 'string' || data['Unternehmen-ID'] instanceof String)) {
            throw new Error("Expected the field `Unternehmen-ID` to be a primitive type in the JSON string but got " + data['Unternehmen-ID']);
        }
        // ensure the json data is a string
        if (data['Unternehmen-ID-Typ'] && !(typeof data['Unternehmen-ID-Typ'] === 'string' || data['Unternehmen-ID-Typ'] instanceof String)) {
            throw new Error("Expected the field `Unternehmen-ID-Typ` to be a primitive type in the JSON string but got " + data['Unternehmen-ID-Typ']);
        }
        // ensure the json data is a string
        if (data['Unternehmen-Kopfzeile'] && !(typeof data['Unternehmen-Kopfzeile'] === 'string' || data['Unternehmen-Kopfzeile'] instanceof String)) {
            throw new Error("Expected the field `Unternehmen-Kopfzeile` to be a primitive type in the JSON string but got " + data['Unternehmen-Kopfzeile']);
        }
        // ensure the json data is a string
        if (data['Unternehmen-Name'] && !(typeof data['Unternehmen-Name'] === 'string' || data['Unternehmen-Name'] instanceof String)) {
            throw new Error("Expected the field `Unternehmen-Name` to be a primitive type in the JSON string but got " + data['Unternehmen-Name']);
        }
        // ensure the json data is a string
        if (data['Unternehmen-Ort'] && !(typeof data['Unternehmen-Ort'] === 'string' || data['Unternehmen-Ort'] instanceof String)) {
            throw new Error("Expected the field `Unternehmen-Ort` to be a primitive type in the JSON string but got " + data['Unternehmen-Ort']);
        }
        // ensure the json data is a string
        if (data['Unternehmen-PLZ'] && !(typeof data['Unternehmen-PLZ'] === 'string' || data['Unternehmen-PLZ'] instanceof String)) {
            throw new Error("Expected the field `Unternehmen-PLZ` to be a primitive type in the JSON string but got " + data['Unternehmen-PLZ']);
        }
        if (data['Zahlungen']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['Zahlungen'])) {
                throw new Error("Expected the field `Zahlungen` to be an array in the JSON data but got " + data['Zahlungen']);
            }
            // validate the optional field `Zahlungen` (array)
            for (const item of data['Zahlungen']) {
                Zahlung.validateJSON(item);
            };
        }

        return true;
    }


}



/**
 * @member {String} Externer-Beleg-Belegkreis
 */
Belegdaten.prototype['Externer-Beleg-Belegkreis'] = undefined;

/**
 * @member {String} Externer-Beleg-Bezeichnung
 */
Belegdaten.prototype['Externer-Beleg-Bezeichnung'] = undefined;

/**
 * @member {String} Externer-Beleg-Referenz
 */
Belegdaten.prototype['Externer-Beleg-Referenz'] = undefined;

/**
 * @member {String} Kunde
 */
Belegdaten.prototype['Kunde'] = undefined;

/**
 * @member {Array.<String>} Notizen
 */
Belegdaten.prototype['Notizen'] = undefined;

/**
 * @member {Array.<module:model/Posten>} Posten
 */
Belegdaten.prototype['Posten'] = undefined;

/**
 * @member {Array.<module:model/Rabatt>} Rabatte
 */
Belegdaten.prototype['Rabatte'] = undefined;

/**
 * Storno?
 * @member {Boolean} Storno
 */
Belegdaten.prototype['Storno'] = undefined;

/**
 * The `Beleg-UUID` property of the `Beleg` to be cancelled
 * @member {String} Storno-Beleg-UUID
 */
Belegdaten.prototype['Storno-Beleg-UUID'] = undefined;

/**
 * @member {String} Storno-Text
 */
Belegdaten.prototype['Storno-Text'] = undefined;

/**
 * Training?
 * @member {Boolean} Training
 */
Belegdaten.prototype['Training'] = undefined;

/**
 * @member {String} Unternehmen-Adresse1
 */
Belegdaten.prototype['Unternehmen-Adresse1'] = undefined;

/**
 * @member {String} Unternehmen-Adresse2
 */
Belegdaten.prototype['Unternehmen-Adresse2'] = undefined;

/**
 * @member {String} Unternehmen-Fusszeile
 */
Belegdaten.prototype['Unternehmen-Fusszeile'] = undefined;

/**
 * @member {String} Unternehmen-ID
 */
Belegdaten.prototype['Unternehmen-ID'] = undefined;

/**
 * @member {module:model/Belegdaten.UnternehmenIDTypEnum} Unternehmen-ID-Typ
 */
Belegdaten.prototype['Unternehmen-ID-Typ'] = undefined;

/**
 * @member {String} Unternehmen-Kopfzeile
 */
Belegdaten.prototype['Unternehmen-Kopfzeile'] = undefined;

/**
 * @member {String} Unternehmen-Name
 */
Belegdaten.prototype['Unternehmen-Name'] = undefined;

/**
 * @member {String} Unternehmen-Ort
 */
Belegdaten.prototype['Unternehmen-Ort'] = undefined;

/**
 * @member {String} Unternehmen-PLZ
 */
Belegdaten.prototype['Unternehmen-PLZ'] = undefined;

/**
 * @member {Array.<module:model/Zahlung>} Zahlungen
 */
Belegdaten.prototype['Zahlungen'] = undefined;





/**
 * Allowed values for the <code>Unternehmen-ID-Typ</code> property.
 * @enum {String}
 * @readonly
 */
Belegdaten['UnternehmenIDTypEnum'] = {

    /**
     * value: "steuernummer"
     * @const
     */
    "steuernummer": "steuernummer",

    /**
     * value: "uid"
     * @const
     */
    "uid": "uid",

    /**
     * value: "gln"
     * @const
     */
    "gln": "gln"
};



export default Belegdaten;

