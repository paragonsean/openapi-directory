/**
 * AGCO API
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: v1
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
    factory(root.expect, root.AgcoApi);
  }
}(this, function(expect, AgcoApi) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new AgcoApi.PriorityPackagesApi();
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

  describe('PriorityPackagesApi', function() {
    describe('priorityPackagesDeletePriorityPackages', function() {
      it('should call priorityPackagesDeletePriorityPackages successfully', function(done) {
        //uncomment below and update the code to test priorityPackagesDeletePriorityPackages
        //instance.priorityPackagesDeletePriorityPackages(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('priorityPackagesGetPriorityPackage', function() {
      it('should call priorityPackagesGetPriorityPackage successfully', function(done) {
        //uncomment below and update the code to test priorityPackagesGetPriorityPackage
        //instance.priorityPackagesGetPriorityPackage(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('priorityPackagesGetPriorityPackages', function() {
      it('should call priorityPackagesGetPriorityPackages successfully', function(done) {
        //uncomment below and update the code to test priorityPackagesGetPriorityPackages
        //instance.priorityPackagesGetPriorityPackages(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('priorityPackagesPostPriorityPackages', function() {
      it('should call priorityPackagesPostPriorityPackages successfully', function(done) {
        //uncomment below and update the code to test priorityPackagesPostPriorityPackages
        //instance.priorityPackagesPostPriorityPackages(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
  });

}));
