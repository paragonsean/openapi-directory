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
    instance = new GooglePayPassesApi.LoyaltyclassApi();
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

  describe('LoyaltyclassApi', function() {
    describe('walletobjectsLoyaltyclassAddmessage', function() {
      it('should call walletobjectsLoyaltyclassAddmessage successfully', function(done) {
        //uncomment below and update the code to test walletobjectsLoyaltyclassAddmessage
        //instance.walletobjectsLoyaltyclassAddmessage(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('walletobjectsLoyaltyclassGet', function() {
      it('should call walletobjectsLoyaltyclassGet successfully', function(done) {
        //uncomment below and update the code to test walletobjectsLoyaltyclassGet
        //instance.walletobjectsLoyaltyclassGet(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('walletobjectsLoyaltyclassInsert', function() {
      it('should call walletobjectsLoyaltyclassInsert successfully', function(done) {
        //uncomment below and update the code to test walletobjectsLoyaltyclassInsert
        //instance.walletobjectsLoyaltyclassInsert(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('walletobjectsLoyaltyclassList', function() {
      it('should call walletobjectsLoyaltyclassList successfully', function(done) {
        //uncomment below and update the code to test walletobjectsLoyaltyclassList
        //instance.walletobjectsLoyaltyclassList(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('walletobjectsLoyaltyclassPatch', function() {
      it('should call walletobjectsLoyaltyclassPatch successfully', function(done) {
        //uncomment below and update the code to test walletobjectsLoyaltyclassPatch
        //instance.walletobjectsLoyaltyclassPatch(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('walletobjectsLoyaltyclassUpdate', function() {
      it('should call walletobjectsLoyaltyclassUpdate successfully', function(done) {
        //uncomment below and update the code to test walletobjectsLoyaltyclassUpdate
        //instance.walletobjectsLoyaltyclassUpdate(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
  });

}));
