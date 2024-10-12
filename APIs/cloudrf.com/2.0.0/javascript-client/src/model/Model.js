/**
 * Cloud-RF API
 * Use this JSON API to build and test radio links for any radio, anywhere. Authenticate with your API2.0 key in the request header as key
 *
 * The version of the OpenAPI document: 2.0.0
 * Contact: support@cloudrf.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';

/**
 * The Model model module.
 * @module model/Model
 * @version 2.0.0
 */
class Model {
    /**
     * Constructs a new <code>Model</code>.
     * @alias module:model/Model
     */
    constructor() { 
        
        Model.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
        obj['cli'] = 6;
        obj['ked'] = 0;
        obj['pe'] = 2;
        obj['pm'] = 1;
        obj['rel'] = 95;
        obj['ter'] = 4;
    }

    /**
     * Constructs a <code>Model</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/Model} obj Optional instance to populate.
     * @return {module:model/Model} The populated <code>Model</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new Model();

            if (data.hasOwnProperty('cli')) {
                obj['cli'] = ApiClient.convertToType(data['cli'], 'Number');
            }
            if (data.hasOwnProperty('ked')) {
                obj['ked'] = ApiClient.convertToType(data['ked'], 'Number');
            }
            if (data.hasOwnProperty('pe')) {
                obj['pe'] = ApiClient.convertToType(data['pe'], 'Number');
            }
            if (data.hasOwnProperty('pm')) {
                obj['pm'] = ApiClient.convertToType(data['pm'], 'Number');
            }
            if (data.hasOwnProperty('rel')) {
                obj['rel'] = ApiClient.convertToType(data['rel'], 'Number');
            }
            if (data.hasOwnProperty('ter')) {
                obj['ter'] = ApiClient.convertToType(data['ter'], 'Number');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>Model</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>Model</code>.
     */
    static validateJSON(data) {

        return true;
    }


}



/**
 * Radio climate for ITM model (1). 1: Equatorial (Congo) 2: Continental Subtropical (Sudan) 3: Maritime Subtropical (West coast of Africa) 4: Desert (Sahara) 5: Continental Temperate 6: Maritime Temperate, over land (UK and west coasts of US & EU) 7: Maritime Temperate, over sea
 * @member {Number} cli
 * @default 6
 */
Model.prototype['cli'] = 6;

/**
 * Knife edge diffraction for enhancing basic empirical models (Already in ITM)
 * @member {Number} ked
 * @default 0
 */
Model.prototype['ked'] = 0;

/**
 * Propagation model subtype/environment. 1=Conservative/Urban,2=Average/Suburban,3=Optimistic/rural
 * @member {Number} pe
 * @default 2
 */
Model.prototype['pe'] = 2;

/**
 * Propagation model. 1=Irregular Terrain Model, 2=Line of Sight (LOS), 3=Hata, 4=ECC33, 5=SUI Microwave, 6=COST231, 7=Free space path loss, 9=Ericsson9999, 10=Plane earth loss, 11=Egli.
 * @member {Number} pm
 * @default 1
 */
Model.prototype['pm'] = 1;

/**
 * ITM model required reliability as %
 * @member {Number} rel
 * @default 95
 */
Model.prototype['rel'] = 95;

/**
 * Terrain code for ITM model (1). 1=Water,2=Wet ground,3=Farmland,4=Forest/Average,5=Mountain/Sand,6=City/Poor ground
 * @member {Number} ter
 * @default 4
 */
Model.prototype['ter'] = 4;






export default Model;

