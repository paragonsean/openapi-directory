/**
 * DRACOON API
 * REST Web Services for DRACOON<br><br>This page provides an overview of all available and documented DRACOON APIs, which are grouped by tags.<br>Each tag provides a collection of APIs that are intended for a specific area of the DRACOON.<br><br><a title='Developer Information' href='https://developer.dracoon.com'>Developer Information</a>&emsp;&emsp;<a title='Get SDKs on GitHub' href='https://github.com/dracoon'>Get SDKs on GitHub</a><br><br><a title='Terms of service' href='https://www.dracoon.com/terms/general-terms-and-conditions/'>Terms of service</a>
 *
 * The version of the OpenAPI document: 4.42.3
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
    factory(root.expect, root.DracoonApi);
  }
}(this, function(expect, DracoonApi) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new DracoonApi.SystemSettingsConfigApi();
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

  describe('SystemSettingsConfigApi', function() {
    describe('requestAuthConfig', function() {
      it('should call requestAuthConfig successfully', function(done) {
        //uncomment below and update the code to test requestAuthConfig
        //instance.requestAuthConfig(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('requestEventlogConfig', function() {
      it('should call requestEventlogConfig successfully', function(done) {
        //uncomment below and update the code to test requestEventlogConfig
        //instance.requestEventlogConfig(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('requestGeneralSettings', function() {
      it('should call requestGeneralSettings successfully', function(done) {
        //uncomment below and update the code to test requestGeneralSettings
        //instance.requestGeneralSettings(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('requestInfrastructureProperties', function() {
      it('should call requestInfrastructureProperties successfully', function(done) {
        //uncomment below and update the code to test requestInfrastructureProperties
        //instance.requestInfrastructureProperties(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('requestSyslogConfig', function() {
      it('should call requestSyslogConfig successfully', function(done) {
        //uncomment below and update the code to test requestSyslogConfig
        //instance.requestSyslogConfig(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('requestSystemDefaults', function() {
      it('should call requestSystemDefaults successfully', function(done) {
        //uncomment below and update the code to test requestSystemDefaults
        //instance.requestSystemDefaults(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('updateAuthConfig', function() {
      it('should call updateAuthConfig successfully', function(done) {
        //uncomment below and update the code to test updateAuthConfig
        //instance.updateAuthConfig(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('updateEventlogConfig', function() {
      it('should call updateEventlogConfig successfully', function(done) {
        //uncomment below and update the code to test updateEventlogConfig
        //instance.updateEventlogConfig(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('updateGeneralSettings', function() {
      it('should call updateGeneralSettings successfully', function(done) {
        //uncomment below and update the code to test updateGeneralSettings
        //instance.updateGeneralSettings(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('updateSyslogConfig', function() {
      it('should call updateSyslogConfig successfully', function(done) {
        //uncomment below and update the code to test updateSyslogConfig
        //instance.updateSyslogConfig(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('updateSystemDefaults', function() {
      it('should call updateSystemDefaults successfully', function(done) {
        //uncomment below and update the code to test updateSystemDefaults
        //instance.updateSystemDefaults(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
  });

}));
