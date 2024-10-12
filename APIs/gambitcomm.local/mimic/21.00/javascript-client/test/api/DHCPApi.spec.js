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
    instance = new MimicRestApi.DHCPApi();
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

  describe('DHCPApi', function() {
    describe('protocolDhcpGetArgs', function() {
      it('should call protocolDhcpGetArgs successfully', function(done) {
        //uncomment below and update the code to test protocolDhcpGetArgs
        //instance.protocolDhcpGetArgs(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('protocolDhcpGetConfig', function() {
      it('should call protocolDhcpGetConfig successfully', function(done) {
        //uncomment below and update the code to test protocolDhcpGetConfig
        //instance.protocolDhcpGetConfig(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('protocolDhcpGetStatistics', function() {
      it('should call protocolDhcpGetStatistics successfully', function(done) {
        //uncomment below and update the code to test protocolDhcpGetStatistics
        //instance.protocolDhcpGetStatistics(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('protocolDhcpGetStatsHdr', function() {
      it('should call protocolDhcpGetStatsHdr successfully', function(done) {
        //uncomment below and update the code to test protocolDhcpGetStatsHdr
        //instance.protocolDhcpGetStatsHdr(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('protocolDhcpGetTrace', function() {
      it('should call protocolDhcpGetTrace successfully', function(done) {
        //uncomment below and update the code to test protocolDhcpGetTrace
        //instance.protocolDhcpGetTrace(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('protocolDhcpParams', function() {
      it('should call protocolDhcpParams successfully', function(done) {
        //uncomment below and update the code to test protocolDhcpParams
        //instance.protocolDhcpParams(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('protocolDhcpSetConfig', function() {
      it('should call protocolDhcpSetConfig successfully', function(done) {
        //uncomment below and update the code to test protocolDhcpSetConfig
        //instance.protocolDhcpSetConfig(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('protocolDhcpSetTrace', function() {
      it('should call protocolDhcpSetTrace successfully', function(done) {
        //uncomment below and update the code to test protocolDhcpSetTrace
        //instance.protocolDhcpSetTrace(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
  });

}));
