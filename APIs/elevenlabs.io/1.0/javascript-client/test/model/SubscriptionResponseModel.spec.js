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
    instance = new ElevenLabsApiDocumentation.SubscriptionResponseModel();
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

  describe('SubscriptionResponseModel', function() {
    it('should create an instance of SubscriptionResponseModel', function() {
      // uncomment below and update the code to test SubscriptionResponseModel
      //var instance = new ElevenLabsApiDocumentation.SubscriptionResponseModel();
      //expect(instance).to.be.a(ElevenLabsApiDocumentation.SubscriptionResponseModel);
    });

    it('should have the property allowedToExtendCharacterLimit (base name: "allowed_to_extend_character_limit")', function() {
      // uncomment below and update the code to test the property allowedToExtendCharacterLimit
      //var instance = new ElevenLabsApiDocumentation.SubscriptionResponseModel();
      //expect(instance).to.be();
    });

    it('should have the property availableModels (base name: "available_models")', function() {
      // uncomment below and update the code to test the property availableModels
      //var instance = new ElevenLabsApiDocumentation.SubscriptionResponseModel();
      //expect(instance).to.be();
    });

    it('should have the property canExtendCharacterLimit (base name: "can_extend_character_limit")', function() {
      // uncomment below and update the code to test the property canExtendCharacterLimit
      //var instance = new ElevenLabsApiDocumentation.SubscriptionResponseModel();
      //expect(instance).to.be();
    });

    it('should have the property canExtendVoiceLimit (base name: "can_extend_voice_limit")', function() {
      // uncomment below and update the code to test the property canExtendVoiceLimit
      //var instance = new ElevenLabsApiDocumentation.SubscriptionResponseModel();
      //expect(instance).to.be();
    });

    it('should have the property canUseDelayedPaymentMethods (base name: "can_use_delayed_payment_methods")', function() {
      // uncomment below and update the code to test the property canUseDelayedPaymentMethods
      //var instance = new ElevenLabsApiDocumentation.SubscriptionResponseModel();
      //expect(instance).to.be();
    });

    it('should have the property canUseInstantVoiceCloning (base name: "can_use_instant_voice_cloning")', function() {
      // uncomment below and update the code to test the property canUseInstantVoiceCloning
      //var instance = new ElevenLabsApiDocumentation.SubscriptionResponseModel();
      //expect(instance).to.be();
    });

    it('should have the property canUseProfessionalVoiceCloning (base name: "can_use_professional_voice_cloning")', function() {
      // uncomment below and update the code to test the property canUseProfessionalVoiceCloning
      //var instance = new ElevenLabsApiDocumentation.SubscriptionResponseModel();
      //expect(instance).to.be();
    });

    it('should have the property characterCount (base name: "character_count")', function() {
      // uncomment below and update the code to test the property characterCount
      //var instance = new ElevenLabsApiDocumentation.SubscriptionResponseModel();
      //expect(instance).to.be();
    });

    it('should have the property characterLimit (base name: "character_limit")', function() {
      // uncomment below and update the code to test the property characterLimit
      //var instance = new ElevenLabsApiDocumentation.SubscriptionResponseModel();
      //expect(instance).to.be();
    });

    it('should have the property currency (base name: "currency")', function() {
      // uncomment below and update the code to test the property currency
      //var instance = new ElevenLabsApiDocumentation.SubscriptionResponseModel();
      //expect(instance).to.be();
    });

    it('should have the property nextCharacterCountResetUnix (base name: "next_character_count_reset_unix")', function() {
      // uncomment below and update the code to test the property nextCharacterCountResetUnix
      //var instance = new ElevenLabsApiDocumentation.SubscriptionResponseModel();
      //expect(instance).to.be();
    });

    it('should have the property professionalVoiceLimit (base name: "professional_voice_limit")', function() {
      // uncomment below and update the code to test the property professionalVoiceLimit
      //var instance = new ElevenLabsApiDocumentation.SubscriptionResponseModel();
      //expect(instance).to.be();
    });

    it('should have the property status (base name: "status")', function() {
      // uncomment below and update the code to test the property status
      //var instance = new ElevenLabsApiDocumentation.SubscriptionResponseModel();
      //expect(instance).to.be();
    });

    it('should have the property tier (base name: "tier")', function() {
      // uncomment below and update the code to test the property tier
      //var instance = new ElevenLabsApiDocumentation.SubscriptionResponseModel();
      //expect(instance).to.be();
    });

    it('should have the property voiceLimit (base name: "voice_limit")', function() {
      // uncomment below and update the code to test the property voiceLimit
      //var instance = new ElevenLabsApiDocumentation.SubscriptionResponseModel();
      //expect(instance).to.be();
    });

  });

}));
