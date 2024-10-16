/**
 * NHL v3 Scores
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
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
import Game from './model/Game';
import News from './model/News';
import OpponentSeason from './model/OpponentSeason';
import Penalty from './model/Penalty';
import Period from './model/Period';
import Player from './model/Player';
import PlayerBasic from './model/PlayerBasic';
import ScheduleBasic from './model/ScheduleBasic';
import ScoreBasic from './model/ScoreBasic';
import ScoringPlay from './model/ScoringPlay';
import Season from './model/Season';
import Series from './model/Series';
import Stadium from './model/Stadium';
import Standing from './model/Standing';
import Team from './model/Team';
import TeamGame from './model/TeamGame';
import TeamSeason from './model/TeamSeason';
import DefaultApi from './api/DefaultApi';


/**
* JS API client generated by OpenAPI Generator.<br>
* The <code>index</code> module provides access to constructors for all the classes which comprise the public API.
* <p>
* An AMD (recommended!) or CommonJS application will generally do something equivalent to the following:
* <pre>
* var NhlV3Scores = require('index'); // See note below*.
* var xxxSvc = new NhlV3Scores.XxxApi(); // Allocate the API class we're going to use.
* var yyyModel = new NhlV3Scores.Yyy(); // Construct a model instance.
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
* var xxxSvc = new NhlV3Scores.XxxApi(); // Allocate the API class we're going to use.
* var yyy = new NhlV3Scores.Yyy(); // Construct a model instance.
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
     * The Game model constructor.
     * @property {module:model/Game}
     */
    Game,

    /**
     * The News model constructor.
     * @property {module:model/News}
     */
    News,

    /**
     * The OpponentSeason model constructor.
     * @property {module:model/OpponentSeason}
     */
    OpponentSeason,

    /**
     * The Penalty model constructor.
     * @property {module:model/Penalty}
     */
    Penalty,

    /**
     * The Period model constructor.
     * @property {module:model/Period}
     */
    Period,

    /**
     * The Player model constructor.
     * @property {module:model/Player}
     */
    Player,

    /**
     * The PlayerBasic model constructor.
     * @property {module:model/PlayerBasic}
     */
    PlayerBasic,

    /**
     * The ScheduleBasic model constructor.
     * @property {module:model/ScheduleBasic}
     */
    ScheduleBasic,

    /**
     * The ScoreBasic model constructor.
     * @property {module:model/ScoreBasic}
     */
    ScoreBasic,

    /**
     * The ScoringPlay model constructor.
     * @property {module:model/ScoringPlay}
     */
    ScoringPlay,

    /**
     * The Season model constructor.
     * @property {module:model/Season}
     */
    Season,

    /**
     * The Series model constructor.
     * @property {module:model/Series}
     */
    Series,

    /**
     * The Stadium model constructor.
     * @property {module:model/Stadium}
     */
    Stadium,

    /**
     * The Standing model constructor.
     * @property {module:model/Standing}
     */
    Standing,

    /**
     * The Team model constructor.
     * @property {module:model/Team}
     */
    Team,

    /**
     * The TeamGame model constructor.
     * @property {module:model/TeamGame}
     */
    TeamGame,

    /**
     * The TeamSeason model constructor.
     * @property {module:model/TeamSeason}
     */
    TeamSeason,

    /**
    * The DefaultApi service constructor.
    * @property {module:api/DefaultApi}
    */
    DefaultApi
};
