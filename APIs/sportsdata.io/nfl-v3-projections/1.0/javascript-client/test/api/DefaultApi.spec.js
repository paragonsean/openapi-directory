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

(function(root, factory) {
  if (typeof define === 'function' && define.amd) {
    // AMD.
    define(['expect.js', process.cwd()+'/src/index'], factory);
  } else if (typeof module === 'object' && module.exports) {
    // CommonJS-like environments that support module.exports, like Node.
    factory(require('expect.js'), require(process.cwd()+'/src/index'));
  } else {
    // Browser globals (root is window)
    factory(root.expect, root.NflV3Projections);
  }
}(this, function(expect, NflV3Projections) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new NflV3Projections.DefaultApi();
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
    describe('dfsSlateOwnershipProjectionsBySlateid', function() {
      it('should call dfsSlateOwnershipProjectionsBySlateid successfully', function(done) {
        //uncomment below and update the code to test dfsSlateOwnershipProjectionsBySlateid
        //instance.dfsSlateOwnershipProjectionsBySlateid(function(error) {
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
    describe('dfsSlatesByWeek', function() {
      it('should call dfsSlatesByWeek successfully', function(done) {
        //uncomment below and update the code to test dfsSlatesByWeek
        //instance.dfsSlatesByWeek(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('idpProjectedPlayerGameStatsByPlayerWInjuriesLineupsDfsSalaries', function() {
      it('should call idpProjectedPlayerGameStatsByPlayerWInjuriesLineupsDfsSalaries successfully', function(done) {
        //uncomment below and update the code to test idpProjectedPlayerGameStatsByPlayerWInjuriesLineupsDfsSalaries
        //instance.idpProjectedPlayerGameStatsByPlayerWInjuriesLineupsDfsSalaries(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('idpProjectedPlayerGameStatsByTeamWInjuriesLineupsDfsSalaries', function() {
      it('should call idpProjectedPlayerGameStatsByTeamWInjuriesLineupsDfsSalaries successfully', function(done) {
        //uncomment below and update the code to test idpProjectedPlayerGameStatsByTeamWInjuriesLineupsDfsSalaries
        //instance.idpProjectedPlayerGameStatsByTeamWInjuriesLineupsDfsSalaries(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('idpProjectedPlayerGameStatsByWeekWInjuriesLineupsDfsSalaries', function() {
      it('should call idpProjectedPlayerGameStatsByWeekWInjuriesLineupsDfsSalaries successfully', function(done) {
        //uncomment below and update the code to test idpProjectedPlayerGameStatsByWeekWInjuriesLineupsDfsSalaries
        //instance.idpProjectedPlayerGameStatsByWeekWInjuriesLineupsDfsSalaries(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('injuredPlayers', function() {
      it('should call injuredPlayers successfully', function(done) {
        //uncomment below and update the code to test injuredPlayers
        //instance.injuredPlayers(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('projectedFantasyDefenseGameStatsWDfsSalaries', function() {
      it('should call projectedFantasyDefenseGameStatsWDfsSalaries successfully', function(done) {
        //uncomment below and update the code to test projectedFantasyDefenseGameStatsWDfsSalaries
        //instance.projectedFantasyDefenseGameStatsWDfsSalaries(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('projectedFantasyDefenseSeasonStatsWAdp', function() {
      it('should call projectedFantasyDefenseSeasonStatsWAdp successfully', function(done) {
        //uncomment below and update the code to test projectedFantasyDefenseSeasonStatsWAdp
        //instance.projectedFantasyDefenseSeasonStatsWAdp(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('projectedPlayerGameStatsByPlayerWInjuriesLineupsDfsSalaries', function() {
      it('should call projectedPlayerGameStatsByPlayerWInjuriesLineupsDfsSalaries successfully', function(done) {
        //uncomment below and update the code to test projectedPlayerGameStatsByPlayerWInjuriesLineupsDfsSalaries
        //instance.projectedPlayerGameStatsByPlayerWInjuriesLineupsDfsSalaries(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('projectedPlayerGameStatsByTeamWInjuriesLineupsDfsSalaries', function() {
      it('should call projectedPlayerGameStatsByTeamWInjuriesLineupsDfsSalaries successfully', function(done) {
        //uncomment below and update the code to test projectedPlayerGameStatsByTeamWInjuriesLineupsDfsSalaries
        //instance.projectedPlayerGameStatsByTeamWInjuriesLineupsDfsSalaries(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('projectedPlayerGameStatsByWeekWInjuriesLineupsDfsSalaries', function() {
      it('should call projectedPlayerGameStatsByWeekWInjuriesLineupsDfsSalaries successfully', function(done) {
        //uncomment below and update the code to test projectedPlayerGameStatsByWeekWInjuriesLineupsDfsSalaries
        //instance.projectedPlayerGameStatsByWeekWInjuriesLineupsDfsSalaries(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('projectedPlayerSeasonStatsByPlayerWAdp', function() {
      it('should call projectedPlayerSeasonStatsByPlayerWAdp successfully', function(done) {
        //uncomment below and update the code to test projectedPlayerSeasonStatsByPlayerWAdp
        //instance.projectedPlayerSeasonStatsByPlayerWAdp(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('projectedPlayerSeasonStatsByTeamWAdp', function() {
      it('should call projectedPlayerSeasonStatsByTeamWAdp successfully', function(done) {
        //uncomment below and update the code to test projectedPlayerSeasonStatsByTeamWAdp
        //instance.projectedPlayerSeasonStatsByTeamWAdp(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('projectedPlayerSeasonStatsWAdp', function() {
      it('should call projectedPlayerSeasonStatsWAdp successfully', function(done) {
        //uncomment below and update the code to test projectedPlayerSeasonStatsWAdp
        //instance.projectedPlayerSeasonStatsWAdp(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('upcomingDfsSlateOwnershipProjections', function() {
      it('should call upcomingDfsSlateOwnershipProjections successfully', function(done) {
        //uncomment below and update the code to test upcomingDfsSlateOwnershipProjections
        //instance.upcomingDfsSlateOwnershipProjections(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
  });

}));
