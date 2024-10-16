/**
 * SheerSEO API
 * Sheerseo API has 2 stages:<br>First stage - initiating the task: You fill in your task and receive in return the task id. <br>Second stage - collecting the results: send a request containing the task ids you got at the first stage and collecting the results.
 *
 * The version of the OpenAPI document: 0.0.1
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */


import ApiClient from './ApiClient';
import CollectRequest from './model/CollectRequest';
import ErrorResponse from './model/ErrorResponse';
import KeywordJobRank from './model/KeywordJobRank';
import KeywordJobSerp from './model/KeywordJobSerp';
import KeywordTask from './model/KeywordTask';
import RankCollectResponse from './model/RankCollectResponse';
import RankCollectResponseTasksInner from './model/RankCollectResponseTasksInner';
import RankCollectResponseTasksInnerTaskId from './model/RankCollectResponseTasksInnerTaskId';
import RankSubmitRequest from './model/RankSubmitRequest';
import RankSubmitResponse from './model/RankSubmitResponse';
import SerpCollectResponse from './model/SerpCollectResponse';
import SerpCollectResponseTasksInner from './model/SerpCollectResponseTasksInner';
import SerpCollectResponseTasksInnerTaskId from './model/SerpCollectResponseTasksInnerTaskId';
import SerpCollectResponseTasksInnerTaskIdOrganicResultsInner from './model/SerpCollectResponseTasksInnerTaskIdOrganicResultsInner';
import SerpSubmitRequest from './model/SerpSubmitRequest';
import SerpSubmitResponse from './model/SerpSubmitResponse';
import DefaultApi from './api/DefaultApi';


/**
* Sheerseo API has 2 stages:&lt;br&gt;First stage - initiating the task: You fill in your task and receive in return the task id. &lt;br&gt;Second stage - collecting the results: send a request containing the task ids you got at the first stage and collecting the results..<br>
* The <code>index</code> module provides access to constructors for all the classes which comprise the public API.
* <p>
* An AMD (recommended!) or CommonJS application will generally do something equivalent to the following:
* <pre>
* var SheerSeoApi = require('index'); // See note below*.
* var xxxSvc = new SheerSeoApi.XxxApi(); // Allocate the API class we're going to use.
* var yyyModel = new SheerSeoApi.Yyy(); // Construct a model instance.
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
* var xxxSvc = new SheerSeoApi.XxxApi(); // Allocate the API class we're going to use.
* var yyy = new SheerSeoApi.Yyy(); // Construct a model instance.
* yyyModel.someProperty = 'someValue';
* ...
* var zzz = xxxSvc.doSomething(yyyModel); // Invoke the service.
* ...
* </pre>
* </p>
* @module index
* @version 0.0.1
*/
export {
    /**
     * The ApiClient constructor.
     * @property {module:ApiClient}
     */
    ApiClient,

    /**
     * The CollectRequest model constructor.
     * @property {module:model/CollectRequest}
     */
    CollectRequest,

    /**
     * The ErrorResponse model constructor.
     * @property {module:model/ErrorResponse}
     */
    ErrorResponse,

    /**
     * The KeywordJobRank model constructor.
     * @property {module:model/KeywordJobRank}
     */
    KeywordJobRank,

    /**
     * The KeywordJobSerp model constructor.
     * @property {module:model/KeywordJobSerp}
     */
    KeywordJobSerp,

    /**
     * The KeywordTask model constructor.
     * @property {module:model/KeywordTask}
     */
    KeywordTask,

    /**
     * The RankCollectResponse model constructor.
     * @property {module:model/RankCollectResponse}
     */
    RankCollectResponse,

    /**
     * The RankCollectResponseTasksInner model constructor.
     * @property {module:model/RankCollectResponseTasksInner}
     */
    RankCollectResponseTasksInner,

    /**
     * The RankCollectResponseTasksInnerTaskId model constructor.
     * @property {module:model/RankCollectResponseTasksInnerTaskId}
     */
    RankCollectResponseTasksInnerTaskId,

    /**
     * The RankSubmitRequest model constructor.
     * @property {module:model/RankSubmitRequest}
     */
    RankSubmitRequest,

    /**
     * The RankSubmitResponse model constructor.
     * @property {module:model/RankSubmitResponse}
     */
    RankSubmitResponse,

    /**
     * The SerpCollectResponse model constructor.
     * @property {module:model/SerpCollectResponse}
     */
    SerpCollectResponse,

    /**
     * The SerpCollectResponseTasksInner model constructor.
     * @property {module:model/SerpCollectResponseTasksInner}
     */
    SerpCollectResponseTasksInner,

    /**
     * The SerpCollectResponseTasksInnerTaskId model constructor.
     * @property {module:model/SerpCollectResponseTasksInnerTaskId}
     */
    SerpCollectResponseTasksInnerTaskId,

    /**
     * The SerpCollectResponseTasksInnerTaskIdOrganicResultsInner model constructor.
     * @property {module:model/SerpCollectResponseTasksInnerTaskIdOrganicResultsInner}
     */
    SerpCollectResponseTasksInnerTaskIdOrganicResultsInner,

    /**
     * The SerpSubmitRequest model constructor.
     * @property {module:model/SerpSubmitRequest}
     */
    SerpSubmitRequest,

    /**
     * The SerpSubmitResponse model constructor.
     * @property {module:model/SerpSubmitResponse}
     */
    SerpSubmitResponse,

    /**
    * The DefaultApi service constructor.
    * @property {module:api/DefaultApi}
    */
    DefaultApi
};
