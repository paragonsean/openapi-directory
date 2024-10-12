/**
 * Braze Endpoints
 * # Braze API Overview  Braze provides a high performance REST API to allow you to track users, send messages, export data, and more.  A REST API is a way to programmatically transfer information over the web using a predefined schema. Braze has created many different endpoints with specific requirements that will perform various actions and/or return various data. API access is done using HTTPS web requests to your company's REST API endpoint (this will correspond to your Dashboard URL as shown in the table below).  Customers using Braze's EU database should use `https://rest.fra-01.braze.eu/`. For more information on REST API endpoints for customers using Braze's EU database see our [EU/US Implementation Differences documentation](https://www.braze.com/docs/developer_guide/eu01_us3_sdk_implementation_differences/overview/).  ## Braze Instances  Instance    | Dashboard URL   | REST Endpoint ----------- |---------------- | -------------------- US-01 | `https://dashboard.braze.com` or<br> `https://dashboard-01.braze.com` | `https://rest.iad-01.braze.com` US-02 | `https://dashboard-02.braze.com` | `https://rest.iad-02.braze.com` US-03 | `https://dashboard-03.braze.com` | `https://rest.iad-03.braze.com` US-04 | `https://dashboard-04.braze.com` | `https://rest.iad-04.braze.com` US-06 | `https://dashboard-06.braze.com` | `https://rest.iad-06.braze.com` EU-01 | `https://dashboard.braze.eu` or<br> `https://dashboard-01.braze.eu` | `https://rest.fra-01.braze.eu`   # Using Braze's Postman Collection   If you have a Postman account (MacOS, Windows, and Linux versions can be downloaded from their website located [here](https://www.getpostman.com)), you can go to our Postman documentation and click the orange `Run in Postman` button in the top, right corner. This will allow you to [create an environment](#setting-up-your-postman-environment), as well as edit the available `POST` and `GET` requests to suit your own needs.  ## Setting Up Your Postman Environment  The Braze Postman Collection uses a templating variable, `{{instance_url}}`, to substitute the REST API URL of your Braze instance into the pre-built requests. Rather than having to manually edit all requests in the Collection, you can set up this variable in your Postman environment. To do so, please follow the steps below:  1. Click on the gear icon in the top right corner of the Postman app.  2. Select \"Manage Environments\" to open a modal window which displays your active environments. 3. In the bottom right corner of the modal window, click \"Add\" to create a new environment. 4. Give this environment a name (e.g. \"Braze API Requests\") and add keys for `instance_url` and `api_key` with values corresponding to [your Braze instance](https://www.braze.com/docs/api/basics/#endpoints) and [Braze REST API Key](https://www.braze.com/docs/api/basics/#app-group-rest-api-keys), as pictured below.   As of April, 2020 Braze has changed how we read App Group API keys. Instead of passing them in the request body or through url parameters, we now read the App Group Rest`api_key` through the HTTP Authorization header. API keys not passed through the HTTP Authorization Header will coninue to work until they have been sunset.   ## Using the Pre-Built Requests from the Collection  Once you have configured your environment. You can use any of the pre-built requests in the collection as a template for building new API requests. To start using one of the pre-built requests, simply click on it within the 'Collections' menu on the left side of Postman. This will open the request as a new tab in the main window of the Postman app.  In general, there are two types of requests that Braze's API endpoints accept - `GET` and `POST`. Depending on which `HTTP` method the endpoint uses, you'll need to edit the pre-built request differently.  ### Edit a POST Request  When editing a `POST` request, you'll need to open the request and navigate to the `Body` section in the request editor. For readability, select the `raw` radio button to format the `JSON` request body.  ### Edit a GET Request  When editing a `GET` request, you will need to edit the parameters passed in the request URL. To edit these easily, select the `Params` button next to the URL bar and edit the key-value pairs in the fields that will appear below the URL bar.  ## Send Your Request  Once your API request is ready to send, click on the 'Send' button next to the URL bar. The request will be sent and the response data will be populated in a section underneath the request editor. From here, you can view the raw data returned from Braze's API, see the HTTP response code, see how long the request took to process, and view header information.
 *
 * The version of the OpenAPI document: 1.0.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */


import ApiClient from "../ApiClient";

/**
* KPI service.
* @module api/KPIApi
* @version 1.0.0
*/
export default class KPIApi {

