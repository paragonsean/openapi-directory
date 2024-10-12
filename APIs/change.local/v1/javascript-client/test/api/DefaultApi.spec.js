/**
 * API V1
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
    factory(root.expect, root.ApiV1);
  }
}(this, function(expect, ApiV1) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new ApiV1.DefaultApi();
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
    describe('apiV1DonationsCarbonCalculateGet', function() {
      it('should call apiV1DonationsCarbonCalculateGet successfully', function(done) {
        //uncomment below and update the code to test apiV1DonationsCarbonCalculateGet
        //instance.apiV1DonationsCarbonCalculateGet(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('apiV1DonationsCarbonStatsGet', function() {
      it('should call apiV1DonationsCarbonStatsGet successfully', function(done) {
        //uncomment below and update the code to test apiV1DonationsCarbonStatsGet
        //instance.apiV1DonationsCarbonStatsGet(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('apiV1DonationsCreatePost', function() {
      it('should call apiV1DonationsCreatePost successfully', function(done) {
        //uncomment below and update the code to test apiV1DonationsCreatePost
        //instance.apiV1DonationsCreatePost(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('apiV1DonationsCryptoCalculateGet', function() {
      it('should call apiV1DonationsCryptoCalculateGet successfully', function(done) {
        //uncomment below and update the code to test apiV1DonationsCryptoCalculateGet
        //instance.apiV1DonationsCryptoCalculateGet(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('apiV1DonationsIndexGet', function() {
      it('should call apiV1DonationsIndexGet successfully', function(done) {
        //uncomment below and update the code to test apiV1DonationsIndexGet
        //instance.apiV1DonationsIndexGet(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('apiV1DonationsShowGet', function() {
      it('should call apiV1DonationsShowGet successfully', function(done) {
        //uncomment below and update the code to test apiV1DonationsShowGet
        //instance.apiV1DonationsShowGet(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('apiV1NonprofitsListGet', function() {
      it('should call apiV1NonprofitsListGet successfully', function(done) {
        //uncomment below and update the code to test apiV1NonprofitsListGet
        //instance.apiV1NonprofitsListGet(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('apiV1NonprofitsShowGet', function() {
      it('should call apiV1NonprofitsShowGet successfully', function(done) {
        //uncomment below and update the code to test apiV1NonprofitsShowGet
        //instance.apiV1NonprofitsShowGet(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
  });

}));
