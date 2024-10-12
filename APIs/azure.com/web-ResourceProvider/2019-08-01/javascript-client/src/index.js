/**
 *  API Client
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 2019-08-01
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */


import ApiClient from './ApiClient';
import BillingMeter from './model/BillingMeter';
import BillingMeterCollection from './model/BillingMeterCollection';
import CsmMoveResourceEnvelope from './model/CsmMoveResourceEnvelope';
import DeploymentLocations from './model/DeploymentLocations';
import DeploymentLocationsHostingEnvironmentsInner from './model/DeploymentLocationsHostingEnvironmentsInner';
import DeploymentLocationsHostingEnvironmentsInnerClusterSettingsInner from './model/DeploymentLocationsHostingEnvironmentsInnerClusterSettingsInner';
import DeploymentLocationsHostingEnvironmentsInnerEnvironmentCapacitiesInner from './model/DeploymentLocationsHostingEnvironmentsInnerEnvironmentCapacitiesInner';
import DeploymentLocationsHostingEnvironmentsInnerNetworkAccessControlListInner from './model/DeploymentLocationsHostingEnvironmentsInnerNetworkAccessControlListInner';
import DeploymentLocationsHostingEnvironmentsInnerVipMappingsInner from './model/DeploymentLocationsHostingEnvironmentsInnerVipMappingsInner';
import DeploymentLocationsHostingEnvironmentsInnerVirtualNetwork from './model/DeploymentLocationsHostingEnvironmentsInnerVirtualNetwork';
import DeploymentLocationsHostingEnvironmentsInnerWorkerPoolsInner from './model/DeploymentLocationsHostingEnvironmentsInnerWorkerPoolsInner';
import GeoRegion from './model/GeoRegion';
import GeoRegionCollection from './model/GeoRegionCollection';
import GetPublishingUser200Response from './model/GetPublishingUser200Response';
import GetPublishingUser200ResponseProperties from './model/GetPublishingUser200ResponseProperties';
import GetPublishingUserDefaultResponse from './model/GetPublishingUserDefaultResponse';
import GetPublishingUserDefaultResponseError from './model/GetPublishingUserDefaultResponseError';
import GetPublishingUserDefaultResponseErrorDetailsInner from './model/GetPublishingUserDefaultResponseErrorDetailsInner';
import GlobalCsmSkuDescription from './model/GlobalCsmSkuDescription';
import GlobalCsmSkuDescriptionCapabilitiesInner from './model/GlobalCsmSkuDescriptionCapabilitiesInner';
import GlobalCsmSkuDescriptionCapacity from './model/GlobalCsmSkuDescriptionCapacity';
import HostingEnvironmentDeploymentInfo from './model/HostingEnvironmentDeploymentInfo';
import ListSiteIdentifiersAssignedToHostName200Response from './model/ListSiteIdentifiersAssignedToHostName200Response';
import ListSiteIdentifiersAssignedToHostName200ResponseValueInner from './model/ListSiteIdentifiersAssignedToHostName200ResponseValueInner';
import ListSiteIdentifiersAssignedToHostName200ResponseValueInnerProperties from './model/ListSiteIdentifiersAssignedToHostName200ResponseValueInnerProperties';
import ListSiteIdentifiersAssignedToHostNameRequest from './model/ListSiteIdentifiersAssignedToHostNameRequest';
import PremierAddOnOffer from './model/PremierAddOnOffer';
import PremierAddOnOfferCollection from './model/PremierAddOnOfferCollection';
import ResourceNameAvailability from './model/ResourceNameAvailability';
import ResourceNameAvailabilityRequest from './model/ResourceNameAvailabilityRequest';
import SkuInfos from './model/SkuInfos';
import SourceControl from './model/SourceControl';
import SourceControlCollection from './model/SourceControlCollection';
import ValidateProperties from './model/ValidateProperties';
import ValidateRequest from './model/ValidateRequest';
import ValidateResponse from './model/ValidateResponse';
import ValidateResponseError from './model/ValidateResponseError';
import VnetParameters from './model/VnetParameters';
import VnetValidationFailureDetails from './model/VnetValidationFailureDetails';
import VnetValidationTestFailure from './model/VnetValidationTestFailure';
import DefaultApi from './api/DefaultApi';


