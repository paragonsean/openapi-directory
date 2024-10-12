/**
 * reverb
 * reverb
 *
 * The version of the OpenAPI document: 3.0
 * Contact: integrations@reverb.com
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
    factory(root.expect, root.Reverb);
  }
}(this, function(expect, Reverb) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new Reverb.ShopsApi();
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

  describe('ShopsApi', function() {
    describe('shopsIdStorefrontsGet', function() {
      it('should call shopsIdStorefrontsGet successfully', function(done) {
        //uncomment below and update the code to test shopsIdStorefrontsGet
        //instance.shopsIdStorefrontsGet(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('shopsShopIdShippingProfilesGet', function() {
      it('should call shopsShopIdShippingProfilesGet successfully', function(done) {
        //uncomment below and update the code to test shopsShopIdShippingProfilesGet
        //instance.shopsShopIdShippingProfilesGet(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('shopsSlugFeedbackBuyerGet', function() {
      it('should call shopsSlugFeedbackBuyerGet successfully', function(done) {
        //uncomment below and update the code to test shopsSlugFeedbackBuyerGet
        //instance.shopsSlugFeedbackBuyerGet(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('shopsSlugFeedbackGet', function() {
      it('should call shopsSlugFeedbackGet successfully', function(done) {
        //uncomment below and update the code to test shopsSlugFeedbackGet
        //instance.shopsSlugFeedbackGet(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('shopsSlugFeedbackSellerGet', function() {
      it('should call shopsSlugFeedbackSellerGet successfully', function(done) {
        //uncomment below and update the code to test shopsSlugFeedbackSellerGet
        //instance.shopsSlugFeedbackSellerGet(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('shopsSlugGet', function() {
      it('should call shopsSlugGet successfully', function(done) {
        //uncomment below and update the code to test shopsSlugGet
        //instance.shopsSlugGet(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
  });

}));
