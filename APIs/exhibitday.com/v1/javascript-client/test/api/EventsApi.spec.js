/**
 * Test the ExhibitDay API with Swagger
 * This API can be used to programmatically pull data out of ExhibitDay or push data into ExhibitDay -- allowing for automation between ExhibitDay and your internal systems (or other third-party software). To use the API, you'll need working knowledge of consuming REST APIs.<br /><br />Docs: https://api.exhibitday.com/swagger/docs/v1
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
    factory(root.expect, root.TestTheExhibitDayApiWithSwagger);
  }
}(this, function(expect, TestTheExhibitDayApiWithSwagger) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new TestTheExhibitDayApiWithSwagger.EventsApi();
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

  describe('EventsApi', function() {
    describe('events0Get', function() {
      it('should call events0Get successfully', function(done) {
        //uncomment below and update the code to test events0Get
        //instance.events0Get(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('events1Post', function() {
      it('should call events1Post successfully', function(done) {
        //uncomment below and update the code to test events1Post
        //instance.events1Post(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('events2Patch', function() {
      it('should call events2Patch successfully', function(done) {
        //uncomment below and update the code to test events2Patch
        //instance.events2Patch(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('events3Delete', function() {
      it('should call events3Delete successfully', function(done) {
        //uncomment below and update the code to test events3Delete
        //instance.events3Delete(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('eventsInfo0Get', function() {
      it('should call eventsInfo0Get successfully', function(done) {
        //uncomment below and update the code to test eventsInfo0Get
        //instance.eventsInfo0Get(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
  });

}));
