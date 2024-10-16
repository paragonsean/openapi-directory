/**
 * GOV.UK Pay API
 * GOV.UK Pay API (This version is no longer maintained. See openapi/publicapi_spec.json for latest API specification)
 *
 * The version of the OpenAPI document: 1.0.3
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import Link from './Link';
import PostLink from './PostLink';

/**
 * The PaymentLinks model module.
 * @module model/PaymentLinks
 * @version 1.0.3
 */
class PaymentLinks {
    /**
     * Constructs a new <code>PaymentLinks</code>.
     * links for payment
     * @alias module:model/PaymentLinks
     */
    constructor() { 
        
        PaymentLinks.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>PaymentLinks</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/PaymentLinks} obj Optional instance to populate.
     * @return {module:model/PaymentLinks} The populated <code>PaymentLinks</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new PaymentLinks();

            if (data.hasOwnProperty('cancel')) {
                obj['cancel'] = PostLink.constructFromObject(data['cancel']);
            }
            if (data.hasOwnProperty('capture')) {
                obj['capture'] = PostLink.constructFromObject(data['capture']);
            }
            if (data.hasOwnProperty('events')) {
                obj['events'] = Link.constructFromObject(data['events']);
            }
            if (data.hasOwnProperty('next_url')) {
                obj['next_url'] = Link.constructFromObject(data['next_url']);
            }
            if (data.hasOwnProperty('next_url_post')) {
                obj['next_url_post'] = PostLink.constructFromObject(data['next_url_post']);
            }
            if (data.hasOwnProperty('refunds')) {
                obj['refunds'] = Link.constructFromObject(data['refunds']);
            }
            if (data.hasOwnProperty('self')) {
                obj['self'] = Link.constructFromObject(data['self']);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>PaymentLinks</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>PaymentLinks</code>.
     */
    static validateJSON(data) {
        // validate the optional field `cancel`
        if (data['cancel']) { // data not null
          PostLink.validateJSON(data['cancel']);
        }
        // validate the optional field `capture`
        if (data['capture']) { // data not null
          PostLink.validateJSON(data['capture']);
        }
        // validate the optional field `events`
        if (data['events']) { // data not null
          Link.validateJSON(data['events']);
        }
        // validate the optional field `next_url`
        if (data['next_url']) { // data not null
          Link.validateJSON(data['next_url']);
        }
        // validate the optional field `next_url_post`
        if (data['next_url_post']) { // data not null
          PostLink.validateJSON(data['next_url_post']);
        }
        // validate the optional field `refunds`
        if (data['refunds']) { // data not null
          Link.validateJSON(data['refunds']);
        }
        // validate the optional field `self`
        if (data['self']) { // data not null
          Link.validateJSON(data['self']);
        }

        return true;
    }


}



/**
 * @member {module:model/PostLink} cancel
 */
PaymentLinks.prototype['cancel'] = undefined;

/**
 * @member {module:model/PostLink} capture
 */
PaymentLinks.prototype['capture'] = undefined;

/**
 * @member {module:model/Link} events
 */
PaymentLinks.prototype['events'] = undefined;

/**
 * @member {module:model/Link} next_url
 */
PaymentLinks.prototype['next_url'] = undefined;

/**
 * @member {module:model/PostLink} next_url_post
 */
PaymentLinks.prototype['next_url_post'] = undefined;

/**
 * @member {module:model/Link} refunds
 */
PaymentLinks.prototype['refunds'] = undefined;

/**
 * @member {module:model/Link} self
 */
PaymentLinks.prototype['self'] = undefined;






export default PaymentLinks;

