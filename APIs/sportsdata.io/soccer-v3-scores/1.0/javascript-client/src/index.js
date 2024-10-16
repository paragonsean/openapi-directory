/**
 * Soccer v3 Scores
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
import Area from './model/Area';
import CanceledMembership from './model/CanceledMembership';
import Competition from './model/Competition';
import CompetitionDetail from './model/CompetitionDetail';
import Game from './model/Game';
import Membership from './model/Membership';
import Player from './model/Player';
import PlayerSeason from './model/PlayerSeason';
import PlayoffAggregateScore from './model/PlayoffAggregateScore';
import Round from './model/Round';
import Season from './model/Season';
import SeasonTeam from './model/SeasonTeam';
import Standing from './model/Standing';
import Team from './model/Team';
import TeamDetail from './model/TeamDetail';
import TeamGame from './model/TeamGame';
import TeamSeason from './model/TeamSeason';
import Venue from './model/Venue';
import DefaultApi from './api/DefaultApi';


/**
* JS API client generated by OpenAPI Generator.<br>
* The <code>index</code> module provides access to constructors for all the classes which comprise the public API.
* <p>
* An AMD (recommended!) or CommonJS application will generally do something equivalent to the following:
* <pre>
* var SoccerV3Scores = require('index'); // See note below*.
* var xxxSvc = new SoccerV3Scores.XxxApi(); // Allocate the API class we're going to use.
* var yyyModel = new SoccerV3Scores.Yyy(); // Construct a model instance.
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
* var xxxSvc = new SoccerV3Scores.XxxApi(); // Allocate the API class we're going to use.
* var yyy = new SoccerV3Scores.Yyy(); // Construct a model instance.
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
     * The Area model constructor.
     * @property {module:model/Area}
     */
    Area,

    /**
     * The CanceledMembership model constructor.
     * @property {module:model/CanceledMembership}
     */
    CanceledMembership,

    /**
     * The Competition model constructor.
     * @property {module:model/Competition}
     */
    Competition,

    /**
     * The CompetitionDetail model constructor.
     * @property {module:model/CompetitionDetail}
     */
    CompetitionDetail,

    /**
     * The Game model constructor.
     * @property {module:model/Game}
     */
    Game,

    /**
     * The Membership model constructor.
     * @property {module:model/Membership}
     */
    Membership,

    /**
     * The Player model constructor.
     * @property {module:model/Player}
     */
    Player,

    /**
     * The PlayerSeason model constructor.
     * @property {module:model/PlayerSeason}
     */
    PlayerSeason,

    /**
     * The PlayoffAggregateScore model constructor.
     * @property {module:model/PlayoffAggregateScore}
     */
    PlayoffAggregateScore,

    /**
     * The Round model constructor.
     * @property {module:model/Round}
     */
    Round,

    /**
     * The Season model constructor.
     * @property {module:model/Season}
     */
    Season,

    /**
     * The SeasonTeam model constructor.
     * @property {module:model/SeasonTeam}
     */
    SeasonTeam,

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
     * The TeamDetail model constructor.
     * @property {module:model/TeamDetail}
     */
    TeamDetail,

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
     * The Venue model constructor.
     * @property {module:model/Venue}
     */
    Venue,

    /**
    * The DefaultApi service constructor.
    * @property {module:api/DefaultApi}
    */
    DefaultApi
};
