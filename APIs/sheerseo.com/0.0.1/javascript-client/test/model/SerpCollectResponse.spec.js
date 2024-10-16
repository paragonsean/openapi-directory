/**
 * SheerSEO API
 * Sheerseo API has 2 stages:<br>First stage - initiating the task: You fill in your task and receive in return the task id. <br>Second stage - collecting the results: send a request containing the task ids you got at the first stage and collecting the results.
 *
 * The version of the OpenAPI document: 0.0.1
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
    factory(root.expect, root.SheerSeoApi);
  }
}(this, function(expect, SheerSeoApi) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new SheerSeoApi.SerpCollectResponse();
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

  describe('SerpCollectResponse', function() {
    it('should create an instance of SerpCollectResponse', function() {
      // uncomment below and update the code to test SerpCollectResponse
      //var instance = new SheerSeoApi.SerpCollectResponse();
      //expect(instance).to.be.a(SheerSeoApi.SerpCollectResponse);
    });

    it('should have the property tasks (base name: "tasks")', function() {
      // uncomment below and update the code to test the property tasks
      //var instance = new SheerSeoApi.SerpCollectResponse();
      //expect(instance).to.be();
    });

  });

}));
