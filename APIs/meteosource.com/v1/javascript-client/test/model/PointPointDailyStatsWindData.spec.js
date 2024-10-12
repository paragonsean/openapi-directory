/**
 * Interactive documentation for your Premium plan
 *   This interactive documentation is using your API key which is filled in automatically, you can find and change this in [your dashboard](https://www.meteosource.com/client).  Using the `GET` button, open your selected endpoint and read the introduction. You will find a detailed description of available parameters. You can complete the `Parameters` section and hit `Execute` to view a full API response. You can then inspect the JSON response, copy the `curl` command to run it on your machine, or obtain a URL of the request. In this way, you can easily build request command for the data you need. 
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
    factory(root.expect, root.InteractiveDocumentationForYourPremiumPlan);
  }
}(this, function(expect, InteractiveDocumentationForYourPremiumPlan) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new InteractiveDocumentationForYourPremiumPlan.PointPointDailyStatsWindData();
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

  describe('PointPointDailyStatsWindData', function() {
    it('should create an instance of PointPointDailyStatsWindData', function() {
      // uncomment below and update the code to test PointPointDailyStatsWindData
      //var instance = new InteractiveDocumentationForYourPremiumPlan.PointPointDailyStatsWindData();
      //expect(instance).to.be.a(InteractiveDocumentationForYourPremiumPlan.PointPointDailyStatsWindData);
    });

    it('should have the property avgAngle (base name: "avg_angle")', function() {
      // uncomment below and update the code to test the property avgAngle
      //var instance = new InteractiveDocumentationForYourPremiumPlan.PointPointDailyStatsWindData();
      //expect(instance).to.be();
    });

    it('should have the property avgDir (base name: "avg_dir")', function() {
      // uncomment below and update the code to test the property avgDir
      //var instance = new InteractiveDocumentationForYourPremiumPlan.PointPointDailyStatsWindData();
      //expect(instance).to.be();
    });

    it('should have the property avgSpeed (base name: "avg_speed")', function() {
      // uncomment below and update the code to test the property avgSpeed
      //var instance = new InteractiveDocumentationForYourPremiumPlan.PointPointDailyStatsWindData();
      //expect(instance).to.be();
    });

    it('should have the property maxGust (base name: "max_gust")', function() {
      // uncomment below and update the code to test the property maxGust
      //var instance = new InteractiveDocumentationForYourPremiumPlan.PointPointDailyStatsWindData();
      //expect(instance).to.be();
    });

    it('should have the property maxSpeed (base name: "max_speed")', function() {
      // uncomment below and update the code to test the property maxSpeed
      //var instance = new InteractiveDocumentationForYourPremiumPlan.PointPointDailyStatsWindData();
      //expect(instance).to.be();
    });

  });

}));
