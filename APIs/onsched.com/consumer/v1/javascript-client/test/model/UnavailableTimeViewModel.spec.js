/**
 * OnSched Consumer API
 * Build secure and scalable custom apps for Online Booking. Our flexible API provides many options for availability and booking.  <br><br>  Take the API for a test drive. Just click on the Authorize button below and authenticate.   You can access our demo company profile if you are not a customer, or your own profile by using your assigned ClientId and Secret.  <br><br>  The API has two interfaces, consumer and setup.   <ul>  <li>  The consumer interface provides all the endpoints required for implementing consumer booking flows.  </li>  <li>  The setup interface provides endpoints for profile configuration and setup.  </li>  </ul>  Toggle freely between the two interfaces using the swagger tool bar option labelled 'Select a definition'.  
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
    factory(root.expect, root.OnSchedConsumerApi);
  }
}(this, function(expect, OnSchedConsumerApi) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new OnSchedConsumerApi.UnavailableTimeViewModel();
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

  describe('UnavailableTimeViewModel', function() {
    it('should create an instance of UnavailableTimeViewModel', function() {
      // uncomment below and update the code to test UnavailableTimeViewModel
      //var instance = new OnSchedConsumerApi.UnavailableTimeViewModel();
      //expect(instance).to.be.a(OnSchedConsumerApi.UnavailableTimeViewModel);
    });

    it('should have the property calendarId (base name: "calendarId")', function() {
      // uncomment below and update the code to test the property calendarId
      //var instance = new OnSchedConsumerApi.UnavailableTimeViewModel();
      //expect(instance).to.be();
    });

    it('should have the property date (base name: "date")', function() {
      // uncomment below and update the code to test the property date
      //var instance = new OnSchedConsumerApi.UnavailableTimeViewModel();
      //expect(instance).to.be();
    });

    it('should have the property endDateTime (base name: "endDateTime")', function() {
      // uncomment below and update the code to test the property endDateTime
      //var instance = new OnSchedConsumerApi.UnavailableTimeViewModel();
      //expect(instance).to.be();
    });

    it('should have the property entityId (base name: "entityId")', function() {
      // uncomment below and update the code to test the property entityId
      //var instance = new OnSchedConsumerApi.UnavailableTimeViewModel();
      //expect(instance).to.be();
    });

    it('should have the property entityType (base name: "entityType")', function() {
      // uncomment below and update the code to test the property entityType
      //var instance = new OnSchedConsumerApi.UnavailableTimeViewModel();
      //expect(instance).to.be();
    });

    it('should have the property fromTime (base name: "fromTime")', function() {
      // uncomment below and update the code to test the property fromTime
      //var instance = new OnSchedConsumerApi.UnavailableTimeViewModel();
      //expect(instance).to.be();
    });

    it('should have the property locationId (base name: "locationId")', function() {
      // uncomment below and update the code to test the property locationId
      //var instance = new OnSchedConsumerApi.UnavailableTimeViewModel();
      //expect(instance).to.be();
    });

    it('should have the property objectName (base name: "objectName")', function() {
      // uncomment below and update the code to test the property objectName
      //var instance = new OnSchedConsumerApi.UnavailableTimeViewModel();
      //expect(instance).to.be();
    });

    it('should have the property reason (base name: "reason")', function() {
      // uncomment below and update the code to test the property reason
      //var instance = new OnSchedConsumerApi.UnavailableTimeViewModel();
      //expect(instance).to.be();
    });

    it('should have the property reasonCode (base name: "reasonCode")', function() {
      // uncomment below and update the code to test the property reasonCode
      //var instance = new OnSchedConsumerApi.UnavailableTimeViewModel();
      //expect(instance).to.be();
    });

    it('should have the property resourceId (base name: "resourceId")', function() {
      // uncomment below and update the code to test the property resourceId
      //var instance = new OnSchedConsumerApi.UnavailableTimeViewModel();
      //expect(instance).to.be();
    });

    it('should have the property resourceName (base name: "resourceName")', function() {
      // uncomment below and update the code to test the property resourceName
      //var instance = new OnSchedConsumerApi.UnavailableTimeViewModel();
      //expect(instance).to.be();
    });

    it('should have the property serviceId (base name: "serviceId")', function() {
      // uncomment below and update the code to test the property serviceId
      //var instance = new OnSchedConsumerApi.UnavailableTimeViewModel();
      //expect(instance).to.be();
    });

    it('should have the property serviceName (base name: "serviceName")', function() {
      // uncomment below and update the code to test the property serviceName
      //var instance = new OnSchedConsumerApi.UnavailableTimeViewModel();
      //expect(instance).to.be();
    });

    it('should have the property startDateTime (base name: "startDateTime")', function() {
      // uncomment below and update the code to test the property startDateTime
      //var instance = new OnSchedConsumerApi.UnavailableTimeViewModel();
      //expect(instance).to.be();
    });

    it('should have the property toTime (base name: "toTime")', function() {
      // uncomment below and update the code to test the property toTime
      //var instance = new OnSchedConsumerApi.UnavailableTimeViewModel();
      //expect(instance).to.be();
    });

    it('should have the property tzOffset (base name: "tzOffset")', function() {
      // uncomment below and update the code to test the property tzOffset
      //var instance = new OnSchedConsumerApi.UnavailableTimeViewModel();
      //expect(instance).to.be();
    });

  });

}));
