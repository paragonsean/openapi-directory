/**
 * Pinecone API
 * Pinecone is a vector database. This is an unofficial, community-managed OpenAPI spec that (should) accurately model the Pinecone API. This project was developed independent of and is unaffiliated with Pinecone Systems. Users should switch to the official API spec, if and when Pinecone releases it.
 *
 * The version of the OpenAPI document: 20230406.1
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import IndexDatabase from './IndexDatabase';
import IndexStatus from './IndexStatus';

/**
 * The Index model module.
 * @module model/Index
 * @version 20230406.1
 */
class Index {
    /**
     * Constructs a new <code>Index</code>.
     * @alias module:model/Index
     */
    constructor() { 
        
        Index.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>Index</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/Index} obj Optional instance to populate.
     * @return {module:model/Index} The populated <code>Index</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new Index();

            if (data.hasOwnProperty('database')) {
                obj['database'] = IndexDatabase.constructFromObject(data['database']);
            }
            if (data.hasOwnProperty('status')) {
                obj['status'] = IndexStatus.constructFromObject(data['status']);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>Index</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>Index</code>.
     */
    static validateJSON(data) {
        // validate the optional field `database`
        if (data['database']) { // data not null
          IndexDatabase.validateJSON(data['database']);
        }
        // validate the optional field `status`
        if (data['status']) { // data not null
          IndexStatus.validateJSON(data['status']);
        }

        return true;
    }


}



/**
 * @member {module:model/IndexDatabase} database
 */
Index.prototype['database'] = undefined;

/**
 * @member {module:model/IndexStatus} status
 */
Index.prototype['status'] = undefined;






export default Index;

