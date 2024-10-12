/**
 * Avaza API Documentation
 * Welcome to the autogenerated documentation & test tool for Avaza's API. <br/><br/><strong>API Security & Authentication</strong><br/>Authentication options include OAuth2 Implicit and Authorization Code flows, and Personal Access Token. All connections should be encrypted over SSL/TLS <br/><br/>You can set up and manage your api authentication credentials from within your Avaza account. (requires Administrator permissions on your Avaza account).<br/><br/> OAuth2 Authorization endpoint: https://any.avaza.com/oauth2/authorize  <br/>OAuth2 Token endpoint: https://any.avaza.com/oauth2/token<br/>Base URL for subsequent API Requests: https://api.avaza.com/ <br/><br/>Blogpost about authenticating with Avaza's API:  https://www.avaza.com/avaza-api-oauth2-authentication/ <br/>Blogpost on using Avaza's webhooks: https://www.avaza.com/avaza-api-webhook-notifications/<br/>The OAuth flow currently issues Access Tokens that last 1 day, and Refresh tokens that last 180 days<br/>The Api respects the security Roles assigned to the authenticating Avaza user and filters the data return appropriately. <br/><br><strong>Support</strong><br/>For API Support, and to request access please contact Avaza Support Team via our support chat. <br/><br/><strong>User Contributed Libraries:</strong><br/>Graciously contributed by 3rd party users like you. <br/>Note these are not tested or endorsesd by Avaza. We encourage you to review before use, and use at own risk.<br/> <ul><li> - <a target='blank' href='https://packagist.org/packages/debiprasad/oauth2-avaza'>PHP OAuth Client Package for Azava API (by Debiprasad Sahoo)</a></li></ul>
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

/**
 * The TimesheetListDetails model module.
 * @module model/TimesheetListDetails
 * @version v1
 */
class TimesheetListDetails {
    /**
     * Constructs a new <code>TimesheetListDetails</code>.
     * @alias module:model/TimesheetListDetails
     */
    constructor() { 
        
        TimesheetListDetails.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>TimesheetListDetails</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/TimesheetListDetails} obj Optional instance to populate.
     * @return {module:model/TimesheetListDetails} The populated <code>TimesheetListDetails</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new TimesheetListDetails();