    /**
    * Constructs a new KPIApi. 
    * @alias module:api/KPIApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the dailyActiveUsersByDate_0 operation.
     * @callback module:api/KPIApi~dailyActiveUsersByDate_0Callback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Daily Active Users by Date
     * This endpoint allows you to retrieve a daily series of the total number of unique active users on each date.   ## Response  ```json Content-Type: application/json Authorization: Bearer YOUR-REST-API-KEY {     \"message\": (required, string) the status of the export, returns 'success' when completed without errors,     \"data\" : [         {             \"time\" : (string) date as ISO 8601 date,             \"dau\" : (int)         },         ...     ] } ```
     * @param {Object} opts Optional parameters
     * @param {String} [length] (Required) Integer  Max number of days before ending_at to include in the returned series - must be between 1 and 100 inclusive
     * @param {String} [endingAt] (Optional) DateTime (ISO 8601 string)  Point in time when the data series should end - defaults to time of the request
     * @param {String} [appId] (Optional) String  App API identifier; if excluded, results for all apps in app group will be returned
     * @param {module:api/KPIApi~dailyActiveUsersByDate_0Callback} callback The callback function, accepting three arguments: error, data, response
     */
    dailyActiveUsersByDate_0(opts, callback) {
      opts = opts || {};
      let postBody = null;

      let pathParams = {
      };
      let queryParams = {
        'length': opts['length'],
        'ending_at': opts['endingAt'],
        'app_id': opts['appId']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = [];
      let accepts = [];
      let returnType = null;
      return this.apiClient.callApi(
        '/kpi/dau/data_series', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the dailyNewUsersByDate_0 operation.
     * @callback module:api/KPIApi~dailyNewUsersByDate_0Callback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Daily New Users by Date
     * This endpoint allows you to retrieve a daily series of the total number of new users on each date.   ## Response  ```json Content-Type: application/json Authorization: Bearer YOUR-REST-API-KEY {     \"message\": (required, string) the status of the export, returns 'success' when completed without errors,     \"data\" : [         {             \"time\" : (string) date as ISO 8601 date,             \"new_users\" : (int)         },         ...     ] } ```
     * @param {Object} opts Optional parameters
     * @param {String} [length] (Required) Integer  Max number of days before ending_at to include in the returned series - must be between 1 and 100 inclusive
     * @param {String} [endingAt] (Optional) DateTime (ISO 8601 string)  Point in time when the data series should end - defaults to time of the request
     * @param {String} [appId] (Optional) String  App API identifier; if excluded, results for all apps in app group will be returned
     * @param {module:api/KPIApi~dailyNewUsersByDate_0Callback} callback The callback function, accepting three arguments: error, data, response
     */
    dailyNewUsersByDate_0(opts, callback) {
      opts = opts || {};
      let postBody = null;

      let pathParams = {
      };
      let queryParams = {
        'length': opts['length'],
        'ending_at': opts['endingAt'],
        'app_id': opts['appId']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = [];
      let accepts = [];
      let returnType = null;
      return this.apiClient.callApi(
        '/kpi/new_users/data_series', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the kpIsForDailyAppUninstallsByDate_0 operation.
     * @callback module:api/KPIApi~kpIsForDailyAppUninstallsByDate_0Callback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * KPIs for Daily App Uninstalls by Date
     * This endpoint allows you to retrieve a daily series of the total number of uninstalls on each date.  ## Response  ```json Content-Type: application/json Authorization: Bearer YOUR-REST-API-KEY {     \"message\": (required, string) the status of the export, returns 'success' when completed without errors,     \"data\" : [         {             \"time\" : (string) date as ISO 8601 date,             \"uninstalls\" : (int)         },         ...     ] } ```
     * @param {Object} opts Optional parameters
     * @param {String} [length] (Required) Integer  Max number of days before ending_at to include in the returned series - must be between 1 and 100 inclusive
     * @param {String} [endingAt] (Optional) DateTime (ISO 8601 string)  Point in time when the data series should end - defaults to time of the request
     * @param {String} [appId] (Optional) String  App API identifier; if excluded, results for all apps in app group will be returned
     * @param {module:api/KPIApi~kpIsForDailyAppUninstallsByDate_0Callback} callback The callback function, accepting three arguments: error, data, response
     */
    kpIsForDailyAppUninstallsByDate_0(opts, callback) {
      opts = opts || {};
      let postBody = null;

      let pathParams = {
      };
      let queryParams = {
        'length': opts['length'],
        'ending_at': opts['endingAt'],
        'app_id': opts['appId']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = [];
      let accepts = [];
      let returnType = null;
      return this.apiClient.callApi(
        '/kpi/uninstalls/data_series', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the monthlyActiveUsersForLast30Days_0 operation.
     * @callback module:api/KPIApi~monthlyActiveUsersForLast30Days_0Callback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Monthly Active Users for Last 30 Days
     * This endpoint allows you to retrieve a daily series of the total number of unique active users over a 30-day rolling window.  ## Response  ```json Content-Type: application/json Authorization: Bearer YOUR-REST-API-KEY {     \"message\": (required, string) the status of the export, returns 'success' when completed without errors,     \"data\" : [         {             \"time\" : (string) date as ISO 8601 date,             \"mau\" : (int)         },         ...     ] } ```
     * @param {Object} opts Optional parameters
     * @param {String} [length] (Required) Integer  Max number of days before ending_at to include in the returned series - must be between 1 and 100 inclusive
     * @param {String} [endingAt] (Optional) DateTime (ISO 8601 string)  Point in time when the data series should end - defaults to time of the request
     * @param {String} [appId] (Optional) String  App API identifier; if excluded, results for all apps in app group will be returned
     * @param {module:api/KPIApi~monthlyActiveUsersForLast30Days_0Callback} callback The callback function, accepting three arguments: error, data, response
     */
    monthlyActiveUsersForLast30Days_0(opts, callback) {
      opts = opts || {};
      let postBody = null;

      let pathParams = {
      };
      let queryParams = {
        'length': opts['length'],
        'ending_at': opts['endingAt'],
        'app_id': opts['appId']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = [];
      let accepts = [];
      let returnType = null;
      return this.apiClient.callApi(
        '/kpi/mau/data_series', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
