/**
 * Quick start - Telematics SDK
 * # Introduction We have prepared a set of APIs for quick start to integrate telematics SDK that powers mobile telematics inside 3rd party mobile applications.  * [CONTACT US](https://telematicssdk.com) * [SANDBOX](https://userdatahub.com) * [DEV.PORTAL](https://docs.telematicssdk.com) * [DEMO APP](https://raxeltelematics.com/telematics-app)   # Overview Datamotion provides telematics infrastructure for mobile applications.   Telematics SDK turns any smartphone into telematics data gathering device to collect Location, driving and behavior data. API services unlocks power of your mobile application  There are 3 groups of methods: * 1 - user management * 2 - statistics for mobile app * 3 - statistics for back-end(s)  in certain cases you will need SNS or any other notification services. read more [here](https://docs.telematicssdk.com/platform-features/sns) # Possible architecture  There are three common schemes that are used by our clients. These schemes can be combined * Collect, Process, Store (required: 1&2) * Collect, Process (required: 1& sns) * Collect (required 1&sns)   ## Collect, Process, Store ![Collect, Process, Store](https://website-cliparts-datamotion.s3.us-east-2.amazonaws.com/Dev.portal/Architecture+-+Collection%2C+processing%2C+storage)  ## Collect, Process ![Collect, Process](https://website-cliparts-datamotion.s3.us-east-2.amazonaws.com/Dev.portal/Architecture+-+Collection+and+processing)  ## Collect ![Collect](https://website-cliparts-datamotion.s3.us-east-2.amazonaws.com/Dev.portal/Architecture+-+Collection+only)  *** ![Telematic sdk](https://website-cliparts-datamotion.s3.us-east-2.amazonaws.com/Github/transportation_small.png)  # Common use-cases: * Safe and efficient driving * Usage-based insurance * Safe driving assessment * Driver assessment * Trip log * Geo-analysis * Accident monitoring * Driving engagements * Location based services * Realtime Tracking and beyond  # How to start * Register a [SANDBOX ACCOUNT](https://userdatahub.com) * Get [CREDENTIALS](https://docs.userdatahub.com/sandbox/credentials)  * Follow the guide from [DEVELOPER POERTAL](https://docs.telematicssdk.com)  # Authentication To create a user on datamotion platform, you require to use InstanceID and InstanceKEY. You can get it in Datahub -> management -> user-service credentials  Once you create a user, you will get Device token, JWT token and refresh token. then, you will use it for APIs
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
import TripsTripDetails200Response from '../model/TripsTripDetails200Response';
import UserSafeScoringAccumulatedValueV1ScoringsIndividual200Response from '../model/UserSafeScoringAccumulatedValueV1ScoringsIndividual200Response';
import UserSafeScoringDailyValueV1ScoringsIndividualDaily200Response from '../model/UserSafeScoringDailyValueV1ScoringsIndividualDaily200Response';
import UserStatisticeDailyValueV1StatisticsIndividualDaily200Response from '../model/UserStatisticeDailyValueV1StatisticsIndividualDaily200Response';
import UserStatisticsAccumulatedValueV1StatisticsIndividual200Response from '../model/UserStatisticsAccumulatedValueV1StatisticsIndividual200Response';

/**
* Class2ForMobileAppOptional service.
* @module api/Class2ForMobileAppOptionalApi
* @version 1.0.0
*/
export default class Class2ForMobileAppOptionalApi {

