/**
 * API v1.0.0
 * [![Run in Postman](https://run.pstmn.io/button.svg)](https://app.getpostman.com/run-collection/80638214aa04722c9203)  <span style='margin-left: 0.5em;'>or</span>  <a href='https://documenter.getpostman.com/view/3559821/TVeqcn2L' class='openapi-button' _ngcontent-c6>View Postman docs</a>    # Quickstart    Visit [github](https://github.com/EmitKnowledge/Envoice) to view the quickstart tutorial.    <div class='postman-tutorial'>    # Tutorial for running the API in postman    Click on \"\"Run in Postman\"\" button  <br /><br />  ![postman - tutorial - 1](/Assets/images/api/postman-tutorial/postman-tutorial-1.png)     ---     A new page will open.  Click the \"\"Postman for windows\"\" to run postman as a desktop app.  Make sure you have already [installed](https://www.getpostman.com/docs/postman/launching_postman/installation_and_updates) Postman.  <br /><br />  ![postman - tutorial - 2](/Assets/images/api/postman-tutorial/postman-tutorial-2.png)     ---     In chrome an alert might show up to set a default app for opening postman links. Click on \"\"Open Postman\"\".  <br /><br />  ![postman - tutorial - 3](/Assets/images/api/postman-tutorial/postman-tutorial-3.png)     ---     The OpenAPI specification will be imported in Postman as a new collection named \"\"Envoice api\"\"  <br /><br />  ![postman - tutorial - 4](/Assets/images/api/postman-tutorial/postman-tutorial-4.png)     ---     When testing be sure to check and modify the environment variables to suit your api key and secret. The domain is set to envoice's endpoint so you don't really need to change that.    <sub>\\*Eye button in top right corner </sub>  <br /><br />   ![postman - tutorial - 5](/Assets/images/api/postman-tutorial/postman-tutorial-5.png)  <br /><br />   ![postman - tutorial - 6](/Assets/images/api/postman-tutorial/postman-tutorial-6.png)     ---     You don't need to change the values of the header parameters, because they will be replaced automatically when you send a request with real values from the environment configured in the previous step.  <br /><br />  ![postman - tutorial - 7](/Assets/images/api/postman-tutorial/postman-tutorial-7.png)     ---     Modify the example data to suit your needs and send a request.  <br /><br />  ![postman - tutorial - 8](/Assets/images/api/postman-tutorial/postman-tutorial-8.png)  </div>    # Webhooks    Webhooks allow you to build or set up Envoice Apps which subscribe to invoice activities.   When one of those events is triggered, we'll send a HTTP POST payload to the webhook's configured URL.   Webhooks can be used to update an external invoice data storage.    In order to use webhooks visit [this link](/account/settings#api-tab) and add upto 10 webhook urls that will return status `200` in order to signal that the webhook is working.  All nonworking webhooks will be ignored after a certain period of time and several retry attempts.  If after several attempts the webhook starts to work, we will send you all activities, both past and present, in chronological order.    The payload of the webhook is in format:  ```  {      Signature: \"\"sha256 string\"\",      Timestamp: \"\"YYYY-MM-DDTHH:mm:ss.FFFFFFFZ\"\",      Activity: {          Message: \"string\",          Link: \"share url\",          Type: int,                  InvoiceNumber: \"string\",          InvoiceId: int,                  OrderNumber: \"string\",          OrderId: int,          Id: int,          CreatedOn: \"YYYY-MM-DDTHH:mm:ss.FFFFFFFZ\"      }  }  ```            
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
import ExternalConnection from './ExternalConnection';
import SubscriptionPlan from './SubscriptionPlan';
import UserSettings from './UserSettings';

/**
 * The User model module.
 * @module model/User
 * @version v1
 */
class User {
    /**
     * Constructs a new <code>User</code>.
     * @alias module:model/User
     */
    constructor() { 
        
        User.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>User</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/User} obj Optional instance to populate.
     * @return {module:model/User} The populated <code>User</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new User();