/**
* JS API client generated by OpenAPI Generator.<br>
* The <code>index</code> module provides access to constructors for all the classes which comprise the public API.
* <p>
* An AMD (recommended!) or CommonJS application will generally do something equivalent to the following:
* <pre>
* var ApiClient = require('index'); // See note below*.
* var xxxSvc = new ApiClient.XxxApi(); // Allocate the API class we're going to use.
* var yyyModel = new ApiClient.Yyy(); // Construct a model instance.
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
* var xxxSvc = new ApiClient.XxxApi(); // Allocate the API class we're going to use.
* var yyy = new ApiClient.Yyy(); // Construct a model instance.
* yyyModel.someProperty = 'someValue';
* ...
* var zzz = xxxSvc.doSomething(yyyModel); // Invoke the service.
* ...
* </pre>
* </p>
* @module index
* @version 2019-08-01
*/
export {
    /**
     * The ApiClient constructor.
     * @property {module:ApiClient}
     */
    ApiClient,

    /**
     * The BillingMeter model constructor.
     * @property {module:model/BillingMeter}
     */
    BillingMeter,

    /**
     * The BillingMeterCollection model constructor.
     * @property {module:model/BillingMeterCollection}
     */
    BillingMeterCollection,

    /**
     * The CsmMoveResourceEnvelope model constructor.
     * @property {module:model/CsmMoveResourceEnvelope}
     */
    CsmMoveResourceEnvelope,

    /**
     * The DeploymentLocations model constructor.
     * @property {module:model/DeploymentLocations}
     */
    DeploymentLocations,

    /**
     * The DeploymentLocationsHostingEnvironmentsInner model constructor.
     * @property {module:model/DeploymentLocationsHostingEnvironmentsInner}
     */
    DeploymentLocationsHostingEnvironmentsInner,

    /**
     * The DeploymentLocationsHostingEnvironmentsInnerClusterSettingsInner model constructor.
     * @property {module:model/DeploymentLocationsHostingEnvironmentsInnerClusterSettingsInner}
     */
    DeploymentLocationsHostingEnvironmentsInnerClusterSettingsInner,

    /**
     * The DeploymentLocationsHostingEnvironmentsInnerEnvironmentCapacitiesInner model constructor.
     * @property {module:model/DeploymentLocationsHostingEnvironmentsInnerEnvironmentCapacitiesInner}
     */
    DeploymentLocationsHostingEnvironmentsInnerEnvironmentCapacitiesInner,

    /**
     * The DeploymentLocationsHostingEnvironmentsInnerNetworkAccessControlListInner model constructor.
     * @property {module:model/DeploymentLocationsHostingEnvironmentsInnerNetworkAccessControlListInner}
     */
    DeploymentLocationsHostingEnvironmentsInnerNetworkAccessControlListInner,

    /**
     * The DeploymentLocationsHostingEnvironmentsInnerVipMappingsInner model constructor.
     * @property {module:model/DeploymentLocationsHostingEnvironmentsInnerVipMappingsInner}
     */
    DeploymentLocationsHostingEnvironmentsInnerVipMappingsInner,

    /**
     * The DeploymentLocationsHostingEnvironmentsInnerVirtualNetwork model constructor.
     * @property {module:model/DeploymentLocationsHostingEnvironmentsInnerVirtualNetwork}
     */
    DeploymentLocationsHostingEnvironmentsInnerVirtualNetwork,

    /**
     * The DeploymentLocationsHostingEnvironmentsInnerWorkerPoolsInner model constructor.
     * @property {module:model/DeploymentLocationsHostingEnvironmentsInnerWorkerPoolsInner}
     */
    DeploymentLocationsHostingEnvironmentsInnerWorkerPoolsInner,

    /**
     * The GeoRegion model constructor.
     * @property {module:model/GeoRegion}
     */
    GeoRegion,

    /**
     * The GeoRegionCollection model constructor.
     * @property {module:model/GeoRegionCollection}
     */
    GeoRegionCollection,

    /**
     * The GetPublishingUser200Response model constructor.
     * @property {module:model/GetPublishingUser200Response}
     */
    GetPublishingUser200Response,

    /**
     * The GetPublishingUser200ResponseProperties model constructor.
     * @property {module:model/GetPublishingUser200ResponseProperties}
     */
    GetPublishingUser200ResponseProperties,

    /**
     * The GetPublishingUserDefaultResponse model constructor.
     * @property {module:model/GetPublishingUserDefaultResponse}
     */
    GetPublishingUserDefaultResponse,

    /**
     * The GetPublishingUserDefaultResponseError model constructor.
     * @property {module:model/GetPublishingUserDefaultResponseError}
     */
    GetPublishingUserDefaultResponseError,

    /**
     * The GetPublishingUserDefaultResponseErrorDetailsInner model constructor.
     * @property {module:model/GetPublishingUserDefaultResponseErrorDetailsInner}
     */
    GetPublishingUserDefaultResponseErrorDetailsInner,

    /**
     * The GlobalCsmSkuDescription model constructor.
     * @property {module:model/GlobalCsmSkuDescription}
     */
    GlobalCsmSkuDescription,

    /**
     * The GlobalCsmSkuDescriptionCapabilitiesInner model constructor.
     * @property {module:model/GlobalCsmSkuDescriptionCapabilitiesInner}
     */
    GlobalCsmSkuDescriptionCapabilitiesInner,

    /**
     * The GlobalCsmSkuDescriptionCapacity model constructor.
     * @property {module:model/GlobalCsmSkuDescriptionCapacity}
     */
    GlobalCsmSkuDescriptionCapacity,

    /**
     * The HostingEnvironmentDeploymentInfo model constructor.
     * @property {module:model/HostingEnvironmentDeploymentInfo}
     */
    HostingEnvironmentDeploymentInfo,

    /**
     * The ListSiteIdentifiersAssignedToHostName200Response model constructor.
     * @property {module:model/ListSiteIdentifiersAssignedToHostName200Response}
     */
    ListSiteIdentifiersAssignedToHostName200Response,

    /**
     * The ListSiteIdentifiersAssignedToHostName200ResponseValueInner model constructor.
     * @property {module:model/ListSiteIdentifiersAssignedToHostName200ResponseValueInner}
     */
    ListSiteIdentifiersAssignedToHostName200ResponseValueInner,

    /**
     * The ListSiteIdentifiersAssignedToHostName200ResponseValueInnerProperties model constructor.
     * @property {module:model/ListSiteIdentifiersAssignedToHostName200ResponseValueInnerProperties}
     */
    ListSiteIdentifiersAssignedToHostName200ResponseValueInnerProperties,

    /**
     * The ListSiteIdentifiersAssignedToHostNameRequest model constructor.
     * @property {module:model/ListSiteIdentifiersAssignedToHostNameRequest}
     */
    ListSiteIdentifiersAssignedToHostNameRequest,

    /**
     * The PremierAddOnOffer model constructor.
     * @property {module:model/PremierAddOnOffer}
     */
    PremierAddOnOffer,

    /**
     * The PremierAddOnOfferCollection model constructor.
     * @property {module:model/PremierAddOnOfferCollection}
     */
    PremierAddOnOfferCollection,

    /**
     * The ResourceNameAvailability model constructor.
     * @property {module:model/ResourceNameAvailability}
     */
    ResourceNameAvailability,

    /**
     * The ResourceNameAvailabilityRequest model constructor.
     * @property {module:model/ResourceNameAvailabilityRequest}
     */
    ResourceNameAvailabilityRequest,

    /**
     * The SkuInfos model constructor.
     * @property {module:model/SkuInfos}
     */
    SkuInfos,

    /**
     * The SourceControl model constructor.
     * @property {module:model/SourceControl}
     */
    SourceControl,

    /**
     * The SourceControlCollection model constructor.
     * @property {module:model/SourceControlCollection}
     */
    SourceControlCollection,

    /**
     * The ValidateProperties model constructor.
     * @property {module:model/ValidateProperties}
     */
    ValidateProperties,

    /**
     * The ValidateRequest model constructor.
     * @property {module:model/ValidateRequest}
     */
    ValidateRequest,

    /**
     * The ValidateResponse model constructor.
     * @property {module:model/ValidateResponse}
     */
    ValidateResponse,

    /**
     * The ValidateResponseError model constructor.
     * @property {module:model/ValidateResponseError}
     */
    ValidateResponseError,

    /**
     * The VnetParameters model constructor.
     * @property {module:model/VnetParameters}
     */
    VnetParameters,

    /**
     * The VnetValidationFailureDetails model constructor.
     * @property {module:model/VnetValidationFailureDetails}
     */
    VnetValidationFailureDetails,

    /**
     * The VnetValidationTestFailure model constructor.
     * @property {module:model/VnetValidationTestFailure}
     */
    VnetValidationTestFailure,

    /**
    * The DefaultApi service constructor.
    * @property {module:api/DefaultApi}
    */
    DefaultApi
};
