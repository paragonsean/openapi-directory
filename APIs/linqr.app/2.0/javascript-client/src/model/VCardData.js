/**
 * LinQR
 * This is LinQR QR Code API documentation. This API allows you to generate custom, visually attractive QR Codes. The cloud infrastructure guarantees high availability and autoscalability of the service. You can generate hundreds of thousands of images this way and use them however you like.  We realize that your API use case may require custom solutions, and perhaps we lack functionality that is very important to you. In that case feel free to write an email to our support and tell us about it. We have repeatedly added new functions of our service directly after the requests of our users.  **General remarks:**  - maximum request size is fixed at 32MB.  - request timeout is fixed at 180 seconds.
 *
 * The version of the OpenAPI document: 2.0
 * Contact: support@linqr.app
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import CellPhone from './CellPhone';
import Email from './Email';
import Fax from './Fax';
import HomePhone from './HomePhone';
import Phone from './Phone';
import Photo from './Photo';
import Title from './Title';
import Url from './Url';
import Videophone from './Videophone';
import WorkPhone from './WorkPhone';

/**
 * The VCardData model module.
 * @module model/VCardData
 * @version 2.0
 */
class VCardData {
    /**
     * Constructs a new <code>VCardData</code>.
     * @alias module:model/VCardData
     * @param lastName {String} Last name.
     */
    constructor(lastName) { 
        
        VCardData.initialize(this, lastName);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, lastName) { 
        obj['encoding'] = 'vcard';
        obj['last_name'] = lastName;
    }

