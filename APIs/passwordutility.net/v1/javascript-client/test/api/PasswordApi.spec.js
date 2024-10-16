/**
 * PasswordUtility.Web
 * Validate and generate passwords using open source tools
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
    factory(root.expect, root.PasswordUtilityWeb);
  }
}(this, function(expect, PasswordUtilityWeb) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new PasswordUtilityWeb.PasswordApi();
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

  describe('PasswordApi', function() {
    describe('passwordGenerate', function() {
      it('should call passwordGenerate successfully', function(done) {
        //uncomment below and update the code to test passwordGenerate
        //instance.passwordGenerate(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('passwordValidate', function() {
      it('should call passwordValidate successfully', function(done) {
        //uncomment below and update the code to test passwordValidate
        //instance.passwordValidate(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
  });

}));
