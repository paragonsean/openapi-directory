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
    instance = new ElevenLabsApiDocumentation.UserResponseModel();
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

  describe('UserResponseModel', function() {
    it('should create an instance of UserResponseModel', function() {
      // uncomment below and update the code to test UserResponseModel
      //var instance = new ElevenLabsApiDocumentation.UserResponseModel();
      //expect(instance).to.be.a(ElevenLabsApiDocumentation.UserResponseModel);
    });

    it('should have the property isNewUser (base name: "is_new_user")', function() {
      // uncomment below and update the code to test the property isNewUser
      //var instance = new ElevenLabsApiDocumentation.UserResponseModel();
      //expect(instance).to.be();
    });

    it('should have the property subscription (base name: "subscription")', function() {
      // uncomment below and update the code to test the property subscription
      //var instance = new ElevenLabsApiDocumentation.UserResponseModel();
      //expect(instance).to.be();
    });

    it('should have the property xiApiKey (base name: "xi_api_key")', function() {
      // uncomment below and update the code to test the property xiApiKey
      //var instance = new ElevenLabsApiDocumentation.UserResponseModel();
      //expect(instance).to.be();
    });

  });

}));
