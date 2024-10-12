/**
 * NHL v3 Stats
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

(function(root, factory) {
  if (typeof define === 'function' && define.amd) {
    // AMD.
    define(['expect.js', process.cwd()+'/src/index'], factory);
  } else if (typeof module === 'object' && module.exports) {
    // CommonJS-like environments that support module.exports, like Node.
    factory(require('expect.js'), require(process.cwd()+'/src/index'));
  } else {
    // Browser globals (root is window)
    factory(root.expect, root.NhlV3Stats);
  }
}(this, function(expect, NhlV3Stats) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new NhlV3Stats.DefaultApi();
  });

  var getProperty = function(object, getter, property) {
    // Use getter method if present; otherwise, get the property directly.
    if (typeof object[getter] === 'function')
      return object[getter]();
    else
      return object[property];
  }

  var setProperty = function(object, setter, property, value) {
    // Use setter method if present; otherwise, set the property directly.
    if (typeof object[setter] === 'function')
      object[setter](value);
    else
      object[property] = value;
  }

  describe('DefaultApi', function() {
    describe('areGamesInProgress', function() {
      it('should call areGamesInProgress successfully', function(done) {
        //uncomment below and update the code to test areGamesInProgress
        //instance.areGamesInProgress(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('boxScore', function() {
      it('should call boxScore successfully', function(done) {
        //uncomment below and update the code to test boxScore
        //instance.boxScore(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('boxScoresByDate', function() {
      it('should call boxScoresByDate successfully', function(done) {
        //uncomment below and update the code to test boxScoresByDate
        //instance.boxScoresByDate(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('boxScoresByDateDelta', function() {
      it('should call boxScoresByDateDelta successfully', function(done) {
        //uncomment below and update the code to test boxScoresByDateDelta
        //instance.boxScoresByDateDelta(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('currentSeason', function() {
      it('should call currentSeason successfully', function(done) {
        //uncomment below and update the code to test currentSeason
        //instance.currentSeason(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('dfsSlatesByDate', function() {
      it('should call dfsSlatesByDate successfully', function(done) {
        //uncomment below and update the code to test dfsSlatesByDate
        //instance.dfsSlatesByDate(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('gamesByDate', function() {
      it('should call gamesByDate successfully', function(done) {
        //uncomment below and update the code to test gamesByDate
        //instance.gamesByDate(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('lineCombinationsBySeason', function() {
      it('should call lineCombinationsBySeason successfully', function(done) {
        //uncomment below and update the code to test lineCombinationsBySeason
        //instance.lineCombinationsBySeason(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('news', function() {
      it('should call news successfully', function(done) {
        //uncomment below and update the code to test news
        //instance.news(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('newsByDate', function() {
      it('should call newsByDate successfully', function(done) {
        //uncomment below and update the code to test newsByDate
        //instance.newsByDate(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('newsByPlayer', function() {
      it('should call newsByPlayer successfully', function(done) {
        //uncomment below and update the code to test newsByPlayer
        //instance.newsByPlayer(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('playerDetailsByActive', function() {
      it('should call playerDetailsByActive successfully', function(done) {
        //uncomment below and update the code to test playerDetailsByActive
        //instance.playerDetailsByActive(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('playerDetailsByFreeAgent', function() {
      it('should call playerDetailsByFreeAgent successfully', function(done) {
        //uncomment below and update the code to test playerDetailsByFreeAgent
        //instance.playerDetailsByFreeAgent(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('playerDetailsByPlayer', function() {
      it('should call playerDetailsByPlayer successfully', function(done) {
        //uncomment below and update the code to test playerDetailsByPlayer
        //instance.playerDetailsByPlayer(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('playerGameLogsBySeason', function() {
      it('should call playerGameLogsBySeason successfully', function(done) {
        //uncomment below and update the code to test playerGameLogsBySeason
        //instance.playerGameLogsBySeason(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('playerGameStatsByDate', function() {
      it('should call playerGameStatsByDate successfully', function(done) {
        //uncomment below and update the code to test playerGameStatsByDate
        //instance.playerGameStatsByDate(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('playerGameStatsByPlayer', function() {
      it('should call playerGameStatsByPlayer successfully', function(done) {
        //uncomment below and update the code to test playerGameStatsByPlayer
        //instance.playerGameStatsByPlayer(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('playerSeasonStats', function() {
      it('should call playerSeasonStats successfully', function(done) {
        //uncomment below and update the code to test playerSeasonStats
        //instance.playerSeasonStats(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('playerSeasonStatsByPlayer', function() {
      it('should call playerSeasonStatsByPlayer successfully', function(done) {
        //uncomment below and update the code to test playerSeasonStatsByPlayer
        //instance.playerSeasonStatsByPlayer(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('playerSeasonStatsByTeam', function() {
      it('should call playerSeasonStatsByTeam successfully', function(done) {
        //uncomment below and update the code to test playerSeasonStatsByTeam
        //instance.playerSeasonStatsByTeam(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('playersByTeam', function() {
      it('should call playersByTeam successfully', function(done) {
        //uncomment below and update the code to test playersByTeam
        //instance.playersByTeam(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('schedules', function() {
      it('should call schedules successfully', function(done) {
        //uncomment below and update the code to test schedules
        //instance.schedules(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('stadiums', function() {
      it('should call stadiums successfully', function(done) {
        //uncomment below and update the code to test stadiums
        //instance.stadiums(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('standings', function() {
      it('should call standings successfully', function(done) {
        //uncomment below and update the code to test standings
        //instance.standings(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('teamGameLogsBySeason', function() {
      it('should call teamGameLogsBySeason successfully', function(done) {
        //uncomment below and update the code to test teamGameLogsBySeason
        //instance.teamGameLogsBySeason(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('teamGameStatsByDate', function() {
      it('should call teamGameStatsByDate successfully', function(done) {
        //uncomment below and update the code to test teamGameStatsByDate
        //instance.teamGameStatsByDate(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('teamSeasonStats', function() {
      it('should call teamSeasonStats successfully', function(done) {
        //uncomment below and update the code to test teamSeasonStats
        //instance.teamSeasonStats(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('teamStatsAllowedByPosition', function() {
      it('should call teamStatsAllowedByPosition successfully', function(done) {
        //uncomment below and update the code to test teamStatsAllowedByPosition
        //instance.teamStatsAllowedByPosition(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('teamsActive', function() {
      it('should call teamsActive successfully', function(done) {
        //uncomment below and update the code to test teamsActive
        //instance.teamsActive(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('teamsAll', function() {
      it('should call teamsAll successfully', function(done) {
        //uncomment below and update the code to test teamsAll
        //instance.teamsAll(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
  });

}));
