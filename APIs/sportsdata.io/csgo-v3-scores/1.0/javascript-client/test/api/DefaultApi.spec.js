/**
 * CS:GO v3 Scores
 * CS:GO v3 Scores
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
    factory(root.expect, root.CsgoV3Scores);
  }
}(this, function(expect, CsgoV3Scores) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new CsgoV3Scores.DefaultApi();
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
    describe('areasCountries', function() {
      it('should call areasCountries successfully', function(done) {
        //uncomment below and update the code to test areasCountries
        //instance.areasCountries(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('competitionFixturesLeagueDetails', function() {
      it('should call competitionFixturesLeagueDetails successfully', function(done) {
        //uncomment below and update the code to test competitionFixturesLeagueDetails
        //instance.competitionFixturesLeagueDetails(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('competitionsLeagues', function() {
      it('should call competitionsLeagues successfully', function(done) {
        //uncomment below and update the code to test competitionsLeagues
        //instance.competitionsLeagues(function(error) {
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
    describe('membershipsActive', function() {
      it('should call membershipsActive successfully', function(done) {
        //uncomment below and update the code to test membershipsActive
        //instance.membershipsActive(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('membershipsByTeamActive', function() {
      it('should call membershipsByTeamActive successfully', function(done) {
        //uncomment below and update the code to test membershipsByTeamActive
        //instance.membershipsByTeamActive(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('membershipsByTeamHistorical', function() {
      it('should call membershipsByTeamHistorical successfully', function(done) {
        //uncomment below and update the code to test membershipsByTeamHistorical
        //instance.membershipsByTeamHistorical(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('membershipsHistorical', function() {
      it('should call membershipsHistorical successfully', function(done) {
        //uncomment below and update the code to test membershipsHistorical
        //instance.membershipsHistorical(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('player', function() {
      it('should call player successfully', function(done) {
        //uncomment below and update the code to test player
        //instance.player(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('players', function() {
      it('should call players successfully', function(done) {
        //uncomment below and update the code to test players
        //instance.players(function(error) {
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
    describe('schedule', function() {
      it('should call schedule successfully', function(done) {
        //uncomment below and update the code to test schedule
        //instance.schedule(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('seasonTeams', function() {
      it('should call seasonTeams successfully', function(done) {
        //uncomment below and update the code to test seasonTeams
        //instance.seasonTeams(function(error) {
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
    describe('teams', function() {
      it('should call teams successfully', function(done) {
        //uncomment below and update the code to test teams
        //instance.teams(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('venues', function() {
      it('should call venues successfully', function(done) {
        //uncomment below and update the code to test venues
        //instance.venues(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
  });

}));
