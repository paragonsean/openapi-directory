/**
 * ContainerRegistryManagementClient
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 2018-09-01
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */


import ApiClient from './ApiClient';
import AgentProperties from './model/AgentProperties';
import Argument from './model/Argument';
import AuthInfo from './model/AuthInfo';
import AuthInfoUpdateParameters from './model/AuthInfoUpdateParameters';
import BaseImageDependency from './model/BaseImageDependency';
import BaseImageTrigger from './model/BaseImageTrigger';
import BaseImageTriggerUpdateParameters from './model/BaseImageTriggerUpdateParameters';
import Credentials from './model/Credentials';
import CustomRegistryCredentials from './model/CustomRegistryCredentials';
import DockerBuildRequest from './model/DockerBuildRequest';
import DockerBuildStep from './model/DockerBuildStep';
import DockerBuildStepUpdateParameters from './model/DockerBuildStepUpdateParameters';
import EncodedTaskRunRequest from './model/EncodedTaskRunRequest';
import EncodedTaskStep from './model/EncodedTaskStep';
import EncodedTaskStepUpdateParameters from './model/EncodedTaskStepUpdateParameters';
import FileTaskRunRequest from './model/FileTaskRunRequest';
import FileTaskStep from './model/FileTaskStep';
import FileTaskStepUpdateParameters from './model/FileTaskStepUpdateParameters';
import ImageDescriptor from './model/ImageDescriptor';
import ImageUpdateTrigger from './model/ImageUpdateTrigger';
import PlatformProperties from './model/PlatformProperties';
import PlatformUpdateParameters from './model/PlatformUpdateParameters';
import ProxyResource from './model/ProxyResource';
import Resource from './model/Resource';
import Run from './model/Run';
import RunFilter from './model/RunFilter';
import RunGetLogResult from './model/RunGetLogResult';
import RunListResult from './model/RunListResult';
import RunProperties from './model/RunProperties';
import RunRequest from './model/RunRequest';
import RunUpdateParameters from './model/RunUpdateParameters';
import SecretObject from './model/SecretObject';
import SetValue from './model/SetValue';
import SourceProperties from './model/SourceProperties';
import SourceRegistryCredentials from './model/SourceRegistryCredentials';
import SourceTrigger from './model/SourceTrigger';
import SourceTriggerDescriptor from './model/SourceTriggerDescriptor';
import SourceTriggerUpdateParameters from './model/SourceTriggerUpdateParameters';
import SourceUpdateParameters from './model/SourceUpdateParameters';
import SourceUploadDefinition from './model/SourceUploadDefinition';
import Task from './model/Task';
import TaskListResult from './model/TaskListResult';
import TaskProperties from './model/TaskProperties';
import TaskPropertiesUpdateParameters from './model/TaskPropertiesUpdateParameters';
import TaskRunRequest from './model/TaskRunRequest';
import TaskStepProperties from './model/TaskStepProperties';
import TaskStepUpdateParameters from './model/TaskStepUpdateParameters';
import TaskUpdateParameters from './model/TaskUpdateParameters';
import TriggerProperties from './model/TriggerProperties';
import TriggerUpdateParameters from './model/TriggerUpdateParameters';
import RegistriesApi from './api/RegistriesApi';
import RunsApi from './api/RunsApi';
import TasksApi from './api/TasksApi';


