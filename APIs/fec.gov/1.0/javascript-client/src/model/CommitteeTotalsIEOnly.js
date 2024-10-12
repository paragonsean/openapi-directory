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
 * The CommitteeTotalsIEOnly model module.
 * @module model/CommitteeTotalsIEOnly
 * @version 1.0
 */
class CommitteeTotalsIEOnly {
    /**
     * Constructs a new <code>CommitteeTotalsIEOnly</code>.
     * @alias module:model/CommitteeTotalsIEOnly
     */
    constructor() { 
        
        CommitteeTotalsIEOnly.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>CommitteeTotalsIEOnly</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/CommitteeTotalsIEOnly} obj Optional instance to populate.
     * @return {module:model/CommitteeTotalsIEOnly} The populated <code>CommitteeTotalsIEOnly</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new CommitteeTotalsIEOnly();

            if (data.hasOwnProperty('committee_id')) {
                obj['committee_id'] = ApiClient.convertToType(data['committee_id'], 'String');
            }
            if (data.hasOwnProperty('committee_state')) {
                obj['committee_state'] = ApiClient.convertToType(data['committee_state'], 'String');
            }
            if (data.hasOwnProperty('contributions_ie_and_party_expenditures_made_percent')) {
                obj['contributions_ie_and_party_expenditures_made_percent'] = ApiClient.convertToType(data['contributions_ie_and_party_expenditures_made_percent'], 'Number');
            }
            if (data.hasOwnProperty('coverage_end_date')) {
                obj['coverage_end_date'] = ApiClient.convertToType(data['coverage_end_date'], 'Date');
            }
            if (data.hasOwnProperty('coverage_start_date')) {
                obj['coverage_start_date'] = ApiClient.convertToType(data['coverage_start_date'], 'Date');
            }
            if (data.hasOwnProperty('cycle')) {
                obj['cycle'] = ApiClient.convertToType(data['cycle'], 'Number');
            }
            if (data.hasOwnProperty('filing_frequency')) {
                obj['filing_frequency'] = ApiClient.convertToType(data['filing_frequency'], 'String');
            }
            if (data.hasOwnProperty('filing_frequency_full')) {
                obj['filing_frequency_full'] = ApiClient.convertToType(data['filing_frequency_full'], 'String');
            }
            if (data.hasOwnProperty('first_file_date')) {
                obj['first_file_date'] = ApiClient.convertToType(data['first_file_date'], 'Date');
            }
            if (data.hasOwnProperty('individual_contributions_percent')) {
                obj['individual_contributions_percent'] = ApiClient.convertToType(data['individual_contributions_percent'], 'Number');
            }
            if (data.hasOwnProperty('last_beginning_image_number')) {
                obj['last_beginning_image_number'] = ApiClient.convertToType(data['last_beginning_image_number'], 'String');
            }
            if (data.hasOwnProperty('last_cash_on_hand_end_period')) {
                obj['last_cash_on_hand_end_period'] = ApiClient.convertToType(data['last_cash_on_hand_end_period'], 'Number');
            }
            if (data.hasOwnProperty('operating_expenditures_percent')) {
                obj['operating_expenditures_percent'] = ApiClient.convertToType(data['operating_expenditures_percent'], 'Number');
            }
            if (data.hasOwnProperty('party_and_other_committee_contributions_percent')) {
                obj['party_and_other_committee_contributions_percent'] = ApiClient.convertToType(data['party_and_other_committee_contributions_percent'], 'Number');
            }
            if (data.hasOwnProperty('pdf_url')) {
                obj['pdf_url'] = ApiClient.convertToType(data['pdf_url'], 'String');
            }
            if (data.hasOwnProperty('report_form')) {
                obj['report_form'] = ApiClient.convertToType(data['report_form'], 'String');
            }
            if (data.hasOwnProperty('total_independent_contributions')) {
                obj['total_independent_contributions'] = ApiClient.convertToType(data['total_independent_contributions'], 'Number');
            }
            if (data.hasOwnProperty('total_independent_expenditures')) {
                obj['total_independent_expenditures'] = ApiClient.convertToType(data['total_independent_expenditures'], 'Number');
            }
            if (data.hasOwnProperty('transaction_coverage_date')) {
                obj['transaction_coverage_date'] = ApiClient.convertToType(data['transaction_coverage_date'], 'Date');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>CommitteeTotalsIEOnly</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>CommitteeTotalsIEOnly</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['committee_id'] && !(typeof data['committee_id'] === 'string' || data['committee_id'] instanceof String)) {
            throw new Error("Expected the field `committee_id` to be a primitive type in the JSON string but got " + data['committee_id']);
        }
        // ensure the json data is a string
        if (data['committee_state'] && !(typeof data['committee_state'] === 'string' || data['committee_state'] instanceof String)) {
            throw new Error("Expected the field `committee_state` to be a primitive type in the JSON string but got " + data['committee_state']);
        }
        // ensure the json data is a string
        if (data['filing_frequency'] && !(typeof data['filing_frequency'] === 'string' || data['filing_frequency'] instanceof String)) {
            throw new Error("Expected the field `filing_frequency` to be a primitive type in the JSON string but got " + data['filing_frequency']);
        }
        // ensure the json data is a string
        if (data['filing_frequency_full'] && !(typeof data['filing_frequency_full'] === 'string' || data['filing_frequency_full'] instanceof String)) {
            throw new Error("Expected the field `filing_frequency_full` to be a primitive type in the JSON string but got " + data['filing_frequency_full']);
        }
        // ensure the json data is a string
        if (data['last_beginning_image_number'] && !(typeof data['last_beginning_image_number'] === 'string' || data['last_beginning_image_number'] instanceof String)) {
            throw new Error("Expected the field `last_beginning_image_number` to be a primitive type in the JSON string but got " + data['last_beginning_image_number']);
        }
        // ensure the json data is a string
        if (data['pdf_url'] && !(typeof data['pdf_url'] === 'string' || data['pdf_url'] instanceof String)) {
            throw new Error("Expected the field `pdf_url` to be a primitive type in the JSON string but got " + data['pdf_url']);
        }
        // ensure the json data is a string
        if (data['report_form'] && !(typeof data['report_form'] === 'string' || data['report_form'] instanceof String)) {
            throw new Error("Expected the field `report_form` to be a primitive type in the JSON string but got " + data['report_form']);
        }

