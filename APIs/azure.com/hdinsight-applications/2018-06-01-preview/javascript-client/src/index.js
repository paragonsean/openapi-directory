/**
 * HDInsightManagementClient
 * The HDInsight Management Client.
 *
 * The version of the OpenAPI document: 2018-06-01-preview
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */


import ApiClient from './ApiClient';
import Application from './model/Application';
import ApplicationGetEndpoint from './model/ApplicationGetEndpoint';
import ApplicationGetHttpsEndpoint from './model/ApplicationGetHttpsEndpoint';
import ApplicationListResult from './model/ApplicationListResult';
import ApplicationProperties from './model/ApplicationProperties';
import ApplicationPropertiesComputeProfile from './model/ApplicationPropertiesComputeProfile';
import ApplicationPropertiesComputeProfileRolesInner from './model/ApplicationPropertiesComputeProfileRolesInner';
import ApplicationPropertiesComputeProfileRolesInnerAutoscale from './model/ApplicationPropertiesComputeProfileRolesInnerAutoscale';
import ApplicationPropertiesComputeProfileRolesInnerAutoscaleCapacity from './model/ApplicationPropertiesComputeProfileRolesInnerAutoscaleCapacity';
import ApplicationPropertiesComputeProfileRolesInnerAutoscaleRecurrence from './model/ApplicationPropertiesComputeProfileRolesInnerAutoscaleRecurrence';
import ApplicationPropertiesComputeProfileRolesInnerAutoscaleRecurrenceScheduleInner from './model/ApplicationPropertiesComputeProfileRolesInnerAutoscaleRecurrenceScheduleInner';
import ApplicationPropertiesComputeProfileRolesInnerAutoscaleRecurrenceScheduleInnerTimeAndCapacity from './model/ApplicationPropertiesComputeProfileRolesInnerAutoscaleRecurrenceScheduleInnerTimeAndCapacity';
import ApplicationPropertiesComputeProfileRolesInnerDataDisksGroupsInner from './model/ApplicationPropertiesComputeProfileRolesInnerDataDisksGroupsInner';
import ApplicationPropertiesComputeProfileRolesInnerHardwareProfile from './model/ApplicationPropertiesComputeProfileRolesInnerHardwareProfile';
import ApplicationPropertiesComputeProfileRolesInnerOsProfile from './model/ApplicationPropertiesComputeProfileRolesInnerOsProfile';
import ApplicationPropertiesComputeProfileRolesInnerOsProfileLinuxOperatingSystemProfile from './model/ApplicationPropertiesComputeProfileRolesInnerOsProfileLinuxOperatingSystemProfile';
import ApplicationPropertiesComputeProfileRolesInnerOsProfileLinuxOperatingSystemProfileSshProfile from './model/ApplicationPropertiesComputeProfileRolesInnerOsProfileLinuxOperatingSystemProfileSshProfile';
import ApplicationPropertiesComputeProfileRolesInnerOsProfileLinuxOperatingSystemProfileSshProfilePublicKeysInner from './model/ApplicationPropertiesComputeProfileRolesInnerOsProfileLinuxOperatingSystemProfileSshProfilePublicKeysInner';
import ApplicationPropertiesComputeProfileRolesInnerScriptActionsInner from './model/ApplicationPropertiesComputeProfileRolesInnerScriptActionsInner';
import ApplicationPropertiesComputeProfileRolesInnerVirtualNetworkProfile from './model/ApplicationPropertiesComputeProfileRolesInnerVirtualNetworkProfile';
import ApplicationPropertiesErrorsInner from './model/ApplicationPropertiesErrorsInner';
import ApplicationPropertiesInstallScriptActionsInner from './model/ApplicationPropertiesInstallScriptActionsInner';
import ApplicationsListByClusterDefaultResponse from './model/ApplicationsListByClusterDefaultResponse';
import ApplicationsApi from './api/ApplicationsApi';


