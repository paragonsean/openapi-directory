/**
 * OpenFEC
 * This application programming interface (API) allows you to explore the way candidates and committees fund their campaigns.    The Federal Election Commission (FEC) API is a RESTful web service supporting full-text and field-specific searches on FEC data. [Bulk downloads](https://www.fec.gov/data/advanced/?tab=bulk-data) are available on the current site. Information is tied to the underlying forms by file ID and image ID. Data is updated nightly.    There are a lot of data, and a good place to start is to use search to find interesting candidates and committees. Then, you can use their IDs to find report or line item details with the other endpoints. If you are interested in individual donors, check out contributor information in the `/schedule_a/` endpoints.    <b class=\"body\" id=\"getting_started_head\">Getting started with the openFEC API</b><br>    If you would like to use the FEC's API programmatically, you can sign up for your own API key using our form. Alternatively, you can still try out our API without an API key by using the web interface and using DEMO_KEY. Note that when you use the openFEC API you are subject to the [Terms of Service](https://github.com/fecgov/FEC/blob/master/TERMS-OF-SERVICE.md) and [Acceptable Use policy](https://github.com/fecgov/FEC/blob/master/ACCEPTABLE-USE-POLICY.md).    Signing up for an API key will enable you to place up to 1,000 calls an hour. Each call is limited to 100 results per page. You can email questions, comments or a request to get a key for 7,200 calls an hour (120 calls per minute) to <a href=\"mailto:APIinfo@fec.gov\">APIinfo@fec.gov</a>. You can also ask questions and discuss the data in a community led [group](https://groups.google.com/forum/#!forum/fec-data).    The model definitions and schema are available at [/swagger](/swagger/). This is useful for making wrappers and exploring the data.    A few restrictions limit the way you can use FEC data. For example, you can’t use contributor lists for commercial purposes or to solicit donations. [Learn more here](https://www.fec.gov/updates/sale-or-use-contributor-information/).    [Inspect our source code](https://github.com/fecgov/openFEC). We welcome issues and pull requests!    <p><br></p> <h2 class=\"title\" id=\"signup_head\">Sign up for an API key</h2> <div id=\"apidatagov_signup\">Loading signup form...</div>
 *
 * The version of the OpenAPI document: 1.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';

/**
 * The CandidateFlags model module.
 * @module model/CandidateFlags
 * @version 1.0
 */
class CandidateFlags {
    /**
     * Constructs a new <code>CandidateFlags</code>.
     * @alias module:model/CandidateFlags
     * @param candidateId {String}  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office. First character indicates office - [P]residential, [H]ouse, [S]enate]. Second character is the last digit of the two-year period the ID was created. Third and fourth is the candidate state. Presidential IDs don't have state. Fifth and sixth is the district when the candidate first ran. This does not change if the candidate/member's district changes during re-districting. Presidential IDs don't have districts. The rest is sequence. 
     */
    constructor(candidateId) { 
        
        CandidateFlags.initialize(this, candidateId);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, candidateId) { 
        obj['candidate_id'] = candidateId;
    }

    /**
     * Constructs a <code>CandidateFlags</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/CandidateFlags} obj Optional instance to populate.
     * @return {module:model/CandidateFlags} The populated <code>CandidateFlags</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new CandidateFlags();

            if (data.hasOwnProperty('candidate_id')) {
                obj['candidate_id'] = ApiClient.convertToType(data['candidate_id'], 'String');
            }
            if (data.hasOwnProperty('federal_funds_flag')) {
                obj['federal_funds_flag'] = ApiClient.convertToType(data['federal_funds_flag'], 'Boolean');
            }
            if (data.hasOwnProperty('has_raised_funds')) {
                obj['has_raised_funds'] = ApiClient.convertToType(data['has_raised_funds'], 'Boolean');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>CandidateFlags</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>CandidateFlags</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of CandidateFlags.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is a string
        if (data['candidate_id'] && !(typeof data['candidate_id'] === 'string' || data['candidate_id'] instanceof String)) {
            throw new Error("Expected the field `candidate_id` to be a primitive type in the JSON string but got " + data['candidate_id']);
        }

        return true;
    }


}

CandidateFlags.RequiredProperties = ["candidate_id"];

/**
 *  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office. First character indicates office - [P]residential, [H]ouse, [S]enate]. Second character is the last digit of the two-year period the ID was created. Third and fourth is the candidate state. Presidential IDs don't have state. Fifth and sixth is the district when the candidate first ran. This does not change if the candidate/member's district changes during re-districting. Presidential IDs don't have districts. The rest is sequence. 
 * @member {String} candidate_id
 */
CandidateFlags.prototype['candidate_id'] = undefined;

/**
 * A boolean the describes if a presidential candidate has accepted federal funds. The flag will be false for House and Senate candidates.
 * @member {Boolean} federal_funds_flag
 */
CandidateFlags.prototype['federal_funds_flag'] = undefined;

/**
 * A boolean that describes if a candidate's committee has ever received any receipts for their campaign for this particular office. (Candidates have separate candidate IDs for each office.)
 * @member {Boolean} has_raised_funds
 */
CandidateFlags.prototype['has_raised_funds'] = undefined;






export default CandidateFlags;

