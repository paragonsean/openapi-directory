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


import ApiClient from "../ApiClient";
import CalendarDatePage from '../model/CalendarDatePage';
import ElectionDatesGetDefaultResponse from '../model/ElectionDatesGetDefaultResponse';
import ReportingDatesGetDefaultResponse from '../model/ReportingDatesGetDefaultResponse';

/**
* Dates service.
* @module api/DatesApi
* @version 1.0
*/
export default class DatesApi {

    /**
    * Constructs a new DatesApi. 
    * @alias module:api/DatesApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the calendarDatesExportGet operation.
     * @callback module:api/DatesApi~calendarDatesExportGetCallback
     * @param {String} error Error message, if any.
     * @param {module:model/CalendarDatePage} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     *  Returns CSV or ICS for downloading directly into calendar applications like Google, Outlook or other applications.  Combines the election and reporting dates with Commission meetings, conferences, outreach, Advisory Opinions, rules, litigation dates and other events into one calendar.  State filtering now applies to elections, reports and reporting periods.  Presidential pre-primary report due dates are not shown on even years. Filers generally opt to file monthly rather than submit over 50 pre-primary election reports. All reporting deadlines are available at /reporting-dates/ for reference.  This is [the sql function](https://github.com/fecgov/openFEC/blob/develop/data/migrations/V40__omnibus_dates.sql) that creates the calendar.  
     * @param {String} apiKey  API key for https://api.data.gov. Get one at https://api.data.gov/signup. 
     * @param {Object} opts Optional parameters
     * @param {Array.<Number>} [calendarCategoryId]  Each type of event has a calendar category with an integer id. Options are: Open Meetings: 32, Executive Sessions: 39, Public Hearings: 40, Conferences: 33, Roundtables: 34, Election Dates: 36, Federal Holidays: 37, FEA Periods: 38, Commission Meetings: 20, Reporting Deadlines: 21, Conferences and Outreach: 22, AOs and Rules: 23, Other: 24, Quarterly: 25, Monthly: 26, Pre and Post-Elections: 27, EC Periods:28, and IE Periods: 29 
     * @param {Array.<String>} [description] Brief description of event
     * @param {Boolean} [sortNullsLast = false)] Toggle that sorts null values last
     * @param {Boolean} [sortNullOnly = false)] Toggle that filters out all rows having sort column that is non-null
     * @param {Number} [page = 1)] For paginating through results, starting at page 1
     * @param {Date} [maxEndDate]  The maximum end date.(MM/DD/YYYY or YYYY-MM-DD) 
     * @param {Array.<String>} [summary] Longer description of event
     * @param {Date} [minEndDate]  The minimum end date.(MM/DD/YYYY or YYYY-MM-DD) 
     * @param {Boolean} [sortHideNull = false)] Hide null values on sorted column(s).
     * @param {Date} [minStartDate]  The minimum start date.(MM/DD/YYYY or YYYY-MM-DD) 
     * @param {Number} [perPage = 20)] The number of results returned per page. Defaults to 20.
     * @param {Date} [maxStartDate]  The maximum start date.(MM/DD/YYYY or YYYY-MM-DD) 
     * @param {module:model/String} [renderer = 'ics')] 
     * @param {String} [sort = '-start_date')] Provide a field to sort by. Use `-` for descending order. 
     * @param {Number} [eventId] An unique ID for an event. Useful for downloading a single event to your calendar. This ID is not a permanent, persistent ID.
     * @param {module:api/DatesApi~calendarDatesExportGetCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/CalendarDatePage}
     */
    calendarDatesExportGet(apiKey, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'apiKey' is set
      if (apiKey === undefined || apiKey === null) {
        throw new Error("Missing the required parameter 'apiKey' when calling calendarDatesExportGet");
      }

      let pathParams = {
      };
      let queryParams = {
        'calendar_category_id': this.apiClient.buildCollectionParam(opts['calendarCategoryId'], 'multi'),
        'api_key': apiKey,
        'description': this.apiClient.buildCollectionParam(opts['description'], 'multi'),
        'sort_nulls_last': opts['sortNullsLast'],
        'sort_null_only': opts['sortNullOnly'],
        'page': opts['page'],
        'max_end_date': opts['maxEndDate'],
        'summary': this.apiClient.buildCollectionParam(opts['summary'], 'multi'),
        'min_end_date': opts['minEndDate'],
        'sort_hide_null': opts['sortHideNull'],
        'min_start_date': opts['minStartDate'],
        'per_page': opts['perPage'],
        'max_start_date': opts['maxStartDate'],
        'renderer': opts['renderer'],
        'sort': opts['sort'],
        'event_id': opts['eventId']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['ApiKeyHeaderAuth', 'ApiKeyQueryAuth', 'apiKey'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = CalendarDatePage;
      return this.apiClient.callApi(
        '/calendar-dates/export/', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the calendarDatesGet operation.
     * @callback module:api/DatesApi~calendarDatesGetCallback
     * @param {String} error Error message, if any.
     * @param {module:model/CalendarDatePage} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     *  Combines the election and reporting dates with Commission meetings, conferences, outreach, Advisory Opinions, rules, litigation dates and other events into one calendar.  State and report type filtering is no longer available. 
     * @param {String} apiKey  API key for https://api.data.gov. Get one at https://api.data.gov/signup. 
     * @param {Object} opts Optional parameters
     * @param {Array.<Number>} [calendarCategoryId]  Each type of event has a calendar category with an integer id. Options are: Open Meetings: 32, Executive Sessions: 39, Public Hearings: 40, Conferences: 33, Roundtables: 34, Election Dates: 36, Federal Holidays: 37, FEA Periods: 38, Commission Meetings: 20, Reporting Deadlines: 21, Conferences and Outreach: 22, AOs and Rules: 23, Other: 24, Quarterly: 25, Monthly: 26, Pre and Post-Elections: 27, EC Periods:28, and IE Periods: 29 
     * @param {Array.<String>} [description] Brief description of event
     * @param {Boolean} [sortNullsLast = false)] Toggle that sorts null values last
     * @param {Boolean} [sortNullOnly = false)] Toggle that filters out all rows having sort column that is non-null
     * @param {Number} [page = 1)] For paginating through results, starting at page 1
     * @param {Date} [maxEndDate]  The maximum end date.(MM/DD/YYYY or YYYY-MM-DD) 
     * @param {Array.<String>} [summary] Longer description of event
     * @param {Date} [minEndDate]  The minimum end date.(MM/DD/YYYY or YYYY-MM-DD) 
     * @param {Boolean} [sortHideNull = false)] Hide null values on sorted column(s).
     * @param {Date} [minStartDate]  The minimum start date.(MM/DD/YYYY or YYYY-MM-DD) 
     * @param {Date} [maxStartDate]  The maximum start date.(MM/DD/YYYY or YYYY-MM-DD) 
     * @param {Number} [perPage = 20)] The number of results returned per page. Defaults to 20.
     * @param {String} [sort = '-start_date')] Provide a field to sort by. Use `-` for descending order. 
     * @param {Number} [eventId] An unique ID for an event. Useful for downloading a single event to your calendar. This ID is not a permanent, persistent ID.
     * @param {module:api/DatesApi~calendarDatesGetCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/CalendarDatePage}
     */
    calendarDatesGet(apiKey, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'apiKey' is set
      if (apiKey === undefined || apiKey === null) {
        throw new Error("Missing the required parameter 'apiKey' when calling calendarDatesGet");
      }

      let pathParams = {
      };
      let queryParams = {
        'calendar_category_id': this.apiClient.buildCollectionParam(opts['calendarCategoryId'], 'multi'),
        'api_key': apiKey,
        'description': this.apiClient.buildCollectionParam(opts['description'], 'multi'),
        'sort_nulls_last': opts['sortNullsLast'],
        'sort_null_only': opts['sortNullOnly'],
        'page': opts['page'],
        'max_end_date': opts['maxEndDate'],
        'summary': this.apiClient.buildCollectionParam(opts['summary'], 'multi'),
        'min_end_date': opts['minEndDate'],
        'sort_hide_null': opts['sortHideNull'],
        'min_start_date': opts['minStartDate'],
        'max_start_date': opts['maxStartDate'],
        'per_page': opts['perPage'],
        'sort': opts['sort'],
        'event_id': opts['eventId']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['ApiKeyHeaderAuth', 'ApiKeyQueryAuth', 'apiKey'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = CalendarDatePage;
      return this.apiClient.callApi(
        '/calendar-dates/', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the electionDatesGet operation.
     * @callback module:api/DatesApi~electionDatesGetCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ElectionDatesGetDefaultResponse} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     *  FEC election dates since 1995. 
     * @param {String} apiKey  API key for https://api.data.gov. Get one at https://api.data.gov/signup. 
     * @param {Object} opts Optional parameters
     * @param {Array.<String>} [electionState]  State or territory of the office sought. 
     * @param {Date} [maxElectionDate]  The maximum date of election. 
     * @param {Array.<String>} [electionDistrict]  House district of the office sought, if applicable. 
     * @param {Date} [minUpdateDate]  The minimum date this record was last updated.(MM/DD/YYYY or YYYY-MM-DD) 
     * @param {Boolean} [sortNullOnly = false)] Toggle that filters out all rows having sort column that is non-null
     * @param {Boolean} [sortHideNull = false)] Hide null values on sorted column(s).
     * @param {Date} [maxCreateDate]  The maximum date this record was added to the system.(MM/DD/YYYY or YYYY-MM-DD) 
     * @param {Number} [perPage = 20)] The number of results returned per page. Defaults to 20.
     * @param {Array.<String>} [electionYear] Year of election
     * @param {String} [sort = '-election_date')] Provide a field to sort by. Use `-` for descending order. 
     * @param {Date} [minCreateDate]  The minimum date this record was added to the system.(MM/DD/YYYY or YYYY-MM-DD) 
     * @param {Array.<String>} [electionParty]  Party, if applicable. 
     * @param {Array.<module:model/String>} [officeSought]  House, Senate or presidential office. 
     * @param {Boolean} [sortNullsLast = false)] Toggle that sorts null values last
     * @param {Number} [page = 1)] For paginating through results, starting at page 1
     * @param {Date} [maxUpdateDate]  The maximum date this record was last updated.(MM/DD/YYYY or YYYY-MM-DD) 
     * @param {Array.<String>} [electionTypeId]  Election type id 
     * @param {Date} [maxPrimaryGeneralDate]  The maximum date of primary or general election.(MM/DD/YYYY or YYYY-MM-DD) 
     * @param {Date} [minElectionDate]  The minimum date of election. 
     * @param {Date} [minPrimaryGeneralDate]  The minimum date of primary or general election.(MM/DD/YYYY or YYYY-MM-DD) 
     * @param {module:api/DatesApi~electionDatesGetCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ElectionDatesGetDefaultResponse}
     */
    electionDatesGet(apiKey, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'apiKey' is set
      if (apiKey === undefined || apiKey === null) {
        throw new Error("Missing the required parameter 'apiKey' when calling electionDatesGet");
      }

      let pathParams = {
      };
      let queryParams = {
        'election_state': this.apiClient.buildCollectionParam(opts['electionState'], 'multi'),
        'max_election_date': opts['maxElectionDate'],
        'election_district': this.apiClient.buildCollectionParam(opts['electionDistrict'], 'multi'),
        'min_update_date': opts['minUpdateDate'],
        'sort_null_only': opts['sortNullOnly'],
        'sort_hide_null': opts['sortHideNull'],
        'max_create_date': opts['maxCreateDate'],
        'per_page': opts['perPage'],
        'election_year': this.apiClient.buildCollectionParam(opts['electionYear'], 'multi'),
        'sort': opts['sort'],
        'min_create_date': opts['minCreateDate'],
        'api_key': apiKey,
        'election_party': this.apiClient.buildCollectionParam(opts['electionParty'], 'multi'),
        'office_sought': this.apiClient.buildCollectionParam(opts['officeSought'], 'multi'),
        'sort_nulls_last': opts['sortNullsLast'],
        'page': opts['page'],
        'max_update_date': opts['maxUpdateDate'],
        'election_type_id': this.apiClient.buildCollectionParam(opts['electionTypeId'], 'multi'),
        'max_primary_general_date': opts['maxPrimaryGeneralDate'],
        'min_election_date': opts['minElectionDate'],
        'min_primary_general_date': opts['minPrimaryGeneralDate']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['ApiKeyHeaderAuth', 'ApiKeyQueryAuth', 'apiKey'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = ElectionDatesGetDefaultResponse;
      return this.apiClient.callApi(
        '/election-dates/', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the reportingDatesGet operation.
     * @callback module:api/DatesApi~reportingDatesGetCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ReportingDatesGetDefaultResponse} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     *  FEC election dates since 1995. 
     * @param {String} apiKey  API key for https://api.data.gov. Get one at https://api.data.gov/signup. 
     * @param {Object} opts Optional parameters
     * @param {Date} [minUpdateDate]  The minimum date this record was last updated.(MM/DD/YYYY or YYYY-MM-DD) 
     * @param {Array.<String>} [reportType] Name of report where the underlying data comes from:     - 10D Pre-Election     - 10G Pre-General     - 10P Pre-Primary     - 10R Pre-Run-Off     - 10S Pre-Special     - 12C Pre-Convention     - 12G Pre-General     - 12P Pre-Primary     - 12R Pre-Run-Off     - 12S Pre-Special     - 30D Post-Election     - 30G Post-General     - 30P Post-Primary     - 30R Post-Run-Off     - 30S Post-Special     - 60D Post-Convention     - M1  January Monthly     - M10 October Monthly     - M11 November Monthly     - M12 December Monthly     - M2  February Monthly     - M3  March Monthly     - M4  April Monthly     - M5  May Monthly     - M6  June Monthly     - M7  July Monthly     - M8  August Monthly     - M9  September Monthly     - MY  Mid-Year Report     - Q1  April Quarterly     - Q2  July Quarterly     - Q3  October Quarterly     - TER Termination Report     - YE  Year-End     - ADJ COMP ADJUST AMEND     - CA  COMPREHENSIVE AMEND     - 90S Post Inaugural Supplement     - 90D Post Inaugural     - 48  48 Hour Notification     - 24  24 Hour Notification     - M7S July Monthly/Semi-Annual     - MSA Monthly Semi-Annual (MY)     - MYS Monthly Year End/Semi-Annual     - Q2S July Quarterly/Semi-Annual     - QSA Quarterly Semi-Annual (MY)     - QYS Quarterly Year End/Semi-Annual     - QYE Quarterly Semi-Annual (YE)     - QMS Quarterly Mid-Year/ Semi-Annual     - MSY Monthly Semi-Annual (YE) 
     * @param {Date} [minDueDate]  The minimum date the report is due.(MM/DD/YYYY or YYYY-MM-DD) 
     * @param {Boolean} [sortNullOnly = false)] Toggle that filters out all rows having sort column that is non-null
     * @param {Number} [page = 1)] For paginating through results, starting at page 1
     * @param {Date} [maxDueDate]  The maximum date the report is due.(MM/DD/YYYY or YYYY-MM-DD) 
     * @param {Array.<Number>} [reportYear]  Forms with coverage date -      year from the coverage ending date. Forms without coverage date -      year from the receipt date. 
     * @param {Boolean} [sortNullsLast = false)] Toggle that sorts null values last
     * @param {Date} [maxCreateDate]  The maximum date this record was added to the system.(MM/DD/YYYY or YYYY-MM-DD) 
     * @param {Date} [maxUpdateDate]  The maximum date this record was last updated.(MM/DD/YYYY or YYYY-MM-DD) 
     * @param {Number} [perPage = 20)] The number of results returned per page. Defaults to 20.
     * @param {Boolean} [sortHideNull = false)] Hide null values on sorted column(s).
     * @param {String} [sort = '-due_date')] Provide a field to sort by. Use `-` for descending order. 
     * @param {Date} [minCreateDate]  The minimum date this record was added to the system.(MM/DD/YYYY or YYYY-MM-DD) 
     * @param {module:api/DatesApi~reportingDatesGetCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ReportingDatesGetDefaultResponse}
     */
    reportingDatesGet(apiKey, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'apiKey' is set
      if (apiKey === undefined || apiKey === null) {
        throw new Error("Missing the required parameter 'apiKey' when calling reportingDatesGet");
      }

      let pathParams = {
      };
      let queryParams = {
        'api_key': apiKey,
        'min_update_date': opts['minUpdateDate'],
        'report_type': this.apiClient.buildCollectionParam(opts['reportType'], 'multi'),
        'min_due_date': opts['minDueDate'],
        'sort_null_only': opts['sortNullOnly'],
        'page': opts['page'],
        'max_due_date': opts['maxDueDate'],
        'report_year': this.apiClient.buildCollectionParam(opts['reportYear'], 'multi'),
        'sort_nulls_last': opts['sortNullsLast'],
        'max_create_date': opts['maxCreateDate'],
        'max_update_date': opts['maxUpdateDate'],
        'per_page': opts['perPage'],
        'sort_hide_null': opts['sortHideNull'],
        'sort': opts['sort'],
        'min_create_date': opts['minCreateDate']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['ApiKeyHeaderAuth', 'ApiKeyQueryAuth', 'apiKey'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = ReportingDatesGetDefaultResponse;
      return this.apiClient.callApi(
        '/reporting-dates/', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
