/**
 * Mailscript
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 0.4.0
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
    factory(root.expect, root.Mailscript);
  }
}(this, function(expect, Mailscript) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new Mailscript.GetAllVerificationsResponseListInner();
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

  describe('GetAllVerificationsResponseListInner', function() {
    it('should create an instance of GetAllVerificationsResponseListInner', function() {
      // uncomment below and update the code to test GetAllVerificationsResponseListInner
      //var instance = new Mailscript.GetAllVerificationsResponseListInner();
      //expect(instance).to.be.a(Mailscript.GetAllVerificationsResponseListInner);
    });

    it('should have the property email (base name: "email")', function() {
      // uncomment below and update the code to test the property email
      //var instance = new Mailscript.GetAllVerificationsResponseListInner();
      //expect(instance).to.be();
    });

    it('should have the property id (base name: "id")', function() {
      // uncomment below and update the code to test the property id
      //var instance = new Mailscript.GetAllVerificationsResponseListInner();
      //expect(instance).to.be();
    });

    it('should have the property type (base name: "type")', function() {
      // uncomment below and update the code to test the property type
      //var instance = new Mailscript.GetAllVerificationsResponseListInner();
      //expect(instance).to.be();
    });

    it('should have the property verified (base name: "verified")', function() {
      // uncomment below and update the code to test the property verified
      //var instance = new Mailscript.GetAllVerificationsResponseListInner();
      //expect(instance).to.be();
    });

    it('should have the property verifiedAt (base name: "verifiedAt")', function() {
      // uncomment below and update the code to test the property verifiedAt
      //var instance = new Mailscript.GetAllVerificationsResponseListInner();
      //expect(instance).to.be();
    });

    it('should have the property verifiedBy (base name: "verifiedBy")', function() {
      // uncomment below and update the code to test the property verifiedBy
      //var instance = new Mailscript.GetAllVerificationsResponseListInner();
      //expect(instance).to.be();
    });

    it('should have the property sms (base name: "sms")', function() {
      // uncomment below and update the code to test the property sms
      //var instance = new Mailscript.GetAllVerificationsResponseListInner();
      //expect(instance).to.be();
    });

  });

}));
