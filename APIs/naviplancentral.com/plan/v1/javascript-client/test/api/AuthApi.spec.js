/**
 * NaviPlan API
 * An API for accessing NaviPlan plan data for a client.
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
    factory(root.expect, root.NaviPlanApi);
  }
}(this, function(expect, NaviPlanApi) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new NaviPlanApi.AuthApi();
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

  describe('AuthApi', function() {
    describe('authLoginByModel', function() {
      it('should call authLoginByModel successfully', function(done) {
        //uncomment below and update the code to test authLoginByModel
        //instance.authLoginByModel(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('authLogout', function() {
      it('should call authLogout successfully', function(done) {
        //uncomment below and update the code to test authLogout
        //instance.authLogout(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('authPasswordRequirements', function() {
      it('should call authPasswordRequirements successfully', function(done) {
        //uncomment below and update the code to test authPasswordRequirements
        //instance.authPasswordRequirements(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('authResumeSession', function() {
      it('should call authResumeSession successfully', function(done) {
        //uncomment below and update the code to test authResumeSession
        //instance.authResumeSession(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
  });

}));
