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
    instance = new InteractiveDocumentationForYourPremiumPlan.AirQualityPointHourlyData();
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

  describe('AirQualityPointHourlyData', function() {
    it('should create an instance of AirQualityPointHourlyData', function() {
      // uncomment below and update the code to test AirQualityPointHourlyData
      //var instance = new InteractiveDocumentationForYourPremiumPlan.AirQualityPointHourlyData();
      //expect(instance).to.be.a(InteractiveDocumentationForYourPremiumPlan.AirQualityPointHourlyData);
    });

    it('should have the property aerosol550 (base name: "aerosol_550")', function() {
      // uncomment below and update the code to test the property aerosol550
      //var instance = new InteractiveDocumentationForYourPremiumPlan.AirQualityPointHourlyData();
      //expect(instance).to.be();
    });

    it('should have the property airQuality (base name: "air_quality")', function() {
      // uncomment below and update the code to test the property airQuality
      //var instance = new InteractiveDocumentationForYourPremiumPlan.AirQualityPointHourlyData();
      //expect(instance).to.be();
    });

    it('should have the property coSurface (base name: "co_surface")', function() {
      // uncomment below and update the code to test the property coSurface
      //var instance = new InteractiveDocumentationForYourPremiumPlan.AirQualityPointHourlyData();
      //expect(instance).to.be();
    });

    it('should have the property date (base name: "date")', function() {
      // uncomment below and update the code to test the property date
      //var instance = new InteractiveDocumentationForYourPremiumPlan.AirQualityPointHourlyData();
      //expect(instance).to.be();
    });

    it('should have the property dust550nm (base name: "dust_550nm")', function() {
      // uncomment below and update the code to test the property dust550nm
      //var instance = new InteractiveDocumentationForYourPremiumPlan.AirQualityPointHourlyData();
      //expect(instance).to.be();
    });

    it('should have the property dustMixingRatio05 (base name: "dust_mixing_ratio_05")', function() {
      // uncomment below and update the code to test the property dustMixingRatio05
      //var instance = new InteractiveDocumentationForYourPremiumPlan.AirQualityPointHourlyData();
      //expect(instance).to.be();
    });

    it('should have the property no2Surface (base name: "no2_surface")', function() {
      // uncomment below and update the code to test the property no2Surface
      //var instance = new InteractiveDocumentationForYourPremiumPlan.AirQualityPointHourlyData();
      //expect(instance).to.be();
    });

    it('should have the property noSurface (base name: "no_surface")', function() {
      // uncomment below and update the code to test the property noSurface
      //var instance = new InteractiveDocumentationForYourPremiumPlan.AirQualityPointHourlyData();
      //expect(instance).to.be();
    });

    it('should have the property ozoneSurface (base name: "ozone_surface")', function() {
      // uncomment below and update the code to test the property ozoneSurface
      //var instance = new InteractiveDocumentationForYourPremiumPlan.AirQualityPointHourlyData();
      //expect(instance).to.be();
    });

    it('should have the property ozoneTotal (base name: "ozone_total")', function() {
      // uncomment below and update the code to test the property ozoneTotal
      //var instance = new InteractiveDocumentationForYourPremiumPlan.AirQualityPointHourlyData();
      //expect(instance).to.be();
    });

    it('should have the property pm10 (base name: "pm10")', function() {
      // uncomment below and update the code to test the property pm10
      //var instance = new InteractiveDocumentationForYourPremiumPlan.AirQualityPointHourlyData();
      //expect(instance).to.be();
    });

    it('should have the property pm25 (base name: "pm25")', function() {
      // uncomment below and update the code to test the property pm25
      //var instance = new InteractiveDocumentationForYourPremiumPlan.AirQualityPointHourlyData();
      //expect(instance).to.be();
    });

    it('should have the property so2Surface (base name: "so2_surface")', function() {
      // uncomment below and update the code to test the property so2Surface
      //var instance = new InteractiveDocumentationForYourPremiumPlan.AirQualityPointHourlyData();
      //expect(instance).to.be();
    });

  });

}));
