/**
 * vRealize Network Insight API Reference
 * vRealize Network Insight API Reference
 *
 * The version of the OpenAPI document: 1.0.0
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
    factory(root.expect, root.VRealizeNetworkInsightApiReference);
  }
}(this, function(expect, VRealizeNetworkInsightApiReference) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new VRealizeNetworkInsightApiReference.Flow();
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

  describe('Flow', function() {
    it('should create an instance of Flow', function() {
      // uncomment below and update the code to test Flow
      //var instance = new VRealizeNetworkInsightApiReference.Flow();
      //expect(instance).to.be.a(VRealizeNetworkInsightApiReference.Flow);
    });

    it('should have the property destinationCluster (base name: "destination_cluster")', function() {
      // uncomment below and update the code to test the property destinationCluster
      //var instance = new VRealizeNetworkInsightApiReference.Flow();
      //expect(instance).to.be();
    });

    it('should have the property destinationDatacenter (base name: "destination_datacenter")', function() {
      // uncomment below and update the code to test the property destinationDatacenter
      //var instance = new VRealizeNetworkInsightApiReference.Flow();
      //expect(instance).to.be();
    });

    it('should have the property destinationFolders (base name: "destination_folders")', function() {
      // uncomment below and update the code to test the property destinationFolders
      //var instance = new VRealizeNetworkInsightApiReference.Flow();
      //expect(instance).to.be();
    });

    it('should have the property destinationHost (base name: "destination_host")', function() {
      // uncomment below and update the code to test the property destinationHost
      //var instance = new VRealizeNetworkInsightApiReference.Flow();
      //expect(instance).to.be();
    });

    it('should have the property destinationIp (base name: "destination_ip")', function() {
      // uncomment below and update the code to test the property destinationIp
      //var instance = new VRealizeNetworkInsightApiReference.Flow();
      //expect(instance).to.be();
    });

    it('should have the property destinationIpSets (base name: "destination_ip_sets")', function() {
      // uncomment below and update the code to test the property destinationIpSets
      //var instance = new VRealizeNetworkInsightApiReference.Flow();
      //expect(instance).to.be();
    });

    it('should have the property destinationL2Network (base name: "destination_l2_network")', function() {
      // uncomment below and update the code to test the property destinationL2Network
      //var instance = new VRealizeNetworkInsightApiReference.Flow();
      //expect(instance).to.be();
    });

    it('should have the property destinationResourcePool (base name: "destination_resource_pool")', function() {
      // uncomment below and update the code to test the property destinationResourcePool
      //var instance = new VRealizeNetworkInsightApiReference.Flow();
      //expect(instance).to.be();
    });

    it('should have the property destinationSecurityGroups (base name: "destination_security_groups")', function() {
      // uncomment below and update the code to test the property destinationSecurityGroups
      //var instance = new VRealizeNetworkInsightApiReference.Flow();
      //expect(instance).to.be();
    });

    it('should have the property destinationSecurityTags (base name: "destination_security_tags")', function() {
      // uncomment below and update the code to test the property destinationSecurityTags
      //var instance = new VRealizeNetworkInsightApiReference.Flow();
      //expect(instance).to.be();
    });

    it('should have the property destinationVm (base name: "destination_vm")', function() {
      // uncomment below and update the code to test the property destinationVm
      //var instance = new VRealizeNetworkInsightApiReference.Flow();
      //expect(instance).to.be();
    });

    it('should have the property destinationVmTags (base name: "destination_vm_tags")', function() {
      // uncomment below and update the code to test the property destinationVmTags
      //var instance = new VRealizeNetworkInsightApiReference.Flow();
      //expect(instance).to.be();
    });

    it('should have the property destinationVnic (base name: "destination_vnic")', function() {
      // uncomment below and update the code to test the property destinationVnic
      //var instance = new VRealizeNetworkInsightApiReference.Flow();
      //expect(instance).to.be();
    });

    it('should have the property destinationVpc (base name: "destination_vpc")', function() {
      // uncomment below and update the code to test the property destinationVpc
      //var instance = new VRealizeNetworkInsightApiReference.Flow();
      //expect(instance).to.be();
    });

    it('should have the property firewallAction (base name: "firewall_action")', function() {
      // uncomment below and update the code to test the property firewallAction
      //var instance = new VRealizeNetworkInsightApiReference.Flow();
      //expect(instance).to.be();
    });

    it('should have the property flowTag (base name: "flow_tag")', function() {
      // uncomment below and update the code to test the property flowTag
      //var instance = new VRealizeNetworkInsightApiReference.Flow();
      //expect(instance).to.be();
    });

    it('should have the property port (base name: "port")', function() {
      // uncomment below and update the code to test the property port
      //var instance = new VRealizeNetworkInsightApiReference.Flow();
      //expect(instance).to.be();
    });

    it('should have the property protocol (base name: "protocol")', function() {
      // uncomment below and update the code to test the property protocol
      //var instance = new VRealizeNetworkInsightApiReference.Flow();
      //expect(instance).to.be();
    });

    it('should have the property sourceCluster (base name: "source_cluster")', function() {
      // uncomment below and update the code to test the property sourceCluster
      //var instance = new VRealizeNetworkInsightApiReference.Flow();
      //expect(instance).to.be();
    });

    it('should have the property sourceDatacenter (base name: "source_datacenter")', function() {
      // uncomment below and update the code to test the property sourceDatacenter
      //var instance = new VRealizeNetworkInsightApiReference.Flow();
      //expect(instance).to.be();
    });

    it('should have the property sourceFolders (base name: "source_folders")', function() {
      // uncomment below and update the code to test the property sourceFolders
      //var instance = new VRealizeNetworkInsightApiReference.Flow();
      //expect(instance).to.be();
    });

    it('should have the property sourceHost (base name: "source_host")', function() {
      // uncomment below and update the code to test the property sourceHost
      //var instance = new VRealizeNetworkInsightApiReference.Flow();
      //expect(instance).to.be();
    });

    it('should have the property sourceIp (base name: "source_ip")', function() {
      // uncomment below and update the code to test the property sourceIp
      //var instance = new VRealizeNetworkInsightApiReference.Flow();
      //expect(instance).to.be();
    });

    it('should have the property sourceIpSets (base name: "source_ip_sets")', function() {
      // uncomment below and update the code to test the property sourceIpSets
      //var instance = new VRealizeNetworkInsightApiReference.Flow();
      //expect(instance).to.be();
    });

    it('should have the property sourceL2Network (base name: "source_l2_network")', function() {
      // uncomment below and update the code to test the property sourceL2Network
      //var instance = new VRealizeNetworkInsightApiReference.Flow();
      //expect(instance).to.be();
    });

    it('should have the property sourceResourcePool (base name: "source_resource_pool")', function() {
      // uncomment below and update the code to test the property sourceResourcePool
      //var instance = new VRealizeNetworkInsightApiReference.Flow();
      //expect(instance).to.be();
    });

    it('should have the property sourceSecurityGroups (base name: "source_security_groups")', function() {
      // uncomment below and update the code to test the property sourceSecurityGroups
      //var instance = new VRealizeNetworkInsightApiReference.Flow();
      //expect(instance).to.be();
    });

    it('should have the property sourceSecurityTags (base name: "source_security_tags")', function() {
      // uncomment below and update the code to test the property sourceSecurityTags
      //var instance = new VRealizeNetworkInsightApiReference.Flow();
      //expect(instance).to.be();
    });

    it('should have the property sourceVm (base name: "source_vm")', function() {
      // uncomment below and update the code to test the property sourceVm
      //var instance = new VRealizeNetworkInsightApiReference.Flow();
      //expect(instance).to.be();
    });

    it('should have the property sourceVmTags (base name: "source_vm_tags")', function() {
      // uncomment below and update the code to test the property sourceVmTags
      //var instance = new VRealizeNetworkInsightApiReference.Flow();
      //expect(instance).to.be();
    });

    it('should have the property sourceVnic (base name: "source_vnic")', function() {
      // uncomment below and update the code to test the property sourceVnic
      //var instance = new VRealizeNetworkInsightApiReference.Flow();
      //expect(instance).to.be();
    });

    it('should have the property sourceVpc (base name: "source_vpc")', function() {
      // uncomment below and update the code to test the property sourceVpc
      //var instance = new VRealizeNetworkInsightApiReference.Flow();
      //expect(instance).to.be();
    });

    it('should have the property trafficType (base name: "traffic_type")', function() {
      // uncomment below and update the code to test the property trafficType
      //var instance = new VRealizeNetworkInsightApiReference.Flow();
      //expect(instance).to.be();
    });

    it('should have the property withinHost (base name: "within_host")', function() {
      // uncomment below and update the code to test the property withinHost
      //var instance = new VRealizeNetworkInsightApiReference.Flow();
      //expect(instance).to.be();
    });

  });

}));