            if (data.hasOwnProperty('ActionNotificationsLastReadOn')) {
                obj['ActionNotificationsLastReadOn'] = ApiClient.convertToType(data['ActionNotificationsLastReadOn'], 'Date');
            }
            if (data.hasOwnProperty('Email')) {
                obj['Email'] = ApiClient.convertToType(data['Email'], 'String');
            }
            if (data.hasOwnProperty('ExternalConnections')) {
                obj['ExternalConnections'] = ApiClient.convertToType(data['ExternalConnections'], [ExternalConnection]);
            }
            if (data.hasOwnProperty('HasBeenOnboarded')) {
                obj['HasBeenOnboarded'] = ApiClient.convertToType(data['HasBeenOnboarded'], 'Boolean');
            }
            if (data.hasOwnProperty('Id')) {
                obj['Id'] = ApiClient.convertToType(data['Id'], 'Number');
            }
            if (data.hasOwnProperty('IsLocked')) {
                obj['IsLocked'] = ApiClient.convertToType(data['IsLocked'], 'Boolean');
            }
            if (data.hasOwnProperty('IsVerified')) {
                obj['IsVerified'] = ApiClient.convertToType(data['IsVerified'], 'Boolean');
            }
            if (data.hasOwnProperty('KnowledgeNotificationsLastReadOn')) {
                obj['KnowledgeNotificationsLastReadOn'] = ApiClient.convertToType(data['KnowledgeNotificationsLastReadOn'], 'Date');
            }
            if (data.hasOwnProperty('LastSeenOn')) {
                obj['LastSeenOn'] = ApiClient.convertToType(data['LastSeenOn'], 'Date');
            }
            if (data.hasOwnProperty('Name')) {
                obj['Name'] = ApiClient.convertToType(data['Name'], 'String');
            }
            if (data.hasOwnProperty('Password')) {
                obj['Password'] = ApiClient.convertToType(data['Password'], 'String');
            }
            if (data.hasOwnProperty('PasswordSalt')) {
                obj['PasswordSalt'] = ApiClient.convertToType(data['PasswordSalt'], 'String');
            }
            if (data.hasOwnProperty('ReferralPath')) {
                obj['ReferralPath'] = ApiClient.convertToType(data['ReferralPath'], 'String');
            }
            if (data.hasOwnProperty('ReferredUsers')) {
                obj['ReferredUsers'] = ApiClient.convertToType(data['ReferredUsers'], 'Number');
            }
            if (data.hasOwnProperty('ReferrerKey')) {
                obj['ReferrerKey'] = ApiClient.convertToType(data['ReferrerKey'], 'String');
            }
            if (data.hasOwnProperty('Settings')) {
                obj['Settings'] = UserSettings.constructFromObject(data['Settings']);
            }
            if (data.hasOwnProperty('Status')) {
                obj['Status'] = ApiClient.convertToType(data['Status'], 'String');
            }
            if (data.hasOwnProperty('SubscriptionPlan')) {
                obj['SubscriptionPlan'] = SubscriptionPlan.constructFromObject(data['SubscriptionPlan']);
            }
            if (data.hasOwnProperty('Type')) {
                obj['Type'] = ApiClient.convertToType(data['Type'], 'String');
            }
            if (data.hasOwnProperty('Username')) {
                obj['Username'] = ApiClient.convertToType(data['Username'], 'String');
            }
            if (data.hasOwnProperty('VerifiedOn')) {
                obj['VerifiedOn'] = ApiClient.convertToType(data['VerifiedOn'], 'Date');
            }
            if (data.hasOwnProperty('YearsOfExperience')) {
                obj['YearsOfExperience'] = ApiClient.convertToType(data['YearsOfExperience'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>User</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>User</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['Email'] && !(typeof data['Email'] === 'string' || data['Email'] instanceof String)) {
            throw new Error("Expected the field `Email` to be a primitive type in the JSON string but got " + data['Email']);
        }
        if (data['ExternalConnections']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['ExternalConnections'])) {
                throw new Error("Expected the field `ExternalConnections` to be an array in the JSON data but got " + data['ExternalConnections']);
            }
            // validate the optional field `ExternalConnections` (array)
            for (const item of data['ExternalConnections']) {
                ExternalConnection.validateJSON(item);
            };
        }
        // ensure the json data is a string
        if (data['Name'] && !(typeof data['Name'] === 'string' || data['Name'] instanceof String)) {
            throw new Error("Expected the field `Name` to be a primitive type in the JSON string but got " + data['Name']);
        }
        // ensure the json data is a string
        if (data['Password'] && !(typeof data['Password'] === 'string' || data['Password'] instanceof String)) {
            throw new Error("Expected the field `Password` to be a primitive type in the JSON string but got " + data['Password']);
        }
        // ensure the json data is a string
        if (data['PasswordSalt'] && !(typeof data['PasswordSalt'] === 'string' || data['PasswordSalt'] instanceof String)) {
            throw new Error("Expected the field `PasswordSalt` to be a primitive type in the JSON string but got " + data['PasswordSalt']);
        }
        // ensure the json data is a string
        if (data['ReferralPath'] && !(typeof data['ReferralPath'] === 'string' || data['ReferralPath'] instanceof String)) {
            throw new Error("Expected the field `ReferralPath` to be a primitive type in the JSON string but got " + data['ReferralPath']);
        }
        // ensure the json data is a string
        if (data['ReferrerKey'] && !(typeof data['ReferrerKey'] === 'string' || data['ReferrerKey'] instanceof String)) {
            throw new Error("Expected the field `ReferrerKey` to be a primitive type in the JSON string but got " + data['ReferrerKey']);
        }
        // validate the optional field `Settings`
        if (data['Settings']) { // data not null
          UserSettings.validateJSON(data['Settings']);
        }
        // ensure the json data is a string
        if (data['Status'] && !(typeof data['Status'] === 'string' || data['Status'] instanceof String)) {
            throw new Error("Expected the field `Status` to be a primitive type in the JSON string but got " + data['Status']);
        }
        // validate the optional field `SubscriptionPlan`
        if (data['SubscriptionPlan']) { // data not null
          SubscriptionPlan.validateJSON(data['SubscriptionPlan']);
        }
        // ensure the json data is a string
        if (data['Type'] && !(typeof data['Type'] === 'string' || data['Type'] instanceof String)) {
            throw new Error("Expected the field `Type` to be a primitive type in the JSON string but got " + data['Type']);
        }
        // ensure the json data is a string
        if (data['Username'] && !(typeof data['Username'] === 'string' || data['Username'] instanceof String)) {
            throw new Error("Expected the field `Username` to be a primitive type in the JSON string but got " + data['Username']);
        }
        // ensure the json data is a string
        if (data['YearsOfExperience'] && !(typeof data['YearsOfExperience'] === 'string' || data['YearsOfExperience'] instanceof String)) {
            throw new Error("Expected the field `YearsOfExperience` to be a primitive type in the JSON string but got " + data['YearsOfExperience']);
        }