            if (data.hasOwnProperty('ApprovedBy')) {
                obj['ApprovedBy'] = ApiClient.convertToType(data['ApprovedBy'], 'String');
            }
            if (data.hasOwnProperty('CategoryName')) {
                obj['CategoryName'] = ApiClient.convertToType(data['CategoryName'], 'String');
            }
            if (data.hasOwnProperty('CustomMetadata')) {
                obj['CustomMetadata'] = ApiClient.convertToType(data['CustomMetadata'], 'String');
            }
            if (data.hasOwnProperty('CustomerIDFK')) {
                obj['CustomerIDFK'] = ApiClient.convertToType(data['CustomerIDFK'], 'Number');
            }
            if (data.hasOwnProperty('CustomerName')) {
                obj['CustomerName'] = ApiClient.convertToType(data['CustomerName'], 'String');
            }
            if (data.hasOwnProperty('DateApproved')) {
                obj['DateApproved'] = ApiClient.convertToType(data['DateApproved'], 'Date');
            }
            if (data.hasOwnProperty('DateCreated')) {
                obj['DateCreated'] = ApiClient.convertToType(data['DateCreated'], 'Date');
            }
            if (data.hasOwnProperty('DateUpdated')) {
                obj['DateUpdated'] = ApiClient.convertToType(data['DateUpdated'], 'Date');
            }
            if (data.hasOwnProperty('Duration')) {
                obj['Duration'] = ApiClient.convertToType(data['Duration'], 'Number');
            }
            if (data.hasOwnProperty('Email')) {
                obj['Email'] = ApiClient.convertToType(data['Email'], 'String');
            }
            if (data.hasOwnProperty('EndTimeLocal')) {
                obj['EndTimeLocal'] = ApiClient.convertToType(data['EndTimeLocal'], 'Date');
            }
            if (data.hasOwnProperty('EndTimeUTC')) {
                obj['EndTimeUTC'] = ApiClient.convertToType(data['EndTimeUTC'], 'Date');
            }
            if (data.hasOwnProperty('EntryDate')) {
                obj['EntryDate'] = ApiClient.convertToType(data['EntryDate'], 'Date');
            }
            if (data.hasOwnProperty('Firstname')) {
                obj['Firstname'] = ApiClient.convertToType(data['Firstname'], 'String');
            }
            if (data.hasOwnProperty('HasTimer')) {
                obj['HasTimer'] = ApiClient.convertToType(data['HasTimer'], 'Boolean');
            }
            if (data.hasOwnProperty('InvoiceIDFK')) {
                obj['InvoiceIDFK'] = ApiClient.convertToType(data['InvoiceIDFK'], 'Number');
            }
            if (data.hasOwnProperty('InvoiceLineItemIDFK')) {
                obj['InvoiceLineItemIDFK'] = ApiClient.convertToType(data['InvoiceLineItemIDFK'], 'Number');
            }
            if (data.hasOwnProperty('Lastname')) {
                obj['Lastname'] = ApiClient.convertToType(data['Lastname'], 'String');
            }
            if (data.hasOwnProperty('Notes')) {
                obj['Notes'] = ApiClient.convertToType(data['Notes'], 'String');
            }
            if (data.hasOwnProperty('ProjectCode')) {
                obj['ProjectCode'] = ApiClient.convertToType(data['ProjectCode'], 'String');
            }
            if (data.hasOwnProperty('ProjectIDFK')) {
                obj['ProjectIDFK'] = ApiClient.convertToType(data['ProjectIDFK'], 'Number');
            }
            if (data.hasOwnProperty('ProjectTitle')) {
                obj['ProjectTitle'] = ApiClient.convertToType(data['ProjectTitle'], 'String');
            }
            if (data.hasOwnProperty('StartTimeLocal')) {
                obj['StartTimeLocal'] = ApiClient.convertToType(data['StartTimeLocal'], 'Date');
            }
            if (data.hasOwnProperty('StartTimeUTC')) {
                obj['StartTimeUTC'] = ApiClient.convertToType(data['StartTimeUTC'], 'Date');
            }
            if (data.hasOwnProperty('TaskIDFK')) {
                obj['TaskIDFK'] = ApiClient.convertToType(data['TaskIDFK'], 'Number');
            }
            if (data.hasOwnProperty('TaskTitle')) {
                obj['TaskTitle'] = ApiClient.convertToType(data['TaskTitle'], 'String');
            }
            if (data.hasOwnProperty('TimerStartedAtUTC')) {
                obj['TimerStartedAtUTC'] = ApiClient.convertToType(data['TimerStartedAtUTC'], 'Date');
            }
            if (data.hasOwnProperty('TimesheetCategoryIDFK')) {
                obj['TimesheetCategoryIDFK'] = ApiClient.convertToType(data['TimesheetCategoryIDFK'], 'Number');
            }
            if (data.hasOwnProperty('TimesheetEntryApprovalStatusCode')) {
                obj['TimesheetEntryApprovalStatusCode'] = ApiClient.convertToType(data['TimesheetEntryApprovalStatusCode'], 'String');
            }
            if (data.hasOwnProperty('TimesheetEntryID')) {
                obj['TimesheetEntryID'] = ApiClient.convertToType(data['TimesheetEntryID'], 'Number');
            }
            if (data.hasOwnProperty('TimesheetUserTimeZone')) {
                obj['TimesheetUserTimeZone'] = ApiClient.convertToType(data['TimesheetUserTimeZone'], 'String');
            }
            if (data.hasOwnProperty('UserIDFK')) {
                obj['UserIDFK'] = ApiClient.convertToType(data['UserIDFK'], 'Number');
            }
            if (data.hasOwnProperty('isBillable')) {
                obj['isBillable'] = ApiClient.convertToType(data['isBillable'], 'Boolean');
            }
            if (data.hasOwnProperty('isInvoiced')) {
                obj['isInvoiced'] = ApiClient.convertToType(data['isInvoiced'], 'Boolean');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>TimesheetListDetails</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>TimesheetListDetails</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['ApprovedBy'] && !(typeof data['ApprovedBy'] === 'string' || data['ApprovedBy'] instanceof String)) {
            throw new Error("Expected the field `ApprovedBy` to be a primitive type in the JSON string but got " + data['ApprovedBy']);
        }
        // ensure the json data is a string
        if (data['CategoryName'] && !(typeof data['CategoryName'] === 'string' || data['CategoryName'] instanceof String)) {
            throw new Error("Expected the field `CategoryName` to be a primitive type in the JSON string but got " + data['CategoryName']);
        }
        // ensure the json data is a string
        if (data['CustomMetadata'] && !(typeof data['CustomMetadata'] === 'string' || data['CustomMetadata'] instanceof String)) {
            throw new Error("Expected the field `CustomMetadata` to be a primitive type in the JSON string but got " + data['CustomMetadata']);
        }
        // ensure the json data is a string
        if (data['CustomerName'] && !(typeof data['CustomerName'] === 'string' || data['CustomerName'] instanceof String)) {
            throw new Error("Expected the field `CustomerName` to be a primitive type in the JSON string but got " + data['CustomerName']);
        }
        // ensure the json data is a string
        if (data['Email'] && !(typeof data['Email'] === 'string' || data['Email'] instanceof String)) {
            throw new Error("Expected the field `Email` to be a primitive type in the JSON string but got " + data['Email']);
        }
        // ensure the json data is a string
        if (data['Firstname'] && !(typeof data['Firstname'] === 'string' || data['Firstname'] instanceof String)) {
            throw new Error("Expected the field `Firstname` to be a primitive type in the JSON string but got " + data['Firstname']);
        }
        // ensure the json data is a string
        if (data['Lastname'] && !(typeof data['Lastname'] === 'string' || data['Lastname'] instanceof String)) {
            throw new Error("Expected the field `Lastname` to be a primitive type in the JSON string but got " + data['Lastname']);
        }
        // ensure the json data is a string
        if (data['Notes'] && !(typeof data['Notes'] === 'string' || data['Notes'] instanceof String)) {
            throw new Error("Expected the field `Notes` to be a primitive type in the JSON string but got " + data['Notes']);
        }
        // ensure the json data is a string
        if (data['ProjectCode'] && !(typeof data['ProjectCode'] === 'string' || data['ProjectCode'] instanceof String)) {
            throw new Error("Expected the field `ProjectCode` to be a primitive type in the JSON string but got " + data['ProjectCode']);
        }
        // ensure the json data is a string
        if (data['ProjectTitle'] && !(typeof data['ProjectTitle'] === 'string' || data['ProjectTitle'] instanceof String)) {
            throw new Error("Expected the field `ProjectTitle` to be a primitive type in the JSON string but got " + data['ProjectTitle']);
        }
        // ensure the json data is a string
        if (data['TaskTitle'] && !(typeof data['TaskTitle'] === 'string' || data['TaskTitle'] instanceof String)) {
            throw new Error("Expected the field `TaskTitle` to be a primitive type in the JSON string but got " + data['TaskTitle']);
        }
        // ensure the json data is a string
        if (data['TimesheetEntryApprovalStatusCode'] && !(typeof data['TimesheetEntryApprovalStatusCode'] === 'string' || data['TimesheetEntryApprovalStatusCode'] instanceof String)) {
            throw new Error("Expected the field `TimesheetEntryApprovalStatusCode` to be a primitive type in the JSON string but got " + data['TimesheetEntryApprovalStatusCode']);
        }
        // ensure the json data is a string
        if (data['TimesheetUserTimeZone'] && !(typeof data['TimesheetUserTimeZone'] === 'string' || data['TimesheetUserTimeZone'] instanceof String)) {
            throw new Error("Expected the field `TimesheetUserTimeZone` to be a primitive type in the JSON string but got " + data['TimesheetUserTimeZone']);
        }

