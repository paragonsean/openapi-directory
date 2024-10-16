/**
 * agentOS API V3, Diary Call Group
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: v3-diary
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
    factory(root.expect, root.AgentOsApiV3DiaryCallGroup);
  }
}(this, function(expect, AgentOsApiV3DiaryCallGroup) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new AgentOsApiV3DiaryCallGroup.DiaryControllerApi();
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

  describe('DiaryControllerApi', function() {
    describe('diaryControllerAddFeedback', function() {
      it('should call diaryControllerAddFeedback successfully', function(done) {
        //uncomment below and update the code to test diaryControllerAddFeedback
        //instance.diaryControllerAddFeedback(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('diaryControllerCancelAppointment', function() {
      it('should call diaryControllerCancelAppointment successfully', function(done) {
        //uncomment below and update the code to test diaryControllerCancelAppointment
        //instance.diaryControllerCancelAppointment(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('diaryControllerDeleteAppointment', function() {
      it('should call diaryControllerDeleteAppointment successfully', function(done) {
        //uncomment below and update the code to test diaryControllerDeleteAppointment
        //instance.diaryControllerDeleteAppointment(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('diaryControllerGetAllocations', function() {
      it('should call diaryControllerGetAllocations successfully', function(done) {
        //uncomment below and update the code to test diaryControllerGetAllocations
        //instance.diaryControllerGetAllocations(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('diaryControllerGetAppointment', function() {
      it('should call diaryControllerGetAppointment successfully', function(done) {
        //uncomment below and update the code to test diaryControllerGetAppointment
        //instance.diaryControllerGetAppointment(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('diaryControllerGetAppointmentTypes', function() {
      it('should call diaryControllerGetAppointmentTypes successfully', function(done) {
        //uncomment below and update the code to test diaryControllerGetAppointmentTypes
        //instance.diaryControllerGetAppointmentTypes(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('diaryControllerGetAppointmentsBetweenDates', function() {
      it('should call diaryControllerGetAppointmentsBetweenDates successfully', function(done) {
        //uncomment below and update the code to test diaryControllerGetAppointmentsBetweenDates
        //instance.diaryControllerGetAppointmentsBetweenDates(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('diaryControllerGetRecurringAppointments', function() {
      it('should call diaryControllerGetRecurringAppointments successfully', function(done) {
        //uncomment below and update the code to test diaryControllerGetRecurringAppointments
        //instance.diaryControllerGetRecurringAppointments(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('diaryControllerPostAppointment', function() {
      it('should call diaryControllerPostAppointment successfully', function(done) {
        //uncomment below and update the code to test diaryControllerPostAppointment
        //instance.diaryControllerPostAppointment(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('diaryControllerPutAppointment', function() {
      it('should call diaryControllerPutAppointment successfully', function(done) {
        //uncomment below and update the code to test diaryControllerPutAppointment
        //instance.diaryControllerPutAppointment(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('diaryControllerSearchGuest', function() {
      it('should call diaryControllerSearchGuest successfully', function(done) {
        //uncomment below and update the code to test diaryControllerSearchGuest
        //instance.diaryControllerSearchGuest(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
  });

}));
