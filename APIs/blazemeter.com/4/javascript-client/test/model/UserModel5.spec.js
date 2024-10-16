/**
 * Blazemeter API Explorer
 * Live API Documentation
 *
 * The version of the OpenAPI document: 4
 * Contact: support@blazemeter.com
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
    factory(root.expect, root.BlazemeterApiExplorer);
  }
}(this, function(expect, BlazemeterApiExplorer) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new BlazemeterApiExplorer.UserModel5();
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

  describe('UserModel5', function() {
    it('should create an instance of UserModel5', function() {
      // uncomment below and update the code to test UserModel5
      //var instance = new BlazemeterApiExplorer.UserModel5();
      //expect(instance).to.be.a(BlazemeterApiExplorer.UserModel5);
    });

    it('should have the property sessionIds (base name: "session_ids")', function() {
      // uncomment below and update the code to test the property sessionIds
      //var instance = new BlazemeterApiExplorer.UserModel5();
      //expect(instance).to.be();
    });

  });

}));
