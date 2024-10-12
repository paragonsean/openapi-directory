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
    instance = new Reverb.ConversationsConversationIdOfferPostRequestOfferItemsInner();
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

  describe('ConversationsConversationIdOfferPostRequestOfferItemsInner', function() {
    it('should create an instance of ConversationsConversationIdOfferPostRequestOfferItemsInner', function() {
      // uncomment below and update the code to test ConversationsConversationIdOfferPostRequestOfferItemsInner
      //var instance = new Reverb.ConversationsConversationIdOfferPostRequestOfferItemsInner();
      //expect(instance).to.be.a(Reverb.ConversationsConversationIdOfferPostRequestOfferItemsInner);
    });

    it('should have the property listingId (base name: "listing_id")', function() {
      // uncomment below and update the code to test the property listingId
      //var instance = new Reverb.ConversationsConversationIdOfferPostRequestOfferItemsInner();
      //expect(instance).to.be();
    });

    it('should have the property price (base name: "price")', function() {
      // uncomment below and update the code to test the property price
      //var instance = new Reverb.ConversationsConversationIdOfferPostRequestOfferItemsInner();
      //expect(instance).to.be();
    });

    it('should have the property shippingPrice (base name: "shipping_price")', function() {
      // uncomment below and update the code to test the property shippingPrice
      //var instance = new Reverb.ConversationsConversationIdOfferPostRequestOfferItemsInner();
      //expect(instance).to.be();
    });

  });

}));
