/**
 * NFL v3 Projections
 * NFL projected stats API.
 *
 * The version of the OpenAPI document: 1.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */


import ApiClient from './ApiClient';
import DfsSlate from './model/DfsSlate';
import DfsSlateGame from './model/DfsSlateGame';
import DfsSlatePlayer from './model/DfsSlatePlayer';
import DfsSlatePlayerOwnershipProjection from './model/DfsSlatePlayerOwnershipProjection';
import DfsSlateWithOwnershipProjection from './model/DfsSlateWithOwnershipProjection';
import FantasyDefenseGameProjection from './model/FantasyDefenseGameProjection';
import FantasyDefenseSeasonProjection from './model/FantasyDefenseSeasonProjection';
import Player from './model/Player';
import PlayerGameProjection from './model/PlayerGameProjection';
import PlayerSeasonProjection from './model/PlayerSeasonProjection';
import Schedule from './model/Schedule';
import ScoringDetail from './model/ScoringDetail';
import Stadium from './model/Stadium';
import DefaultApi from './api/DefaultApi';


/**
* NFL projected stats API..<br>
* The <code>index</code> module provides access to constructors for all the classes which comprise the public API.
* <p>
* An AMD (recommended!) or CommonJS application will generally do something equivalent to the following:
* <pre>
* var NflV3Projections = require('index'); // See note below*.
* var xxxSvc = new NflV3Projections.XxxApi(); // Allocate the API class we're going to use.
* var yyyModel = new NflV3Projections.Yyy(); // Construct a model instance.
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
* var xxxSvc = new NflV3Projections.XxxApi(); // Allocate the API class we're going to use.
* var yyy = new NflV3Projections.Yyy(); // Construct a model instance.
* yyyModel.someProperty = 'someValue';
* ...
* var zzz = xxxSvc.doSomething(yyyModel); // Invoke the service.
* ...
* </pre>
* </p>
* @module index
* @version 1.0
*/
export {
    /**
     * The ApiClient constructor.
     * @property {module:ApiClient}
     */
    ApiClient,

    /**
     * The DfsSlate model constructor.
     * @property {module:model/DfsSlate}
     */
    DfsSlate,

    /**
     * The DfsSlateGame model constructor.
     * @property {module:model/DfsSlateGame}
     */
    DfsSlateGame,

    /**
     * The DfsSlatePlayer model constructor.
     * @property {module:model/DfsSlatePlayer}
     */
    DfsSlatePlayer,

    /**
     * The DfsSlatePlayerOwnershipProjection model constructor.
     * @property {module:model/DfsSlatePlayerOwnershipProjection}
     */
    DfsSlatePlayerOwnershipProjection,

    /**
     * The DfsSlateWithOwnershipProjection model constructor.
     * @property {module:model/DfsSlateWithOwnershipProjection}
     */
    DfsSlateWithOwnershipProjection,

    /**
     * The FantasyDefenseGameProjection model constructor.
     * @property {module:model/FantasyDefenseGameProjection}
     */
    FantasyDefenseGameProjection,

    /**
     * The FantasyDefenseSeasonProjection model constructor.
     * @property {module:model/FantasyDefenseSeasonProjection}
     */
    FantasyDefenseSeasonProjection,

    /**
     * The Player model constructor.
     * @property {module:model/Player}
     */
    Player,

    /**
     * The PlayerGameProjection model constructor.
     * @property {module:model/PlayerGameProjection}
     */
    PlayerGameProjection,

    /**
     * The PlayerSeasonProjection model constructor.
     * @property {module:model/PlayerSeasonProjection}
     */
    PlayerSeasonProjection,

    /**
     * The Schedule model constructor.
     * @property {module:model/Schedule}
     */
    Schedule,

    /**
     * The ScoringDetail model constructor.
     * @property {module:model/ScoringDetail}
     */
    ScoringDetail,

    /**
     * The Stadium model constructor.
     * @property {module:model/Stadium}
     */
    Stadium,

    /**
    * The DefaultApi service constructor.
    * @property {module:api/DefaultApi}
    */
    DefaultApi
};
