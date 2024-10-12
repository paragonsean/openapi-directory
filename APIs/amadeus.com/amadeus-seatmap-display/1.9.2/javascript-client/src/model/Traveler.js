/**
 * Seatmap Display
 * Before using this API, we recommend you read our **[Authorization Guide](https://developers.amadeus.com/self-service/apis-docs/guides/authorization-262)** for more information on how to generate an access token.   Please also be aware that our test environment is based on a subset of the production, if you are not returning any results try with big cities/airports like LON (London) or NYC (New-York).
 *
 * The version of the OpenAPI document: 1.9.2
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import Contact from './Contact';
import Discount from './Discount';
import EmergencyContact from './EmergencyContact';
import IdentityDocument from './IdentityDocument';
import LoyaltyProgram from './LoyaltyProgram';
import Name from './Name';
import Stakeholder from './Stakeholder';
import StakeholderGender from './StakeholderGender';

/**
 * The Traveler model module.
 * @module model/Traveler
 * @version 1.9.2
 */
class Traveler {
    /**
     * Constructs a new <code>Traveler</code>.
     * the traveler of the trip
     * @alias module:model/Traveler
     * @implements module:model/Stakeholder
     */
    constructor() { 
        Stakeholder.initialize(this);
        Traveler.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>Traveler</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/Traveler} obj Optional instance to populate.
     * @return {module:model/Traveler} The populated <code>Traveler</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new Traveler();
            Stakeholder.constructFromObject(data, obj);

            if (data.hasOwnProperty('dateOfBirth')) {
                obj['dateOfBirth'] = ApiClient.convertToType(data['dateOfBirth'], 'Date');
            }
            if (data.hasOwnProperty('documents')) {
                obj['documents'] = ApiClient.convertToType(data['documents'], [IdentityDocument]);
            }
            if (data.hasOwnProperty('gender')) {
                obj['gender'] = StakeholderGender.constructFromObject(data['gender']);
            }
            if (data.hasOwnProperty('id')) {
                obj['id'] = ApiClient.convertToType(data['id'], 'String');
            }
            if (data.hasOwnProperty('name')) {
                obj['name'] = Name.constructFromObject(data['name']);
            }
            if (data.hasOwnProperty('contact')) {
                obj['contact'] = Contact.constructFromObject(data['contact']);
            }
            if (data.hasOwnProperty('discountEligibility')) {
                obj['discountEligibility'] = ApiClient.convertToType(data['discountEligibility'], [Discount]);
            }
            if (data.hasOwnProperty('emergencyContact')) {
                obj['emergencyContact'] = EmergencyContact.constructFromObject(data['emergencyContact']);
            }
            if (data.hasOwnProperty('loyaltyPrograms')) {
                obj['loyaltyPrograms'] = ApiClient.convertToType(data['loyaltyPrograms'], [LoyaltyProgram]);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>Traveler</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>Traveler</code>.
     */
    static validateJSON(data) {
        if (data['documents']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['documents'])) {
                throw new Error("Expected the field `documents` to be an array in the JSON data but got " + data['documents']);
            }
            // validate the optional field `documents` (array)
            for (const item of data['documents']) {
                IdentityDocument.validateJSON(item);
            };
        }
        // ensure the json data is a string
        if (data['id'] && !(typeof data['id'] === 'string' || data['id'] instanceof String)) {
            throw new Error("Expected the field `id` to be a primitive type in the JSON string but got " + data['id']);
        }
        // validate the optional field `name`
        if (data['name']) { // data not null
          Name.validateJSON(data['name']);
        }
        // validate the optional field `contact`
        if (data['contact']) { // data not null
          Contact.validateJSON(data['contact']);
        }
        if (data['discountEligibility']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['discountEligibility'])) {
                throw new Error("Expected the field `discountEligibility` to be an array in the JSON data but got " + data['discountEligibility']);
            }
            // validate the optional field `discountEligibility` (array)
            for (const item of data['discountEligibility']) {
                Discount.validateJSON(item);
            };
        }
        // validate the optional field `emergencyContact`
        if (data['emergencyContact']) { // data not null
          EmergencyContact.validateJSON(data['emergencyContact']);
        }
        if (data['loyaltyPrograms']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['loyaltyPrograms'])) {
                throw new Error("Expected the field `loyaltyPrograms` to be an array in the JSON data but got " + data['loyaltyPrograms']);
            }
            // validate the optional field `loyaltyPrograms` (array)
            for (const item of data['loyaltyPrograms']) {
                LoyaltyProgram.validateJSON(item);
            };
        }

        return true;
    }


}



/**
 * The date of birth in ISO 8601 format (yyyy-mm-dd)
 * @member {Date} dateOfBirth
 */
Traveler.prototype['dateOfBirth'] = undefined;

/**
 * Advanced Passenger Information - regulatory identity documents - SSR DOCS & DOCO elements
 * @member {Array.<module:model/IdentityDocument>} documents
 */
Traveler.prototype['documents'] = undefined;

/**
 * @member {module:model/StakeholderGender} gender
 */
Traveler.prototype['gender'] = undefined;

/**
 * item identifier
 * @member {String} id
 */
Traveler.prototype['id'] = undefined;

/**
 * @member {module:model/Name} name
 */
Traveler.prototype['name'] = undefined;

/**
 * @member {module:model/Contact} contact
 */
Traveler.prototype['contact'] = undefined;

/**
 * list of element that allow a discount.
 * @member {Array.<module:model/Discount>} discountEligibility
 */
Traveler.prototype['discountEligibility'] = undefined;

/**
 * @member {module:model/EmergencyContact} emergencyContact
 */
Traveler.prototype['emergencyContact'] = undefined;

/**
 * list of loyalty program followed by the traveler
 * @member {Array.<module:model/LoyaltyProgram>} loyaltyPrograms
 */
Traveler.prototype['loyaltyPrograms'] = undefined;


// Implement Stakeholder interface:
/**
 * The date of birth in ISO 8601 format (yyyy-mm-dd)
 * @member {Date} dateOfBirth
 */
Stakeholder.prototype['dateOfBirth'] = undefined;
/**
 * Advanced Passenger Information - regulatory identity documents - SSR DOCS & DOCO elements
 * @member {Array.<module:model/IdentityDocument>} documents
 */
Stakeholder.prototype['documents'] = undefined;
/**
 * @member {module:model/StakeholderGender} gender
 */
Stakeholder.prototype['gender'] = undefined;
/**
 * item identifier
 * @member {String} id
 */
Stakeholder.prototype['id'] = undefined;
/**
 * @member {module:model/Name} name
 */
Stakeholder.prototype['name'] = undefined;




export default Traveler;

