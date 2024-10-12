/**
 * Velo Payments APIs
 * ## Terms and Definitions  Throughout this document and the Velo platform the following terms are used:  * **Payor.** An entity (typically a corporation) which wishes to pay funds to one or more payees via a payout. * **Payee.** The recipient of funds paid out by a payor. * **Payment.** A single transfer of funds from a payor to a payee. * **Payout.** A batch of Payments, typically used by a payor to logically group payments (e.g. by business day). Technically there need be no relationship between the payments in a payout - a single payout can contain payments to multiple payees and/or multiple payments to a single payee. * **Sandbox.** An integration environment provided by Velo Payments which offers a similar API experience to the production environment, but all funding and payment events are simulated, along with many other services such as OFAC sanctions list checking.  ## Overview  The Velo Payments API allows a payor to perform a number of operations. The following is a list of the main capabilities in a natural order of execution:  * Authenticate with the Velo platform * Maintain a collection of payees * Query the payor’s current balance of funds within the platform and perform additional funding * Issue payments to payees * Query the platform for a history of those payments  This document describes the main concepts and APIs required to get up and running with the Velo Payments platform. It is not an exhaustive API reference. For that, please see the separate Velo Payments API Reference.  ## API Considerations  The Velo Payments API is REST based and uses the JSON format for requests and responses.  Most calls are secured using OAuth 2 security and require a valid authentication access token for successful operation. See the Authentication section for details.  Where a dynamic value is required in the examples below, the {token} format is used, suggesting that the caller needs to supply the appropriate value of the token in question (without including the { or } characters).  Where curl examples are given, the –d @filename.json approach is used, indicating that the request body should be placed into a file named filename.json in the current directory. Each of the curl examples in this document should be considered a single line on the command-line, regardless of how they appear in print.  ## Authenticating with the Velo Platform  Once Velo backoffice staff have added your organization as a payor within the Velo platform sandbox, they will create you a payor Id, an API key and an API secret and share these with you in a secure manner.  You will need to use these values to authenticate with the Velo platform in order to gain access to the APIs. The steps to take are explained in the following:  create a string comprising the API key (e.g. 44a9537d-d55d-4b47-8082-14061c2bcdd8) and API secret (e.g. c396b26b-137a-44fd-87f5-34631f8fd529) with a colon between them. E.g. 44a9537d-d55d-4b47-8082-14061c2bcdd8:c396b26b-137a-44fd-87f5-34631f8fd529  base64 encode this string. E.g.: NDRhOTUzN2QtZDU1ZC00YjQ3LTgwODItMTQwNjFjMmJjZGQ4OmMzOTZiMjZiLTEzN2EtNDRmZC04N2Y1LTM0NjMxZjhmZDUyOQ==  create an HTTP **Authorization** header with the value set to e.g. Basic NDRhOTUzN2QtZDU1ZC00YjQ3LTgwODItMTQwNjFjMmJjZGQ4OmMzOTZiMjZiLTEzN2EtNDRmZC04N2Y1LTM0NjMxZjhmZDUyOQ==  perform the Velo authentication REST call using the HTTP header created above e.g. via curl:  ```   curl -X POST \\   -H \"Content-Type: application/json\" \\   -H \"Authorization: Basic NDRhOTUzN2QtZDU1ZC00YjQ3LTgwODItMTQwNjFjMmJjZGQ4OmMzOTZiMjZiLTEzN2EtNDRmZC04N2Y1LTM0NjMxZjhmZDUyOQ==\" \\   'https://api.sandbox.velopayments.com/v1/authenticate?grant_type=client_credentials' ```  If successful, this call will result in a **200** HTTP status code and a response body such as:  ```   {     \"access_token\":\"19f6bafd-93fd-4747-b229-00507bbc991f\",     \"token_type\":\"bearer\",     \"expires_in\":1799,     \"scope\":\"...\"   } ``` ## API access following authentication Following successful authentication, the value of the access_token field in the response (indicated in green above) should then be presented with all subsequent API calls to allow the Velo platform to validate that the caller is authenticated.  This is achieved by setting the HTTP Authorization header with the value set to e.g. Bearer 19f6bafd-93fd-4747-b229-00507bbc991f such as the curl example below:  ```   -H \"Authorization: Bearer 19f6bafd-93fd-4747-b229-00507bbc991f \" ```  If you make other Velo API calls which require authorization but the Authorization header is missing or invalid then you will get a **401** HTTP status response. 
 *
 * The version of the OpenAPI document: 2.35.57
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';

/**
 * The PayeeUserSelfUpdateRequest model module.
 * @module model/PayeeUserSelfUpdateRequest
 * @version 2.35.57
 */