        return true;
    }


}



/**
 * @member {Date} ActionNotificationsLastReadOn
 */
User.prototype['ActionNotificationsLastReadOn'] = undefined;

/**
 * @member {String} Email
 */
User.prototype['Email'] = undefined;

/**
 * @member {Array.<module:model/ExternalConnection>} ExternalConnections
 */
User.prototype['ExternalConnections'] = undefined;

/**
 * @member {Boolean} HasBeenOnboarded
 */
User.prototype['HasBeenOnboarded'] = undefined;

/**
 * @member {Number} Id
 */
User.prototype['Id'] = undefined;

/**
 * @member {Boolean} IsLocked
 */
User.prototype['IsLocked'] = undefined;

/**
 * @member {Boolean} IsVerified
 */
User.prototype['IsVerified'] = undefined;

/**
 * @member {Date} KnowledgeNotificationsLastReadOn
 */
User.prototype['KnowledgeNotificationsLastReadOn'] = undefined;

/**
 * @member {Date} LastSeenOn
 */
User.prototype['LastSeenOn'] = undefined;

/**
 * @member {String} Name
 */
User.prototype['Name'] = undefined;

/**
 * @member {String} Password
 */
User.prototype['Password'] = undefined;

/**
 * @member {String} PasswordSalt
 */
User.prototype['PasswordSalt'] = undefined;

/**
 * @member {String} ReferralPath
 */
User.prototype['ReferralPath'] = undefined;

/**
 * @member {Number} ReferredUsers
 */
User.prototype['ReferredUsers'] = undefined;

/**
 * @member {String} ReferrerKey
 */
User.prototype['ReferrerKey'] = undefined;

/**
 * @member {module:model/UserSettings} Settings
 */
User.prototype['Settings'] = undefined;

/**
 * @member {module:model/User.StatusEnum} Status
 */
User.prototype['Status'] = undefined;

/**
 * @member {module:model/SubscriptionPlan} SubscriptionPlan
 */
User.prototype['SubscriptionPlan'] = undefined;

/**
 * @member {module:model/User.TypeEnum} Type
 */
User.prototype['Type'] = undefined;

/**
 * @member {String} Username
 */
User.prototype['Username'] = undefined;

/**
 * @member {Date} VerifiedOn
 */
User.prototype['VerifiedOn'] = undefined;

/**
 * @member {module:model/User.YearsOfExperienceEnum} YearsOfExperience
 */
User.prototype['YearsOfExperience'] = undefined;





/**
 * Allowed values for the <code>Status</code> property.
 * @enum {String}
 * @readonly
 */
User['StatusEnum'] = {

    /**
     * value: "Normal"
     * @const
     */
    "Normal": "Normal",

    /**
     * value: "Fraudlent"
     * @const
     */
    "Fraudlent": "Fraudlent",

    /**
     * value: "Locked"
     * @const
     */
    "Locked": "Locked"
};


/**
 * Allowed values for the <code>Type</code> property.
 * @enum {String}
 * @readonly
 */
User['TypeEnum'] = {

    /**
     * value: "Anonymous"
     * @const
     */
    "Anonymous": "Anonymous",

    /**
     * value: "Customer"
     * @const
     */
    "Customer": "Customer",

    /**
     * value: "SystemAdministrator"
     * @const
     */
    "SystemAdministrator": "SystemAdministrator",

    /**
     * value: "Collaborator"
     * @const
     */
    "Collaborator": "Collaborator"
};


/**
 * Allowed values for the <code>YearsOfExperience</code> property.
 * @enum {String}
 * @readonly
 */
User['YearsOfExperienceEnum'] = {

    /**
     * value: "One"
     * @const
     */
    "One": "One",

    /**
     * value: "OneToThree"
     * @const
     */
    "OneToThree": "OneToThree",

    /**
     * value: "ThreeToFive"
     * @const
     */
    "ThreeToFive": "ThreeToFive",

    /**
     * value: "SixPlus"
     * @const
     */
    "SixPlus": "SixPlus"
};



export default User;

