/**
 * agentOS API V3, Diary Call Group
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: v3-diary
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */


import ApiClient from './ApiClient';
import AdvertisingBranchModel from './model/AdvertisingBranchModel';
import AdvertisingBranchModelResults from './model/AdvertisingBranchModelResults';
import BaseHypermediaLink from './model/BaseHypermediaLink';
import DiaryAppointmentDetails from './model/DiaryAppointmentDetails';
import DiaryAppointmentModel from './model/DiaryAppointmentModel';
import DiaryAppointmentModelResults from './model/DiaryAppointmentModelResults';
import DiaryAppointmentTypeModel from './model/DiaryAppointmentTypeModel';
import DiaryAppointmentTypeModelResults from './model/DiaryAppointmentTypeModelResults';
import DiaryBookingModel from './model/DiaryBookingModel';
import DiaryGuestDetails from './model/DiaryGuestDetails';
import FeedbackSubmissionModel from './model/FeedbackSubmissionModel';
import GuestDiaryParametersModel from './model/GuestDiaryParametersModel';
import GuestDiaryParametersResultsModel from './model/GuestDiaryParametersResultsModel';
import LatestTenancyModel from './model/LatestTenancyModel';
import LinkedGuestModel from './model/LinkedGuestModel';
import LinkedLandlordModel from './model/LinkedLandlordModel';
import LinkedPropertiesModel from './model/LinkedPropertiesModel';
import LinkedTenantModel from './model/LinkedTenantModel';
import CompanyControllerApi from './api/CompanyControllerApi';
import DiaryControllerApi from './api/DiaryControllerApi';


/**
* JS API client generated by OpenAPI Generator.<br>
* The <code>index</code> module provides access to constructors for all the classes which comprise the public API.
* <p>
* An AMD (recommended!) or CommonJS application will generally do something equivalent to the following:
* <pre>
* var AgentOsApiV3DiaryCallGroup = require('index'); // See note below*.
* var xxxSvc = new AgentOsApiV3DiaryCallGroup.XxxApi(); // Allocate the API class we're going to use.
* var yyyModel = new AgentOsApiV3DiaryCallGroup.Yyy(); // Construct a model instance.
* yyyModel.someProperty = 'someValue';
* ...
* var zzz = xxxSvc.doSomething(yyyModel); // Invoke the service.
* ...
* </pre>
* <em>*NOTE: For a top-level AMD script, use require(['index'], function(){...})
* and put the application logic within the callback function.</em>
* </p>
* <p>
* A non-AMD browser application (discouraged) might do something like this:
* <pre>
* var xxxSvc = new AgentOsApiV3DiaryCallGroup.XxxApi(); // Allocate the API class we're going to use.
* var yyy = new AgentOsApiV3DiaryCallGroup.Yyy(); // Construct a model instance.
* yyyModel.someProperty = 'someValue';
* ...
* var zzz = xxxSvc.doSomething(yyyModel); // Invoke the service.
* ...
* </pre>
* </p>
* @module index
* @version v3-diary
*/
export {
    /**
     * The ApiClient constructor.
     * @property {module:ApiClient}
     */
    ApiClient,

    /**
     * The AdvertisingBranchModel model constructor.
     * @property {module:model/AdvertisingBranchModel}
     */
    AdvertisingBranchModel,

    /**
     * The AdvertisingBranchModelResults model constructor.
     * @property {module:model/AdvertisingBranchModelResults}
     */
    AdvertisingBranchModelResults,

    /**
     * The BaseHypermediaLink model constructor.
     * @property {module:model/BaseHypermediaLink}
     */
    BaseHypermediaLink,

    /**
     * The DiaryAppointmentDetails model constructor.
     * @property {module:model/DiaryAppointmentDetails}
     */
    DiaryAppointmentDetails,

    /**
     * The DiaryAppointmentModel model constructor.
     * @property {module:model/DiaryAppointmentModel}
     */
    DiaryAppointmentModel,

    /**
     * The DiaryAppointmentModelResults model constructor.
     * @property {module:model/DiaryAppointmentModelResults}
     */
    DiaryAppointmentModelResults,

    /**
     * The DiaryAppointmentTypeModel model constructor.
     * @property {module:model/DiaryAppointmentTypeModel}
     */
    DiaryAppointmentTypeModel,

    /**
     * The DiaryAppointmentTypeModelResults model constructor.
     * @property {module:model/DiaryAppointmentTypeModelResults}
     */
    DiaryAppointmentTypeModelResults,

    /**
     * The DiaryBookingModel model constructor.
     * @property {module:model/DiaryBookingModel}
     */
    DiaryBookingModel,

    /**
     * The DiaryGuestDetails model constructor.
     * @property {module:model/DiaryGuestDetails}
     */
    DiaryGuestDetails,

    /**
     * The FeedbackSubmissionModel model constructor.
     * @property {module:model/FeedbackSubmissionModel}
     */
    FeedbackSubmissionModel,

    /**
     * The GuestDiaryParametersModel model constructor.
     * @property {module:model/GuestDiaryParametersModel}
     */
    GuestDiaryParametersModel,

    /**
     * The GuestDiaryParametersResultsModel model constructor.
     * @property {module:model/GuestDiaryParametersResultsModel}
     */
    GuestDiaryParametersResultsModel,

    /**
     * The LatestTenancyModel model constructor.
     * @property {module:model/LatestTenancyModel}
     */
    LatestTenancyModel,

    /**
     * The LinkedGuestModel model constructor.
     * @property {module:model/LinkedGuestModel}
     */
    LinkedGuestModel,

    /**
     * The LinkedLandlordModel model constructor.
     * @property {module:model/LinkedLandlordModel}
     */
    LinkedLandlordModel,

    /**
     * The LinkedPropertiesModel model constructor.
     * @property {module:model/LinkedPropertiesModel}
     */
    LinkedPropertiesModel,

    /**
     * The LinkedTenantModel model constructor.
     * @property {module:model/LinkedTenantModel}
     */
    LinkedTenantModel,

    /**
    * The CompanyControllerApi service constructor.
    * @property {module:api/CompanyControllerApi}
    */
    CompanyControllerApi,

    /**
    * The DiaryControllerApi service constructor.
    * @property {module:api/DiaryControllerApi}
    */
    DiaryControllerApi
};
