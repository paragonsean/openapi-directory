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
    instance = new UpApi.WebhookEventResourceRelationships();
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

  describe('WebhookEventResourceRelationships', function() {
    it('should create an instance of WebhookEventResourceRelationships', function() {
      // uncomment below and update the code to test WebhookEventResourceRelationships
      //var instance = new UpApi.WebhookEventResourceRelationships();
      //expect(instance).to.be.a(UpApi.WebhookEventResourceRelationships);
    });

    it('should have the property transaction (base name: "transaction")', function() {
      // uncomment below and update the code to test the property transaction
      //var instance = new UpApi.WebhookEventResourceRelationships();
      //expect(instance).to.be();
    });

    it('should have the property webhook (base name: "webhook")', function() {
      // uncomment below and update the code to test the property webhook
      //var instance = new UpApi.WebhookEventResourceRelationships();
      //expect(instance).to.be();
    });

  });

}));