    /**
    * Constructs a new Class2ForMobileAppOptionalApi. 
    * @alias module:api/Class2ForMobileAppOptionalApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the tripsTripDetails operation.
     * @callback module:api/Class2ForMobileAppOptionalApi~tripsTripDetailsCallback
     * @param {String} error Error message, if any.
     * @param {module:model/TripsTripDetails200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Trips - trip details
     * Trips - trip details
     * @param {Object} opts Optional parameters
     * @param {String} [trackToken] 
     * @param {module:api/Class2ForMobileAppOptionalApi~tripsTripDetailsCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/TripsTripDetails200Response}
     */
    tripsTripDetails(opts, callback) {
      opts = opts || {};
      let postBody = null;

      let pathParams = {
      };
      let queryParams = {
        'trackToken': opts['trackToken']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = TripsTripDetails200Response;
      return this.apiClient.callApi(
        '/mobilesdk/stage/track/get_track/v1', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the userSafeScoringAccumulatedValueV1ScoringsIndividual operation.
     * @callback module:api/Class2ForMobileAppOptionalApi~userSafeScoringAccumulatedValueV1ScoringsIndividualCallback
     * @param {String} error Error message, if any.
     * @param {module:model/UserSafeScoringAccumulatedValueV1ScoringsIndividual200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * User safe scoring - Accumulated value - v1/Scorings/individual
     * Safe driving score API. This API is a part of Telematics API that we provide to our clients.  Rating description presents the universal approach, developed by our company on the basis of many years of experience; most of the input variables presented in this document could be adopted depending on the needs of the company and the focus on the specific characteristics of clients' driving style. Since 2019 we have moved to the 3rd Generation of the scoring model which allows distinguishing a context of events and add penalty points in accordance with a level of risk generated by an event  [More details](https://docs.telematicssdk.com)
     * @param {Object} opts Optional parameters
     * @param {String} [startDate] 
     * @param {String} [endDate] 
     * @param {module:api/Class2ForMobileAppOptionalApi~userSafeScoringAccumulatedValueV1ScoringsIndividualCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/UserSafeScoringAccumulatedValueV1ScoringsIndividual200Response}
     */
    userSafeScoringAccumulatedValueV1ScoringsIndividual(opts, callback) {
      opts = opts || {};
      let postBody = null;

      let pathParams = {
      };
      let queryParams = {
        'startDate': opts['startDate'],
        'endDate': opts['endDate']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = UserSafeScoringAccumulatedValueV1ScoringsIndividual200Response;
      return this.apiClient.callApi(
        '/statistics/v1/Scorings/individual/', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the userSafeScoringDailyValueV1ScoringsIndividualDaily operation.
     * @callback module:api/Class2ForMobileAppOptionalApi~userSafeScoringDailyValueV1ScoringsIndividualDailyCallback
     * @param {String} error Error message, if any.
     * @param {module:model/UserSafeScoringDailyValueV1ScoringsIndividualDaily200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * User safe scoring - daily value - /v1/Scorings/individual/daily
     * User safe scoring - daily value - /v1/Scorings/individual/daily
     * @param {Object} opts Optional parameters
     * @param {String} [tag] Optional
     * @param {String} [startDate] (Required) 
     * @param {String} [endDate] (Required) 
     * @param {module:api/Class2ForMobileAppOptionalApi~userSafeScoringDailyValueV1ScoringsIndividualDailyCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/UserSafeScoringDailyValueV1ScoringsIndividualDaily200Response}
     */
    userSafeScoringDailyValueV1ScoringsIndividualDaily(opts, callback) {
      opts = opts || {};
      let postBody = null;

      let pathParams = {
      };
      let queryParams = {
        'Tag': opts['tag'],
        'StartDate': opts['startDate'],
        'EndDate': opts['endDate']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = UserSafeScoringDailyValueV1ScoringsIndividualDaily200Response;
      return this.apiClient.callApi(
        '/statistics/v1/Scorings/individual/daily', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the userStatisticeDailyValueV1StatisticsIndividualDaily operation.
     * @callback module:api/Class2ForMobileAppOptionalApi~userStatisticeDailyValueV1StatisticsIndividualDailyCallback
     * @param {String} error Error message, if any.
     * @param {module:model/UserStatisticeDailyValueV1StatisticsIndividualDaily200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * User statistice - Daily value - v1/Statistics/individual/daily
     * User statistice - Daily value - v1/Statistics/individual/daily
     * @param {Object} opts Optional parameters
     * @param {String} [startDate] 
     * @param {String} [endDate] 
     * @param {module:api/Class2ForMobileAppOptionalApi~userStatisticeDailyValueV1StatisticsIndividualDailyCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/UserStatisticeDailyValueV1StatisticsIndividualDaily200Response}
     */
    userStatisticeDailyValueV1StatisticsIndividualDaily(opts, callback) {
      opts = opts || {};
      let postBody = null;

      let pathParams = {
      };
      let queryParams = {
        'startDate': opts['startDate'],
        'endDate': opts['endDate']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = UserStatisticeDailyValueV1StatisticsIndividualDaily200Response;
      return this.apiClient.callApi(
        '/statistics/v1/Statistics/individual/daily/', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the userStatisticsAccumulatedValueV1StatisticsIndividual operation.
     * @callback module:api/Class2ForMobileAppOptionalApi~userStatisticsAccumulatedValueV1StatisticsIndividualCallback
     * @param {String} error Error message, if any.
     * @param {module:model/UserStatisticsAccumulatedValueV1StatisticsIndividual200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * User statistics - Accumulated value - /v1/Statistics/individual
     * User statistics - Accumulated value - /v1/Statistics/individual
     * @param {Object} opts Optional parameters
     * @param {String} [startDate] 
     * @param {String} [endDate] 
     * @param {module:api/Class2ForMobileAppOptionalApi~userStatisticsAccumulatedValueV1StatisticsIndividualCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/UserStatisticsAccumulatedValueV1StatisticsIndividual200Response}
     */
    userStatisticsAccumulatedValueV1StatisticsIndividual(opts, callback) {
      opts = opts || {};
      let postBody = null;

      let pathParams = {
      };
      let queryParams = {
        'startDate': opts['startDate'],
        'endDate': opts['endDate']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = UserStatisticsAccumulatedValueV1StatisticsIndividual200Response;
      return this.apiClient.callApi(
        '/statistics/v1/Statistics/individual/', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
