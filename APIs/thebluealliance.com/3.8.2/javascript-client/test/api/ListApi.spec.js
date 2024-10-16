/**
 * The Blue Alliance API v3
 * # Overview    Information and statistics about FIRST Robotics Competition teams and events.   # Authentication   All endpoints require an Auth Key to be passed in the header `X-TBA-Auth-Key`. If you do not have an auth key yet, you can obtain one from your [Account Page](/account).
 *
 * The version of the OpenAPI document: 3.8.2
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
    factory(root.expect, root.TheBlueAllianceApiV3);
  }
}(this, function(expect, TheBlueAllianceApiV3) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new TheBlueAllianceApiV3.ListApi();
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

  describe('ListApi', function() {
    describe('getDistrictEventsKeys_1', function() {
      it('should call getDistrictEventsKeys_1 successfully', function(done) {
        //uncomment below and update the code to test getDistrictEventsKeys_1
        //instance.getDistrictEventsKeys_1(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('getDistrictEventsSimple_1', function() {
      it('should call getDistrictEventsSimple_1 successfully', function(done) {
        //uncomment below and update the code to test getDistrictEventsSimple_1
        //instance.getDistrictEventsSimple_1(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('getDistrictEvents_1', function() {
      it('should call getDistrictEvents_1 successfully', function(done) {
        //uncomment below and update the code to test getDistrictEvents_1
        //instance.getDistrictEvents_1(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('getDistrictRankings_1', function() {
      it('should call getDistrictRankings_1 successfully', function(done) {
        //uncomment below and update the code to test getDistrictRankings_1
        //instance.getDistrictRankings_1(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('getDistrictTeamsKeys_1', function() {
      it('should call getDistrictTeamsKeys_1 successfully', function(done) {
        //uncomment below and update the code to test getDistrictTeamsKeys_1
        //instance.getDistrictTeamsKeys_1(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('getDistrictTeamsSimple_1', function() {
      it('should call getDistrictTeamsSimple_1 successfully', function(done) {
        //uncomment below and update the code to test getDistrictTeamsSimple_1
        //instance.getDistrictTeamsSimple_1(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('getDistrictTeams_1', function() {
      it('should call getDistrictTeams_1 successfully', function(done) {
        //uncomment below and update the code to test getDistrictTeams_1
        //instance.getDistrictTeams_1(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('getEventTeamsKeys_1', function() {
      it('should call getEventTeamsKeys_1 successfully', function(done) {
        //uncomment below and update the code to test getEventTeamsKeys_1
        //instance.getEventTeamsKeys_1(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('getEventTeamsSimple_1', function() {
      it('should call getEventTeamsSimple_1 successfully', function(done) {
        //uncomment below and update the code to test getEventTeamsSimple_1
        //instance.getEventTeamsSimple_1(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('getEventTeamsStatuses_1', function() {
      it('should call getEventTeamsStatuses_1 successfully', function(done) {
        //uncomment below and update the code to test getEventTeamsStatuses_1
        //instance.getEventTeamsStatuses_1(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('getEventTeams_1', function() {
      it('should call getEventTeams_1 successfully', function(done) {
        //uncomment below and update the code to test getEventTeams_1
        //instance.getEventTeams_1(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('getEventsByYearKeys_0', function() {
      it('should call getEventsByYearKeys_0 successfully', function(done) {
        //uncomment below and update the code to test getEventsByYearKeys_0
        //instance.getEventsByYearKeys_0(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('getEventsByYearSimple_0', function() {
      it('should call getEventsByYearSimple_0 successfully', function(done) {
        //uncomment below and update the code to test getEventsByYearSimple_0
        //instance.getEventsByYearSimple_0(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('getEventsByYear_0', function() {
      it('should call getEventsByYear_0 successfully', function(done) {
        //uncomment below and update the code to test getEventsByYear_0
        //instance.getEventsByYear_0(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('getTeamEventsStatusesByYear', function() {
      it('should call getTeamEventsStatusesByYear successfully', function(done) {
        //uncomment below and update the code to test getTeamEventsStatusesByYear
        //instance.getTeamEventsStatusesByYear(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('getTeamsByYearKeys_0', function() {
      it('should call getTeamsByYearKeys_0 successfully', function(done) {
        //uncomment below and update the code to test getTeamsByYearKeys_0
        //instance.getTeamsByYearKeys_0(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('getTeamsByYearSimple_0', function() {
      it('should call getTeamsByYearSimple_0 successfully', function(done) {
        //uncomment below and update the code to test getTeamsByYearSimple_0
        //instance.getTeamsByYearSimple_0(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('getTeamsByYear_0', function() {
      it('should call getTeamsByYear_0 successfully', function(done) {
        //uncomment below and update the code to test getTeamsByYear_0
        //instance.getTeamsByYear_0(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('getTeamsKeys_0', function() {
      it('should call getTeamsKeys_0 successfully', function(done) {
        //uncomment below and update the code to test getTeamsKeys_0
        //instance.getTeamsKeys_0(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('getTeamsSimple_0', function() {
      it('should call getTeamsSimple_0 successfully', function(done) {
        //uncomment below and update the code to test getTeamsSimple_0
        //instance.getTeamsSimple_0(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('getTeams_0', function() {
      it('should call getTeams_0 successfully', function(done) {
        //uncomment below and update the code to test getTeams_0
        //instance.getTeams_0(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
  });

}));
