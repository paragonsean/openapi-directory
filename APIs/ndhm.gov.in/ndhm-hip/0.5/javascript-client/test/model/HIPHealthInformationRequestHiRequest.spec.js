/**
 * Health Repository Provider Specifications for HIP
 * The following are the specifications for the APIs to be implemented at the Health Repository end if an entity is only serving the role of a HIP. The specs are essentially duplicates from the Gateway and Health Repository, but put together so as to make it clear to *HIPs* which set of APIs they should implement to participate in the network.  
 *
 * The version of the OpenAPI document: 0.5
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
    factory(root.expect, root.HealthRepositoryProviderSpecificationsForHip);
  }
}(this, function(expect, HealthRepositoryProviderSpecificationsForHip) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new HealthRepositoryProviderSpecificationsForHip.HIPHealthInformationRequestHiRequest();
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

  describe('HIPHealthInformationRequestHiRequest', function() {
    it('should create an instance of HIPHealthInformationRequestHiRequest', function() {
      // uncomment below and update the code to test HIPHealthInformationRequestHiRequest
      //var instance = new HealthRepositoryProviderSpecificationsForHip.HIPHealthInformationRequestHiRequest();
      //expect(instance).to.be.a(HealthRepositoryProviderSpecificationsForHip.HIPHealthInformationRequestHiRequest);
    });

    it('should have the property consent (base name: "consent")', function() {
      // uncomment below and update the code to test the property consent
      //var instance = new HealthRepositoryProviderSpecificationsForHip.HIPHealthInformationRequestHiRequest();
      //expect(instance).to.be();
    });

    it('should have the property dataPushUrl (base name: "dataPushUrl")', function() {
      // uncomment below and update the code to test the property dataPushUrl
      //var instance = new HealthRepositoryProviderSpecificationsForHip.HIPHealthInformationRequestHiRequest();
      //expect(instance).to.be();
    });

    it('should have the property dateRange (base name: "dateRange")', function() {
      // uncomment below and update the code to test the property dateRange
      //var instance = new HealthRepositoryProviderSpecificationsForHip.HIPHealthInformationRequestHiRequest();
      //expect(instance).to.be();
    });

    it('should have the property keyMaterial (base name: "keyMaterial")', function() {
      // uncomment below and update the code to test the property keyMaterial
      //var instance = new HealthRepositoryProviderSpecificationsForHip.HIPHealthInformationRequestHiRequest();
      //expect(instance).to.be();
    });

  });

}));
