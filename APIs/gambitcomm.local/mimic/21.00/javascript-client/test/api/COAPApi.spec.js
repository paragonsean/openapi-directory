/**
 * MIMIC REST API
 * This is the API for MIMIC client to connect to MIMIC daemon.
 *
 * The version of the OpenAPI document: 21.00
 * Contact: support@gambitcomm.com
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
    factory(root.expect, root.MimicRestApi);
  }
}(this, function(expect, MimicRestApi) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new MimicRestApi.COAPApi();
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

  describe('COAPApi', function() {
    describe('protocolCoapGetArgs', function() {
      it('should call protocolCoapGetArgs successfully', function(done) {
        //uncomment below and update the code to test protocolCoapGetArgs
        //instance.protocolCoapGetArgs(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('protocolCoapGetConfig', function() {
      it('should call protocolCoapGetConfig successfully', function(done) {
        //uncomment below and update the code to test protocolCoapGetConfig
        //instance.protocolCoapGetConfig(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('protocolCoapGetStatistics', function() {
      it('should call protocolCoapGetStatistics successfully', function(done) {
        //uncomment below and update the code to test protocolCoapGetStatistics
        //instance.protocolCoapGetStatistics(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('protocolCoapGetStatsHdr', function() {
      it('should call protocolCoapGetStatsHdr successfully', function(done) {
        //uncomment below and update the code to test protocolCoapGetStatsHdr
        //instance.protocolCoapGetStatsHdr(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('protocolCoapGetTrace', function() {
      it('should call protocolCoapGetTrace successfully', function(done) {
        //uncomment below and update the code to test protocolCoapGetTrace
        //instance.protocolCoapGetTrace(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('protocolCoapSetConfig', function() {
      it('should call protocolCoapSetConfig successfully', function(done) {
        //uncomment below and update the code to test protocolCoapSetConfig
        //instance.protocolCoapSetConfig(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('protocolCoapSetTrace', function() {
      it('should call protocolCoapSetTrace successfully', function(done) {
        //uncomment below and update the code to test protocolCoapSetTrace
        //instance.protocolCoapSetTrace(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
  });

}));
