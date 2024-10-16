/**
 * brainbi
 * Welcome to the official API of the brainbi platform. Using this API you can freely integrate our analytics platform with any other solution.  Please refer to the following documentation and in case of any issues, please contact us at service@brainbi.net.  Please note: for this API you will use your email and password from the brainbi.net platform to gather a Bearer Token for any API calls (use Login and get token). Once you are finished with your calls, please do a logout to remove your token and keep your account safe (use logout).
 *
 * The version of the OpenAPI document: 1.0.0
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
    factory(root.expect, root.Brainbi);
  }
}(this, function(expect, Brainbi) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new Brainbi.DefaultApi();
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

  describe('DefaultApi', function() {
    describe('loginAndGetBearerToken', function() {
      it('should call loginAndGetBearerToken successfully', function(done) {
        //uncomment below and update the code to test loginAndGetBearerToken
        //instance.loginAndGetBearerToken(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('logout', function() {
      it('should call logout successfully', function(done) {
        //uncomment below and update the code to test logout
        //instance.logout(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('register', function() {
      it('should call register successfully', function(done) {
        //uncomment below and update the code to test register
        //instance.register(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('registerAndCreateStoreConnectionForWooCommerce', function() {
      it('should call registerAndCreateStoreConnectionForWooCommerce successfully', function(done) {
        //uncomment below and update the code to test registerAndCreateStoreConnectionForWooCommerce
        //instance.registerAndCreateStoreConnectionForWooCommerce(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
  });

}));
