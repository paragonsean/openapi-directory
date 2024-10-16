/**
 * ElevenLabs API Documentation
 * This is the documentation for the ElevenLabs API. You can use this API to use our service programmatically, this is done by using your xi-api-key. <br/> You can view your xi-api-key using the 'Profile' tab on https://beta.elevenlabs.io. Our API is experimental so all endpoints are subject to change.
 *
 * The version of the OpenAPI document: 1.0
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
    factory(root.expect, root.ElevenLabsApiDocumentation);
  }
}(this, function(expect, ElevenLabsApiDocumentation) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new ElevenLabsApiDocumentation.UserApi();
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

  describe('UserApi', function() {
    describe('getUserInfoV1UserGet', function() {
      it('should call getUserInfoV1UserGet successfully', function(done) {
        //uncomment below and update the code to test getUserInfoV1UserGet
        //instance.getUserInfoV1UserGet(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('getUserSubscriptionInfoV1UserSubscriptionGet', function() {
      it('should call getUserSubscriptionInfoV1UserSubscriptionGet successfully', function(done) {
        //uncomment below and update the code to test getUserSubscriptionInfoV1UserSubscriptionGet
        //instance.getUserSubscriptionInfoV1UserSubscriptionGet(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
  });

}));