/**
* The HDInsight Management Client..<br>
* The <code>index</code> module provides access to constructors for all the classes which comprise the public API.
* <p>
* An AMD (recommended!) or CommonJS application will generally do something equivalent to the following:
* <pre>
* var HdInsightManagementClient = require('index'); // See note below*.
* var xxxSvc = new HdInsightManagementClient.XxxApi(); // Allocate the API class we're going to use.
* var yyyModel = new HdInsightManagementClient.Yyy(); // Construct a model instance.
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
* var xxxSvc = new HdInsightManagementClient.XxxApi(); // Allocate the API class we're going to use.
* var yyy = new HdInsightManagementClient.Yyy(); // Construct a model instance.
* yyyModel.someProperty = 'someValue';
* ...
* var zzz = xxxSvc.doSomething(yyyModel); // Invoke the service.
* ...
* </pre>
* </p>
* @module index
* @version 2018-06-01-preview
*/
export {
    /**
     * The ApiClient constructor.
     * @property {module:ApiClient}
     */
    ApiClient,

    /**
     * The Application model constructor.
     * @property {module:model/Application}
     */
    Application,

    /**
     * The ApplicationGetEndpoint model constructor.
     * @property {module:model/ApplicationGetEndpoint}
     */
    ApplicationGetEndpoint,

    /**
     * The ApplicationGetHttpsEndpoint model constructor.
     * @property {module:model/ApplicationGetHttpsEndpoint}
     */
    ApplicationGetHttpsEndpoint,

    /**
     * The ApplicationListResult model constructor.
     * @property {module:model/ApplicationListResult}
     */
    ApplicationListResult,

    /**
     * The ApplicationProperties model constructor.
     * @property {module:model/ApplicationProperties}
     */
    ApplicationProperties,

    /**
     * The ApplicationPropertiesComputeProfile model constructor.
     * @property {module:model/ApplicationPropertiesComputeProfile}
     */
    ApplicationPropertiesComputeProfile,

    /**
     * The ApplicationPropertiesComputeProfileRolesInner model constructor.
     * @property {module:model/ApplicationPropertiesComputeProfileRolesInner}
     */
    ApplicationPropertiesComputeProfileRolesInner,

    /**
     * The ApplicationPropertiesComputeProfileRolesInnerAutoscale model constructor.
     * @property {module:model/ApplicationPropertiesComputeProfileRolesInnerAutoscale}
     */
    ApplicationPropertiesComputeProfileRolesInnerAutoscale,

    /**
     * The ApplicationPropertiesComputeProfileRolesInnerAutoscaleCapacity model constructor.
     * @property {module:model/ApplicationPropertiesComputeProfileRolesInnerAutoscaleCapacity}
     */
    ApplicationPropertiesComputeProfileRolesInnerAutoscaleCapacity,

    /**
     * The ApplicationPropertiesComputeProfileRolesInnerAutoscaleRecurrence model constructor.
     * @property {module:model/ApplicationPropertiesComputeProfileRolesInnerAutoscaleRecurrence}
     */
    ApplicationPropertiesComputeProfileRolesInnerAutoscaleRecurrence,

    /**
     * The ApplicationPropertiesComputeProfileRolesInnerAutoscaleRecurrenceScheduleInner model constructor.
     * @property {module:model/ApplicationPropertiesComputeProfileRolesInnerAutoscaleRecurrenceScheduleInner}
     */
    ApplicationPropertiesComputeProfileRolesInnerAutoscaleRecurrenceScheduleInner,

    /**
     * The ApplicationPropertiesComputeProfileRolesInnerAutoscaleRecurrenceScheduleInnerTimeAndCapacity model constructor.
     * @property {module:model/ApplicationPropertiesComputeProfileRolesInnerAutoscaleRecurrenceScheduleInnerTimeAndCapacity}
     */
    ApplicationPropertiesComputeProfileRolesInnerAutoscaleRecurrenceScheduleInnerTimeAndCapacity,

    /**
     * The ApplicationPropertiesComputeProfileRolesInnerDataDisksGroupsInner model constructor.
     * @property {module:model/ApplicationPropertiesComputeProfileRolesInnerDataDisksGroupsInner}
     */
    ApplicationPropertiesComputeProfileRolesInnerDataDisksGroupsInner,

    /**
     * The ApplicationPropertiesComputeProfileRolesInnerHardwareProfile model constructor.
     * @property {module:model/ApplicationPropertiesComputeProfileRolesInnerHardwareProfile}
     */
    ApplicationPropertiesComputeProfileRolesInnerHardwareProfile,

    /**
     * The ApplicationPropertiesComputeProfileRolesInnerOsProfile model constructor.
     * @property {module:model/ApplicationPropertiesComputeProfileRolesInnerOsProfile}
     */
    ApplicationPropertiesComputeProfileRolesInnerOsProfile,

    /**
     * The ApplicationPropertiesComputeProfileRolesInnerOsProfileLinuxOperatingSystemProfile model constructor.
     * @property {module:model/ApplicationPropertiesComputeProfileRolesInnerOsProfileLinuxOperatingSystemProfile}
     */
    ApplicationPropertiesComputeProfileRolesInnerOsProfileLinuxOperatingSystemProfile,

    /**
     * The ApplicationPropertiesComputeProfileRolesInnerOsProfileLinuxOperatingSystemProfileSshProfile model constructor.
     * @property {module:model/ApplicationPropertiesComputeProfileRolesInnerOsProfileLinuxOperatingSystemProfileSshProfile}
     */
    ApplicationPropertiesComputeProfileRolesInnerOsProfileLinuxOperatingSystemProfileSshProfile,

    /**
     * The ApplicationPropertiesComputeProfileRolesInnerOsProfileLinuxOperatingSystemProfileSshProfilePublicKeysInner model constructor.
     * @property {module:model/ApplicationPropertiesComputeProfileRolesInnerOsProfileLinuxOperatingSystemProfileSshProfilePublicKeysInner}
     */
    ApplicationPropertiesComputeProfileRolesInnerOsProfileLinuxOperatingSystemProfileSshProfilePublicKeysInner,

    /**
     * The ApplicationPropertiesComputeProfileRolesInnerScriptActionsInner model constructor.
     * @property {module:model/ApplicationPropertiesComputeProfileRolesInnerScriptActionsInner}
     */
    ApplicationPropertiesComputeProfileRolesInnerScriptActionsInner,

    /**
     * The ApplicationPropertiesComputeProfileRolesInnerVirtualNetworkProfile model constructor.
     * @property {module:model/ApplicationPropertiesComputeProfileRolesInnerVirtualNetworkProfile}
     */
    ApplicationPropertiesComputeProfileRolesInnerVirtualNetworkProfile,

    /**
     * The ApplicationPropertiesErrorsInner model constructor.
     * @property {module:model/ApplicationPropertiesErrorsInner}
     */
    ApplicationPropertiesErrorsInner,

    /**
     * The ApplicationPropertiesInstallScriptActionsInner model constructor.
     * @property {module:model/ApplicationPropertiesInstallScriptActionsInner}
     */
    ApplicationPropertiesInstallScriptActionsInner,

    /**
     * The ApplicationsListByClusterDefaultResponse model constructor.
     * @property {module:model/ApplicationsListByClusterDefaultResponse}
     */
    ApplicationsListByClusterDefaultResponse,

    /**
    * The ApplicationsApi service constructor.
    * @property {module:api/ApplicationsApi}
    */
    ApplicationsApi
};
