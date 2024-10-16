/**
 * Microcks API v1.7
 * API offered by Microcks, the Kubernetes native tools for API and microservices mocking and testing (microcks.io)
 *
 * The version of the OpenAPI document: 1.7.0
 * Contact: laurent@microcks.io
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
    factory(root.expect, root.MicrocksApiV17);
  }
}(this, function(expect, MicrocksApiV17) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new MicrocksApiV17.MockApi();
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

  describe('MockApi', function() {
    describe('deleteService', function() {
      it('should call deleteService successfully', function(done) {
        //uncomment below and update the code to test deleteService
        //instance.deleteService(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('exportSnapshot', function() {
      it('should call exportSnapshot successfully', function(done) {
        //uncomment below and update the code to test exportSnapshot
        //instance.exportSnapshot(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('getService', function() {
      it('should call getService successfully', function(done) {
        //uncomment below and update the code to test getService
        //instance.getService(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('getServices', function() {
      it('should call getServices successfully', function(done) {
        //uncomment below and update the code to test getServices
        //instance.getServices(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('getServicesCounter', function() {
      it('should call getServicesCounter successfully', function(done) {
        //uncomment below and update the code to test getServicesCounter
        //instance.getServicesCounter(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('getServicesLabels', function() {
      it('should call getServicesLabels successfully', function(done) {
        //uncomment below and update the code to test getServicesLabels
        //instance.getServicesLabels(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('importSnapshot', function() {
      it('should call importSnapshot successfully', function(done) {
        //uncomment below and update the code to test importSnapshot
        //instance.importSnapshot(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('overrideServiceOperation', function() {
      it('should call overrideServiceOperation successfully', function(done) {
        //uncomment below and update the code to test overrideServiceOperation
        //instance.overrideServiceOperation(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('searchServices', function() {
      it('should call searchServices successfully', function(done) {
        //uncomment below and update the code to test searchServices
        //instance.searchServices(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('updateServiceMetadata', function() {
      it('should call updateServiceMetadata successfully', function(done) {
        //uncomment below and update the code to test updateServiceMetadata
        //instance.updateServiceMetadata(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
  });

}));
