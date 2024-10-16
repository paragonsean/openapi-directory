/**
 * NHL v3 Projections
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
    factory(root.expect, root.NhlV3Projections);
  }
}(this, function(expect, NhlV3Projections) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new NhlV3Projections.DefaultApi();
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
    describe('projectedPlayerGameStatsByDateWInjuriesDfsSalaries', function() {
      it('should call projectedPlayerGameStatsByDateWInjuriesDfsSalaries successfully', function(done) {
        //uncomment below and update the code to test projectedPlayerGameStatsByDateWInjuriesDfsSalaries
        //instance.projectedPlayerGameStatsByDateWInjuriesDfsSalaries(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('projectedPlayerGameStatsByPlayerWInjuriesDfsSalaries', function() {
      it('should call projectedPlayerGameStatsByPlayerWInjuriesDfsSalaries successfully', function(done) {
        //uncomment below and update the code to test projectedPlayerGameStatsByPlayerWInjuriesDfsSalaries
        //instance.projectedPlayerGameStatsByPlayerWInjuriesDfsSalaries(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('startingGoaltendersByDate', function() {
      it('should call startingGoaltendersByDate successfully', function(done) {
        //uncomment below and update the code to test startingGoaltendersByDate
        //instance.startingGoaltendersByDate(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
  });

}));
