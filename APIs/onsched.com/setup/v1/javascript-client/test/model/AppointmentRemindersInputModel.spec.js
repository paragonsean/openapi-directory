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
    instance = new OnSchedSetupApi.AppointmentRemindersInputModel();
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

  describe('AppointmentRemindersInputModel', function() {
    it('should create an instance of AppointmentRemindersInputModel', function() {
      // uncomment below and update the code to test AppointmentRemindersInputModel
      //var instance = new OnSchedSetupApi.AppointmentRemindersInputModel();
      //expect(instance).to.be.a(OnSchedSetupApi.AppointmentRemindersInputModel);
    });

    it('should have the property emailFirstReminder (base name: "emailFirstReminder")', function() {
      // uncomment below and update the code to test the property emailFirstReminder
      //var instance = new OnSchedSetupApi.AppointmentRemindersInputModel();
      //expect(instance).to.be();
    });

    it('should have the property emailFirstReminderInterval (base name: "emailFirstReminderInterval")', function() {
      // uncomment below and update the code to test the property emailFirstReminderInterval
      //var instance = new OnSchedSetupApi.AppointmentRemindersInputModel();
      //expect(instance).to.be();
    });

    it('should have the property emailSecondReminder (base name: "emailSecondReminder")', function() {
      // uncomment below and update the code to test the property emailSecondReminder
      //var instance = new OnSchedSetupApi.AppointmentRemindersInputModel();
      //expect(instance).to.be();
    });

    it('should have the property emailSecondReminderInterval (base name: "emailSecondReminderInterval")', function() {
      // uncomment below and update the code to test the property emailSecondReminderInterval
      //var instance = new OnSchedSetupApi.AppointmentRemindersInputModel();
      //expect(instance).to.be();
    });

    it('should have the property smsFirstReminder (base name: "smsFirstReminder")', function() {
      // uncomment below and update the code to test the property smsFirstReminder
      //var instance = new OnSchedSetupApi.AppointmentRemindersInputModel();
      //expect(instance).to.be();
    });

    it('should have the property smsFirstReminderInterval (base name: "smsFirstReminderInterval")', function() {
      // uncomment below and update the code to test the property smsFirstReminderInterval
      //var instance = new OnSchedSetupApi.AppointmentRemindersInputModel();
      //expect(instance).to.be();
    });

    it('should have the property smsSecondReminder (base name: "smsSecondReminder")', function() {
      // uncomment below and update the code to test the property smsSecondReminder
      //var instance = new OnSchedSetupApi.AppointmentRemindersInputModel();
      //expect(instance).to.be();
    });

    it('should have the property smsSecondReminderInterval (base name: "smsSecondReminderInterval")', function() {
      // uncomment below and update the code to test the property smsSecondReminderInterval
      //var instance = new OnSchedSetupApi.AppointmentRemindersInputModel();
      //expect(instance).to.be();
    });

  });

}));