    /**
     * Constructs a <code>VCardData</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/VCardData} obj Optional instance to populate.
     * @return {module:model/VCardData} The populated <code>VCardData</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new VCardData();

            if (data.hasOwnProperty('birthday')) {
                obj['birthday'] = ApiClient.convertToType(data['birthday'], 'Date');
            }
            if (data.hasOwnProperty('cell_phone')) {
                obj['cell_phone'] = CellPhone.constructFromObject(data['cell_phone']);
            }
            if (data.hasOwnProperty('city')) {
                obj['city'] = ApiClient.convertToType(data['city'], 'String');
            }
            if (data.hasOwnProperty('country')) {
                obj['country'] = ApiClient.convertToType(data['country'], 'String');
            }
            if (data.hasOwnProperty('display_name')) {
                obj['display_name'] = ApiClient.convertToType(data['display_name'], 'String');
            }
            if (data.hasOwnProperty('email')) {
                obj['email'] = Email.constructFromObject(data['email']);
            }
            if (data.hasOwnProperty('encoding')) {
                obj['encoding'] = ApiClient.convertToType(data['encoding'], 'String');
            }
            if (data.hasOwnProperty('fax')) {
                obj['fax'] = Fax.constructFromObject(data['fax']);
            }
            if (data.hasOwnProperty('first_name')) {
                obj['first_name'] = ApiClient.convertToType(data['first_name'], 'String');
            }
            if (data.hasOwnProperty('home_phone')) {
                obj['home_phone'] = HomePhone.constructFromObject(data['home_phone']);
            }
            if (data.hasOwnProperty('last_name')) {
                obj['last_name'] = ApiClient.convertToType(data['last_name'], 'String');
            }
            if (data.hasOwnProperty('latitude')) {
                obj['latitude'] = ApiClient.convertToType(data['latitude'], 'Number');
            }
            if (data.hasOwnProperty('longitude')) {
                obj['longitude'] = ApiClient.convertToType(data['longitude'], 'Number');
            }
            if (data.hasOwnProperty('memo')) {
                obj['memo'] = ApiClient.convertToType(data['memo'], 'String');
            }
            if (data.hasOwnProperty('nickname')) {
                obj['nickname'] = ApiClient.convertToType(data['nickname'], 'String');
            }
            if (data.hasOwnProperty('organization')) {
                obj['organization'] = ApiClient.convertToType(data['organization'], 'String');
            }
            if (data.hasOwnProperty('phone')) {
                obj['phone'] = Phone.constructFromObject(data['phone']);
            }
            if (data.hasOwnProperty('photo')) {
                obj['photo'] = Photo.constructFromObject(data['photo']);
            }
            if (data.hasOwnProperty('po_box')) {
                obj['po_box'] = ApiClient.convertToType(data['po_box'], 'String');
            }
            if (data.hasOwnProperty('region')) {
                obj['region'] = ApiClient.convertToType(data['region'], 'String');
            }
            if (data.hasOwnProperty('revision')) {
                obj['revision'] = ApiClient.convertToType(data['revision'], 'Date');
            }
            if (data.hasOwnProperty('source')) {
                obj['source'] = ApiClient.convertToType(data['source'], 'String');
            }
            if (data.hasOwnProperty('street')) {
                obj['street'] = ApiClient.convertToType(data['street'], 'String');
            }
            if (data.hasOwnProperty('title')) {
                obj['title'] = Title.constructFromObject(data['title']);
            }
            if (data.hasOwnProperty('url')) {
                obj['url'] = Url.constructFromObject(data['url']);
            }
            if (data.hasOwnProperty('videophone')) {
                obj['videophone'] = Videophone.constructFromObject(data['videophone']);
            }
            if (data.hasOwnProperty('work_phone')) {
                obj['work_phone'] = WorkPhone.constructFromObject(data['work_phone']);
            }
            if (data.hasOwnProperty('zip_code')) {
                obj['zip_code'] = ApiClient.convertToType(data['zip_code'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>VCardData</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>VCardData</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of VCardData.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // validate the optional field `cell_phone`
        if (data['cell_phone']) { // data not null
          CellPhone.validateJSON(data['cell_phone']);
        }
        // ensure the json data is a string
        if (data['city'] && !(typeof data['city'] === 'string' || data['city'] instanceof String)) {
            throw new Error("Expected the field `city` to be a primitive type in the JSON string but got " + data['city']);
        }
        // ensure the json data is a string
        if (data['country'] && !(typeof data['country'] === 'string' || data['country'] instanceof String)) {
            throw new Error("Expected the field `country` to be a primitive type in the JSON string but got " + data['country']);
        }
        // ensure the json data is a string
        if (data['display_name'] && !(typeof data['display_name'] === 'string' || data['display_name'] instanceof String)) {
            throw new Error("Expected the field `display_name` to be a primitive type in the JSON string but got " + data['display_name']);
        }
        // validate the optional field `email`
        if (data['email']) { // data not null
          Email.validateJSON(data['email']);
        }
        // ensure the json data is a string
        if (data['encoding'] && !(typeof data['encoding'] === 'string' || data['encoding'] instanceof String)) {
            throw new Error("Expected the field `encoding` to be a primitive type in the JSON string but got " + data['encoding']);
        }
        // validate the optional field `fax`
        if (data['fax']) { // data not null
          Fax.validateJSON(data['fax']);
        }
        // ensure the json data is a string
        if (data['first_name'] && !(typeof data['first_name'] === 'string' || data['first_name'] instanceof String)) {
            throw new Error("Expected the field `first_name` to be a primitive type in the JSON string but got " + data['first_name']);
        }
        // validate the optional field `home_phone`
        if (data['home_phone']) { // data not null
          HomePhone.validateJSON(data['home_phone']);
        }
        // ensure the json data is a string
        if (data['last_name'] && !(typeof data['last_name'] === 'string' || data['last_name'] instanceof String)) {
            throw new Error("Expected the field `last_name` to be a primitive type in the JSON string but got " + data['last_name']);
        }
        // ensure the json data is a string
        if (data['memo'] && !(typeof data['memo'] === 'string' || data['memo'] instanceof String)) {
            throw new Error("Expected the field `memo` to be a primitive type in the JSON string but got " + data['memo']);
        }
        // ensure the json data is a string
        if (data['nickname'] && !(typeof data['nickname'] === 'string' || data['nickname'] instanceof String)) {
            throw new Error("Expected the field `nickname` to be a primitive type in the JSON string but got " + data['nickname']);
        }
        // ensure the json data is a string
        if (data['organization'] && !(typeof data['organization'] === 'string' || data['organization'] instanceof String)) {
            throw new Error("Expected the field `organization` to be a primitive type in the JSON string but got " + data['organization']);
        }
        // validate the optional field `phone`
        if (data['phone']) { // data not null
          Phone.validateJSON(data['phone']);
        }
        // validate the optional field `photo`
        if (data['photo']) { // data not null
          Photo.validateJSON(data['photo']);
        }
        // ensure the json data is a string
        if (data['po_box'] && !(typeof data['po_box'] === 'string' || data['po_box'] instanceof String)) {
            throw new Error("Expected the field `po_box` to be a primitive type in the JSON string but got " + data['po_box']);
        }
        // ensure the json data is a string
        if (data['region'] && !(typeof data['region'] === 'string' || data['region'] instanceof String)) {
            throw new Error("Expected the field `region` to be a primitive type in the JSON string but got " + data['region']);
        }
        // ensure the json data is a string
        if (data['source'] && !(typeof data['source'] === 'string' || data['source'] instanceof String)) {
            throw new Error("Expected the field `source` to be a primitive type in the JSON string but got " + data['source']);
        }
        // ensure the json data is a string
        if (data['street'] && !(typeof data['street'] === 'string' || data['street'] instanceof String)) {
            throw new Error("Expected the field `street` to be a primitive type in the JSON string but got " + data['street']);
        }
        // validate the optional field `title`
        if (data['title']) { // data not null
          Title.validateJSON(data['title']);
        }
        // validate the optional field `url`
        if (data['url']) { // data not null
          Url.validateJSON(data['url']);
        }
        // validate the optional field `videophone`
        if (data['videophone']) { // data not null
          Videophone.validateJSON(data['videophone']);
        }
        // validate the optional field `work_phone`
        if (data['work_phone']) { // data not null
          WorkPhone.validateJSON(data['work_phone']);
        }
        // ensure the json data is a string
        if (data['zip_code'] && !(typeof data['zip_code'] === 'string' || data['zip_code'] instanceof String)) {
            throw new Error("Expected the field `zip_code` to be a primitive type in the JSON string but got " + data['zip_code']);
        }

        return true;
    }


}

VCardData.RequiredProperties = ["last_name"];

/**
 * Birthday.
 * @member {Date} birthday
 */
VCardData.prototype['birthday'] = undefined;

/**
 * @member {module:model/CellPhone} cell_phone
 */
VCardData.prototype['cell_phone'] = undefined;

/**
 * Address information: City.
 * @member {String} city
 */
VCardData.prototype['city'] = undefined;

/**
 * Address information: Country.
 * @member {String} country
 */
VCardData.prototype['country'] = undefined;

/**
 * Common name. By default, equals to concatenated `first_name` and `last_name`.
 * @member {String} display_name
 */
VCardData.prototype['display_name'] = undefined;

/**
 * @member {module:model/Email} email
 */
VCardData.prototype['email'] = undefined;

/**
 * `vcard` encoding. Universal standard for electronic business cards, typically stored as `*.vcf` file. It allows you to encode more types of data compared to its `mecard` equivalent, but it results in a larger QR code.  For more information please refer to: <a href=\"https://en.wikipedia.org/wiki/VCard\" rel=\"noopener noreferrer\" target=\"_blank\" >en.wikipedia.org</a>.
 * @member {module:model/VCardData.EncodingEnum} encoding
 * @default 'vcard'
 */
VCardData.prototype['encoding'] = 'vcard';

/**
 * @member {module:model/Fax} fax
 */
VCardData.prototype['fax'] = undefined;

/**
 * First name.
 * @member {String} first_name
 */
VCardData.prototype['first_name'] = undefined;

/**
 * @member {module:model/HomePhone} home_phone
 */
VCardData.prototype['home_phone'] = undefined;

/**
 * Last name.
 * @member {String} last_name
 */
VCardData.prototype['last_name'] = undefined;

/**
 * Location latitude.
 * @member {Number} latitude
 */
VCardData.prototype['latitude'] = undefined;

/**
 * Location longitude.
 * @member {Number} longitude
 */
VCardData.prototype['longitude'] = undefined;

/**
 * Short notice.
 * @member {String} memo
 */
VCardData.prototype['memo'] = undefined;

/**
 * Nickname.
 * @member {String} nickname
 */
VCardData.prototype['nickname'] = undefined;

/**
 * Organization/company name
 * @member {String} organization
 */
VCardData.prototype['organization'] = undefined;

/**
 * @member {module:model/Phone} phone
 */
VCardData.prototype['phone'] = undefined;

/**
 * @member {module:model/Photo} photo
 */
VCardData.prototype['photo'] = undefined;

/**
 * Address information: Post Office Box.
 * @member {String} po_box
 */
VCardData.prototype['po_box'] = undefined;

/**
 * Address information: Region.
 * @member {String} region
 */
VCardData.prototype['region'] = undefined;

/**
 * vCard revision/last modification date.
 * @member {Date} revision
 */
VCardData.prototype['revision'] = undefined;

/**
 * URL pointing to vCard file itself.
 * @member {String} source
 */
VCardData.prototype['source'] = undefined;

/**
 * Address information: Street.
 * @member {String} street
 */
VCardData.prototype['street'] = undefined;

/**
 * @member {module:model/Title} title
 */
VCardData.prototype['title'] = undefined;

/**
 * @member {module:model/Url} url
 */
VCardData.prototype['url'] = undefined;

/**
 * @member {module:model/Videophone} videophone
 */
VCardData.prototype['videophone'] = undefined;

/**
 * @member {module:model/WorkPhone} work_phone
 */
VCardData.prototype['work_phone'] = undefined;

/**
 * Address information: ZIP code.
 * @member {String} zip_code
 */
VCardData.prototype['zip_code'] = undefined;





/**
 * Allowed values for the <code>encoding</code> property.
 * @enum {String}
 * @readonly
 */
VCardData['EncodingEnum'] = {

    /**
     * value: "vcard"
     * @const
     */
    "vcard": "vcard"
};



export default VCardData;

