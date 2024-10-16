/**
 * OnSched Setup API
 * Build secure and scalable custom apps for onboarding and setup. Our flexible API provides many options for configuration.  <br><br>  Take the API for a test drive. Just click on the Authorize button below and authenticate.   You can access our demo company profile if you are not a customer, or your own profile by using your assigned ClientId and Secret.  <br><br>  The API has two interfaces, consumer and setup.   <ul>  <li>  The consumer interface provides all the endpoints required for implementing consumer booking flows.  </li>  <li>  The setup interface provides endpoints for profile configuration and setup.  </li>  </ul>  Toggle freely between the two interfaces using the swagger tool bar option labelled 'Select a definition'.  
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
    factory(root.expect, root.OnSchedSetupApi);
  }
}(this, function(expect, OnSchedSetupApi) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new OnSchedSetupApi.TravelViewModel();
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

  describe('TravelViewModel', function() {
    it('should create an instance of TravelViewModel', function() {
      // uncomment below and update the code to test TravelViewModel
      //var instance = new OnSchedSetupApi.TravelViewModel();
      //expect(instance).to.be.a(OnSchedSetupApi.TravelViewModel);
    });

    it('should have the property distance (base name: "distance")', function() {
      // uncomment below and update the code to test the property distance
      //var instance = new OnSchedSetupApi.TravelViewModel();
      //expect(instance).to.be();
    });

    it('should have the property proximity (base name: "proximity")', function() {
      // uncomment below and update the code to test the property proximity
      //var instance = new OnSchedSetupApi.TravelViewModel();
      //expect(instance).to.be();
    });

    it('should have the property startAddress (base name: "startAddress")', function() {
      // uncomment below and update the code to test the property startAddress
      //var instance = new OnSchedSetupApi.TravelViewModel();
      //expect(instance).to.be();
    });

    it('should have the property startLat (base name: "startLat")', function() {
      // uncomment below and update the code to test the property startLat
      //var instance = new OnSchedSetupApi.TravelViewModel();
      //expect(instance).to.be();
    });

    it('should have the property startLon (base name: "startLon")', function() {
      // uncomment below and update the code to test the property startLon
      //var instance = new OnSchedSetupApi.TravelViewModel();
      //expect(instance).to.be();
    });

    it('should have the property units (base name: "units")', function() {
      // uncomment below and update the code to test the property units
      //var instance = new OnSchedSetupApi.TravelViewModel();
      //expect(instance).to.be();
    });

  });

}));