/**
* JS API client generated by OpenAPI Generator.<br>
* The <code>index</code> module provides access to constructors for all the classes which comprise the public API.
* <p>
* An AMD (recommended!) or CommonJS application will generally do something equivalent to the following:
* <pre>
* var ContainerRegistryManagementClient = require('index'); // See note below*.
* var xxxSvc = new ContainerRegistryManagementClient.XxxApi(); // Allocate the API class we're going to use.
* var yyyModel = new ContainerRegistryManagementClient.Yyy(); // Construct a model instance.
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
* var xxxSvc = new ContainerRegistryManagementClient.XxxApi(); // Allocate the API class we're going to use.
* var yyy = new ContainerRegistryManagementClient.Yyy(); // Construct a model instance.
* yyyModel.someProperty = 'someValue';
* ...
* var zzz = xxxSvc.doSomething(yyyModel); // Invoke the service.
* ...
* </pre>
* </p>
* @module index
* @version 2018-09-01
*/
export {
    /**
     * The ApiClient constructor.
     * @property {module:ApiClient}
     */
    ApiClient,

    /**
     * The AgentProperties model constructor.
     * @property {module:model/AgentProperties}
     */
    AgentProperties,

    /**
     * The Argument model constructor.
     * @property {module:model/Argument}
     */
    Argument,

    /**
     * The AuthInfo model constructor.
     * @property {module:model/AuthInfo}
     */
    AuthInfo,

    /**
     * The AuthInfoUpdateParameters model constructor.
     * @property {module:model/AuthInfoUpdateParameters}
     */
    AuthInfoUpdateParameters,

    /**
     * The BaseImageDependency model constructor.
     * @property {module:model/BaseImageDependency}
     */
    BaseImageDependency,

    /**
     * The BaseImageTrigger model constructor.
     * @property {module:model/BaseImageTrigger}
     */
    BaseImageTrigger,

    /**
     * The BaseImageTriggerUpdateParameters model constructor.
     * @property {module:model/BaseImageTriggerUpdateParameters}
     */
    BaseImageTriggerUpdateParameters,

    /**
     * The Credentials model constructor.
     * @property {module:model/Credentials}
     */
    Credentials,

    /**
     * The CustomRegistryCredentials model constructor.
     * @property {module:model/CustomRegistryCredentials}
     */
    CustomRegistryCredentials,

    /**
     * The DockerBuildRequest model constructor.
     * @property {module:model/DockerBuildRequest}
     */
    DockerBuildRequest,

    /**
     * The DockerBuildStep model constructor.
     * @property {module:model/DockerBuildStep}
     */
    DockerBuildStep,

    /**
     * The DockerBuildStepUpdateParameters model constructor.
     * @property {module:model/DockerBuildStepUpdateParameters}
     */
    DockerBuildStepUpdateParameters,

    /**
     * The EncodedTaskRunRequest model constructor.
     * @property {module:model/EncodedTaskRunRequest}
     */
    EncodedTaskRunRequest,

    /**
     * The EncodedTaskStep model constructor.
     * @property {module:model/EncodedTaskStep}
     */
    EncodedTaskStep,

    /**
     * The EncodedTaskStepUpdateParameters model constructor.
     * @property {module:model/EncodedTaskStepUpdateParameters}
     */
    EncodedTaskStepUpdateParameters,

    /**
     * The FileTaskRunRequest model constructor.
     * @property {module:model/FileTaskRunRequest}
     */
    FileTaskRunRequest,

    /**
     * The FileTaskStep model constructor.
     * @property {module:model/FileTaskStep}
     */
    FileTaskStep,

    /**
     * The FileTaskStepUpdateParameters model constructor.
     * @property {module:model/FileTaskStepUpdateParameters}
     */
    FileTaskStepUpdateParameters,

    /**
     * The ImageDescriptor model constructor.
     * @property {module:model/ImageDescriptor}
     */
    ImageDescriptor,

    /**
     * The ImageUpdateTrigger model constructor.
     * @property {module:model/ImageUpdateTrigger}
     */
    ImageUpdateTrigger,

    /**
     * The PlatformProperties model constructor.
     * @property {module:model/PlatformProperties}
     */
    PlatformProperties,

    /**
     * The PlatformUpdateParameters model constructor.
     * @property {module:model/PlatformUpdateParameters}
     */
    PlatformUpdateParameters,

    /**
     * The ProxyResource model constructor.
     * @property {module:model/ProxyResource}
     */
    ProxyResource,

    /**
     * The Resource model constructor.
     * @property {module:model/Resource}
     */
    Resource,

    /**
     * The Run model constructor.
     * @property {module:model/Run}
     */
    Run,

    /**
     * The RunFilter model constructor.
     * @property {module:model/RunFilter}
     */
    RunFilter,

    /**
     * The RunGetLogResult model constructor.
     * @property {module:model/RunGetLogResult}
     */
    RunGetLogResult,

    /**
     * The RunListResult model constructor.
     * @property {module:model/RunListResult}
     */
    RunListResult,

    /**
     * The RunProperties model constructor.
     * @property {module:model/RunProperties}
     */
    RunProperties,

    /**
     * The RunRequest model constructor.
     * @property {module:model/RunRequest}
     */
    RunRequest,

    /**
     * The RunUpdateParameters model constructor.
     * @property {module:model/RunUpdateParameters}
     */
    RunUpdateParameters,

    /**
     * The SecretObject model constructor.
     * @property {module:model/SecretObject}
     */
    SecretObject,

    /**
     * The SetValue model constructor.
     * @property {module:model/SetValue}
     */
    SetValue,

    /**
     * The SourceProperties model constructor.
     * @property {module:model/SourceProperties}
     */
    SourceProperties,

    /**
     * The SourceRegistryCredentials model constructor.
     * @property {module:model/SourceRegistryCredentials}
     */
    SourceRegistryCredentials,

    /**
     * The SourceTrigger model constructor.
     * @property {module:model/SourceTrigger}
     */
    SourceTrigger,

    /**
     * The SourceTriggerDescriptor model constructor.
     * @property {module:model/SourceTriggerDescriptor}
     */
    SourceTriggerDescriptor,

    /**
     * The SourceTriggerUpdateParameters model constructor.
     * @property {module:model/SourceTriggerUpdateParameters}
     */
    SourceTriggerUpdateParameters,

    /**
     * The SourceUpdateParameters model constructor.
     * @property {module:model/SourceUpdateParameters}
     */
    SourceUpdateParameters,

    /**
     * The SourceUploadDefinition model constructor.
     * @property {module:model/SourceUploadDefinition}
     */
    SourceUploadDefinition,

    /**
     * The Task model constructor.
     * @property {module:model/Task}
     */
    Task,

    /**
     * The TaskListResult model constructor.
     * @property {module:model/TaskListResult}
     */
    TaskListResult,

    /**
     * The TaskProperties model constructor.
     * @property {module:model/TaskProperties}
     */
    TaskProperties,

    /**
     * The TaskPropertiesUpdateParameters model constructor.
     * @property {module:model/TaskPropertiesUpdateParameters}
     */
    TaskPropertiesUpdateParameters,

    /**
     * The TaskRunRequest model constructor.
     * @property {module:model/TaskRunRequest}
     */
    TaskRunRequest,

    /**
     * The TaskStepProperties model constructor.
     * @property {module:model/TaskStepProperties}
     */
    TaskStepProperties,

    /**
     * The TaskStepUpdateParameters model constructor.
     * @property {module:model/TaskStepUpdateParameters}
     */
    TaskStepUpdateParameters,

    /**
     * The TaskUpdateParameters model constructor.
     * @property {module:model/TaskUpdateParameters}
     */
    TaskUpdateParameters,

    /**
     * The TriggerProperties model constructor.
     * @property {module:model/TriggerProperties}
     */
    TriggerProperties,

    /**
     * The TriggerUpdateParameters model constructor.
     * @property {module:model/TriggerUpdateParameters}
     */
    TriggerUpdateParameters,

    /**
    * The RegistriesApi service constructor.
    * @property {module:api/RegistriesApi}
    */
    RegistriesApi,

    /**
    * The RunsApi service constructor.
    * @property {module:api/RunsApi}
    */
    RunsApi,

    /**
    * The TasksApi service constructor.
    * @property {module:api/TasksApi}
    */
    TasksApi
};
