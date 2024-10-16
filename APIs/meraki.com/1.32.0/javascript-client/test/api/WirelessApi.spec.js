/**
 * Meraki Dashboard API
 * The Cisco Meraki Dashboard API is a modern REST API based on the OpenAPI specification.  > Date: 05 April, 2023 > > [Recent Updates](https://meraki.io/whats-new/)  ---  [API Documentation](https://meraki.io/api)  [Community Support](https://meraki.io/community)  [Meraki Homepage](https://www.meraki.com) 
 *
 * The version of the OpenAPI document: 1.32.0
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
    factory(root.expect, root.MerakiDashboardApi);
  }
}(this, function(expect, MerakiDashboardApi) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new MerakiDashboardApi.WirelessApi();
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

  describe('WirelessApi', function() {
    describe('createNetworkWirelessRfProfile', function() {
      it('should call createNetworkWirelessRfProfile successfully', function(done) {
        //uncomment below and update the code to test createNetworkWirelessRfProfile
        //instance.createNetworkWirelessRfProfile(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('createNetworkWirelessSsidIdentityPsk', function() {
      it('should call createNetworkWirelessSsidIdentityPsk successfully', function(done) {
        //uncomment below and update the code to test createNetworkWirelessSsidIdentityPsk
        //instance.createNetworkWirelessSsidIdentityPsk(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('deleteNetworkWirelessRfProfile', function() {
      it('should call deleteNetworkWirelessRfProfile successfully', function(done) {
        //uncomment below and update the code to test deleteNetworkWirelessRfProfile
        //instance.deleteNetworkWirelessRfProfile(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('deleteNetworkWirelessSsidIdentityPsk', function() {
      it('should call deleteNetworkWirelessSsidIdentityPsk successfully', function(done) {
        //uncomment below and update the code to test deleteNetworkWirelessSsidIdentityPsk
        //instance.deleteNetworkWirelessSsidIdentityPsk(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('getDeviceWirelessBluetoothSettings', function() {
      it('should call getDeviceWirelessBluetoothSettings successfully', function(done) {
        //uncomment below and update the code to test getDeviceWirelessBluetoothSettings
        //instance.getDeviceWirelessBluetoothSettings(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('getDeviceWirelessConnectionStats', function() {
      it('should call getDeviceWirelessConnectionStats successfully', function(done) {
        //uncomment below and update the code to test getDeviceWirelessConnectionStats
        //instance.getDeviceWirelessConnectionStats(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('getDeviceWirelessLatencyStats', function() {
      it('should call getDeviceWirelessLatencyStats successfully', function(done) {
        //uncomment below and update the code to test getDeviceWirelessLatencyStats
        //instance.getDeviceWirelessLatencyStats(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('getDeviceWirelessRadioSettings', function() {
      it('should call getDeviceWirelessRadioSettings successfully', function(done) {
        //uncomment below and update the code to test getDeviceWirelessRadioSettings
        //instance.getDeviceWirelessRadioSettings(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('getDeviceWirelessStatus', function() {
      it('should call getDeviceWirelessStatus successfully', function(done) {
        //uncomment below and update the code to test getDeviceWirelessStatus
        //instance.getDeviceWirelessStatus(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('getNetworkWirelessAirMarshal', function() {
      it('should call getNetworkWirelessAirMarshal successfully', function(done) {
        //uncomment below and update the code to test getNetworkWirelessAirMarshal
        //instance.getNetworkWirelessAirMarshal(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('getNetworkWirelessAlternateManagementInterface', function() {
      it('should call getNetworkWirelessAlternateManagementInterface successfully', function(done) {
        //uncomment below and update the code to test getNetworkWirelessAlternateManagementInterface
        //instance.getNetworkWirelessAlternateManagementInterface(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('getNetworkWirelessBilling', function() {
      it('should call getNetworkWirelessBilling successfully', function(done) {
        //uncomment below and update the code to test getNetworkWirelessBilling
        //instance.getNetworkWirelessBilling(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('getNetworkWirelessBluetoothSettings', function() {
      it('should call getNetworkWirelessBluetoothSettings successfully', function(done) {
        //uncomment below and update the code to test getNetworkWirelessBluetoothSettings
        //instance.getNetworkWirelessBluetoothSettings(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('getNetworkWirelessChannelUtilizationHistory', function() {
      it('should call getNetworkWirelessChannelUtilizationHistory successfully', function(done) {
        //uncomment below and update the code to test getNetworkWirelessChannelUtilizationHistory
        //instance.getNetworkWirelessChannelUtilizationHistory(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('getNetworkWirelessClientConnectionStats', function() {
      it('should call getNetworkWirelessClientConnectionStats successfully', function(done) {
        //uncomment below and update the code to test getNetworkWirelessClientConnectionStats
        //instance.getNetworkWirelessClientConnectionStats(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('getNetworkWirelessClientConnectivityEvents', function() {
      it('should call getNetworkWirelessClientConnectivityEvents successfully', function(done) {
        //uncomment below and update the code to test getNetworkWirelessClientConnectivityEvents
        //instance.getNetworkWirelessClientConnectivityEvents(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('getNetworkWirelessClientCountHistory', function() {
      it('should call getNetworkWirelessClientCountHistory successfully', function(done) {
        //uncomment below and update the code to test getNetworkWirelessClientCountHistory
        //instance.getNetworkWirelessClientCountHistory(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('getNetworkWirelessClientLatencyHistory', function() {
      it('should call getNetworkWirelessClientLatencyHistory successfully', function(done) {
        //uncomment below and update the code to test getNetworkWirelessClientLatencyHistory
        //instance.getNetworkWirelessClientLatencyHistory(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('getNetworkWirelessClientLatencyStats', function() {
      it('should call getNetworkWirelessClientLatencyStats successfully', function(done) {
        //uncomment below and update the code to test getNetworkWirelessClientLatencyStats
        //instance.getNetworkWirelessClientLatencyStats(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('getNetworkWirelessClientsConnectionStats', function() {
      it('should call getNetworkWirelessClientsConnectionStats successfully', function(done) {
        //uncomment below and update the code to test getNetworkWirelessClientsConnectionStats
        //instance.getNetworkWirelessClientsConnectionStats(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('getNetworkWirelessClientsLatencyStats', function() {
      it('should call getNetworkWirelessClientsLatencyStats successfully', function(done) {
        //uncomment below and update the code to test getNetworkWirelessClientsLatencyStats
        //instance.getNetworkWirelessClientsLatencyStats(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('getNetworkWirelessConnectionStats', function() {
      it('should call getNetworkWirelessConnectionStats successfully', function(done) {
        //uncomment below and update the code to test getNetworkWirelessConnectionStats
        //instance.getNetworkWirelessConnectionStats(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('getNetworkWirelessDataRateHistory', function() {
      it('should call getNetworkWirelessDataRateHistory successfully', function(done) {
        //uncomment below and update the code to test getNetworkWirelessDataRateHistory
        //instance.getNetworkWirelessDataRateHistory(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('getNetworkWirelessDevicesConnectionStats', function() {
      it('should call getNetworkWirelessDevicesConnectionStats successfully', function(done) {
        //uncomment below and update the code to test getNetworkWirelessDevicesConnectionStats
        //instance.getNetworkWirelessDevicesConnectionStats(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('getNetworkWirelessDevicesLatencyStats', function() {
      it('should call getNetworkWirelessDevicesLatencyStats successfully', function(done) {
        //uncomment below and update the code to test getNetworkWirelessDevicesLatencyStats
        //instance.getNetworkWirelessDevicesLatencyStats(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('getNetworkWirelessFailedConnections', function() {
      it('should call getNetworkWirelessFailedConnections successfully', function(done) {
        //uncomment below and update the code to test getNetworkWirelessFailedConnections
        //instance.getNetworkWirelessFailedConnections(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('getNetworkWirelessLatencyHistory', function() {
      it('should call getNetworkWirelessLatencyHistory successfully', function(done) {
        //uncomment below and update the code to test getNetworkWirelessLatencyHistory
        //instance.getNetworkWirelessLatencyHistory(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('getNetworkWirelessLatencyStats', function() {
      it('should call getNetworkWirelessLatencyStats successfully', function(done) {
        //uncomment below and update the code to test getNetworkWirelessLatencyStats
        //instance.getNetworkWirelessLatencyStats(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('getNetworkWirelessMeshStatuses', function() {
      it('should call getNetworkWirelessMeshStatuses successfully', function(done) {
        //uncomment below and update the code to test getNetworkWirelessMeshStatuses
        //instance.getNetworkWirelessMeshStatuses(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('getNetworkWirelessRfProfile', function() {
      it('should call getNetworkWirelessRfProfile successfully', function(done) {
        //uncomment below and update the code to test getNetworkWirelessRfProfile
        //instance.getNetworkWirelessRfProfile(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('getNetworkWirelessRfProfiles', function() {
      it('should call getNetworkWirelessRfProfiles successfully', function(done) {
        //uncomment below and update the code to test getNetworkWirelessRfProfiles
        //instance.getNetworkWirelessRfProfiles(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('getNetworkWirelessSettings', function() {
      it('should call getNetworkWirelessSettings successfully', function(done) {
        //uncomment below and update the code to test getNetworkWirelessSettings
        //instance.getNetworkWirelessSettings(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('getNetworkWirelessSignalQualityHistory', function() {
      it('should call getNetworkWirelessSignalQualityHistory successfully', function(done) {
        //uncomment below and update the code to test getNetworkWirelessSignalQualityHistory
        //instance.getNetworkWirelessSignalQualityHistory(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('getNetworkWirelessSsid', function() {
      it('should call getNetworkWirelessSsid successfully', function(done) {
        //uncomment below and update the code to test getNetworkWirelessSsid
        //instance.getNetworkWirelessSsid(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('getNetworkWirelessSsidBonjourForwarding', function() {
      it('should call getNetworkWirelessSsidBonjourForwarding successfully', function(done) {
        //uncomment below and update the code to test getNetworkWirelessSsidBonjourForwarding
        //instance.getNetworkWirelessSsidBonjourForwarding(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('getNetworkWirelessSsidDeviceTypeGroupPolicies', function() {
      it('should call getNetworkWirelessSsidDeviceTypeGroupPolicies successfully', function(done) {
        //uncomment below and update the code to test getNetworkWirelessSsidDeviceTypeGroupPolicies
        //instance.getNetworkWirelessSsidDeviceTypeGroupPolicies(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('getNetworkWirelessSsidEapOverride', function() {
      it('should call getNetworkWirelessSsidEapOverride successfully', function(done) {
        //uncomment below and update the code to test getNetworkWirelessSsidEapOverride
        //instance.getNetworkWirelessSsidEapOverride(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('getNetworkWirelessSsidFirewallL3FirewallRules', function() {
      it('should call getNetworkWirelessSsidFirewallL3FirewallRules successfully', function(done) {
        //uncomment below and update the code to test getNetworkWirelessSsidFirewallL3FirewallRules
        //instance.getNetworkWirelessSsidFirewallL3FirewallRules(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('getNetworkWirelessSsidFirewallL7FirewallRules', function() {
      it('should call getNetworkWirelessSsidFirewallL7FirewallRules successfully', function(done) {
        //uncomment below and update the code to test getNetworkWirelessSsidFirewallL7FirewallRules
        //instance.getNetworkWirelessSsidFirewallL7FirewallRules(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('getNetworkWirelessSsidHotspot20', function() {
      it('should call getNetworkWirelessSsidHotspot20 successfully', function(done) {
        //uncomment below and update the code to test getNetworkWirelessSsidHotspot20
        //instance.getNetworkWirelessSsidHotspot20(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('getNetworkWirelessSsidIdentityPsk', function() {
      it('should call getNetworkWirelessSsidIdentityPsk successfully', function(done) {
        //uncomment below and update the code to test getNetworkWirelessSsidIdentityPsk
        //instance.getNetworkWirelessSsidIdentityPsk(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('getNetworkWirelessSsidIdentityPsks', function() {
      it('should call getNetworkWirelessSsidIdentityPsks successfully', function(done) {
        //uncomment below and update the code to test getNetworkWirelessSsidIdentityPsks
        //instance.getNetworkWirelessSsidIdentityPsks(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('getNetworkWirelessSsidSchedules', function() {
      it('should call getNetworkWirelessSsidSchedules successfully', function(done) {
        //uncomment below and update the code to test getNetworkWirelessSsidSchedules
        //instance.getNetworkWirelessSsidSchedules(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('getNetworkWirelessSsidSplashSettings', function() {
      it('should call getNetworkWirelessSsidSplashSettings successfully', function(done) {
        //uncomment below and update the code to test getNetworkWirelessSsidSplashSettings
        //instance.getNetworkWirelessSsidSplashSettings(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('getNetworkWirelessSsidTrafficShapingRules', function() {
      it('should call getNetworkWirelessSsidTrafficShapingRules successfully', function(done) {
        //uncomment below and update the code to test getNetworkWirelessSsidTrafficShapingRules
        //instance.getNetworkWirelessSsidTrafficShapingRules(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('getNetworkWirelessSsidVpn', function() {
      it('should call getNetworkWirelessSsidVpn successfully', function(done) {
        //uncomment below and update the code to test getNetworkWirelessSsidVpn
        //instance.getNetworkWirelessSsidVpn(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('getNetworkWirelessSsids', function() {
      it('should call getNetworkWirelessSsids successfully', function(done) {
        //uncomment below and update the code to test getNetworkWirelessSsids
        //instance.getNetworkWirelessSsids(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('getNetworkWirelessUsageHistory', function() {
      it('should call getNetworkWirelessUsageHistory successfully', function(done) {
        //uncomment below and update the code to test getNetworkWirelessUsageHistory
        //instance.getNetworkWirelessUsageHistory(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('getOrganizationWirelessDevicesEthernetStatuses', function() {
      it('should call getOrganizationWirelessDevicesEthernetStatuses successfully', function(done) {
        //uncomment below and update the code to test getOrganizationWirelessDevicesEthernetStatuses
        //instance.getOrganizationWirelessDevicesEthernetStatuses(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('updateDeviceWirelessBluetoothSettings', function() {
      it('should call updateDeviceWirelessBluetoothSettings successfully', function(done) {
        //uncomment below and update the code to test updateDeviceWirelessBluetoothSettings
        //instance.updateDeviceWirelessBluetoothSettings(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('updateDeviceWirelessRadioSettings', function() {
      it('should call updateDeviceWirelessRadioSettings successfully', function(done) {
        //uncomment below and update the code to test updateDeviceWirelessRadioSettings
        //instance.updateDeviceWirelessRadioSettings(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('updateNetworkWirelessAlternateManagementInterface', function() {
      it('should call updateNetworkWirelessAlternateManagementInterface successfully', function(done) {
        //uncomment below and update the code to test updateNetworkWirelessAlternateManagementInterface
        //instance.updateNetworkWirelessAlternateManagementInterface(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('updateNetworkWirelessBilling', function() {
      it('should call updateNetworkWirelessBilling successfully', function(done) {
        //uncomment below and update the code to test updateNetworkWirelessBilling
        //instance.updateNetworkWirelessBilling(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('updateNetworkWirelessBluetoothSettings', function() {
      it('should call updateNetworkWirelessBluetoothSettings successfully', function(done) {
        //uncomment below and update the code to test updateNetworkWirelessBluetoothSettings
        //instance.updateNetworkWirelessBluetoothSettings(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('updateNetworkWirelessRfProfile', function() {
      it('should call updateNetworkWirelessRfProfile successfully', function(done) {
        //uncomment below and update the code to test updateNetworkWirelessRfProfile
        //instance.updateNetworkWirelessRfProfile(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('updateNetworkWirelessSettings', function() {
      it('should call updateNetworkWirelessSettings successfully', function(done) {
        //uncomment below and update the code to test updateNetworkWirelessSettings
        //instance.updateNetworkWirelessSettings(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('updateNetworkWirelessSsid', function() {
      it('should call updateNetworkWirelessSsid successfully', function(done) {
        //uncomment below and update the code to test updateNetworkWirelessSsid
        //instance.updateNetworkWirelessSsid(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('updateNetworkWirelessSsidBonjourForwarding', function() {
      it('should call updateNetworkWirelessSsidBonjourForwarding successfully', function(done) {
        //uncomment below and update the code to test updateNetworkWirelessSsidBonjourForwarding
        //instance.updateNetworkWirelessSsidBonjourForwarding(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('updateNetworkWirelessSsidDeviceTypeGroupPolicies', function() {
      it('should call updateNetworkWirelessSsidDeviceTypeGroupPolicies successfully', function(done) {
        //uncomment below and update the code to test updateNetworkWirelessSsidDeviceTypeGroupPolicies
        //instance.updateNetworkWirelessSsidDeviceTypeGroupPolicies(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('updateNetworkWirelessSsidEapOverride', function() {
      it('should call updateNetworkWirelessSsidEapOverride successfully', function(done) {
        //uncomment below and update the code to test updateNetworkWirelessSsidEapOverride
        //instance.updateNetworkWirelessSsidEapOverride(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('updateNetworkWirelessSsidFirewallL3FirewallRules', function() {
      it('should call updateNetworkWirelessSsidFirewallL3FirewallRules successfully', function(done) {
        //uncomment below and update the code to test updateNetworkWirelessSsidFirewallL3FirewallRules
        //instance.updateNetworkWirelessSsidFirewallL3FirewallRules(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('updateNetworkWirelessSsidFirewallL7FirewallRules', function() {
      it('should call updateNetworkWirelessSsidFirewallL7FirewallRules successfully', function(done) {
        //uncomment below and update the code to test updateNetworkWirelessSsidFirewallL7FirewallRules
        //instance.updateNetworkWirelessSsidFirewallL7FirewallRules(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('updateNetworkWirelessSsidHotspot20', function() {
      it('should call updateNetworkWirelessSsidHotspot20 successfully', function(done) {
        //uncomment below and update the code to test updateNetworkWirelessSsidHotspot20
        //instance.updateNetworkWirelessSsidHotspot20(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('updateNetworkWirelessSsidIdentityPsk', function() {
      it('should call updateNetworkWirelessSsidIdentityPsk successfully', function(done) {
        //uncomment below and update the code to test updateNetworkWirelessSsidIdentityPsk
        //instance.updateNetworkWirelessSsidIdentityPsk(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('updateNetworkWirelessSsidSchedules', function() {
      it('should call updateNetworkWirelessSsidSchedules successfully', function(done) {
        //uncomment below and update the code to test updateNetworkWirelessSsidSchedules
        //instance.updateNetworkWirelessSsidSchedules(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('updateNetworkWirelessSsidSplashSettings', function() {
      it('should call updateNetworkWirelessSsidSplashSettings successfully', function(done) {
        //uncomment below and update the code to test updateNetworkWirelessSsidSplashSettings
        //instance.updateNetworkWirelessSsidSplashSettings(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('updateNetworkWirelessSsidTrafficShapingRules', function() {
      it('should call updateNetworkWirelessSsidTrafficShapingRules successfully', function(done) {
        //uncomment below and update the code to test updateNetworkWirelessSsidTrafficShapingRules
        //instance.updateNetworkWirelessSsidTrafficShapingRules(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('updateNetworkWirelessSsidVpn', function() {
      it('should call updateNetworkWirelessSsidVpn successfully', function(done) {
        //uncomment below and update the code to test updateNetworkWirelessSsidVpn
        //instance.updateNetworkWirelessSsidVpn(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
  });

}));
