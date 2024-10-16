/**
 * Story
 * This API is the main entry point for creating, editing and publishing analytics throught the Presalytics API
 *
 * The version of the OpenAPI document: 0.3.1
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
    factory(root.expect, root.Story);
  }
}(this, function(expect, Story) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new Story.View();
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

  describe('View', function() {
    it('should create an instance of View', function() {
      // uncomment below and update the code to test View
      //var instance = new Story.View();
      //expect(instance).to.be.a(Story.View);
    });

    it('should have the property createdAt (base name: "created_at")', function() {
      // uncomment below and update the code to test the property createdAt
      //var instance = new Story.View();
      //expect(instance).to.be();
    });

    it('should have the property createdBy (base name: "created_by")', function() {
      // uncomment below and update the code to test the property createdBy
      //var instance = new Story.View();
      //expect(instance).to.be();
    });

    it('should have the property id (base name: "id")', function() {
      // uncomment below and update the code to test the property id
      //var instance = new Story.View();
      //expect(instance).to.be();
    });

    it('should have the property updatedAt (base name: "updated_at")', function() {
      // uncomment below and update the code to test the property updatedAt
      //var instance = new Story.View();
      //expect(instance).to.be();
    });

    it('should have the property updatedBy (base name: "updated_by")', function() {
      // uncomment below and update the code to test the property updatedBy
      //var instance = new Story.View();
      //expect(instance).to.be();
    });

    it('should have the property activeMsecs (base name: "active_msecs")', function() {
      // uncomment below and update the code to test the property activeMsecs
      //var instance = new Story.View();
      //expect(instance).to.be();
    });

    it('should have the property additional (base name: "additional")', function() {
      // uncomment below and update the code to test the property additional
      //var instance = new Story.View();
      //expect(instance).to.be();
    });

    it('should have the property endTime (base name: "end_time")', function() {
      // uncomment below and update the code to test the property endTime
      //var instance = new Story.View();
      //expect(instance).to.be();
    });

    it('should have the property pageNumber (base name: "page_number")', function() {
      // uncomment below and update the code to test the property pageNumber
      //var instance = new Story.View();
      //expect(instance).to.be();
    });

    it('should have the property sessionId (base name: "session_id")', function() {
      // uncomment below and update the code to test the property sessionId
      //var instance = new Story.View();
      //expect(instance).to.be();
    });

    it('should have the property startTime (base name: "start_time")', function() {
      // uncomment below and update the code to test the property startTime
      //var instance = new Story.View();
      //expect(instance).to.be();
    });

    it('should have the property totalMsecs (base name: "total_msecs")', function() {
      // uncomment below and update the code to test the property totalMsecs
      //var instance = new Story.View();
      //expect(instance).to.be();
    });

  });

}));