        return true;
    }


}



/**
 * @member {String} ApprovedBy
 */
TimesheetListDetails.prototype['ApprovedBy'] = undefined;

/**
 * @member {String} CategoryName
 */
TimesheetListDetails.prototype['CategoryName'] = undefined;

/**
 * @member {String} CustomMetadata
 */
TimesheetListDetails.prototype['CustomMetadata'] = undefined;

/**
 * @member {Number} CustomerIDFK
 */
TimesheetListDetails.prototype['CustomerIDFK'] = undefined;

/**
 * @member {String} CustomerName
 */
TimesheetListDetails.prototype['CustomerName'] = undefined;

/**
 * @member {Date} DateApproved
 */
TimesheetListDetails.prototype['DateApproved'] = undefined;

/**
 * @member {Date} DateCreated
 */
TimesheetListDetails.prototype['DateCreated'] = undefined;

/**
 * @member {Date} DateUpdated
 */
TimesheetListDetails.prototype['DateUpdated'] = undefined;

/**
 * @member {Number} Duration
 */
TimesheetListDetails.prototype['Duration'] = undefined;

/**
 * @member {String} Email
 */
TimesheetListDetails.prototype['Email'] = undefined;

/**
 * @member {Date} EndTimeLocal
 */
TimesheetListDetails.prototype['EndTimeLocal'] = undefined;

