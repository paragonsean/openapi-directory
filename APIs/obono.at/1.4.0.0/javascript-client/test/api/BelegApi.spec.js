/**
 * obono RKSV API
 * Provides a RESTful API for interacting with virtual cash registers and creating receipts that are conform with the Registrierkassensicherheitsverordnung (RKSV).  You may find our [automatically generated clients](./clients) for various programming languages and environments helpful... 
 *
 * The version of the OpenAPI document: 1.4.0.0
 * Contact: info@obono.at
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
    factory(root.expect, root.ObonoRksvApi);
  }
}(this, function(expect, ObonoRksvApi) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new ObonoRksvApi.BelegApi();
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

  describe('BelegApi', function() {
    describe('addBeleg', function() {
      it('should call addBeleg successfully', function(done) {
        //uncomment below and update the code to test addBeleg
        //instance.addBeleg(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('belegeBelegUuidGet', function() {
      it('should call belegeBelegUuidGet successfully', function(done) {
        //uncomment below and update the code to test belegeBelegUuidGet
        //instance.belegeBelegUuidGet(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('createAbschluss', function() {
      it('should call createAbschluss successfully', function(done) {
        //uncomment below and update the code to test createAbschluss
        //instance.createAbschluss(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('getBeleg', function() {
      it('should call getBeleg successfully', function(done) {
        //uncomment below and update the code to test getBeleg
        //instance.getBeleg(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('getBelege', function() {
      it('should call getBelege successfully', function(done) {
        //uncomment below and update the code to test getBelege
        //instance.getBelege(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
  });

}));
