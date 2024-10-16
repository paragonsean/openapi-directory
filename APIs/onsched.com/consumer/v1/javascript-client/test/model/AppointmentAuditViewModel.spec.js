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
    instance = new OnSchedConsumerApi.AppointmentAuditViewModel();
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

  describe('AppointmentAuditViewModel', function() {
    it('should create an instance of AppointmentAuditViewModel', function() {
      // uncomment below and update the code to test AppointmentAuditViewModel
      //var instance = new OnSchedConsumerApi.AppointmentAuditViewModel();
      //expect(instance).to.be.a(OnSchedConsumerApi.AppointmentAuditViewModel);
    });

    it('should have the property appointmentId (base name: "appointmentId")', function() {
      // uncomment below and update the code to test the property appointmentId
      //var instance = new OnSchedConsumerApi.AppointmentAuditViewModel();
      //expect(instance).to.be();
    });

    it('should have the property id (base name: "id")', function() {
      // uncomment below and update the code to test the property id
      //var instance = new OnSchedConsumerApi.AppointmentAuditViewModel();
      //expect(instance).to.be();
    });

    it('should have the property modificationType (base name: "modificationType")', function() {
      // uncomment below and update the code to test the property modificationType
      //var instance = new OnSchedConsumerApi.AppointmentAuditViewModel();
      //expect(instance).to.be();
    });

    it('should have the property modifiedBy (base name: "modifiedBy")', function() {
      // uncomment below and update the code to test the property modifiedBy
      //var instance = new OnSchedConsumerApi.AppointmentAuditViewModel();
      //expect(instance).to.be();
    });

    it('should have the property modifiedOn (base name: "modifiedOn")', function() {
      // uncomment below and update the code to test the property modifiedOn
      //var instance = new OnSchedConsumerApi.AppointmentAuditViewModel();
      //expect(instance).to.be();
    });

    it('should have the property notesAfter (base name: "notesAfter")', function() {
      // uncomment below and update the code to test the property notesAfter
      //var instance = new OnSchedConsumerApi.AppointmentAuditViewModel();
      //expect(instance).to.be();
    });

    it('should have the property notesBefore (base name: "notesBefore")', function() {
      // uncomment below and update the code to test the property notesBefore
      //var instance = new OnSchedConsumerApi.AppointmentAuditViewModel();
      //expect(instance).to.be();
    });

    it('should have the property statusAfter (base name: "statusAfter")', function() {
      // uncomment below and update the code to test the property statusAfter
      //var instance = new OnSchedConsumerApi.AppointmentAuditViewModel();
      //expect(instance).to.be();
    });

    it('should have the property statusBefore (base name: "statusBefore")', function() {
      // uncomment below and update the code to test the property statusBefore
      //var instance = new OnSchedConsumerApi.AppointmentAuditViewModel();
      //expect(instance).to.be();
    });

  });

}));
