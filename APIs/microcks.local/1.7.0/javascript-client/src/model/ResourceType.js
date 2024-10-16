/**
 * Microcks API v1.7
 * API offered by Microcks, the Kubernetes native tools for API and microservices mocking and testing (microcks.io)
 *
 * The version of the OpenAPI document: 1.7.0
 * Contact: laurent@microcks.io
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
/**
* Enum class ResourceType.
* @enum {}
* @readonly
*/
export default class ResourceType {
    
        /**
         * value: "WSDL"
         * @const
         */
        "WSDL" = "WSDL";

    
        /**
         * value: "XSD"
         * @const
         */
        "XSD" = "XSD";

    
        /**
         * value: "JSON_SCHEMA"
         * @const
         */
        "JSON_SCHEMA" = "JSON_SCHEMA";

    
        /**
         * value: "OPEN_API_SPEC"
         * @const
         */
        "OPEN_API_SPEC" = "OPEN_API_SPEC";

    
        /**
         * value: "OPEN_API_SCHEMA"
         * @const
         */
        "OPEN_API_SCHEMA" = "OPEN_API_SCHEMA";

    
        /**
         * value: "ASYNC_API_SPEC"
         * @const
         */
        "ASYNC_API_SPEC" = "ASYNC_API_SPEC";

    
        /**
         * value: "ASYNC_API_SCHEMA"
         * @const
         */
        "ASYNC_API_SCHEMA" = "ASYNC_API_SCHEMA";

    
        /**
         * value: "AVRO_SCHEMA"
         * @const
         */
        "AVRO_SCHEMA" = "AVRO_SCHEMA";

    
        /**
         * value: "PROTOBUF_SCHEMA"
         * @const
         */
        "PROTOBUF_SCHEMA" = "PROTOBUF_SCHEMA";

    
        /**
         * value: "PROTOBUF_DESCRIPTION"
         * @const
         */
        "PROTOBUF_DESCRIPTION" = "PROTOBUF_DESCRIPTION";

    
        /**
         * value: "GRAPHQL_SCHEMA"
         * @const
         */
        "GRAPHQL_SCHEMA" = "GRAPHQL_SCHEMA";

    

    /**
    * Returns a <code>ResourceType</code> enum value from a Javascript object name.
    * @param {Object} data The plain JavaScript object containing the name of the enum value.
    * @return {module:model/ResourceType} The enum <code>ResourceType</code> value.
    */
    static constructFromObject(object) {
        return object;
    }
}

