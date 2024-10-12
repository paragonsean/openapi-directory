/**
 * KeyServ
 * KeyServ API
 *
 * The version of the OpenAPI document: 1.4.5
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
    factory(root.expect, root.KeyServ);
  }
}(this, function(expect, KeyServ) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new KeyServ.SubscriptionCreateModify();
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

  describe('SubscriptionCreateModify', function() {
    it('should create an instance of SubscriptionCreateModify', function() {
      // uncomment below and update the code to test SubscriptionCreateModify
      //var instance = new KeyServ.SubscriptionCreateModify();
      //expect(instance).to.be.a(KeyServ.SubscriptionCreateModify);
    });

    it('should have the property action (base name: "action")', function() {
      // uncomment below and update the code to test the property action
      //var instance = new KeyServ.SubscriptionCreateModify();
      //expect(instance).to.be();
    });

    it('should have the property callbackOnModify (base name: "callbackOnModify")', function() {
      // uncomment below and update the code to test the property callbackOnModify
      //var instance = new KeyServ.SubscriptionCreateModify();
      //expect(instance).to.be();
    });

    it('should have the property callbackUrl (base name: "callbackUrl")', function() {
      // uncomment below and update the code to test the property callbackUrl
      //var instance = new KeyServ.SubscriptionCreateModify();
      //expect(instance).to.be();
    });

    it('should have the property custom (base name: "custom")', function() {
      // uncomment below and update the code to test the property custom
      //var instance = new KeyServ.SubscriptionCreateModify();
      //expect(instance).to.be();
    });

    it('should have the property frequency (base name: "frequency")', function() {
      // uncomment below and update the code to test the property frequency
      //var instance = new KeyServ.SubscriptionCreateModify();
      //expect(instance).to.be();
    });

    it('should have the property key (base name: "key")', function() {
      // uncomment below and update the code to test the property key
      //var instance = new KeyServ.SubscriptionCreateModify();
      //expect(instance).to.be();
    });

    it('should have the property name (base name: "name")', function() {
      // uncomment below and update the code to test the property name
      //var instance = new KeyServ.SubscriptionCreateModify();
      //expect(instance).to.be();
    });

    it('should have the property serial (base name: "serial")', function() {
      // uncomment below and update the code to test the property serial
      //var instance = new KeyServ.SubscriptionCreateModify();
      //expect(instance).to.be();
    });

    it('should have the property startFrom (base name: "startFrom")', function() {
      // uncomment below and update the code to test the property startFrom
      //var instance = new KeyServ.SubscriptionCreateModify();
      //expect(instance).to.be();
    });

  });

}));
