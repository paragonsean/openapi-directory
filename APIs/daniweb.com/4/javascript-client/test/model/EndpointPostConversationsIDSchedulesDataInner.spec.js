/**
 * DaniWeb Connect API
 * User Recommendation Engine and Chat Network
 *
 * The version of the OpenAPI document: 4
 * Contact: dani@daniwebmail.com
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
    factory(root.expect, root.DaniWebConnectApi);
  }
}(this, function(expect, DaniWebConnectApi) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new DaniWebConnectApi.EndpointPostConversationsIDSchedulesDataInner();
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

  describe('EndpointPostConversationsIDSchedulesDataInner', function() {
    it('should create an instance of EndpointPostConversationsIDSchedulesDataInner', function() {
      // uncomment below and update the code to test EndpointPostConversationsIDSchedulesDataInner
      //var instance = new DaniWebConnectApi.EndpointPostConversationsIDSchedulesDataInner();
      //expect(instance).to.be.a(DaniWebConnectApi.EndpointPostConversationsIDSchedulesDataInner);
    });

    it('should have the property authorCount (base name: "author_count")', function() {
      // uncomment below and update the code to test the property authorCount
      //var instance = new DaniWebConnectApi.EndpointPostConversationsIDSchedulesDataInner();
      //expect(instance).to.be();
    });

    it('should have the property conversationCount (base name: "conversation_count")', function() {
      // uncomment below and update the code to test the property conversationCount
      //var instance = new DaniWebConnectApi.EndpointPostConversationsIDSchedulesDataInner();
      //expect(instance).to.be();
    });

    it('should have the property conversationId (base name: "conversation_id")', function() {
      // uncomment below and update the code to test the property conversationId
      //var instance = new DaniWebConnectApi.EndpointPostConversationsIDSchedulesDataInner();
      //expect(instance).to.be();
    });

    it('should have the property date (base name: "date")', function() {
      // uncomment below and update the code to test the property date
      //var instance = new DaniWebConnectApi.EndpointPostConversationsIDSchedulesDataInner();
      //expect(instance).to.be();
    });

    it('should have the property firstMessage (base name: "first_message")', function() {
      // uncomment below and update the code to test the property firstMessage
      //var instance = new DaniWebConnectApi.EndpointPostConversationsIDSchedulesDataInner();
      //expect(instance).to.be();
    });

    it('should have the property lastMessage (base name: "last_message")', function() {
      // uncomment below and update the code to test the property lastMessage
      //var instance = new DaniWebConnectApi.EndpointPostConversationsIDSchedulesDataInner();
      //expect(instance).to.be();
    });

    it('should have the property messageCount (base name: "message_count")', function() {
      // uncomment below and update the code to test the property messageCount
      //var instance = new DaniWebConnectApi.EndpointPostConversationsIDSchedulesDataInner();
      //expect(instance).to.be();
    });

    it('should have the property myMessageCount (base name: "my_message_count")', function() {
      // uncomment below and update the code to test the property myMessageCount
      //var instance = new DaniWebConnectApi.EndpointPostConversationsIDSchedulesDataInner();
      //expect(instance).to.be();
    });

    it('should have the property navigation (base name: "navigation")', function() {
      // uncomment below and update the code to test the property navigation
      //var instance = new DaniWebConnectApi.EndpointPostConversationsIDSchedulesDataInner();
      //expect(instance).to.be();
    });

  });

}));