class PayeeUserSelfUpdateRequest {
    /**
     * Constructs a new <code>PayeeUserSelfUpdateRequest</code>.
     * &lt;p&gt;All properties are optional&lt;/p&gt; &lt;p&gt;Only provided properties will be updated&lt;/p&gt; &lt;p&gt;Use null to null out a property that is allowed to be nullable&lt;/p&gt; 
     * @alias module:model/PayeeUserSelfUpdateRequest
     */
    constructor() { 
        
        PayeeUserSelfUpdateRequest.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>PayeeUserSelfUpdateRequest</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/PayeeUserSelfUpdateRequest} obj Optional instance to populate.
     * @return {module:model/PayeeUserSelfUpdateRequest} The populated <code>PayeeUserSelfUpdateRequest</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new PayeeUserSelfUpdateRequest();

            if (data.hasOwnProperty('email')) {
                obj['email'] = ApiClient.convertToType(data['email'], 'String');
            }
            if (data.hasOwnProperty('firstName')) {
                obj['firstName'] = ApiClient.convertToType(data['firstName'], 'String');
            }
            if (data.hasOwnProperty('lastName')) {
                obj['lastName'] = ApiClient.convertToType(data['lastName'], 'String');
            }
            if (data.hasOwnProperty('primaryContactNumber')) {
                obj['primaryContactNumber'] = ApiClient.convertToType(data['primaryContactNumber'], 'String');
            }
            if (data.hasOwnProperty('secondaryContactNumber')) {
                obj['secondaryContactNumber'] = ApiClient.convertToType(data['secondaryContactNumber'], 'String');
            }
            if (data.hasOwnProperty('smsNumber')) {
                obj['smsNumber'] = ApiClient.convertToType(data['smsNumber'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>PayeeUserSelfUpdateRequest</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>PayeeUserSelfUpdateRequest</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['email'] && !(typeof data['email'] === 'string' || data['email'] instanceof String)) {
            throw new Error("Expected the field `email` to be a primitive type in the JSON string but got " + data['email']);
        }
        // ensure the json data is a string
        if (data['firstName'] && !(typeof data['firstName'] === 'string' || data['firstName'] instanceof String)) {
            throw new Error("Expected the field `firstName` to be a primitive type in the JSON string but got " + data['firstName']);
        }
        // ensure the json data is a string
        if (data['lastName'] && !(typeof data['lastName'] === 'string' || data['lastName'] instanceof String)) {
            throw new Error("Expected the field `lastName` to be a primitive type in the JSON string but got " + data['lastName']);
        }
        // ensure the json data is a string
        if (data['primaryContactNumber'] && !(typeof data['primaryContactNumber'] === 'string' || data['primaryContactNumber'] instanceof String)) {
            throw new Error("Expected the field `primaryContactNumber` to be a primitive type in the JSON string but got " + data['primaryContactNumber']);
        }
        // ensure the json data is a string
        if (data['secondaryContactNumber'] && !(typeof data['secondaryContactNumber'] === 'string' || data['secondaryContactNumber'] instanceof String)) {
            throw new Error("Expected the field `secondaryContactNumber` to be a primitive type in the JSON string but got " + data['secondaryContactNumber']);
        }
        // ensure the json data is a string
        if (data['smsNumber'] && !(typeof data['smsNumber'] === 'string' || data['smsNumber'] instanceof String)) {
            throw new Error("Expected the field `smsNumber` to be a primitive type in the JSON string but got " + data['smsNumber']);
        }

        return true;
    }


}



/**
 * the email address of the user
 * @member {String} email
 */
PayeeUserSelfUpdateRequest.prototype['email'] = undefined;

/**
 * @member {String} firstName
 */
PayeeUserSelfUpdateRequest.prototype['firstName'] = undefined;

/**
 * @member {String} lastName
 */
PayeeUserSelfUpdateRequest.prototype['lastName'] = undefined;

/**
 * The main contact number for the user 
 * @member {String} primaryContactNumber
 */
PayeeUserSelfUpdateRequest.prototype['primaryContactNumber'] = undefined;

/**
 * The secondary contact number for the user 
 * @member {String} secondaryContactNumber
 */
PayeeUserSelfUpdateRequest.prototype['secondaryContactNumber'] = undefined;

/**
 * The phone number of a device that the user can receive sms messages on 
 * @member {String} smsNumber
 */
PayeeUserSelfUpdateRequest.prototype['smsNumber'] = undefined;






export default PayeeUserSelfUpdateRequest;