        return true;
    }


}



/**
 *  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id's begin with the letter C which is followed by eight digits. 
 * @member {String} committee_id
 */
CommitteeTotalsIEOnly.prototype['committee_id'] = undefined;

/**
 *  State of the committee's address as filed on the Form 1 
 * @member {String} committee_state
 */
CommitteeTotalsIEOnly.prototype['committee_state'] = undefined;

/**
 * @member {Number} contributions_ie_and_party_expenditures_made_percent
 */
CommitteeTotalsIEOnly.prototype['contributions_ie_and_party_expenditures_made_percent'] = undefined;

/**
 * Ending date of the reporting period
 * @member {Date} coverage_end_date
 */
CommitteeTotalsIEOnly.prototype['coverage_end_date'] = undefined;

/**
 * Beginning date of the reporting period
 * @member {Date} coverage_start_date
 */
CommitteeTotalsIEOnly.prototype['coverage_start_date'] = undefined;

/**
 *  Filter records to only those that are applicable to a given two-year period. This cycle follows the traditional House election cycle and subdivides the presidential and Senate elections into comparable two-year blocks. The cycle begins with an odd year and is named for its ending, even year. 
 * @member {Number} cycle
 */
CommitteeTotalsIEOnly.prototype['cycle'] = undefined;

/**
 * The one-letter      code of the filing frequency:          - A Administratively terminated          - D Debt          - M Monthly filer          - Q Quarterly filer          - T Terminated          - W Waived 
 * @member {String} filing_frequency
 */
CommitteeTotalsIEOnly.prototype['filing_frequency'] = undefined;

/**
 * The one-letter      code of the filing frequency:          - A Administratively terminated          - D Debt          - M Monthly filer          - Q Quarterly filer          - T Terminated          - W Waived 
 * @member {String} filing_frequency_full
 */
CommitteeTotalsIEOnly.prototype['filing_frequency_full'] = undefined;

/**
 * The day the FEC received the committee's first filing. This is usually a Form 1 committee registration.
 * @member {Date} first_file_date
 */
CommitteeTotalsIEOnly.prototype['first_file_date'] = undefined;

/**
 * @member {Number} individual_contributions_percent
 */
CommitteeTotalsIEOnly.prototype['individual_contributions_percent'] = undefined;

/**
 * @member {String} last_beginning_image_number
 */
CommitteeTotalsIEOnly.prototype['last_beginning_image_number'] = undefined;

/**
 * @member {Number} last_cash_on_hand_end_period
 */
CommitteeTotalsIEOnly.prototype['last_cash_on_hand_end_period'] = undefined;

/**
 * @member {Number} operating_expenditures_percent
 */
CommitteeTotalsIEOnly.prototype['operating_expenditures_percent'] = undefined;

/**
 * @member {Number} party_and_other_committee_contributions_percent
 */
CommitteeTotalsIEOnly.prototype['party_and_other_committee_contributions_percent'] = undefined;

/**
 * @member {String} pdf_url
 */
CommitteeTotalsIEOnly.prototype['pdf_url'] = undefined;

/**
 * @member {String} report_form
 */
CommitteeTotalsIEOnly.prototype['report_form'] = undefined;

/**
 * @member {Number} total_independent_contributions
 */
CommitteeTotalsIEOnly.prototype['total_independent_contributions'] = undefined;

/**
 * @member {Number} total_independent_expenditures
 */
CommitteeTotalsIEOnly.prototype['total_independent_expenditures'] = undefined;

/**
 * @member {Date} transaction_coverage_date
 */
CommitteeTotalsIEOnly.prototype['transaction_coverage_date'] = undefined;






export default CommitteeTotalsIEOnly;

