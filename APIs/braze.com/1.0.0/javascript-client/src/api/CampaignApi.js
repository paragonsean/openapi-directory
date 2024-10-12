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
* Campaign service.
* @module api/CampaignApi
* @version 1.0.0
*/
export default class CampaignApi {

    /**
    * Constructs a new CampaignApi. 
    * @alias module:api/CampaignApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the campaignAnalytics_0 operation.
     * @callback module:api/CampaignApi~campaignAnalytics_0Callback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Campaign Analytics
     * This endpoint allows you to retrieve a daily series of various stats for a campaign over time. Data returned includes how many messages were sent, opened, clicked, converted, etc., broken down by message channel.   ### Components Used -[Campaign Identifier](https://www.braze.com/docs/api/identifier_types/)   ### Responses  #### Multi-Channel Response  ```json Content-Type: application/json Authorization: Bearer YOUR-REST-API-KEY {     \"message\": (required, string) the status of the export, returns 'success' when completed without errors,     \"data\" : [         {             \"time\" : (string) date as ISO 8601 date,             \"messages\" : {                 \"ios_push\" : [                     {                       \"variation_name\": \"iOS_Push\",                       \"sent\" : (int),                       \"direct_opens\" : (int),                       \"total_opens\" : (int),                       \"bounces\" : (int),                       \"body_clicks\" : (int)                       \"revenue\": 0,                       \"unique_recipients\": 1,                       \"conversions\": 0,                       \"conversions_by_send_time\": 0,                       \"conversions1\": 0,                       \"conversions1_by_send_time\": 0,                       \"conversions2\": 0,                       \"conversions2_by_send_time\": 0,                       \"conversions3\": 0,                       \"conversions3_by_send_time\": 0,                       \"carousel_slide_[NUM]_[TITLE]_click\": (optional, int),                       \"notif_button_[NUM]_[TITLE]_click\": (optional, int)                     }                 ],                 \"android_push\" : [                     {                       \"sent\" : (int),                       \"direct_opens\" : (int),                       \"total_opens\" : (int),                       \"bounces\" : (int),                       \"body_clicks\" : (int)                     }                 ],                 \"webhook\": [                     {                       \"sent\": (int),                       \"errors\": (int)                     }                 ],                 \"email\" : [                     {                       \"sent\": (int),                       \"opens\": (int),                       \"unique_opens\": (int),                       \"clicks\": (int),                       \"unique_clicks\": (int),                       \"unsubscribes\": (int),                       \"bounces\": (int),                       \"delivered\": (int),                       \"reported_spam\": (int)                     }                 ],                 \"sms\" : [                   {                     \"sent\": (int),                     \"delivered\": (int),                     \"undelivered\": (int),                     \"delivery_failed\": (int)                   }                 ]               },            \"conversions_by_send_time\": (optional, int),            \"conversions1_by_send_time\": (optional, int),            \"conversions2_by_send_time\": (optional, int),            \"conversions3_by_send_time\": (optional, int),            \"conversions\": (int),            \"conversions1\": (optional, int),            \"conversions2\": (optional, int),            \"conversions3\": (optional, int),            \"unique_recipients\": (int),            \"revenue\": (optional, float)         },         ...     ],     ... } ```  #### Multivariate Response  ```json Content-Type: application/json Authorization: Bearer YOUR-REST-API-KEY {     \"data\" : [         {             \"time\" : (string) date as ISO 8601 date,             \"conversions\" : (int),             \"revenue\": (float),             \"conversions_by_send_time\": (int),             \"messages\" : {                \"trigger_in_app_message\": [{           \"variation_name\": (optional, string),           \"impressions\": (int),           \"clicks\": (int),           \"first_button_clicks\": (int),           \"second_button_clicks\": (int),           \"revenue\": (optional, float),,           \"unique_recipients\": (int),           \"conversions\": (optional, int),           \"conversions_by_send_time\": (optional, int),           \"conversions1\": (optional, int),           \"conversions1_by_send_time\": (optional, int),           \"conversions2\": (optional, int),           \"conversions2_by_send_time\": (optional, int),           \"conversions3\": (optional, int),           \"conversions3_by_send_time\": (optional, int)          }, {           \"variation_name\": (optional, string),           \"impressions\": (int),           \"clicks\": (int),           \"first_button_clicks\": (int),           \"second_button_clicks\": (int),           \"revenue\": (optional, float),,           \"unique_recipients\": (int),           \"conversions\": (optional, int),           \"conversions_by_send_time\": (optional, int),           \"conversions1\": (optional, int),           \"conversions1_by_send_time\": (optional, int),           \"conversions2\": (optional, int),           \"conversions2_by_send_time\": (optional, int),           \"conversions3\": (optional, int).           \"conversions3_by_send_time\": (optional, int)          }, {           \"variation_name\": (optional, string),           \"revenue\": (optional, float),,           \"unique_recipients\": (int),           \"conversions\": (optional, int),           \"conversions_by_send_time\": (optional, int),           \"conversions1\": (optional, int),           \"conversions1_by_send_time\": (optional, int),           \"conversions2\": (optional, int),           \"conversions2_by_send_time\": (optional, int),           \"conversions3\": (optional, int),           \"conversions3_by_send_time\": (optional, int),           \"enrolled\": (optional, int)          }]         },         \"conversions_by_send_time\": (optional, int),         \"conversions1_by_send_time\": (optional, int),         \"conversions2_by_send_time\": (optional, int),         \"conversions3_by_send_time\": (optional, int),         \"conversions\": (optional, int,         \"conversions1\": (optional, int),         \"conversions2\": (optional, int),         \"conversions3\": (optional, int),         \"unique_recipients\": (int),         \"revenue\": (optional, float)          }],          ... } ```  Possible message types are `email`, `in_app_message`, `webhook`, `android_push`, `apple_push`, `kindle_push`, `web_push`, `windows_phone8_push`, and `windows_universal_push`. All push message types will have the same statistics shown for `android_push` above.
     * @param {Object} opts Optional parameters
     * @param {String} [campaignId] (Required) String  Campaign API identifier
     * @param {String} [length] (Required) Integer  Max number of days before ending_at to include in the returned series - must be between 1 and 100 inclusive
     * @param {String} [endingAt] (Optional) DateTime (ISO 8601 string)  Date on which the data series should end - defaults to time of the request
     * @param {module:api/CampaignApi~campaignAnalytics_0Callback} callback The callback function, accepting three arguments: error, data, response
     */
    campaignAnalytics_0(opts, callback) {
      opts = opts || {};
      let postBody = null;

      let pathParams = {
      };
      let queryParams = {
        'campaign_id': opts['campaignId'],
        'length': opts['length'],
        'ending_at': opts['endingAt']
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
        '/campaigns/data_series', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the campaignDetails_0 operation.
     * @callback module:api/CampaignApi~campaignDetails_0Callback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Campaign Details
     * This endpoint allows you to retrieve relevant information on a specified campaign, which can be identified by the `campaign_id`.   > The campaign_id for API campaigns can be found on the Developer Console page and the campaign details page within your dashboard or you can use the Campaign List Endpoint.  ### Components Used - [Campaign Identifier](https://www.braze.com/docs/api/identifier_types/)   ### Campaign Details Endpoint API Response  ```json Content-Type: application/json Authorization: Bearer YOUR-REST-API-KEY {     \"message\": (required, string) the status of the export, returns 'success' when completed without errors,     \"created_at\" : (string) date created as ISO 8601 date,     \"updated_at\" : (string) date last updated as ISO 8601 date,     \"archived\": (boolean) whether this Campaign is archived,     \"draft\": (boolean) whether this Campaign is a draft,     \"name\" : (string) campaign name,     \"description\" : (string) campaign description,     \"schedule_type\" : (string) type of scheduling action,     \"channels\" : (array) list of channels to send via,     \"first_sent\" : (string) date and hour of first sent as ISO 8601 date,     \"last_sent\" : (string) date and hour of last sent as ISO 8601 date,     \"tags\" : (array) tag names associated with the campaign,     \"messages\": {         \"message_variation_id\": (string) { // <=This is the actual id             \"channel\": (string) channel type of the message (as in, \"email\", \"ios_push\", \"webhook\", \"content_card\", \"in-app_message\", \"sms\"),             \"name\": (string) name of the message in the Dashboard (eg., \"Variation 1\")             ... channel-specific fields for this message, see below ...         }     },     \"conversion_behaviors\": (array) conversion event behaviors assigned to the campaign (see below) } ```  #### Messages  The `messages` response will contain information about each message. Example message responses for channels are below:  ##### Push Channels  ```json {     \"channel\": (string) description of the channel, such as \"ios_push\" or \"android_push\"     \"alert\": (string) alert body text,     \"extras\": (hash) any key value pairs provided } ```  ##### Email Channel  ```json {     \"channel\": \"email\",     \"subject\": (string) subject,     \"body\": (string) HTML body,     \"from\": (string) from address and display name,     \"reply_to\": (string) reply-to for message, if different than \"from\" address,     \"title\": (string) name of the email,     \"extras\": (hash) any key value pairs provided } ```  ##### Content Card Channel  ```json {     \"channel\": \"content_cards\",     \"name\": (string) name of variant,     \"extras\": (hash) any key value pairs provided; only present if at least one key-value pair has been set } ```  ##### Webhook Channel  ```json {     \"channel\": \"webhook\",     \"url\": (string) url for webhook,     \"body\": (string) payload body,     \"type\": (string) body content type,     \"headers\": (hash) specified request headers,     \"method\": (string) HTTP method (e.g., \"POST\" or \"GET\"), } ```  ##### SMS Channel  ```json {   \"channel\": \"sms\",   \"body\": (string) payload body,   \"from\": (string) list of numbers associated with the subscription group,   \"subscription_group_id\": (string) API id of the subscription group targeted in the SMS message } ```  ##### Control Messages  ```json {     \"channel\": (string) description of the channel that the control is for,     \"type\": \"control\" } ```  #### Conversion Behaviors  The `conversion_behaviors` array will contain information about each conversion event behavior set for the campaign. These behaviors are in order as set by the campaign. For example, Conversion Event A will be the first item in the array, Conversion Event B will be second, etc. Example conversion event behavior responses for are below:  ##### Clicks Email  ```json {     \"type\": \"Clicks Email\",     \"window\": (integer) number of seconds during which the user can convert on this event, i.e. - 86400, which is 24 hours } ```  ##### Opens Email  ```json {     \"type\": \"Opens Email\",     \"window\": (integer) number of seconds during which the user can convert on this event, i.e. - 86400, which is 24 hours } ```  ##### Makes Purchase (any purchase)  ```json {     \"type\": \"Makes Any Purchase\",     \"window\": (integer) number of seconds during which the user can convert on this event, i.e. - 86400, which is 24 hours } ```  ##### Makes Purchase (specific product)  ```json {     \"type\": \"Makes Specific Purchase\",     \"window\": (integer) number of seconds during which the user can convert on this event, i.e. - 86400, which is 24 hours,     \"product\": (string) name of the product, i.e. - \"Feline Body Armor\" } ```  ##### Performs Custom Event  ```json {     \"type\": \"Performs Custom Event\",     \"window\": (integer) number of seconds during which the user can convert on this event, i.e. - 86400, which is 24 hours,     \"custom_event_name\": (string) name of the event, i.e. - \"Used Feline Body Armor\" } ```  ##### Upgrades App  ```json {     \"type\": \"Upgrades App\",     \"window\": (integer) number of seconds during which the user can convert on this event, i.e. - 86400, which is 24 hours,     \"app_ids\": (array|null) array of app ids, i.e. - [\"12345\", \"67890\"], or `null` if \"Track sessions for any app\" is selected in the UI } ```  ##### Uses App  ```json {     \"type\": \"Starts Session\",     \"window\": (integer) number of seconds during which the user can convert on this event, i.e. - 86400, which is 24 hours,     \"app_ids\": (array|null) array of app ids, i.e. - [\"12345\", \"67890\"], or `null` if \"Track sessions for any app\" is selected in the UI } ```
     * @param {Object} opts Optional parameters
     * @param {String} [campaignId] (Required) String  Campaign API identifier
     * @param {module:api/CampaignApi~campaignDetails_0Callback} callback The callback function, accepting three arguments: error, data, response
     */
    campaignDetails_0(opts, callback) {
      opts = opts || {};
      let postBody = null;

      let pathParams = {
      };
      let queryParams = {
        'campaign_id': opts['campaignId']
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
        '/campaigns/details', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the campaignList_0 operation.
     * @callback module:api/CampaignApi~campaignList_0Callback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Campaign List
     * This endpoint allows you to export a list of campaigns, each of which will include its name, Campaign API Identifier, whether it is an API Campaign, and Tags associated with the campaign. The campaigns are returned in groups of 100 sorted by time of creation (oldest to newest by default).  ## Campaign List Endpoint API Response  ```json Content-Type: application/json Authorization: Bearer YOUR-REST-API-KEY {     \"message\": (required, string) the status of the export, returns 'success' when completed without errors,     \"campaigns\" : [         {             \"id\" : (string) Campaign API Identifier,             \"last_edited\": (ISO 8601 string) the last edited time for the message              \"name\" : (string) campaign name,             \"is_api_campaign\" : (boolean) whether the campaign is an API Campaign,             \"tags\" : (array) tag names associated with the campaign         },         ...     ] } ```
     * @param {Object} opts Optional parameters
     * @param {String} [page] (Optional) Integer  The page of campaigns to return, defaults to 0 (returns the first set of up to 100)
     * @param {String} [includeArchived] (Optional) Boolean  Whether or not to include archived campaigns, defaults to false
     * @param {String} [sortDirection] (Optional) String  Pass in the value `desc` to sort by creation time from newest to oldest. Pass in `asc` to sort from oldest to newest. If sort_direction is not included, the default order is oldest to newest.
     * @param {String} [lastEditTimeGt] (Optional) DateTime (ISO 8601 string)  Filters the results and only returns campaigns that were edited greater than the time provided till now. 
     * @param {module:api/CampaignApi~campaignList_0Callback} callback The callback function, accepting three arguments: error, data, response
     */
    campaignList_0(opts, callback) {
      opts = opts || {};
      let postBody = null;

      let pathParams = {
      };
      let queryParams = {
        'page': opts['page'],
        'include_archived': opts['includeArchived'],
        'sort_direction': opts['sortDirection'],
        'last_edit.time[gt]': opts['lastEditTimeGt']
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
        '/campaigns/list', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the sendAnalytics_0 operation.
     * @callback module:api/CampaignApi~sendAnalytics_0Callback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Send Analytics
     * This endpoint allows you to retrieve a daily series of various stats for a tracked `send_id`. Braze stores send analytics for 14 days after the send.  Campaign conversions will be attributed towards the most recent send id that a given user has received from the campaign.  > The `send_id` is only generated for API campaign sends targeting segments, connected audiences or broadcasts. When relevant, the `send_id` is included in response for the `messages/send`, `messages/schedule`, `campaign/trigger/send` and `campaign/trigger/schedule` endpoints.  ### Components Used - [Campaign Identifier](https://www.braze.com/docs/api/identifier_types/)  ### Send Analytics Endpoint API Response  ```json Content-Type: application/json Authorization: Bearer YOUR-REST-API-KEY {             \"variation_name\": (string) variation name,             \"sent\": (int) the number of sends,             \"delivered\": (int) the number of messages successfully delivered,             \"undelivered\": (int) the number of undelivered,             \"delivery_failed\": (int) the number of rejected,             \"direct_opens\": (int) the number of direct opens,             \"total_opens\": (int) the number of total opens,             \"bounces\": (int) the number of bounces,             \"body_clicks\": (int) the number of body clicks,             \"revenue\": (float) the number of dollars of revenue (USD),             \"unique_recipients\": (int) the number of unique recipients,             \"conversions\": (int) the number of conversions,             \"conversions_by_send_time\": (int) the number of conversions,             \"conversions1\": (int, optional) the number of conversions for the second conversion event,             \"conversions1_by_send_time\": (int, optional) the number of conversions for the second conversion event by send time,             \"conversions2\": (int, optional) the number of conversions for the third conversion event,             \"conversions2_by_send_time\": (int, optional) the number of conversions for the third conversion event by send time,             \"conversions3\": (int, optional) the number of conversions for the fourth conversion event,             \"conversions3_by_send_time\": (int, optional) the number of conversions for the fourth conversion event by send time           }         ]       },       \"conversions_by_send_time\": 0,       \"conversions1_by_send_time\": 0,       \"conversions2_by_send_time\": 0,       \"conversions3_by_send_time\": 0,       \"conversions\": 0,       \"conversions1\": 0,       \"conversions2\": 0,       \"conversions3\": 0,       \"unique_recipients\": 1,       \"revenue\": 0     }   ],   \"message\": \"success\" } ```
     * @param {Object} opts Optional parameters
     * @param {String} [campaignId] (Required) String  Campaign API identifier.
     * @param {String} [sendId] (Required) String  Send API identifier.
     * @param {String} [length] (Required) Integer  Maximum number of days before `ending_at` to include in the returned series. Must be between 1 and 100 inclusive.
     * @param {String} [endingAt] (Optional) Datetime ISO 8601 string  Date on which the data series should end. Defaults to time of the request.
     * @param {module:api/CampaignApi~sendAnalytics_0Callback} callback The callback function, accepting three arguments: error, data, response
     */
    sendAnalytics_0(opts, callback) {
      opts = opts || {};
      let postBody = null;

      let pathParams = {
      };
      let queryParams = {
        'campaign_id': opts['campaignId'],
        'send_id': opts['sendId'],
        'length': opts['length'],
        'ending_at': opts['endingAt']
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
        '/sends/data_series', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
