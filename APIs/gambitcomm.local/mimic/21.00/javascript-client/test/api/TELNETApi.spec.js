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
    instance = new MimicRestApi.TELNETApi();
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

  describe('TELNETApi', function() {
    describe('protocolTelnetConnectionLogon', function() {
      it('should call protocolTelnetConnectionLogon successfully', function(done) {
        //uncomment below and update the code to test protocolTelnetConnectionLogon
        //instance.protocolTelnetConnectionLogon(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('protocolTelnetConnectionRequest', function() {
      it('should call protocolTelnetConnectionRequest successfully', function(done) {
        //uncomment below and update the code to test protocolTelnetConnectionRequest
        //instance.protocolTelnetConnectionRequest(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('protocolTelnetConnectionSignal', function() {
      it('should call protocolTelnetConnectionSignal successfully', function(done) {
        //uncomment below and update the code to test protocolTelnetConnectionSignal
        //instance.protocolTelnetConnectionSignal(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('protocolTelnetGetArgs', function() {
      it('should call protocolTelnetGetArgs successfully', function(done) {
        //uncomment below and update the code to test protocolTelnetGetArgs
        //instance.protocolTelnetGetArgs(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('protocolTelnetGetConfig', function() {
      it('should call protocolTelnetGetConfig successfully', function(done) {
        //uncomment below and update the code to test protocolTelnetGetConfig
        //instance.protocolTelnetGetConfig(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('protocolTelnetGetStatistics', function() {
      it('should call protocolTelnetGetStatistics successfully', function(done) {
        //uncomment below and update the code to test protocolTelnetGetStatistics
        //instance.protocolTelnetGetStatistics(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('protocolTelnetGetStatsHdr', function() {
      it('should call protocolTelnetGetStatsHdr successfully', function(done) {
        //uncomment below and update the code to test protocolTelnetGetStatsHdr
        //instance.protocolTelnetGetStatsHdr(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('protocolTelnetGetTrace', function() {
      it('should call protocolTelnetGetTrace successfully', function(done) {
        //uncomment below and update the code to test protocolTelnetGetTrace
        //instance.protocolTelnetGetTrace(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('protocolTelnetIpaliasDisable', function() {
      it('should call protocolTelnetIpaliasDisable successfully', function(done) {
        //uncomment below and update the code to test protocolTelnetIpaliasDisable
        //instance.protocolTelnetIpaliasDisable(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('protocolTelnetIpaliasEnable', function() {
      it('should call protocolTelnetIpaliasEnable successfully', function(done) {
        //uncomment below and update the code to test protocolTelnetIpaliasEnable
        //instance.protocolTelnetIpaliasEnable(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('protocolTelnetIpaliasIsenabled', function() {
      it('should call protocolTelnetIpaliasIsenabled successfully', function(done) {
        //uncomment below and update the code to test protocolTelnetIpaliasIsenabled
        //instance.protocolTelnetIpaliasIsenabled(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('protocolTelnetIpaliasList', function() {
      it('should call protocolTelnetIpaliasList successfully', function(done) {
        //uncomment below and update the code to test protocolTelnetIpaliasList
        //instance.protocolTelnetIpaliasList(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('protocolTelnetServerGetConnections', function() {
      it('should call protocolTelnetServerGetConnections successfully', function(done) {
        //uncomment below and update the code to test protocolTelnetServerGetConnections
        //instance.protocolTelnetServerGetConnections(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('protocolTelnetServerGetKeymap', function() {
      it('should call protocolTelnetServerGetKeymap successfully', function(done) {
        //uncomment below and update the code to test protocolTelnetServerGetKeymap
        //instance.protocolTelnetServerGetKeymap(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('protocolTelnetServerGetRulesdb', function() {
      it('should call protocolTelnetServerGetRulesdb successfully', function(done) {
        //uncomment below and update the code to test protocolTelnetServerGetRulesdb
        //instance.protocolTelnetServerGetRulesdb(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('protocolTelnetServerGetState', function() {
      it('should call protocolTelnetServerGetState successfully', function(done) {
        //uncomment below and update the code to test protocolTelnetServerGetState
        //instance.protocolTelnetServerGetState(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('protocolTelnetServerGetUserdb', function() {
      it('should call protocolTelnetServerGetUserdb successfully', function(done) {
        //uncomment below and update the code to test protocolTelnetServerGetUserdb
        //instance.protocolTelnetServerGetUserdb(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('protocolTelnetServerGetUsers', function() {
      it('should call protocolTelnetServerGetUsers successfully', function(done) {
        //uncomment below and update the code to test protocolTelnetServerGetUsers
        //instance.protocolTelnetServerGetUsers(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('protocolTelnetSetConfig', function() {
      it('should call protocolTelnetSetConfig successfully', function(done) {
        //uncomment below and update the code to test protocolTelnetSetConfig
        //instance.protocolTelnetSetConfig(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('protocolTelnetSetTrace', function() {
      it('should call protocolTelnetSetTrace successfully', function(done) {
        //uncomment below and update the code to test protocolTelnetSetTrace
        //instance.protocolTelnetSetTrace(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
  });

}));
