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
    instance = new MerakiDashboardApi.UpdateNetworkWirelessSsidRequest();
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

  describe('UpdateNetworkWirelessSsidRequest', function() {
    it('should create an instance of UpdateNetworkWirelessSsidRequest', function() {
      // uncomment below and update the code to test UpdateNetworkWirelessSsidRequest
      //var instance = new MerakiDashboardApi.UpdateNetworkWirelessSsidRequest();
      //expect(instance).to.be.a(MerakiDashboardApi.UpdateNetworkWirelessSsidRequest);
    });

    it('should have the property activeDirectory (base name: "activeDirectory")', function() {
      // uncomment below and update the code to test the property activeDirectory
      //var instance = new MerakiDashboardApi.UpdateNetworkWirelessSsidRequest();
      //expect(instance).to.be();
    });

    it('should have the property adultContentFilteringEnabled (base name: "adultContentFilteringEnabled")', function() {
      // uncomment below and update the code to test the property adultContentFilteringEnabled
      //var instance = new MerakiDashboardApi.UpdateNetworkWirelessSsidRequest();
      //expect(instance).to.be();
    });

    it('should have the property apTagsAndVlanIds (base name: "apTagsAndVlanIds")', function() {
      // uncomment below and update the code to test the property apTagsAndVlanIds
      //var instance = new MerakiDashboardApi.UpdateNetworkWirelessSsidRequest();
      //expect(instance).to.be();
    });

    it('should have the property authMode (base name: "authMode")', function() {
      // uncomment below and update the code to test the property authMode
      //var instance = new MerakiDashboardApi.UpdateNetworkWirelessSsidRequest();
      //expect(instance).to.be();
    });

    it('should have the property availabilityTags (base name: "availabilityTags")', function() {
      // uncomment below and update the code to test the property availabilityTags
      //var instance = new MerakiDashboardApi.UpdateNetworkWirelessSsidRequest();
      //expect(instance).to.be();
    });

    it('should have the property availableOnAllAps (base name: "availableOnAllAps")', function() {
      // uncomment below and update the code to test the property availableOnAllAps
      //var instance = new MerakiDashboardApi.UpdateNetworkWirelessSsidRequest();
      //expect(instance).to.be();
    });

    it('should have the property bandSelection (base name: "bandSelection")', function() {
      // uncomment below and update the code to test the property bandSelection
      //var instance = new MerakiDashboardApi.UpdateNetworkWirelessSsidRequest();
      //expect(instance).to.be();
    });

    it('should have the property concentratorNetworkId (base name: "concentratorNetworkId")', function() {
      // uncomment below and update the code to test the property concentratorNetworkId
      //var instance = new MerakiDashboardApi.UpdateNetworkWirelessSsidRequest();
      //expect(instance).to.be();
    });

    it('should have the property defaultVlanId (base name: "defaultVlanId")', function() {
      // uncomment below and update the code to test the property defaultVlanId
      //var instance = new MerakiDashboardApi.UpdateNetworkWirelessSsidRequest();
      //expect(instance).to.be();
    });

    it('should have the property disassociateClientsOnVpnFailover (base name: "disassociateClientsOnVpnFailover")', function() {
      // uncomment below and update the code to test the property disassociateClientsOnVpnFailover
      //var instance = new MerakiDashboardApi.UpdateNetworkWirelessSsidRequest();
      //expect(instance).to.be();
    });

    it('should have the property dnsRewrite (base name: "dnsRewrite")', function() {
      // uncomment below and update the code to test the property dnsRewrite
      //var instance = new MerakiDashboardApi.UpdateNetworkWirelessSsidRequest();
      //expect(instance).to.be();
    });

    it('should have the property dot11r (base name: "dot11r")', function() {
      // uncomment below and update the code to test the property dot11r
      //var instance = new MerakiDashboardApi.UpdateNetworkWirelessSsidRequest();
      //expect(instance).to.be();
    });

    it('should have the property dot11w (base name: "dot11w")', function() {
      // uncomment below and update the code to test the property dot11w
      //var instance = new MerakiDashboardApi.UpdateNetworkWirelessSsidRequest();
      //expect(instance).to.be();
    });

    it('should have the property enabled (base name: "enabled")', function() {
      // uncomment below and update the code to test the property enabled
      //var instance = new MerakiDashboardApi.UpdateNetworkWirelessSsidRequest();
      //expect(instance).to.be();
    });

    it('should have the property encryptionMode (base name: "encryptionMode")', function() {
      // uncomment below and update the code to test the property encryptionMode
      //var instance = new MerakiDashboardApi.UpdateNetworkWirelessSsidRequest();
      //expect(instance).to.be();
    });

    it('should have the property enterpriseAdminAccess (base name: "enterpriseAdminAccess")', function() {
      // uncomment below and update the code to test the property enterpriseAdminAccess
      //var instance = new MerakiDashboardApi.UpdateNetworkWirelessSsidRequest();
      //expect(instance).to.be();
    });

    it('should have the property gre (base name: "gre")', function() {
      // uncomment below and update the code to test the property gre
      //var instance = new MerakiDashboardApi.UpdateNetworkWirelessSsidRequest();
      //expect(instance).to.be();
    });

    it('should have the property ipAssignmentMode (base name: "ipAssignmentMode")', function() {
      // uncomment below and update the code to test the property ipAssignmentMode
      //var instance = new MerakiDashboardApi.UpdateNetworkWirelessSsidRequest();
      //expect(instance).to.be();
    });

    it('should have the property lanIsolationEnabled (base name: "lanIsolationEnabled")', function() {
      // uncomment below and update the code to test the property lanIsolationEnabled
      //var instance = new MerakiDashboardApi.UpdateNetworkWirelessSsidRequest();
      //expect(instance).to.be();
    });

    it('should have the property ldap (base name: "ldap")', function() {
      // uncomment below and update the code to test the property ldap
      //var instance = new MerakiDashboardApi.UpdateNetworkWirelessSsidRequest();
      //expect(instance).to.be();
    });

    it('should have the property localRadius (base name: "localRadius")', function() {
      // uncomment below and update the code to test the property localRadius
      //var instance = new MerakiDashboardApi.UpdateNetworkWirelessSsidRequest();
      //expect(instance).to.be();
    });

    it('should have the property mandatoryDhcpEnabled (base name: "mandatoryDhcpEnabled")', function() {
      // uncomment below and update the code to test the property mandatoryDhcpEnabled
      //var instance = new MerakiDashboardApi.UpdateNetworkWirelessSsidRequest();
      //expect(instance).to.be();
    });

    it('should have the property minBitrate (base name: "minBitrate")', function() {
      // uncomment below and update the code to test the property minBitrate
      //var instance = new MerakiDashboardApi.UpdateNetworkWirelessSsidRequest();
      //expect(instance).to.be();
    });

    it('should have the property name (base name: "name")', function() {
      // uncomment below and update the code to test the property name
      //var instance = new MerakiDashboardApi.UpdateNetworkWirelessSsidRequest();
      //expect(instance).to.be();
    });

    it('should have the property oauth (base name: "oauth")', function() {
      // uncomment below and update the code to test the property oauth
      //var instance = new MerakiDashboardApi.UpdateNetworkWirelessSsidRequest();
      //expect(instance).to.be();
    });

    it('should have the property perClientBandwidthLimitDown (base name: "perClientBandwidthLimitDown")', function() {
      // uncomment below and update the code to test the property perClientBandwidthLimitDown
      //var instance = new MerakiDashboardApi.UpdateNetworkWirelessSsidRequest();
      //expect(instance).to.be();
    });

    it('should have the property perClientBandwidthLimitUp (base name: "perClientBandwidthLimitUp")', function() {
      // uncomment below and update the code to test the property perClientBandwidthLimitUp
      //var instance = new MerakiDashboardApi.UpdateNetworkWirelessSsidRequest();
      //expect(instance).to.be();
    });

    it('should have the property perSsidBandwidthLimitDown (base name: "perSsidBandwidthLimitDown")', function() {
      // uncomment below and update the code to test the property perSsidBandwidthLimitDown
      //var instance = new MerakiDashboardApi.UpdateNetworkWirelessSsidRequest();
      //expect(instance).to.be();
    });

    it('should have the property perSsidBandwidthLimitUp (base name: "perSsidBandwidthLimitUp")', function() {
      // uncomment below and update the code to test the property perSsidBandwidthLimitUp
      //var instance = new MerakiDashboardApi.UpdateNetworkWirelessSsidRequest();
      //expect(instance).to.be();
    });

    it('should have the property psk (base name: "psk")', function() {
      // uncomment below and update the code to test the property psk
      //var instance = new MerakiDashboardApi.UpdateNetworkWirelessSsidRequest();
      //expect(instance).to.be();
    });

    it('should have the property radiusAccountingEnabled (base name: "radiusAccountingEnabled")', function() {
      // uncomment below and update the code to test the property radiusAccountingEnabled
      //var instance = new MerakiDashboardApi.UpdateNetworkWirelessSsidRequest();
      //expect(instance).to.be();
    });

    it('should have the property radiusAccountingInterimInterval (base name: "radiusAccountingInterimInterval")', function() {
      // uncomment below and update the code to test the property radiusAccountingInterimInterval
      //var instance = new MerakiDashboardApi.UpdateNetworkWirelessSsidRequest();
      //expect(instance).to.be();
    });

    it('should have the property radiusAccountingServers (base name: "radiusAccountingServers")', function() {
      // uncomment below and update the code to test the property radiusAccountingServers
      //var instance = new MerakiDashboardApi.UpdateNetworkWirelessSsidRequest();
      //expect(instance).to.be();
    });

    it('should have the property radiusAttributeForGroupPolicies (base name: "radiusAttributeForGroupPolicies")', function() {
      // uncomment below and update the code to test the property radiusAttributeForGroupPolicies
      //var instance = new MerakiDashboardApi.UpdateNetworkWirelessSsidRequest();
      //expect(instance).to.be();
    });

    it('should have the property radiusAuthenticationNasId (base name: "radiusAuthenticationNasId")', function() {
      // uncomment below and update the code to test the property radiusAuthenticationNasId
      //var instance = new MerakiDashboardApi.UpdateNetworkWirelessSsidRequest();
      //expect(instance).to.be();
    });

    it('should have the property radiusCalledStationId (base name: "radiusCalledStationId")', function() {
      // uncomment below and update the code to test the property radiusCalledStationId
      //var instance = new MerakiDashboardApi.UpdateNetworkWirelessSsidRequest();
      //expect(instance).to.be();
    });

    it('should have the property radiusCoaEnabled (base name: "radiusCoaEnabled")', function() {
      // uncomment below and update the code to test the property radiusCoaEnabled
      //var instance = new MerakiDashboardApi.UpdateNetworkWirelessSsidRequest();
      //expect(instance).to.be();
    });

    it('should have the property radiusFailoverPolicy (base name: "radiusFailoverPolicy")', function() {
      // uncomment below and update the code to test the property radiusFailoverPolicy
      //var instance = new MerakiDashboardApi.UpdateNetworkWirelessSsidRequest();
      //expect(instance).to.be();
    });

    it('should have the property radiusFallbackEnabled (base name: "radiusFallbackEnabled")', function() {
      // uncomment below and update the code to test the property radiusFallbackEnabled
      //var instance = new MerakiDashboardApi.UpdateNetworkWirelessSsidRequest();
      //expect(instance).to.be();
    });

    it('should have the property radiusGuestVlanEnabled (base name: "radiusGuestVlanEnabled")', function() {
      // uncomment below and update the code to test the property radiusGuestVlanEnabled
      //var instance = new MerakiDashboardApi.UpdateNetworkWirelessSsidRequest();
      //expect(instance).to.be();
    });

    it('should have the property radiusGuestVlanId (base name: "radiusGuestVlanId")', function() {
      // uncomment below and update the code to test the property radiusGuestVlanId
      //var instance = new MerakiDashboardApi.UpdateNetworkWirelessSsidRequest();
      //expect(instance).to.be();
    });

    it('should have the property radiusLoadBalancingPolicy (base name: "radiusLoadBalancingPolicy")', function() {
      // uncomment below and update the code to test the property radiusLoadBalancingPolicy
      //var instance = new MerakiDashboardApi.UpdateNetworkWirelessSsidRequest();
      //expect(instance).to.be();
    });

    it('should have the property radiusOverride (base name: "radiusOverride")', function() {
      // uncomment below and update the code to test the property radiusOverride
      //var instance = new MerakiDashboardApi.UpdateNetworkWirelessSsidRequest();
      //expect(instance).to.be();
    });

    it('should have the property radiusProxyEnabled (base name: "radiusProxyEnabled")', function() {
      // uncomment below and update the code to test the property radiusProxyEnabled
      //var instance = new MerakiDashboardApi.UpdateNetworkWirelessSsidRequest();
      //expect(instance).to.be();
    });

    it('should have the property radiusServerAttemptsLimit (base name: "radiusServerAttemptsLimit")', function() {
      // uncomment below and update the code to test the property radiusServerAttemptsLimit
      //var instance = new MerakiDashboardApi.UpdateNetworkWirelessSsidRequest();
      //expect(instance).to.be();
    });

    it('should have the property radiusServerTimeout (base name: "radiusServerTimeout")', function() {
      // uncomment below and update the code to test the property radiusServerTimeout
      //var instance = new MerakiDashboardApi.UpdateNetworkWirelessSsidRequest();
      //expect(instance).to.be();
    });

    it('should have the property radiusServers (base name: "radiusServers")', function() {
      // uncomment below and update the code to test the property radiusServers
      //var instance = new MerakiDashboardApi.UpdateNetworkWirelessSsidRequest();
      //expect(instance).to.be();
    });

    it('should have the property radiusTestingEnabled (base name: "radiusTestingEnabled")', function() {
      // uncomment below and update the code to test the property radiusTestingEnabled
      //var instance = new MerakiDashboardApi.UpdateNetworkWirelessSsidRequest();
      //expect(instance).to.be();
    });

    it('should have the property secondaryConcentratorNetworkId (base name: "secondaryConcentratorNetworkId")', function() {
      // uncomment below and update the code to test the property secondaryConcentratorNetworkId
      //var instance = new MerakiDashboardApi.UpdateNetworkWirelessSsidRequest();
      //expect(instance).to.be();
    });

    it('should have the property speedBurst (base name: "speedBurst")', function() {
      // uncomment below and update the code to test the property speedBurst
      //var instance = new MerakiDashboardApi.UpdateNetworkWirelessSsidRequest();
      //expect(instance).to.be();
    });

    it('should have the property splashGuestSponsorDomains (base name: "splashGuestSponsorDomains")', function() {
      // uncomment below and update the code to test the property splashGuestSponsorDomains
      //var instance = new MerakiDashboardApi.UpdateNetworkWirelessSsidRequest();
      //expect(instance).to.be();
    });

    it('should have the property splashPage (base name: "splashPage")', function() {
      // uncomment below and update the code to test the property splashPage
      //var instance = new MerakiDashboardApi.UpdateNetworkWirelessSsidRequest();
      //expect(instance).to.be();
    });

    it('should have the property useVlanTagging (base name: "useVlanTagging")', function() {
      // uncomment below and update the code to test the property useVlanTagging
      //var instance = new MerakiDashboardApi.UpdateNetworkWirelessSsidRequest();
      //expect(instance).to.be();
    });

    it('should have the property visible (base name: "visible")', function() {
      // uncomment below and update the code to test the property visible
      //var instance = new MerakiDashboardApi.UpdateNetworkWirelessSsidRequest();
      //expect(instance).to.be();
    });

    it('should have the property vlanId (base name: "vlanId")', function() {
      // uncomment below and update the code to test the property vlanId
      //var instance = new MerakiDashboardApi.UpdateNetworkWirelessSsidRequest();
      //expect(instance).to.be();
    });

    it('should have the property walledGardenEnabled (base name: "walledGardenEnabled")', function() {
      // uncomment below and update the code to test the property walledGardenEnabled
      //var instance = new MerakiDashboardApi.UpdateNetworkWirelessSsidRequest();
      //expect(instance).to.be();
    });

    it('should have the property walledGardenRanges (base name: "walledGardenRanges")', function() {
      // uncomment below and update the code to test the property walledGardenRanges
      //var instance = new MerakiDashboardApi.UpdateNetworkWirelessSsidRequest();
      //expect(instance).to.be();
    });

    it('should have the property wpaEncryptionMode (base name: "wpaEncryptionMode")', function() {
      // uncomment below and update the code to test the property wpaEncryptionMode
      //var instance = new MerakiDashboardApi.UpdateNetworkWirelessSsidRequest();
      //expect(instance).to.be();
    });

  });

}));
