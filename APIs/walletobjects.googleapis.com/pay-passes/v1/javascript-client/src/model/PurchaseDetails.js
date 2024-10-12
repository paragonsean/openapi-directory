/**
 * Google Pay Passes API
 * API for issuers to save and manage Google Wallet Objects.
 *
 * The version of the OpenAPI document: v1
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import TicketCost from './TicketCost';

/**
 * The PurchaseDetails model module.
 * @module model/PurchaseDetails
 * @version v1
 */
class PurchaseDetails {
    /**
     * Constructs a new <code>PurchaseDetails</code>.
     * @alias module:model/PurchaseDetails
     */
    constructor() { 
        
        PurchaseDetails.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>PurchaseDetails</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/PurchaseDetails} obj Optional instance to populate.
     * @return {module:model/PurchaseDetails} The populated <code>PurchaseDetails</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new PurchaseDetails();

            if (data.hasOwnProperty('accountId')) {
                obj['accountId'] = ApiClient.convertToType(data['accountId'], 'String');
            }
            if (data.hasOwnProperty('confirmationCode')) {
                obj['confirmationCode'] = ApiClient.convertToType(data['confirmationCode'], 'String');
            }
            if (data.hasOwnProperty('purchaseDateTime')) {
                obj['purchaseDateTime'] = ApiClient.convertToType(data['purchaseDateTime'], 'String');
            }
            if (data.hasOwnProperty('purchaseReceiptNumber')) {
                obj['purchaseReceiptNumber'] = ApiClient.convertToType(data['purchaseReceiptNumber'], 'String');
            }
            if (data.hasOwnProperty('ticketCost')) {
                obj['ticketCost'] = TicketCost.constructFromObject(data['ticketCost']);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>PurchaseDetails</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>PurchaseDetails</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['accountId'] && !(typeof data['accountId'] === 'string' || data['accountId'] instanceof String)) {
            throw new Error("Expected the field `accountId` to be a primitive type in the JSON string but got " + data['accountId']);
        }
        // ensure the json data is a string
        if (data['confirmationCode'] && !(typeof data['confirmationCode'] === 'string' || data['confirmationCode'] instanceof String)) {
            throw new Error("Expected the field `confirmationCode` to be a primitive type in the JSON string but got " + data['confirmationCode']);
        }
        // ensure the json data is a string
        if (data['purchaseDateTime'] && !(typeof data['purchaseDateTime'] === 'string' || data['purchaseDateTime'] instanceof String)) {
            throw new Error("Expected the field `purchaseDateTime` to be a primitive type in the JSON string but got " + data['purchaseDateTime']);
        }
        // ensure the json data is a string
        if (data['purchaseReceiptNumber'] && !(typeof data['purchaseReceiptNumber'] === 'string' || data['purchaseReceiptNumber'] instanceof String)) {
            throw new Error("Expected the field `purchaseReceiptNumber` to be a primitive type in the JSON string but got " + data['purchaseReceiptNumber']);
        }
        // validate the optional field `ticketCost`
        if (data['ticketCost']) { // data not null
          TicketCost.validateJSON(data['ticketCost']);
        }

        return true;
    }


}



/**
 * ID of the account used to purchase the ticket.
 * @member {String} accountId
 */
PurchaseDetails.prototype['accountId'] = undefined;

/**
 * The confirmation code for the purchase. This may be the same for multiple different tickets and is used to group tickets together.
 * @member {String} confirmationCode
 */
PurchaseDetails.prototype['confirmationCode'] = undefined;

/**
 * The purchase date/time of the ticket. This is an ISO 8601 extended format date/time, with or without an offset. Time may be specified up to nanosecond precision. Offsets may be specified with seconds precision (even though offset seconds is not part of ISO 8601). For example: `1985-04-12T23:20:50.52Z` would be 20 minutes and 50.52 seconds after the 23rd hour of April 12th, 1985 in UTC. `1985-04-12T19:20:50.52-04:00` would be 20 minutes and 50.52 seconds after the 19th hour of April 12th, 1985, 4 hours before UTC (same instant in time as the above example). If the event were in New York, this would be the equivalent of Eastern Daylight Time (EDT). Remember that offset varies in regions that observe Daylight Saving Time (or Summer Time), depending on the time of the year. `1985-04-12T19:20:50.52` would be 20 minutes and 50.52 seconds after the 19th hour of April 12th, 1985 with no offset information. Without offset information, some rich features may not be available.
 * @member {String} purchaseDateTime
 */
PurchaseDetails.prototype['purchaseDateTime'] = undefined;

/**
 * Receipt number/identifier for tracking the ticket purchase via the body that sold the ticket.
 * @member {String} purchaseReceiptNumber
 */
PurchaseDetails.prototype['purchaseReceiptNumber'] = undefined;

/**
 * @member {module:model/TicketCost} ticketCost
 */
PurchaseDetails.prototype['ticketCost'] = undefined;






export default PurchaseDetails;