/**
 * @member {Date} EndTimeUTC
 */
TimesheetListDetails.prototype['EndTimeUTC'] = undefined;

/**
 * @member {Date} EntryDate
 */
TimesheetListDetails.prototype['EntryDate'] = undefined;

/**
 * @member {String} Firstname
 */
TimesheetListDetails.prototype['Firstname'] = undefined;

/**
 * @member {Boolean} HasTimer
 */
TimesheetListDetails.prototype['HasTimer'] = undefined;

/**
 * This InvoiceIDFK is only included when the api get parameter includeInvoiceDetails==true
 * @member {Number} InvoiceIDFK
 */
TimesheetListDetails.prototype['InvoiceIDFK'] = undefined;

/**
 * @member {Number} InvoiceLineItemIDFK
 */
TimesheetListDetails.prototype['InvoiceLineItemIDFK'] = undefined;

/**
 * @member {String} Lastname
 */
TimesheetListDetails.prototype['Lastname'] = undefined;

/**
 * @member {String} Notes
 */
TimesheetListDetails.prototype['Notes'] = undefined;

/**
 * @member {String} ProjectCode
 */
TimesheetListDetails.prototype['ProjectCode'] = undefined;

/**
 * @member {Number} ProjectIDFK
 */
TimesheetListDetails.prototype['ProjectIDFK'] = undefined;

/**
 * @member {String} ProjectTitle
 */
TimesheetListDetails.prototype['ProjectTitle'] = undefined;

/**
 * @member {Date} StartTimeLocal
 */
TimesheetListDetails.prototype['StartTimeLocal'] = undefined;

/**
 * @member {Date} StartTimeUTC
 */
TimesheetListDetails.prototype['StartTimeUTC'] = undefined;

/**
 * @member {Number} TaskIDFK
 */
TimesheetListDetails.prototype['TaskIDFK'] = undefined;

/**
 * @member {String} TaskTitle
 */
TimesheetListDetails.prototype['TaskTitle'] = undefined;

/**
 * @member {Date} TimerStartedAtUTC
 */
TimesheetListDetails.prototype['TimerStartedAtUTC'] = undefined;

/**
 * @member {Number} TimesheetCategoryIDFK
 */
TimesheetListDetails.prototype['TimesheetCategoryIDFK'] = undefined;

/**
 * @member {String} TimesheetEntryApprovalStatusCode
 */
TimesheetListDetails.prototype['TimesheetEntryApprovalStatusCode'] = undefined;

/**
 * @member {Number} TimesheetEntryID
 */
TimesheetListDetails.prototype['TimesheetEntryID'] = undefined;

/**
 * @member {String} TimesheetUserTimeZone
 */
TimesheetListDetails.prototype['TimesheetUserTimeZone'] = undefined;

/**
 * @member {Number} UserIDFK
 */
TimesheetListDetails.prototype['UserIDFK'] = undefined;

/**
 * @member {Boolean} isBillable
 */
TimesheetListDetails.prototype['isBillable'] = undefined;

/**
 * @member {Boolean} isInvoiced
 */
TimesheetListDetails.prototype['isInvoiced'] = undefined;






export default TimesheetListDetails;

