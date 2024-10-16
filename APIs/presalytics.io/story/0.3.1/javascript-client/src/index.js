/**
 * Story
 * This API is the main entry point for creating, editing and publishing analytics throught the Presalytics API
 *
 * The version of the OpenAPI document: 0.3.1
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */


import ApiClient from './ApiClient';
import AddNewCollaboratorRequest from './model/AddNewCollaboratorRequest';
import BaseModel from './model/BaseModel';
import CachePostRequest from './model/CachePostRequest';
import CollaboratorBulkUpdateRequest from './model/CollaboratorBulkUpdateRequest';
import CreateSessionRequest from './model/CreateSessionRequest';
import Event from './model/Event';
import FileUpload from './model/FileUpload';
import ManageEvent from './model/ManageEvent';
import Message from './model/Message';
import ModifyInactiveCollaborator from './model/ModifyInactiveCollaborator';
import OoxmlDocument from './model/OoxmlDocument';
import Outline from './model/Outline';
import PermissionType from './model/PermissionType';
import ProblemDetail from './model/ProblemDetail';
import RequiredParametersToCreateAView from './model/RequiredParametersToCreateAView';
import Session from './model/Session';
import Status from './model/Status';
import Story from './model/Story';
import StoryCollaborator from './model/StoryCollaborator';
import StoryOutlineHistory from './model/StoryOutlineHistory';
import View from './model/View';
import CacheApi from './api/CacheApi';
import ConversationApi from './api/ConversationApi';
import DefaultApi from './api/DefaultApi';
import EventsApi from './api/EventsApi';
import PermissionsApi from './api/PermissionsApi';
import RestrictedApi from './api/RestrictedApi';
import SchemasApi from './api/SchemasApi';
import SessionsApi from './api/SessionsApi';
import StoryApi from './api/StoryApi';
import StoryCollaboratorsApi from './api/StoryCollaboratorsApi';
import ViewsApi from './api/ViewsApi';


/**
* This API is the main entry point for creating, editing and publishing analytics throught the Presalytics API.<br>
* The <code>index</code> module provides access to constructors for all the classes which comprise the public API.
* <p>
* An AMD (recommended!) or CommonJS application will generally do something equivalent to the following:
* <pre>
* var Story = require('index'); // See note below*.
* var xxxSvc = new Story.XxxApi(); // Allocate the API class we're going to use.
* var yyyModel = new Story.Yyy(); // Construct a model instance.
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
* var xxxSvc = new Story.XxxApi(); // Allocate the API class we're going to use.
* var yyy = new Story.Yyy(); // Construct a model instance.
* yyyModel.someProperty = 'someValue';
* ...
* var zzz = xxxSvc.doSomething(yyyModel); // Invoke the service.
* ...
* </pre>
* </p>
* @module index
* @version 0.3.1
*/
export {
    /**
     * The ApiClient constructor.
     * @property {module:ApiClient}
     */
    ApiClient,

    /**
     * The AddNewCollaboratorRequest model constructor.
     * @property {module:model/AddNewCollaboratorRequest}
     */
    AddNewCollaboratorRequest,

    /**
     * The BaseModel model constructor.
     * @property {module:model/BaseModel}
     */
    BaseModel,

    /**
     * The CachePostRequest model constructor.
     * @property {module:model/CachePostRequest}
     */
    CachePostRequest,

    /**
     * The CollaboratorBulkUpdateRequest model constructor.
     * @property {module:model/CollaboratorBulkUpdateRequest}
     */
    CollaboratorBulkUpdateRequest,

    /**
     * The CreateSessionRequest model constructor.
     * @property {module:model/CreateSessionRequest}
     */
    CreateSessionRequest,

    /**
     * The Event model constructor.
     * @property {module:model/Event}
     */
    Event,

    /**
     * The FileUpload model constructor.
     * @property {module:model/FileUpload}
     */
    FileUpload,

    /**
     * The ManageEvent model constructor.
     * @property {module:model/ManageEvent}
     */
    ManageEvent,

    /**
     * The Message model constructor.
     * @property {module:model/Message}
     */
    Message,

    /**
     * The ModifyInactiveCollaborator model constructor.
     * @property {module:model/ModifyInactiveCollaborator}
     */
    ModifyInactiveCollaborator,

    /**
     * The OoxmlDocument model constructor.
     * @property {module:model/OoxmlDocument}
     */
    OoxmlDocument,

    /**
     * The Outline model constructor.
     * @property {module:model/Outline}
     */
    Outline,

    /**
     * The PermissionType model constructor.
     * @property {module:model/PermissionType}
     */
    PermissionType,

    /**
     * The ProblemDetail model constructor.
     * @property {module:model/ProblemDetail}
     */
    ProblemDetail,

    /**
     * The RequiredParametersToCreateAView model constructor.
     * @property {module:model/RequiredParametersToCreateAView}
     */
    RequiredParametersToCreateAView,

    /**
     * The Session model constructor.
     * @property {module:model/Session}
     */
    Session,

    /**
     * The Status model constructor.
     * @property {module:model/Status}
     */
    Status,

    /**
     * The Story model constructor.
     * @property {module:model/Story}
     */
    Story,

    /**
     * The StoryCollaborator model constructor.
     * @property {module:model/StoryCollaborator}
     */
    StoryCollaborator,

    /**
     * The StoryOutlineHistory model constructor.
     * @property {module:model/StoryOutlineHistory}
     */
    StoryOutlineHistory,

    /**
     * The View model constructor.
     * @property {module:model/View}
     */
    View,

    /**
    * The CacheApi service constructor.
    * @property {module:api/CacheApi}
    */
    CacheApi,

    /**
    * The ConversationApi service constructor.
    * @property {module:api/ConversationApi}
    */
    ConversationApi,

    /**
    * The DefaultApi service constructor.
    * @property {module:api/DefaultApi}
    */
    DefaultApi,

    /**
    * The EventsApi service constructor.
    * @property {module:api/EventsApi}
    */
    EventsApi,

    /**
    * The PermissionsApi service constructor.
    * @property {module:api/PermissionsApi}
    */
    PermissionsApi,

    /**
    * The RestrictedApi service constructor.
    * @property {module:api/RestrictedApi}
    */
    RestrictedApi,

    /**
    * The SchemasApi service constructor.
    * @property {module:api/SchemasApi}
    */
    SchemasApi,

    /**
    * The SessionsApi service constructor.
    * @property {module:api/SessionsApi}
    */
    SessionsApi,

    /**
    * The StoryApi service constructor.
    * @property {module:api/StoryApi}
    */
    StoryApi,

    /**
    * The StoryCollaboratorsApi service constructor.
    * @property {module:api/StoryCollaboratorsApi}
    */
    StoryCollaboratorsApi,

    /**
    * The ViewsApi service constructor.
    * @property {module:api/ViewsApi}
    */
    ViewsApi
};
