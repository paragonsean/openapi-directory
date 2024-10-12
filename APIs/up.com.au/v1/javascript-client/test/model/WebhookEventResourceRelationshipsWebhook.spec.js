/**
 * Up API
 * The Up API gives you programmatic access to your balances and transaction data. You can request past transactions or set up webhooks to receive real-time events when new transactions hit your account. It’s new, it’s exciting and it’s just the beginning. 
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
    factory(root.expect, root.UpApi);
  }
}(this, function(expect, UpApi) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new UpApi.WebhookEventResourceRelationshipsWebhook();
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

  describe('WebhookEventResourceRelationshipsWebhook', function() {
    it('should create an instance of WebhookEventResourceRelationshipsWebhook', function() {
      // uncomment below and update the code to test WebhookEventResourceRelationshipsWebhook
      //var instance = new UpApi.WebhookEventResourceRelationshipsWebhook();
      //expect(instance).to.be.a(UpApi.WebhookEventResourceRelationshipsWebhook);
    });

    it('should have the property data (base name: "data")', function() {
      // uncomment below and update the code to test the property data
      //var instance = new UpApi.WebhookEventResourceRelationshipsWebhook();
      //expect(instance).to.be();
    });

    it('should have the property links (base name: "links")', function() {
      // uncomment below and update the code to test the property links
      //var instance = new UpApi.WebhookEventResourceRelationshipsWebhook();
      //expect(instance).to.be();
    });

  });

}));
