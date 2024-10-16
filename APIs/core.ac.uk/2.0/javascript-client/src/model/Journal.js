/**
 * CORE API v2
 * <p style=\"text-align: justify;\">You can use the CORE API to access the      resources harvested and enriched by CORE. If you encounter any problems with the API, please <a href=\"/contact\">report them to us</a>.</p>  <h2>Overview</h2> <p style=\"text-align: justify;\">The API is organised by resource type. The resources are <b>articles</b>,      <b>journals</b> and <b>repositories</b> and are represented using JSON data format. Furthermore,      each resource has a list of methods. The API also provides two global methods for accessing all resources at once.</p>  <h2>Response format</h2> <p style=\"text-align: justify;\">Response for each query contains two fields: <b>status</b> and <b>data</b>.     In case of an error status, the data field is empty. The data field contains a single object     in case the request is for a specific identifier (e.g. CORE ID, CORE repository ID, etc.), or       contains a list of objects, for example for search queries. In case of batch requests, the response     is an array of objects, each of which contains its own <b>status</b> and <b>data</b> fields.     For search queries the response contains an additional field <b>totalHits</b>, which is the      total number of items which match the search criteria.</p>  <h2>Search query syntax</h2>  <p style=\"text-align: justify\">Complex search queries can be used in all of the API search methods.     The query can be a simple string or it can be built using terms and operators described in Elasticsearch     <a href=\"http://www.elastic.co/guide/en/elasticsearch/reference/1.4/query-dsl-query-string-query.html#query-string-syntax\">documentation</a>.     The usable field names are <strong>title</strong>, <strong>description</strong>, <strong>fullText</strong>,      <strong>authors</strong>, <strong>publisher</strong>, <strong>repositories.id</strong>, <strong>repositories.name</strong>,      <strong>doi</strong>, <strong>oai</strong>, <strong>identifiers</strong> (which is a list of article identifiers including OAI, URL, etc.), <strong>language.name</strong>      and <strong>year</strong>. Some example queries: </p>  <ul style=\"margin-left: 30px;\">     <li><p>title:psychology and language.name:English</p></li>     <li><p>repositories.id:86 AND year:2014</p></li>     <li><p>identifiers:\"oai:aura.abdn.ac.uk:2164/3837\" OR identifiers:\"oai:aura.abdn.ac.uk:2164/3843\"</p></li>     <li><p>doi:\"10.1186/1471-2458-6-309\"</p></li> </ul>  <h3>Retrieving the latest Articles</h3> <p style=\"text-align: justify\">     You can retrieve the harvested items since specific dates using the following queries: </p>  <ul style=\"margin-left: 30px;\">     <li><p>repositoryDocument.metadataUpdated:>2017-02-10</p></li>     <li><p>repositoryDocument.metadataUpdated:>2017-03-01 AND repositoryDocument.metadataUpdated:<2017-03-31</p></li>     </ul>  <h2>Sort order</h2>  <p style=\"text-align: justify;\">For search queries, the results are ordered by relevance score. For batch      requests, the results are retrieved in the order of the requests.</p>  <h2>Parameters</h2> <p style=\"text-align: justify;\">The API methods allow different parameters to be passed. Additionally, there is an API key parameter which is common to all API methods. For all API methods      the API key can be provided either as a query parameter or in the request header. If the API key      is not provided, the API will return HTTP 401 error. You can register for an API key <a href=\"/services#api\">here</a>.</p>  <h2>API methods</h2>
 *
 * The version of the OpenAPI document: 2.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';

/**
 * The Journal model module.
 * @module model/Journal
 * @version 2.0
 */
class Journal {
    /**
     * Constructs a new <code>Journal</code>.
     * @alias module:model/Journal
     * @param identifiers {Array.<String>} List of journal identifiers (e.g. URL, OAI or ISSN). The type is prepended to the identifier string (e.g. 'issn:2296-0597')
     */
    constructor(identifiers) { 
        
        Journal.initialize(this, identifiers);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, identifiers) { 
        obj['identifiers'] = identifiers;
    }

    /**
     * Constructs a <code>Journal</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/Journal} obj Optional instance to populate.
     * @return {module:model/Journal} The populated <code>Journal</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new Journal();

            if (data.hasOwnProperty('identifiers')) {
                obj['identifiers'] = ApiClient.convertToType(data['identifiers'], ['String']);
            }
            if (data.hasOwnProperty('language')) {
                obj['language'] = ApiClient.convertToType(data['language'], 'String');
            }
            if (data.hasOwnProperty('publisher')) {
                obj['publisher'] = ApiClient.convertToType(data['publisher'], 'String');
            }
            if (data.hasOwnProperty('rights')) {
                obj['rights'] = ApiClient.convertToType(data['rights'], 'String');
            }
            if (data.hasOwnProperty('subjects')) {
                obj['subjects'] = ApiClient.convertToType(data['subjects'], ['String']);
            }
            if (data.hasOwnProperty('title')) {
                obj['title'] = ApiClient.convertToType(data['title'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>Journal</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>Journal</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of Journal.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is an array
        if (!Array.isArray(data['identifiers'])) {
            throw new Error("Expected the field `identifiers` to be an array in the JSON data but got " + data['identifiers']);
        }
        // ensure the json data is a string
        if (data['language'] && !(typeof data['language'] === 'string' || data['language'] instanceof String)) {
            throw new Error("Expected the field `language` to be a primitive type in the JSON string but got " + data['language']);
        }
        // ensure the json data is a string
        if (data['publisher'] && !(typeof data['publisher'] === 'string' || data['publisher'] instanceof String)) {
            throw new Error("Expected the field `publisher` to be a primitive type in the JSON string but got " + data['publisher']);
        }
        // ensure the json data is a string
        if (data['rights'] && !(typeof data['rights'] === 'string' || data['rights'] instanceof String)) {
            throw new Error("Expected the field `rights` to be a primitive type in the JSON string but got " + data['rights']);
        }
        // ensure the json data is an array
        if (!Array.isArray(data['subjects'])) {
            throw new Error("Expected the field `subjects` to be an array in the JSON data but got " + data['subjects']);
        }
        // ensure the json data is a string
        if (data['title'] && !(typeof data['title'] === 'string' || data['title'] instanceof String)) {
            throw new Error("Expected the field `title` to be a primitive type in the JSON string but got " + data['title']);
        }

        return true;
    }


}

Journal.RequiredProperties = ["identifiers"];

/**
 * List of journal identifiers (e.g. URL, OAI or ISSN). The type is prepended to the identifier string (e.g. 'issn:2296-0597')
 * @member {Array.<String>} identifiers
 */
Journal.prototype['identifiers'] = undefined;

/**
 * Language of the journal
 * @member {String} language
 */
Journal.prototype['language'] = undefined;

/**
 * Publisher of the journal
 * @member {String} publisher
 */
Journal.prototype['publisher'] = undefined;

/**
 * Copyright license of the journal
 * @member {String} rights
 */
Journal.prototype['rights'] = undefined;

/**
 * List of journal subjects
 * @member {Array.<String>} subjects
 */
Journal.prototype['subjects'] = undefined;

/**
 * Journal title
 * @member {String} title
 */
Journal.prototype['title'] = undefined;






export default Journal;

