/**
 * SubscriptionClient
 * The User Subscription Management Client.
 *
 * The version of the OpenAPI document: 2015-11-01
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
    factory(root.expect, root.SubscriptionClient);
  }
}(this, function(expect, SubscriptionClient) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new SubscriptionClient.DelegatedProviderOffersApi();
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

  describe('DelegatedProviderOffersApi', function() {
    describe('delegatedProviderOffersGet', function() {
      it('should call delegatedProviderOffersGet successfully', function(done) {
        //uncomment below and update the code to test delegatedProviderOffersGet
        //instance.delegatedProviderOffersGet(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('delegatedProviderOffersList', function() {
      it('should call delegatedProviderOffersList successfully', function(done) {
        //uncomment below and update the code to test delegatedProviderOffersList
        //instance.delegatedProviderOffersList(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
  });

}));
