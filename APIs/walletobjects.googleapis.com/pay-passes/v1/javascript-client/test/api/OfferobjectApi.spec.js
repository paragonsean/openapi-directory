/**
 * Google Pay Passes API
 * API for issuers to save and manage Google Wallet Objects.
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
    factory(root.expect, root.GooglePayPassesApi);
  }
}(this, function(expect, GooglePayPassesApi) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new GooglePayPassesApi.OfferobjectApi();
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

  describe('OfferobjectApi', function() {
    describe('walletobjectsOfferobjectAddmessage', function() {
      it('should call walletobjectsOfferobjectAddmessage successfully', function(done) {
        //uncomment below and update the code to test walletobjectsOfferobjectAddmessage
        //instance.walletobjectsOfferobjectAddmessage(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('walletobjectsOfferobjectGet', function() {
      it('should call walletobjectsOfferobjectGet successfully', function(done) {
        //uncomment below and update the code to test walletobjectsOfferobjectGet
        //instance.walletobjectsOfferobjectGet(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('walletobjectsOfferobjectInsert', function() {
      it('should call walletobjectsOfferobjectInsert successfully', function(done) {
        //uncomment below and update the code to test walletobjectsOfferobjectInsert
        //instance.walletobjectsOfferobjectInsert(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('walletobjectsOfferobjectList', function() {
      it('should call walletobjectsOfferobjectList successfully', function(done) {
        //uncomment below and update the code to test walletobjectsOfferobjectList
        //instance.walletobjectsOfferobjectList(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('walletobjectsOfferobjectPatch', function() {
      it('should call walletobjectsOfferobjectPatch successfully', function(done) {
        //uncomment below and update the code to test walletobjectsOfferobjectPatch
        //instance.walletobjectsOfferobjectPatch(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('walletobjectsOfferobjectUpdate', function() {
      it('should call walletobjectsOfferobjectUpdate successfully', function(done) {
        //uncomment below and update the code to test walletobjectsOfferobjectUpdate
        //instance.walletobjectsOfferobjectUpdate(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
  });

}));
