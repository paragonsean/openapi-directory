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
    instance = new OnSchedSetupApi.ContactUpdateModel();
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

  describe('ContactUpdateModel', function() {
    it('should create an instance of ContactUpdateModel', function() {
      // uncomment below and update the code to test ContactUpdateModel
      //var instance = new OnSchedSetupApi.ContactUpdateModel();
      //expect(instance).to.be.a(OnSchedSetupApi.ContactUpdateModel);
    });

    it('should have the property businessPhone (base name: "businessPhone")', function() {
      // uncomment below and update the code to test the property businessPhone
      //var instance = new OnSchedSetupApi.ContactUpdateModel();
      //expect(instance).to.be();
    });

    it('should have the property businessPhoneExt (base name: "businessPhoneExt")', function() {
      // uncomment below and update the code to test the property businessPhoneExt
      //var instance = new OnSchedSetupApi.ContactUpdateModel();
      //expect(instance).to.be();
    });

    it('should have the property conferenceInfo (base name: "conferenceInfo")', function() {
      // uncomment below and update the code to test the property conferenceInfo
      //var instance = new OnSchedSetupApi.ContactUpdateModel();
      //expect(instance).to.be();
    });

    it('should have the property homePhone (base name: "homePhone")', function() {
      // uncomment below and update the code to test the property homePhone
      //var instance = new OnSchedSetupApi.ContactUpdateModel();
      //expect(instance).to.be();
    });

    it('should have the property mobilePhone (base name: "mobilePhone")', function() {
      // uncomment below and update the code to test the property mobilePhone
      //var instance = new OnSchedSetupApi.ContactUpdateModel();
      //expect(instance).to.be();
    });

    it('should have the property preferredPhoneType (base name: "preferredPhoneType")', function() {
      // uncomment below and update the code to test the property preferredPhoneType
      //var instance = new OnSchedSetupApi.ContactUpdateModel();
      //expect(instance).to.be();
    });

    it('should have the property skypeUsername (base name: "skypeUsername")', function() {
      // uncomment below and update the code to test the property skypeUsername
      //var instance = new OnSchedSetupApi.ContactUpdateModel();
      //expect(instance).to.be();
    });

  });

}));
