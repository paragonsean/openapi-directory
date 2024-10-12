# DcimApi

All URIs are relative to *http://netboxdemo.com/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**dcimChoicesList**](DcimApi.md#dcimChoicesList) | **GET** /dcim/_choices/ |  |
| [**dcimChoicesRead**](DcimApi.md#dcimChoicesRead) | **GET** /dcim/_choices/{id}/ |  |
| [**dcimConnectedDeviceList**](DcimApi.md#dcimConnectedDeviceList) | **GET** /dcim/connected-device/ |  |
| [**dcimConsoleConnectionsList**](DcimApi.md#dcimConsoleConnectionsList) | **GET** /dcim/console-connections/ |  |
| [**dcimConsolePortTemplatesCreate**](DcimApi.md#dcimConsolePortTemplatesCreate) | **POST** /dcim/console-port-templates/ |  |
| [**dcimConsolePortTemplatesDelete**](DcimApi.md#dcimConsolePortTemplatesDelete) | **DELETE** /dcim/console-port-templates/{id}/ |  |
| [**dcimConsolePortTemplatesList**](DcimApi.md#dcimConsolePortTemplatesList) | **GET** /dcim/console-port-templates/ |  |
| [**dcimConsolePortTemplatesPartialUpdate**](DcimApi.md#dcimConsolePortTemplatesPartialUpdate) | **PATCH** /dcim/console-port-templates/{id}/ |  |
| [**dcimConsolePortTemplatesRead**](DcimApi.md#dcimConsolePortTemplatesRead) | **GET** /dcim/console-port-templates/{id}/ |  |
| [**dcimConsolePortTemplatesUpdate**](DcimApi.md#dcimConsolePortTemplatesUpdate) | **PUT** /dcim/console-port-templates/{id}/ |  |
| [**dcimConsolePortsCreate**](DcimApi.md#dcimConsolePortsCreate) | **POST** /dcim/console-ports/ |  |
| [**dcimConsolePortsDelete**](DcimApi.md#dcimConsolePortsDelete) | **DELETE** /dcim/console-ports/{id}/ |  |
| [**dcimConsolePortsList**](DcimApi.md#dcimConsolePortsList) | **GET** /dcim/console-ports/ |  |
| [**dcimConsolePortsPartialUpdate**](DcimApi.md#dcimConsolePortsPartialUpdate) | **PATCH** /dcim/console-ports/{id}/ |  |
| [**dcimConsolePortsRead**](DcimApi.md#dcimConsolePortsRead) | **GET** /dcim/console-ports/{id}/ |  |
| [**dcimConsolePortsUpdate**](DcimApi.md#dcimConsolePortsUpdate) | **PUT** /dcim/console-ports/{id}/ |  |
| [**dcimConsoleServerPortTemplatesCreate**](DcimApi.md#dcimConsoleServerPortTemplatesCreate) | **POST** /dcim/console-server-port-templates/ |  |
| [**dcimConsoleServerPortTemplatesDelete**](DcimApi.md#dcimConsoleServerPortTemplatesDelete) | **DELETE** /dcim/console-server-port-templates/{id}/ |  |
| [**dcimConsoleServerPortTemplatesList**](DcimApi.md#dcimConsoleServerPortTemplatesList) | **GET** /dcim/console-server-port-templates/ |  |
| [**dcimConsoleServerPortTemplatesPartialUpdate**](DcimApi.md#dcimConsoleServerPortTemplatesPartialUpdate) | **PATCH** /dcim/console-server-port-templates/{id}/ |  |
| [**dcimConsoleServerPortTemplatesRead**](DcimApi.md#dcimConsoleServerPortTemplatesRead) | **GET** /dcim/console-server-port-templates/{id}/ |  |
| [**dcimConsoleServerPortTemplatesUpdate**](DcimApi.md#dcimConsoleServerPortTemplatesUpdate) | **PUT** /dcim/console-server-port-templates/{id}/ |  |
| [**dcimConsoleServerPortsCreate**](DcimApi.md#dcimConsoleServerPortsCreate) | **POST** /dcim/console-server-ports/ |  |
| [**dcimConsoleServerPortsDelete**](DcimApi.md#dcimConsoleServerPortsDelete) | **DELETE** /dcim/console-server-ports/{id}/ |  |
| [**dcimConsoleServerPortsList**](DcimApi.md#dcimConsoleServerPortsList) | **GET** /dcim/console-server-ports/ |  |
| [**dcimConsoleServerPortsPartialUpdate**](DcimApi.md#dcimConsoleServerPortsPartialUpdate) | **PATCH** /dcim/console-server-ports/{id}/ |  |
| [**dcimConsoleServerPortsRead**](DcimApi.md#dcimConsoleServerPortsRead) | **GET** /dcim/console-server-ports/{id}/ |  |
| [**dcimConsoleServerPortsUpdate**](DcimApi.md#dcimConsoleServerPortsUpdate) | **PUT** /dcim/console-server-ports/{id}/ |  |
| [**dcimDeviceBayTemplatesCreate**](DcimApi.md#dcimDeviceBayTemplatesCreate) | **POST** /dcim/device-bay-templates/ |  |
| [**dcimDeviceBayTemplatesDelete**](DcimApi.md#dcimDeviceBayTemplatesDelete) | **DELETE** /dcim/device-bay-templates/{id}/ |  |
| [**dcimDeviceBayTemplatesList**](DcimApi.md#dcimDeviceBayTemplatesList) | **GET** /dcim/device-bay-templates/ |  |
| [**dcimDeviceBayTemplatesPartialUpdate**](DcimApi.md#dcimDeviceBayTemplatesPartialUpdate) | **PATCH** /dcim/device-bay-templates/{id}/ |  |
| [**dcimDeviceBayTemplatesRead**](DcimApi.md#dcimDeviceBayTemplatesRead) | **GET** /dcim/device-bay-templates/{id}/ |  |
| [**dcimDeviceBayTemplatesUpdate**](DcimApi.md#dcimDeviceBayTemplatesUpdate) | **PUT** /dcim/device-bay-templates/{id}/ |  |
| [**dcimDeviceBaysCreate**](DcimApi.md#dcimDeviceBaysCreate) | **POST** /dcim/device-bays/ |  |
| [**dcimDeviceBaysDelete**](DcimApi.md#dcimDeviceBaysDelete) | **DELETE** /dcim/device-bays/{id}/ |  |
| [**dcimDeviceBaysList**](DcimApi.md#dcimDeviceBaysList) | **GET** /dcim/device-bays/ |  |
| [**dcimDeviceBaysPartialUpdate**](DcimApi.md#dcimDeviceBaysPartialUpdate) | **PATCH** /dcim/device-bays/{id}/ |  |
| [**dcimDeviceBaysRead**](DcimApi.md#dcimDeviceBaysRead) | **GET** /dcim/device-bays/{id}/ |  |
| [**dcimDeviceBaysUpdate**](DcimApi.md#dcimDeviceBaysUpdate) | **PUT** /dcim/device-bays/{id}/ |  |
| [**dcimDeviceRolesCreate**](DcimApi.md#dcimDeviceRolesCreate) | **POST** /dcim/device-roles/ |  |
| [**dcimDeviceRolesDelete**](DcimApi.md#dcimDeviceRolesDelete) | **DELETE** /dcim/device-roles/{id}/ |  |
| [**dcimDeviceRolesList**](DcimApi.md#dcimDeviceRolesList) | **GET** /dcim/device-roles/ |  |
| [**dcimDeviceRolesPartialUpdate**](DcimApi.md#dcimDeviceRolesPartialUpdate) | **PATCH** /dcim/device-roles/{id}/ |  |
| [**dcimDeviceRolesRead**](DcimApi.md#dcimDeviceRolesRead) | **GET** /dcim/device-roles/{id}/ |  |
| [**dcimDeviceRolesUpdate**](DcimApi.md#dcimDeviceRolesUpdate) | **PUT** /dcim/device-roles/{id}/ |  |
| [**dcimDeviceTypesCreate**](DcimApi.md#dcimDeviceTypesCreate) | **POST** /dcim/device-types/ |  |
| [**dcimDeviceTypesDelete**](DcimApi.md#dcimDeviceTypesDelete) | **DELETE** /dcim/device-types/{id}/ |  |
| [**dcimDeviceTypesList**](DcimApi.md#dcimDeviceTypesList) | **GET** /dcim/device-types/ |  |
| [**dcimDeviceTypesPartialUpdate**](DcimApi.md#dcimDeviceTypesPartialUpdate) | **PATCH** /dcim/device-types/{id}/ |  |
| [**dcimDeviceTypesRead**](DcimApi.md#dcimDeviceTypesRead) | **GET** /dcim/device-types/{id}/ |  |
| [**dcimDeviceTypesUpdate**](DcimApi.md#dcimDeviceTypesUpdate) | **PUT** /dcim/device-types/{id}/ |  |
| [**dcimDevicesCreate**](DcimApi.md#dcimDevicesCreate) | **POST** /dcim/devices/ |  |
| [**dcimDevicesDelete**](DcimApi.md#dcimDevicesDelete) | **DELETE** /dcim/devices/{id}/ |  |
| [**dcimDevicesList**](DcimApi.md#dcimDevicesList) | **GET** /dcim/devices/ |  |
| [**dcimDevicesNapalm**](DcimApi.md#dcimDevicesNapalm) | **GET** /dcim/devices/{id}/napalm/ |  |
| [**dcimDevicesPartialUpdate**](DcimApi.md#dcimDevicesPartialUpdate) | **PATCH** /dcim/devices/{id}/ |  |
| [**dcimDevicesRead**](DcimApi.md#dcimDevicesRead) | **GET** /dcim/devices/{id}/ |  |
| [**dcimDevicesUpdate**](DcimApi.md#dcimDevicesUpdate) | **PUT** /dcim/devices/{id}/ |  |
| [**dcimInterfaceConnectionsCreate**](DcimApi.md#dcimInterfaceConnectionsCreate) | **POST** /dcim/interface-connections/ |  |
| [**dcimInterfaceConnectionsDelete**](DcimApi.md#dcimInterfaceConnectionsDelete) | **DELETE** /dcim/interface-connections/{id}/ |  |
| [**dcimInterfaceConnectionsList**](DcimApi.md#dcimInterfaceConnectionsList) | **GET** /dcim/interface-connections/ |  |
| [**dcimInterfaceConnectionsPartialUpdate**](DcimApi.md#dcimInterfaceConnectionsPartialUpdate) | **PATCH** /dcim/interface-connections/{id}/ |  |
| [**dcimInterfaceConnectionsRead**](DcimApi.md#dcimInterfaceConnectionsRead) | **GET** /dcim/interface-connections/{id}/ |  |
| [**dcimInterfaceConnectionsUpdate**](DcimApi.md#dcimInterfaceConnectionsUpdate) | **PUT** /dcim/interface-connections/{id}/ |  |
| [**dcimInterfaceTemplatesCreate**](DcimApi.md#dcimInterfaceTemplatesCreate) | **POST** /dcim/interface-templates/ |  |
| [**dcimInterfaceTemplatesDelete**](DcimApi.md#dcimInterfaceTemplatesDelete) | **DELETE** /dcim/interface-templates/{id}/ |  |
| [**dcimInterfaceTemplatesList**](DcimApi.md#dcimInterfaceTemplatesList) | **GET** /dcim/interface-templates/ |  |
| [**dcimInterfaceTemplatesPartialUpdate**](DcimApi.md#dcimInterfaceTemplatesPartialUpdate) | **PATCH** /dcim/interface-templates/{id}/ |  |
| [**dcimInterfaceTemplatesRead**](DcimApi.md#dcimInterfaceTemplatesRead) | **GET** /dcim/interface-templates/{id}/ |  |
| [**dcimInterfaceTemplatesUpdate**](DcimApi.md#dcimInterfaceTemplatesUpdate) | **PUT** /dcim/interface-templates/{id}/ |  |
| [**dcimInterfacesCreate**](DcimApi.md#dcimInterfacesCreate) | **POST** /dcim/interfaces/ |  |
| [**dcimInterfacesDelete**](DcimApi.md#dcimInterfacesDelete) | **DELETE** /dcim/interfaces/{id}/ |  |
| [**dcimInterfacesGraphs**](DcimApi.md#dcimInterfacesGraphs) | **GET** /dcim/interfaces/{id}/graphs/ |  |
| [**dcimInterfacesList**](DcimApi.md#dcimInterfacesList) | **GET** /dcim/interfaces/ |  |
| [**dcimInterfacesPartialUpdate**](DcimApi.md#dcimInterfacesPartialUpdate) | **PATCH** /dcim/interfaces/{id}/ |  |
| [**dcimInterfacesRead**](DcimApi.md#dcimInterfacesRead) | **GET** /dcim/interfaces/{id}/ |  |
| [**dcimInterfacesUpdate**](DcimApi.md#dcimInterfacesUpdate) | **PUT** /dcim/interfaces/{id}/ |  |
| [**dcimInventoryItemsCreate**](DcimApi.md#dcimInventoryItemsCreate) | **POST** /dcim/inventory-items/ |  |
| [**dcimInventoryItemsDelete**](DcimApi.md#dcimInventoryItemsDelete) | **DELETE** /dcim/inventory-items/{id}/ |  |
| [**dcimInventoryItemsList**](DcimApi.md#dcimInventoryItemsList) | **GET** /dcim/inventory-items/ |  |
| [**dcimInventoryItemsPartialUpdate**](DcimApi.md#dcimInventoryItemsPartialUpdate) | **PATCH** /dcim/inventory-items/{id}/ |  |
| [**dcimInventoryItemsRead**](DcimApi.md#dcimInventoryItemsRead) | **GET** /dcim/inventory-items/{id}/ |  |
| [**dcimInventoryItemsUpdate**](DcimApi.md#dcimInventoryItemsUpdate) | **PUT** /dcim/inventory-items/{id}/ |  |
| [**dcimManufacturersCreate**](DcimApi.md#dcimManufacturersCreate) | **POST** /dcim/manufacturers/ |  |
| [**dcimManufacturersDelete**](DcimApi.md#dcimManufacturersDelete) | **DELETE** /dcim/manufacturers/{id}/ |  |
| [**dcimManufacturersList**](DcimApi.md#dcimManufacturersList) | **GET** /dcim/manufacturers/ |  |
| [**dcimManufacturersPartialUpdate**](DcimApi.md#dcimManufacturersPartialUpdate) | **PATCH** /dcim/manufacturers/{id}/ |  |
| [**dcimManufacturersRead**](DcimApi.md#dcimManufacturersRead) | **GET** /dcim/manufacturers/{id}/ |  |
| [**dcimManufacturersUpdate**](DcimApi.md#dcimManufacturersUpdate) | **PUT** /dcim/manufacturers/{id}/ |  |
| [**dcimPlatformsCreate**](DcimApi.md#dcimPlatformsCreate) | **POST** /dcim/platforms/ |  |
| [**dcimPlatformsDelete**](DcimApi.md#dcimPlatformsDelete) | **DELETE** /dcim/platforms/{id}/ |  |
| [**dcimPlatformsList**](DcimApi.md#dcimPlatformsList) | **GET** /dcim/platforms/ |  |
| [**dcimPlatformsPartialUpdate**](DcimApi.md#dcimPlatformsPartialUpdate) | **PATCH** /dcim/platforms/{id}/ |  |
| [**dcimPlatformsRead**](DcimApi.md#dcimPlatformsRead) | **GET** /dcim/platforms/{id}/ |  |
| [**dcimPlatformsUpdate**](DcimApi.md#dcimPlatformsUpdate) | **PUT** /dcim/platforms/{id}/ |  |
| [**dcimPowerConnectionsList**](DcimApi.md#dcimPowerConnectionsList) | **GET** /dcim/power-connections/ |  |
| [**dcimPowerOutletTemplatesCreate**](DcimApi.md#dcimPowerOutletTemplatesCreate) | **POST** /dcim/power-outlet-templates/ |  |
| [**dcimPowerOutletTemplatesDelete**](DcimApi.md#dcimPowerOutletTemplatesDelete) | **DELETE** /dcim/power-outlet-templates/{id}/ |  |
| [**dcimPowerOutletTemplatesList**](DcimApi.md#dcimPowerOutletTemplatesList) | **GET** /dcim/power-outlet-templates/ |  |
| [**dcimPowerOutletTemplatesPartialUpdate**](DcimApi.md#dcimPowerOutletTemplatesPartialUpdate) | **PATCH** /dcim/power-outlet-templates/{id}/ |  |
| [**dcimPowerOutletTemplatesRead**](DcimApi.md#dcimPowerOutletTemplatesRead) | **GET** /dcim/power-outlet-templates/{id}/ |  |
| [**dcimPowerOutletTemplatesUpdate**](DcimApi.md#dcimPowerOutletTemplatesUpdate) | **PUT** /dcim/power-outlet-templates/{id}/ |  |
| [**dcimPowerOutletsCreate**](DcimApi.md#dcimPowerOutletsCreate) | **POST** /dcim/power-outlets/ |  |
| [**dcimPowerOutletsDelete**](DcimApi.md#dcimPowerOutletsDelete) | **DELETE** /dcim/power-outlets/{id}/ |  |
| [**dcimPowerOutletsList**](DcimApi.md#dcimPowerOutletsList) | **GET** /dcim/power-outlets/ |  |
| [**dcimPowerOutletsPartialUpdate**](DcimApi.md#dcimPowerOutletsPartialUpdate) | **PATCH** /dcim/power-outlets/{id}/ |  |
| [**dcimPowerOutletsRead**](DcimApi.md#dcimPowerOutletsRead) | **GET** /dcim/power-outlets/{id}/ |  |
| [**dcimPowerOutletsUpdate**](DcimApi.md#dcimPowerOutletsUpdate) | **PUT** /dcim/power-outlets/{id}/ |  |
| [**dcimPowerPortTemplatesCreate**](DcimApi.md#dcimPowerPortTemplatesCreate) | **POST** /dcim/power-port-templates/ |  |
| [**dcimPowerPortTemplatesDelete**](DcimApi.md#dcimPowerPortTemplatesDelete) | **DELETE** /dcim/power-port-templates/{id}/ |  |
| [**dcimPowerPortTemplatesList**](DcimApi.md#dcimPowerPortTemplatesList) | **GET** /dcim/power-port-templates/ |  |
| [**dcimPowerPortTemplatesPartialUpdate**](DcimApi.md#dcimPowerPortTemplatesPartialUpdate) | **PATCH** /dcim/power-port-templates/{id}/ |  |
| [**dcimPowerPortTemplatesRead**](DcimApi.md#dcimPowerPortTemplatesRead) | **GET** /dcim/power-port-templates/{id}/ |  |
| [**dcimPowerPortTemplatesUpdate**](DcimApi.md#dcimPowerPortTemplatesUpdate) | **PUT** /dcim/power-port-templates/{id}/ |  |
| [**dcimPowerPortsCreate**](DcimApi.md#dcimPowerPortsCreate) | **POST** /dcim/power-ports/ |  |
| [**dcimPowerPortsDelete**](DcimApi.md#dcimPowerPortsDelete) | **DELETE** /dcim/power-ports/{id}/ |  |
| [**dcimPowerPortsList**](DcimApi.md#dcimPowerPortsList) | **GET** /dcim/power-ports/ |  |
| [**dcimPowerPortsPartialUpdate**](DcimApi.md#dcimPowerPortsPartialUpdate) | **PATCH** /dcim/power-ports/{id}/ |  |
| [**dcimPowerPortsRead**](DcimApi.md#dcimPowerPortsRead) | **GET** /dcim/power-ports/{id}/ |  |
| [**dcimPowerPortsUpdate**](DcimApi.md#dcimPowerPortsUpdate) | **PUT** /dcim/power-ports/{id}/ |  |
| [**dcimRackGroupsCreate**](DcimApi.md#dcimRackGroupsCreate) | **POST** /dcim/rack-groups/ |  |
| [**dcimRackGroupsDelete**](DcimApi.md#dcimRackGroupsDelete) | **DELETE** /dcim/rack-groups/{id}/ |  |
| [**dcimRackGroupsList**](DcimApi.md#dcimRackGroupsList) | **GET** /dcim/rack-groups/ |  |
| [**dcimRackGroupsPartialUpdate**](DcimApi.md#dcimRackGroupsPartialUpdate) | **PATCH** /dcim/rack-groups/{id}/ |  |
| [**dcimRackGroupsRead**](DcimApi.md#dcimRackGroupsRead) | **GET** /dcim/rack-groups/{id}/ |  |
| [**dcimRackGroupsUpdate**](DcimApi.md#dcimRackGroupsUpdate) | **PUT** /dcim/rack-groups/{id}/ |  |
| [**dcimRackReservationsCreate**](DcimApi.md#dcimRackReservationsCreate) | **POST** /dcim/rack-reservations/ |  |
| [**dcimRackReservationsDelete**](DcimApi.md#dcimRackReservationsDelete) | **DELETE** /dcim/rack-reservations/{id}/ |  |
| [**dcimRackReservationsList**](DcimApi.md#dcimRackReservationsList) | **GET** /dcim/rack-reservations/ |  |
| [**dcimRackReservationsPartialUpdate**](DcimApi.md#dcimRackReservationsPartialUpdate) | **PATCH** /dcim/rack-reservations/{id}/ |  |
| [**dcimRackReservationsRead**](DcimApi.md#dcimRackReservationsRead) | **GET** /dcim/rack-reservations/{id}/ |  |
| [**dcimRackReservationsUpdate**](DcimApi.md#dcimRackReservationsUpdate) | **PUT** /dcim/rack-reservations/{id}/ |  |
| [**dcimRackRolesCreate**](DcimApi.md#dcimRackRolesCreate) | **POST** /dcim/rack-roles/ |  |
| [**dcimRackRolesDelete**](DcimApi.md#dcimRackRolesDelete) | **DELETE** /dcim/rack-roles/{id}/ |  |
| [**dcimRackRolesList**](DcimApi.md#dcimRackRolesList) | **GET** /dcim/rack-roles/ |  |
| [**dcimRackRolesPartialUpdate**](DcimApi.md#dcimRackRolesPartialUpdate) | **PATCH** /dcim/rack-roles/{id}/ |  |
| [**dcimRackRolesRead**](DcimApi.md#dcimRackRolesRead) | **GET** /dcim/rack-roles/{id}/ |  |
| [**dcimRackRolesUpdate**](DcimApi.md#dcimRackRolesUpdate) | **PUT** /dcim/rack-roles/{id}/ |  |
| [**dcimRacksCreate**](DcimApi.md#dcimRacksCreate) | **POST** /dcim/racks/ |  |
| [**dcimRacksDelete**](DcimApi.md#dcimRacksDelete) | **DELETE** /dcim/racks/{id}/ |  |
| [**dcimRacksList**](DcimApi.md#dcimRacksList) | **GET** /dcim/racks/ |  |
| [**dcimRacksPartialUpdate**](DcimApi.md#dcimRacksPartialUpdate) | **PATCH** /dcim/racks/{id}/ |  |
| [**dcimRacksRead**](DcimApi.md#dcimRacksRead) | **GET** /dcim/racks/{id}/ |  |
| [**dcimRacksUnits**](DcimApi.md#dcimRacksUnits) | **GET** /dcim/racks/{id}/units/ |  |
| [**dcimRacksUpdate**](DcimApi.md#dcimRacksUpdate) | **PUT** /dcim/racks/{id}/ |  |
| [**dcimRegionsCreate**](DcimApi.md#dcimRegionsCreate) | **POST** /dcim/regions/ |  |
| [**dcimRegionsDelete**](DcimApi.md#dcimRegionsDelete) | **DELETE** /dcim/regions/{id}/ |  |
| [**dcimRegionsList**](DcimApi.md#dcimRegionsList) | **GET** /dcim/regions/ |  |
| [**dcimRegionsPartialUpdate**](DcimApi.md#dcimRegionsPartialUpdate) | **PATCH** /dcim/regions/{id}/ |  |
| [**dcimRegionsRead**](DcimApi.md#dcimRegionsRead) | **GET** /dcim/regions/{id}/ |  |
| [**dcimRegionsUpdate**](DcimApi.md#dcimRegionsUpdate) | **PUT** /dcim/regions/{id}/ |  |
| [**dcimSitesCreate**](DcimApi.md#dcimSitesCreate) | **POST** /dcim/sites/ |  |
| [**dcimSitesDelete**](DcimApi.md#dcimSitesDelete) | **DELETE** /dcim/sites/{id}/ |  |
| [**dcimSitesGraphs**](DcimApi.md#dcimSitesGraphs) | **GET** /dcim/sites/{id}/graphs/ |  |
| [**dcimSitesList**](DcimApi.md#dcimSitesList) | **GET** /dcim/sites/ |  |
| [**dcimSitesPartialUpdate**](DcimApi.md#dcimSitesPartialUpdate) | **PATCH** /dcim/sites/{id}/ |  |
| [**dcimSitesRead**](DcimApi.md#dcimSitesRead) | **GET** /dcim/sites/{id}/ |  |
| [**dcimSitesUpdate**](DcimApi.md#dcimSitesUpdate) | **PUT** /dcim/sites/{id}/ |  |
| [**dcimVirtualChassisCreate**](DcimApi.md#dcimVirtualChassisCreate) | **POST** /dcim/virtual-chassis/ |  |
| [**dcimVirtualChassisDelete**](DcimApi.md#dcimVirtualChassisDelete) | **DELETE** /dcim/virtual-chassis/{id}/ |  |
| [**dcimVirtualChassisList**](DcimApi.md#dcimVirtualChassisList) | **GET** /dcim/virtual-chassis/ |  |
| [**dcimVirtualChassisPartialUpdate**](DcimApi.md#dcimVirtualChassisPartialUpdate) | **PATCH** /dcim/virtual-chassis/{id}/ |  |
| [**dcimVirtualChassisRead**](DcimApi.md#dcimVirtualChassisRead) | **GET** /dcim/virtual-chassis/{id}/ |  |
| [**dcimVirtualChassisUpdate**](DcimApi.md#dcimVirtualChassisUpdate) | **PUT** /dcim/virtual-chassis/{id}/ |  |


<a id="dcimChoicesList"></a>
# **dcimChoicesList**
> dcimChoicesList()





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DcimApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    DcimApi apiInstance = new DcimApi(defaultClient);
    try {
      apiInstance.dcimChoicesList();
    } catch (ApiException e) {
      System.err.println("Exception when calling DcimApi#dcimChoicesList");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="dcimChoicesRead"></a>
# **dcimChoicesRead**
> dcimChoicesRead(id)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DcimApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    DcimApi apiInstance = new DcimApi(defaultClient);
    String id = "id_example"; // String | 
    try {
      apiInstance.dcimChoicesRead(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling DcimApi#dcimChoicesRead");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**|  | |

### Return type

null (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="dcimConnectedDeviceList"></a>
# **dcimConnectedDeviceList**
> Device dcimConnectedDeviceList(peerDevice, peerInterface)



This endpoint allows a user to determine what device (if any) is connected to a given peer device and peer interface. This is useful in a situation where a device boots with no configuration, but can detect its neighbors via a protocol such as LLDP. Two query parameters must be included in the request:  * &#x60;peer_device&#x60;: The name of the peer device * &#x60;peer_interface&#x60;: The name of the peer interface

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DcimApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    DcimApi apiInstance = new DcimApi(defaultClient);
    String peerDevice = "peerDevice_example"; // String | The name of the peer device
    String peerInterface = "peerInterface_example"; // String | The name of the peer interface
    try {
      Device result = apiInstance.dcimConnectedDeviceList(peerDevice, peerInterface);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DcimApi#dcimConnectedDeviceList");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **peerDevice** | **String**| The name of the peer device | |
| **peerInterface** | **String**| The name of the peer interface | |

### Return type

[**Device**](Device.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="dcimConsoleConnectionsList"></a>
# **dcimConsoleConnectionsList**
> DcimConsoleConnectionsList200Response dcimConsoleConnectionsList(name, connectionStatus, site, device, limit, offset)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DcimApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    DcimApi apiInstance = new DcimApi(defaultClient);
    String name = "name_example"; // String | 
    String connectionStatus = "connectionStatus_example"; // String | 
    String site = "site_example"; // String | 
    String device = "device_example"; // String | 
    Integer limit = 56; // Integer | Number of results to return per page.
    Integer offset = 56; // Integer | The initial index from which to return the results.
    try {
      DcimConsoleConnectionsList200Response result = apiInstance.dcimConsoleConnectionsList(name, connectionStatus, site, device, limit, offset);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DcimApi#dcimConsoleConnectionsList");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **name** | **String**|  | [optional] |
| **connectionStatus** | **String**|  | [optional] |
| **site** | **String**|  | [optional] |
| **device** | **String**|  | [optional] |
| **limit** | **Integer**| Number of results to return per page. | [optional] |
| **offset** | **Integer**| The initial index from which to return the results. | [optional] |

### Return type

[**DcimConsoleConnectionsList200Response**](DcimConsoleConnectionsList200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="dcimConsolePortTemplatesCreate"></a>
# **dcimConsolePortTemplatesCreate**
> ConsolePortTemplate dcimConsolePortTemplatesCreate(writableConsolePortTemplate)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DcimApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    DcimApi apiInstance = new DcimApi(defaultClient);
    WritableConsolePortTemplate writableConsolePortTemplate = new WritableConsolePortTemplate(); // WritableConsolePortTemplate | 
    try {
      ConsolePortTemplate result = apiInstance.dcimConsolePortTemplatesCreate(writableConsolePortTemplate);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DcimApi#dcimConsolePortTemplatesCreate");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **writableConsolePortTemplate** | [**WritableConsolePortTemplate**](WritableConsolePortTemplate.md)|  | |

### Return type

[**ConsolePortTemplate**](ConsolePortTemplate.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** |  |  -  |

<a id="dcimConsolePortTemplatesDelete"></a>
# **dcimConsolePortTemplatesDelete**
> dcimConsolePortTemplatesDelete(id)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DcimApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    DcimApi apiInstance = new DcimApi(defaultClient);
    Integer id = 56; // Integer | A unique integer value identifying this console port template.
    try {
      apiInstance.dcimConsolePortTemplatesDelete(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling DcimApi#dcimConsolePortTemplatesDelete");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **Integer**| A unique integer value identifying this console port template. | |

### Return type

null (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** |  |  -  |

<a id="dcimConsolePortTemplatesList"></a>
# **dcimConsolePortTemplatesList**
> DcimConsolePortTemplatesList200Response dcimConsolePortTemplatesList(name, devicetypeId, limit, offset)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DcimApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    DcimApi apiInstance = new DcimApi(defaultClient);
    String name = "name_example"; // String | 
    String devicetypeId = "devicetypeId_example"; // String | 
    Integer limit = 56; // Integer | Number of results to return per page.
    Integer offset = 56; // Integer | The initial index from which to return the results.
    try {
      DcimConsolePortTemplatesList200Response result = apiInstance.dcimConsolePortTemplatesList(name, devicetypeId, limit, offset);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DcimApi#dcimConsolePortTemplatesList");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **name** | **String**|  | [optional] |
| **devicetypeId** | **String**|  | [optional] |
| **limit** | **Integer**| Number of results to return per page. | [optional] |
| **offset** | **Integer**| The initial index from which to return the results. | [optional] |

### Return type

[**DcimConsolePortTemplatesList200Response**](DcimConsolePortTemplatesList200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="dcimConsolePortTemplatesPartialUpdate"></a>
# **dcimConsolePortTemplatesPartialUpdate**
> ConsolePortTemplate dcimConsolePortTemplatesPartialUpdate(id, writableConsolePortTemplate)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DcimApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    DcimApi apiInstance = new DcimApi(defaultClient);
    Integer id = 56; // Integer | A unique integer value identifying this console port template.
    WritableConsolePortTemplate writableConsolePortTemplate = new WritableConsolePortTemplate(); // WritableConsolePortTemplate | 
    try {
      ConsolePortTemplate result = apiInstance.dcimConsolePortTemplatesPartialUpdate(id, writableConsolePortTemplate);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DcimApi#dcimConsolePortTemplatesPartialUpdate");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **Integer**| A unique integer value identifying this console port template. | |
| **writableConsolePortTemplate** | [**WritableConsolePortTemplate**](WritableConsolePortTemplate.md)|  | |

### Return type

[**ConsolePortTemplate**](ConsolePortTemplate.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="dcimConsolePortTemplatesRead"></a>
# **dcimConsolePortTemplatesRead**
> ConsolePortTemplate dcimConsolePortTemplatesRead(id)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DcimApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    DcimApi apiInstance = new DcimApi(defaultClient);
    Integer id = 56; // Integer | A unique integer value identifying this console port template.
    try {
      ConsolePortTemplate result = apiInstance.dcimConsolePortTemplatesRead(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DcimApi#dcimConsolePortTemplatesRead");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **Integer**| A unique integer value identifying this console port template. | |

### Return type

[**ConsolePortTemplate**](ConsolePortTemplate.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="dcimConsolePortTemplatesUpdate"></a>
# **dcimConsolePortTemplatesUpdate**
> ConsolePortTemplate dcimConsolePortTemplatesUpdate(id, writableConsolePortTemplate)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DcimApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    DcimApi apiInstance = new DcimApi(defaultClient);
    Integer id = 56; // Integer | A unique integer value identifying this console port template.
    WritableConsolePortTemplate writableConsolePortTemplate = new WritableConsolePortTemplate(); // WritableConsolePortTemplate | 
    try {
      ConsolePortTemplate result = apiInstance.dcimConsolePortTemplatesUpdate(id, writableConsolePortTemplate);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DcimApi#dcimConsolePortTemplatesUpdate");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **Integer**| A unique integer value identifying this console port template. | |
| **writableConsolePortTemplate** | [**WritableConsolePortTemplate**](WritableConsolePortTemplate.md)|  | |

### Return type

[**ConsolePortTemplate**](ConsolePortTemplate.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="dcimConsolePortsCreate"></a>
# **dcimConsolePortsCreate**
> ConsolePort dcimConsolePortsCreate(writableConsolePort)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DcimApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    DcimApi apiInstance = new DcimApi(defaultClient);
    WritableConsolePort writableConsolePort = new WritableConsolePort(); // WritableConsolePort | 
    try {
      ConsolePort result = apiInstance.dcimConsolePortsCreate(writableConsolePort);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DcimApi#dcimConsolePortsCreate");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **writableConsolePort** | [**WritableConsolePort**](WritableConsolePort.md)|  | |

### Return type

[**ConsolePort**](ConsolePort.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** |  |  -  |

<a id="dcimConsolePortsDelete"></a>
# **dcimConsolePortsDelete**
> dcimConsolePortsDelete(id)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DcimApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    DcimApi apiInstance = new DcimApi(defaultClient);
    Integer id = 56; // Integer | A unique integer value identifying this console port.
    try {
      apiInstance.dcimConsolePortsDelete(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling DcimApi#dcimConsolePortsDelete");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **Integer**| A unique integer value identifying this console port. | |

### Return type

null (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** |  |  -  |

<a id="dcimConsolePortsList"></a>
# **dcimConsolePortsList**
> DcimConsoleConnectionsList200Response dcimConsolePortsList(name, deviceId, device, tag, limit, offset)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DcimApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    DcimApi apiInstance = new DcimApi(defaultClient);
    String name = "name_example"; // String | 
    String deviceId = "deviceId_example"; // String | 
    String device = "device_example"; // String | 
    String tag = "tag_example"; // String | 
    Integer limit = 56; // Integer | Number of results to return per page.
    Integer offset = 56; // Integer | The initial index from which to return the results.
    try {
      DcimConsoleConnectionsList200Response result = apiInstance.dcimConsolePortsList(name, deviceId, device, tag, limit, offset);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DcimApi#dcimConsolePortsList");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **name** | **String**|  | [optional] |
| **deviceId** | **String**|  | [optional] |
| **device** | **String**|  | [optional] |
| **tag** | **String**|  | [optional] |
| **limit** | **Integer**| Number of results to return per page. | [optional] |
| **offset** | **Integer**| The initial index from which to return the results. | [optional] |

### Return type

[**DcimConsoleConnectionsList200Response**](DcimConsoleConnectionsList200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="dcimConsolePortsPartialUpdate"></a>
# **dcimConsolePortsPartialUpdate**
> ConsolePort dcimConsolePortsPartialUpdate(id, writableConsolePort)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DcimApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    DcimApi apiInstance = new DcimApi(defaultClient);
    Integer id = 56; // Integer | A unique integer value identifying this console port.
    WritableConsolePort writableConsolePort = new WritableConsolePort(); // WritableConsolePort | 
    try {
      ConsolePort result = apiInstance.dcimConsolePortsPartialUpdate(id, writableConsolePort);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DcimApi#dcimConsolePortsPartialUpdate");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **Integer**| A unique integer value identifying this console port. | |
| **writableConsolePort** | [**WritableConsolePort**](WritableConsolePort.md)|  | |

### Return type

[**ConsolePort**](ConsolePort.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="dcimConsolePortsRead"></a>
# **dcimConsolePortsRead**
> ConsolePort dcimConsolePortsRead(id)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DcimApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    DcimApi apiInstance = new DcimApi(defaultClient);
    Integer id = 56; // Integer | A unique integer value identifying this console port.
    try {
      ConsolePort result = apiInstance.dcimConsolePortsRead(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DcimApi#dcimConsolePortsRead");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **Integer**| A unique integer value identifying this console port. | |

### Return type

[**ConsolePort**](ConsolePort.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="dcimConsolePortsUpdate"></a>
# **dcimConsolePortsUpdate**
> ConsolePort dcimConsolePortsUpdate(id, writableConsolePort)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DcimApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    DcimApi apiInstance = new DcimApi(defaultClient);
    Integer id = 56; // Integer | A unique integer value identifying this console port.
    WritableConsolePort writableConsolePort = new WritableConsolePort(); // WritableConsolePort | 
    try {
      ConsolePort result = apiInstance.dcimConsolePortsUpdate(id, writableConsolePort);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DcimApi#dcimConsolePortsUpdate");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **Integer**| A unique integer value identifying this console port. | |
| **writableConsolePort** | [**WritableConsolePort**](WritableConsolePort.md)|  | |

### Return type

[**ConsolePort**](ConsolePort.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="dcimConsoleServerPortTemplatesCreate"></a>
# **dcimConsoleServerPortTemplatesCreate**
> ConsoleServerPortTemplate dcimConsoleServerPortTemplatesCreate(writableConsoleServerPortTemplate)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DcimApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    DcimApi apiInstance = new DcimApi(defaultClient);
    WritableConsoleServerPortTemplate writableConsoleServerPortTemplate = new WritableConsoleServerPortTemplate(); // WritableConsoleServerPortTemplate | 
    try {
      ConsoleServerPortTemplate result = apiInstance.dcimConsoleServerPortTemplatesCreate(writableConsoleServerPortTemplate);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DcimApi#dcimConsoleServerPortTemplatesCreate");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **writableConsoleServerPortTemplate** | [**WritableConsoleServerPortTemplate**](WritableConsoleServerPortTemplate.md)|  | |

### Return type

[**ConsoleServerPortTemplate**](ConsoleServerPortTemplate.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** |  |  -  |

<a id="dcimConsoleServerPortTemplatesDelete"></a>
# **dcimConsoleServerPortTemplatesDelete**
> dcimConsoleServerPortTemplatesDelete(id)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DcimApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    DcimApi apiInstance = new DcimApi(defaultClient);
    Integer id = 56; // Integer | A unique integer value identifying this console server port template.
    try {
      apiInstance.dcimConsoleServerPortTemplatesDelete(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling DcimApi#dcimConsoleServerPortTemplatesDelete");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **Integer**| A unique integer value identifying this console server port template. | |

### Return type

null (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** |  |  -  |

<a id="dcimConsoleServerPortTemplatesList"></a>
# **dcimConsoleServerPortTemplatesList**
> DcimConsoleServerPortTemplatesList200Response dcimConsoleServerPortTemplatesList(name, devicetypeId, limit, offset)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DcimApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    DcimApi apiInstance = new DcimApi(defaultClient);
    String name = "name_example"; // String | 
    String devicetypeId = "devicetypeId_example"; // String | 
    Integer limit = 56; // Integer | Number of results to return per page.
    Integer offset = 56; // Integer | The initial index from which to return the results.
    try {
      DcimConsoleServerPortTemplatesList200Response result = apiInstance.dcimConsoleServerPortTemplatesList(name, devicetypeId, limit, offset);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DcimApi#dcimConsoleServerPortTemplatesList");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **name** | **String**|  | [optional] |
| **devicetypeId** | **String**|  | [optional] |
| **limit** | **Integer**| Number of results to return per page. | [optional] |
| **offset** | **Integer**| The initial index from which to return the results. | [optional] |

### Return type

[**DcimConsoleServerPortTemplatesList200Response**](DcimConsoleServerPortTemplatesList200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="dcimConsoleServerPortTemplatesPartialUpdate"></a>
# **dcimConsoleServerPortTemplatesPartialUpdate**
> ConsoleServerPortTemplate dcimConsoleServerPortTemplatesPartialUpdate(id, writableConsoleServerPortTemplate)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DcimApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    DcimApi apiInstance = new DcimApi(defaultClient);
    Integer id = 56; // Integer | A unique integer value identifying this console server port template.
    WritableConsoleServerPortTemplate writableConsoleServerPortTemplate = new WritableConsoleServerPortTemplate(); // WritableConsoleServerPortTemplate | 
    try {
      ConsoleServerPortTemplate result = apiInstance.dcimConsoleServerPortTemplatesPartialUpdate(id, writableConsoleServerPortTemplate);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DcimApi#dcimConsoleServerPortTemplatesPartialUpdate");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **Integer**| A unique integer value identifying this console server port template. | |
| **writableConsoleServerPortTemplate** | [**WritableConsoleServerPortTemplate**](WritableConsoleServerPortTemplate.md)|  | |

### Return type

[**ConsoleServerPortTemplate**](ConsoleServerPortTemplate.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="dcimConsoleServerPortTemplatesRead"></a>
# **dcimConsoleServerPortTemplatesRead**
> ConsoleServerPortTemplate dcimConsoleServerPortTemplatesRead(id)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DcimApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    DcimApi apiInstance = new DcimApi(defaultClient);
    Integer id = 56; // Integer | A unique integer value identifying this console server port template.
    try {
      ConsoleServerPortTemplate result = apiInstance.dcimConsoleServerPortTemplatesRead(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DcimApi#dcimConsoleServerPortTemplatesRead");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **Integer**| A unique integer value identifying this console server port template. | |

### Return type

[**ConsoleServerPortTemplate**](ConsoleServerPortTemplate.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="dcimConsoleServerPortTemplatesUpdate"></a>
# **dcimConsoleServerPortTemplatesUpdate**
> ConsoleServerPortTemplate dcimConsoleServerPortTemplatesUpdate(id, writableConsoleServerPortTemplate)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DcimApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    DcimApi apiInstance = new DcimApi(defaultClient);
    Integer id = 56; // Integer | A unique integer value identifying this console server port template.
    WritableConsoleServerPortTemplate writableConsoleServerPortTemplate = new WritableConsoleServerPortTemplate(); // WritableConsoleServerPortTemplate | 
    try {
      ConsoleServerPortTemplate result = apiInstance.dcimConsoleServerPortTemplatesUpdate(id, writableConsoleServerPortTemplate);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DcimApi#dcimConsoleServerPortTemplatesUpdate");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **Integer**| A unique integer value identifying this console server port template. | |
| **writableConsoleServerPortTemplate** | [**WritableConsoleServerPortTemplate**](WritableConsoleServerPortTemplate.md)|  | |

### Return type

[**ConsoleServerPortTemplate**](ConsoleServerPortTemplate.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="dcimConsoleServerPortsCreate"></a>
# **dcimConsoleServerPortsCreate**
> ConsoleServerPort dcimConsoleServerPortsCreate(writableConsoleServerPort)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DcimApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    DcimApi apiInstance = new DcimApi(defaultClient);
    WritableConsoleServerPort writableConsoleServerPort = new WritableConsoleServerPort(); // WritableConsoleServerPort | 
    try {
      ConsoleServerPort result = apiInstance.dcimConsoleServerPortsCreate(writableConsoleServerPort);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DcimApi#dcimConsoleServerPortsCreate");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **writableConsoleServerPort** | [**WritableConsoleServerPort**](WritableConsoleServerPort.md)|  | |

### Return type

[**ConsoleServerPort**](ConsoleServerPort.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** |  |  -  |

<a id="dcimConsoleServerPortsDelete"></a>
# **dcimConsoleServerPortsDelete**
> dcimConsoleServerPortsDelete(id)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DcimApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    DcimApi apiInstance = new DcimApi(defaultClient);
    Integer id = 56; // Integer | A unique integer value identifying this console server port.
    try {
      apiInstance.dcimConsoleServerPortsDelete(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling DcimApi#dcimConsoleServerPortsDelete");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **Integer**| A unique integer value identifying this console server port. | |

### Return type

null (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** |  |  -  |

<a id="dcimConsoleServerPortsList"></a>
# **dcimConsoleServerPortsList**
> DcimConsoleServerPortsList200Response dcimConsoleServerPortsList(name, deviceId, device, tag, limit, offset)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DcimApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    DcimApi apiInstance = new DcimApi(defaultClient);
    String name = "name_example"; // String | 
    String deviceId = "deviceId_example"; // String | 
    String device = "device_example"; // String | 
    String tag = "tag_example"; // String | 
    Integer limit = 56; // Integer | Number of results to return per page.
    Integer offset = 56; // Integer | The initial index from which to return the results.
    try {
      DcimConsoleServerPortsList200Response result = apiInstance.dcimConsoleServerPortsList(name, deviceId, device, tag, limit, offset);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DcimApi#dcimConsoleServerPortsList");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **name** | **String**|  | [optional] |
| **deviceId** | **String**|  | [optional] |
| **device** | **String**|  | [optional] |
| **tag** | **String**|  | [optional] |
| **limit** | **Integer**| Number of results to return per page. | [optional] |
| **offset** | **Integer**| The initial index from which to return the results. | [optional] |

### Return type

[**DcimConsoleServerPortsList200Response**](DcimConsoleServerPortsList200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="dcimConsoleServerPortsPartialUpdate"></a>
# **dcimConsoleServerPortsPartialUpdate**
> ConsoleServerPort dcimConsoleServerPortsPartialUpdate(id, writableConsoleServerPort)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DcimApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    DcimApi apiInstance = new DcimApi(defaultClient);
    Integer id = 56; // Integer | A unique integer value identifying this console server port.
    WritableConsoleServerPort writableConsoleServerPort = new WritableConsoleServerPort(); // WritableConsoleServerPort | 
    try {
      ConsoleServerPort result = apiInstance.dcimConsoleServerPortsPartialUpdate(id, writableConsoleServerPort);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DcimApi#dcimConsoleServerPortsPartialUpdate");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **Integer**| A unique integer value identifying this console server port. | |
| **writableConsoleServerPort** | [**WritableConsoleServerPort**](WritableConsoleServerPort.md)|  | |

### Return type

[**ConsoleServerPort**](ConsoleServerPort.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="dcimConsoleServerPortsRead"></a>
# **dcimConsoleServerPortsRead**
> ConsoleServerPort dcimConsoleServerPortsRead(id)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DcimApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    DcimApi apiInstance = new DcimApi(defaultClient);
    Integer id = 56; // Integer | A unique integer value identifying this console server port.
    try {
      ConsoleServerPort result = apiInstance.dcimConsoleServerPortsRead(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DcimApi#dcimConsoleServerPortsRead");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **Integer**| A unique integer value identifying this console server port. | |

### Return type

[**ConsoleServerPort**](ConsoleServerPort.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="dcimConsoleServerPortsUpdate"></a>
# **dcimConsoleServerPortsUpdate**
> ConsoleServerPort dcimConsoleServerPortsUpdate(id, writableConsoleServerPort)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DcimApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    DcimApi apiInstance = new DcimApi(defaultClient);
    Integer id = 56; // Integer | A unique integer value identifying this console server port.
    WritableConsoleServerPort writableConsoleServerPort = new WritableConsoleServerPort(); // WritableConsoleServerPort | 
    try {
      ConsoleServerPort result = apiInstance.dcimConsoleServerPortsUpdate(id, writableConsoleServerPort);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DcimApi#dcimConsoleServerPortsUpdate");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **Integer**| A unique integer value identifying this console server port. | |
| **writableConsoleServerPort** | [**WritableConsoleServerPort**](WritableConsoleServerPort.md)|  | |

### Return type

[**ConsoleServerPort**](ConsoleServerPort.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="dcimDeviceBayTemplatesCreate"></a>
# **dcimDeviceBayTemplatesCreate**
> DeviceBayTemplate dcimDeviceBayTemplatesCreate(writableDeviceBayTemplate)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DcimApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    DcimApi apiInstance = new DcimApi(defaultClient);
    WritableDeviceBayTemplate writableDeviceBayTemplate = new WritableDeviceBayTemplate(); // WritableDeviceBayTemplate | 
    try {
      DeviceBayTemplate result = apiInstance.dcimDeviceBayTemplatesCreate(writableDeviceBayTemplate);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DcimApi#dcimDeviceBayTemplatesCreate");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **writableDeviceBayTemplate** | [**WritableDeviceBayTemplate**](WritableDeviceBayTemplate.md)|  | |

### Return type

[**DeviceBayTemplate**](DeviceBayTemplate.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** |  |  -  |

<a id="dcimDeviceBayTemplatesDelete"></a>
# **dcimDeviceBayTemplatesDelete**
> dcimDeviceBayTemplatesDelete(id)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DcimApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    DcimApi apiInstance = new DcimApi(defaultClient);
    Integer id = 56; // Integer | A unique integer value identifying this device bay template.
    try {
      apiInstance.dcimDeviceBayTemplatesDelete(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling DcimApi#dcimDeviceBayTemplatesDelete");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **Integer**| A unique integer value identifying this device bay template. | |

### Return type

null (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** |  |  -  |

<a id="dcimDeviceBayTemplatesList"></a>
# **dcimDeviceBayTemplatesList**
> DcimDeviceBayTemplatesList200Response dcimDeviceBayTemplatesList(name, devicetypeId, limit, offset)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DcimApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    DcimApi apiInstance = new DcimApi(defaultClient);
    String name = "name_example"; // String | 
    String devicetypeId = "devicetypeId_example"; // String | 
    Integer limit = 56; // Integer | Number of results to return per page.
    Integer offset = 56; // Integer | The initial index from which to return the results.
    try {
      DcimDeviceBayTemplatesList200Response result = apiInstance.dcimDeviceBayTemplatesList(name, devicetypeId, limit, offset);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DcimApi#dcimDeviceBayTemplatesList");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **name** | **String**|  | [optional] |
| **devicetypeId** | **String**|  | [optional] |
| **limit** | **Integer**| Number of results to return per page. | [optional] |
| **offset** | **Integer**| The initial index from which to return the results. | [optional] |

### Return type

[**DcimDeviceBayTemplatesList200Response**](DcimDeviceBayTemplatesList200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="dcimDeviceBayTemplatesPartialUpdate"></a>
# **dcimDeviceBayTemplatesPartialUpdate**
> DeviceBayTemplate dcimDeviceBayTemplatesPartialUpdate(id, writableDeviceBayTemplate)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DcimApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    DcimApi apiInstance = new DcimApi(defaultClient);
    Integer id = 56; // Integer | A unique integer value identifying this device bay template.
    WritableDeviceBayTemplate writableDeviceBayTemplate = new WritableDeviceBayTemplate(); // WritableDeviceBayTemplate | 
    try {
      DeviceBayTemplate result = apiInstance.dcimDeviceBayTemplatesPartialUpdate(id, writableDeviceBayTemplate);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DcimApi#dcimDeviceBayTemplatesPartialUpdate");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **Integer**| A unique integer value identifying this device bay template. | |
| **writableDeviceBayTemplate** | [**WritableDeviceBayTemplate**](WritableDeviceBayTemplate.md)|  | |

### Return type

[**DeviceBayTemplate**](DeviceBayTemplate.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="dcimDeviceBayTemplatesRead"></a>
# **dcimDeviceBayTemplatesRead**
> DeviceBayTemplate dcimDeviceBayTemplatesRead(id)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DcimApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    DcimApi apiInstance = new DcimApi(defaultClient);
    Integer id = 56; // Integer | A unique integer value identifying this device bay template.
    try {
      DeviceBayTemplate result = apiInstance.dcimDeviceBayTemplatesRead(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DcimApi#dcimDeviceBayTemplatesRead");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **Integer**| A unique integer value identifying this device bay template. | |

### Return type

[**DeviceBayTemplate**](DeviceBayTemplate.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="dcimDeviceBayTemplatesUpdate"></a>
# **dcimDeviceBayTemplatesUpdate**
> DeviceBayTemplate dcimDeviceBayTemplatesUpdate(id, writableDeviceBayTemplate)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DcimApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    DcimApi apiInstance = new DcimApi(defaultClient);
    Integer id = 56; // Integer | A unique integer value identifying this device bay template.
    WritableDeviceBayTemplate writableDeviceBayTemplate = new WritableDeviceBayTemplate(); // WritableDeviceBayTemplate | 
    try {
      DeviceBayTemplate result = apiInstance.dcimDeviceBayTemplatesUpdate(id, writableDeviceBayTemplate);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DcimApi#dcimDeviceBayTemplatesUpdate");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **Integer**| A unique integer value identifying this device bay template. | |
| **writableDeviceBayTemplate** | [**WritableDeviceBayTemplate**](WritableDeviceBayTemplate.md)|  | |

### Return type

[**DeviceBayTemplate**](DeviceBayTemplate.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="dcimDeviceBaysCreate"></a>
# **dcimDeviceBaysCreate**
> DeviceBay dcimDeviceBaysCreate(writableDeviceBay)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DcimApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    DcimApi apiInstance = new DcimApi(defaultClient);
    WritableDeviceBay writableDeviceBay = new WritableDeviceBay(); // WritableDeviceBay | 
    try {
      DeviceBay result = apiInstance.dcimDeviceBaysCreate(writableDeviceBay);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DcimApi#dcimDeviceBaysCreate");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **writableDeviceBay** | [**WritableDeviceBay**](WritableDeviceBay.md)|  | |

### Return type

[**DeviceBay**](DeviceBay.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** |  |  -  |

<a id="dcimDeviceBaysDelete"></a>
# **dcimDeviceBaysDelete**
> dcimDeviceBaysDelete(id)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DcimApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    DcimApi apiInstance = new DcimApi(defaultClient);
    Integer id = 56; // Integer | A unique integer value identifying this device bay.
    try {
      apiInstance.dcimDeviceBaysDelete(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling DcimApi#dcimDeviceBaysDelete");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **Integer**| A unique integer value identifying this device bay. | |

### Return type

null (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** |  |  -  |

<a id="dcimDeviceBaysList"></a>
# **dcimDeviceBaysList**
> DcimDeviceBaysList200Response dcimDeviceBaysList(name, deviceId, device, tag, limit, offset)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DcimApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    DcimApi apiInstance = new DcimApi(defaultClient);
    String name = "name_example"; // String | 
    String deviceId = "deviceId_example"; // String | 
    String device = "device_example"; // String | 
    String tag = "tag_example"; // String | 
    Integer limit = 56; // Integer | Number of results to return per page.
    Integer offset = 56; // Integer | The initial index from which to return the results.
    try {
      DcimDeviceBaysList200Response result = apiInstance.dcimDeviceBaysList(name, deviceId, device, tag, limit, offset);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DcimApi#dcimDeviceBaysList");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **name** | **String**|  | [optional] |
| **deviceId** | **String**|  | [optional] |
| **device** | **String**|  | [optional] |
| **tag** | **String**|  | [optional] |
| **limit** | **Integer**| Number of results to return per page. | [optional] |
| **offset** | **Integer**| The initial index from which to return the results. | [optional] |

### Return type

[**DcimDeviceBaysList200Response**](DcimDeviceBaysList200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="dcimDeviceBaysPartialUpdate"></a>
# **dcimDeviceBaysPartialUpdate**
> DeviceBay dcimDeviceBaysPartialUpdate(id, writableDeviceBay)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DcimApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    DcimApi apiInstance = new DcimApi(defaultClient);
    Integer id = 56; // Integer | A unique integer value identifying this device bay.
    WritableDeviceBay writableDeviceBay = new WritableDeviceBay(); // WritableDeviceBay | 
    try {
      DeviceBay result = apiInstance.dcimDeviceBaysPartialUpdate(id, writableDeviceBay);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DcimApi#dcimDeviceBaysPartialUpdate");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **Integer**| A unique integer value identifying this device bay. | |
| **writableDeviceBay** | [**WritableDeviceBay**](WritableDeviceBay.md)|  | |

### Return type

[**DeviceBay**](DeviceBay.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="dcimDeviceBaysRead"></a>
# **dcimDeviceBaysRead**
> DeviceBay dcimDeviceBaysRead(id)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DcimApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    DcimApi apiInstance = new DcimApi(defaultClient);
    Integer id = 56; // Integer | A unique integer value identifying this device bay.
    try {
      DeviceBay result = apiInstance.dcimDeviceBaysRead(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DcimApi#dcimDeviceBaysRead");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **Integer**| A unique integer value identifying this device bay. | |

### Return type

[**DeviceBay**](DeviceBay.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="dcimDeviceBaysUpdate"></a>
# **dcimDeviceBaysUpdate**
> DeviceBay dcimDeviceBaysUpdate(id, writableDeviceBay)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DcimApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    DcimApi apiInstance = new DcimApi(defaultClient);
    Integer id = 56; // Integer | A unique integer value identifying this device bay.
    WritableDeviceBay writableDeviceBay = new WritableDeviceBay(); // WritableDeviceBay | 
    try {
      DeviceBay result = apiInstance.dcimDeviceBaysUpdate(id, writableDeviceBay);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DcimApi#dcimDeviceBaysUpdate");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **Integer**| A unique integer value identifying this device bay. | |
| **writableDeviceBay** | [**WritableDeviceBay**](WritableDeviceBay.md)|  | |

### Return type

[**DeviceBay**](DeviceBay.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="dcimDeviceRolesCreate"></a>
# **dcimDeviceRolesCreate**
> DeviceRole dcimDeviceRolesCreate(deviceRole)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DcimApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    DcimApi apiInstance = new DcimApi(defaultClient);
    DeviceRole deviceRole = new DeviceRole(); // DeviceRole | 
    try {
      DeviceRole result = apiInstance.dcimDeviceRolesCreate(deviceRole);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DcimApi#dcimDeviceRolesCreate");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **deviceRole** | [**DeviceRole**](DeviceRole.md)|  | |

### Return type

[**DeviceRole**](DeviceRole.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** |  |  -  |

<a id="dcimDeviceRolesDelete"></a>
# **dcimDeviceRolesDelete**
> dcimDeviceRolesDelete(id)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DcimApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    DcimApi apiInstance = new DcimApi(defaultClient);
    Integer id = 56; // Integer | A unique integer value identifying this device role.
    try {
      apiInstance.dcimDeviceRolesDelete(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling DcimApi#dcimDeviceRolesDelete");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **Integer**| A unique integer value identifying this device role. | |

### Return type

null (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** |  |  -  |

<a id="dcimDeviceRolesList"></a>
# **dcimDeviceRolesList**
> DcimDeviceRolesList200Response dcimDeviceRolesList(name, slug, color, vmRole, limit, offset)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DcimApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    DcimApi apiInstance = new DcimApi(defaultClient);
    String name = "name_example"; // String | 
    String slug = "slug_example"; // String | 
    String color = "color_example"; // String | 
    String vmRole = "vmRole_example"; // String | 
    Integer limit = 56; // Integer | Number of results to return per page.
    Integer offset = 56; // Integer | The initial index from which to return the results.
    try {
      DcimDeviceRolesList200Response result = apiInstance.dcimDeviceRolesList(name, slug, color, vmRole, limit, offset);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DcimApi#dcimDeviceRolesList");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **name** | **String**|  | [optional] |
| **slug** | **String**|  | [optional] |
| **color** | **String**|  | [optional] |
| **vmRole** | **String**|  | [optional] |
| **limit** | **Integer**| Number of results to return per page. | [optional] |
| **offset** | **Integer**| The initial index from which to return the results. | [optional] |

### Return type

[**DcimDeviceRolesList200Response**](DcimDeviceRolesList200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="dcimDeviceRolesPartialUpdate"></a>
# **dcimDeviceRolesPartialUpdate**
> DeviceRole dcimDeviceRolesPartialUpdate(id, deviceRole)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DcimApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    DcimApi apiInstance = new DcimApi(defaultClient);
    Integer id = 56; // Integer | A unique integer value identifying this device role.
    DeviceRole deviceRole = new DeviceRole(); // DeviceRole | 
    try {
      DeviceRole result = apiInstance.dcimDeviceRolesPartialUpdate(id, deviceRole);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DcimApi#dcimDeviceRolesPartialUpdate");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **Integer**| A unique integer value identifying this device role. | |
| **deviceRole** | [**DeviceRole**](DeviceRole.md)|  | |

### Return type

[**DeviceRole**](DeviceRole.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="dcimDeviceRolesRead"></a>
# **dcimDeviceRolesRead**
> DeviceRole dcimDeviceRolesRead(id)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DcimApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    DcimApi apiInstance = new DcimApi(defaultClient);
    Integer id = 56; // Integer | A unique integer value identifying this device role.
    try {
      DeviceRole result = apiInstance.dcimDeviceRolesRead(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DcimApi#dcimDeviceRolesRead");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **Integer**| A unique integer value identifying this device role. | |

### Return type

[**DeviceRole**](DeviceRole.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="dcimDeviceRolesUpdate"></a>
# **dcimDeviceRolesUpdate**
> DeviceRole dcimDeviceRolesUpdate(id, deviceRole)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DcimApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    DcimApi apiInstance = new DcimApi(defaultClient);
    Integer id = 56; // Integer | A unique integer value identifying this device role.
    DeviceRole deviceRole = new DeviceRole(); // DeviceRole | 
    try {
      DeviceRole result = apiInstance.dcimDeviceRolesUpdate(id, deviceRole);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DcimApi#dcimDeviceRolesUpdate");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **Integer**| A unique integer value identifying this device role. | |
| **deviceRole** | [**DeviceRole**](DeviceRole.md)|  | |

### Return type

[**DeviceRole**](DeviceRole.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="dcimDeviceTypesCreate"></a>
# **dcimDeviceTypesCreate**
> DeviceType dcimDeviceTypesCreate(writableDeviceType)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DcimApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    DcimApi apiInstance = new DcimApi(defaultClient);
    WritableDeviceType writableDeviceType = new WritableDeviceType(); // WritableDeviceType | 
    try {
      DeviceType result = apiInstance.dcimDeviceTypesCreate(writableDeviceType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DcimApi#dcimDeviceTypesCreate");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **writableDeviceType** | [**WritableDeviceType**](WritableDeviceType.md)|  | |

### Return type

[**DeviceType**](DeviceType.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** |  |  -  |

<a id="dcimDeviceTypesDelete"></a>
# **dcimDeviceTypesDelete**
> dcimDeviceTypesDelete(id)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DcimApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    DcimApi apiInstance = new DcimApi(defaultClient);
    Integer id = 56; // Integer | A unique integer value identifying this device type.
    try {
      apiInstance.dcimDeviceTypesDelete(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling DcimApi#dcimDeviceTypesDelete");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **Integer**| A unique integer value identifying this device type. | |

### Return type

null (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** |  |  -  |

<a id="dcimDeviceTypesList"></a>
# **dcimDeviceTypesList**
> DcimDeviceTypesList200Response dcimDeviceTypesList(model, slug, partNumber, uHeight, isFullDepth, isConsoleServer, isPdu, isNetworkDevice, subdeviceRole, idIn, q, manufacturerId, manufacturer, tag, limit, offset)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DcimApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    DcimApi apiInstance = new DcimApi(defaultClient);
    String model = "model_example"; // String | 
    String slug = "slug_example"; // String | 
    String partNumber = "partNumber_example"; // String | 
    BigDecimal uHeight = new BigDecimal(78); // BigDecimal | 
    String isFullDepth = "isFullDepth_example"; // String | 
    String isConsoleServer = "isConsoleServer_example"; // String | 
    String isPdu = "isPdu_example"; // String | 
    String isNetworkDevice = "isNetworkDevice_example"; // String | 
    String subdeviceRole = "subdeviceRole_example"; // String | 
    String idIn = "idIn_example"; // String | Multiple values may be separated by commas.
    String q = "q_example"; // String | 
    String manufacturerId = "manufacturerId_example"; // String | 
    String manufacturer = "manufacturer_example"; // String | 
    String tag = "tag_example"; // String | 
    Integer limit = 56; // Integer | Number of results to return per page.
    Integer offset = 56; // Integer | The initial index from which to return the results.
    try {
      DcimDeviceTypesList200Response result = apiInstance.dcimDeviceTypesList(model, slug, partNumber, uHeight, isFullDepth, isConsoleServer, isPdu, isNetworkDevice, subdeviceRole, idIn, q, manufacturerId, manufacturer, tag, limit, offset);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DcimApi#dcimDeviceTypesList");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **model** | **String**|  | [optional] |
| **slug** | **String**|  | [optional] |
| **partNumber** | **String**|  | [optional] |
| **uHeight** | **BigDecimal**|  | [optional] |
| **isFullDepth** | **String**|  | [optional] |
| **isConsoleServer** | **String**|  | [optional] |
| **isPdu** | **String**|  | [optional] |
| **isNetworkDevice** | **String**|  | [optional] |
| **subdeviceRole** | **String**|  | [optional] |
| **idIn** | **String**| Multiple values may be separated by commas. | [optional] |
| **q** | **String**|  | [optional] |
| **manufacturerId** | **String**|  | [optional] |
| **manufacturer** | **String**|  | [optional] |
| **tag** | **String**|  | [optional] |
| **limit** | **Integer**| Number of results to return per page. | [optional] |
| **offset** | **Integer**| The initial index from which to return the results. | [optional] |

### Return type

[**DcimDeviceTypesList200Response**](DcimDeviceTypesList200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="dcimDeviceTypesPartialUpdate"></a>
# **dcimDeviceTypesPartialUpdate**
> DeviceType dcimDeviceTypesPartialUpdate(id, writableDeviceType)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DcimApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    DcimApi apiInstance = new DcimApi(defaultClient);
    Integer id = 56; // Integer | A unique integer value identifying this device type.
    WritableDeviceType writableDeviceType = new WritableDeviceType(); // WritableDeviceType | 
    try {
      DeviceType result = apiInstance.dcimDeviceTypesPartialUpdate(id, writableDeviceType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DcimApi#dcimDeviceTypesPartialUpdate");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **Integer**| A unique integer value identifying this device type. | |
| **writableDeviceType** | [**WritableDeviceType**](WritableDeviceType.md)|  | |

### Return type

[**DeviceType**](DeviceType.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="dcimDeviceTypesRead"></a>
# **dcimDeviceTypesRead**
> DeviceType dcimDeviceTypesRead(id)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DcimApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    DcimApi apiInstance = new DcimApi(defaultClient);
    Integer id = 56; // Integer | A unique integer value identifying this device type.
    try {
      DeviceType result = apiInstance.dcimDeviceTypesRead(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DcimApi#dcimDeviceTypesRead");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **Integer**| A unique integer value identifying this device type. | |

### Return type

[**DeviceType**](DeviceType.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="dcimDeviceTypesUpdate"></a>
# **dcimDeviceTypesUpdate**
> DeviceType dcimDeviceTypesUpdate(id, writableDeviceType)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DcimApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    DcimApi apiInstance = new DcimApi(defaultClient);
    Integer id = 56; // Integer | A unique integer value identifying this device type.
    WritableDeviceType writableDeviceType = new WritableDeviceType(); // WritableDeviceType | 
    try {
      DeviceType result = apiInstance.dcimDeviceTypesUpdate(id, writableDeviceType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DcimApi#dcimDeviceTypesUpdate");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **Integer**| A unique integer value identifying this device type. | |
| **writableDeviceType** | [**WritableDeviceType**](WritableDeviceType.md)|  | |

### Return type

[**DeviceType**](DeviceType.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="dcimDevicesCreate"></a>
# **dcimDevicesCreate**
> Device dcimDevicesCreate(writableDevice)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DcimApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    DcimApi apiInstance = new DcimApi(defaultClient);
    WritableDevice writableDevice = new WritableDevice(); // WritableDevice | 
    try {
      Device result = apiInstance.dcimDevicesCreate(writableDevice);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DcimApi#dcimDevicesCreate");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **writableDevice** | [**WritableDevice**](WritableDevice.md)|  | |

### Return type

[**Device**](Device.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** |  |  -  |

<a id="dcimDevicesDelete"></a>
# **dcimDevicesDelete**
> dcimDevicesDelete(id)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DcimApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    DcimApi apiInstance = new DcimApi(defaultClient);
    Integer id = 56; // Integer | A unique integer value identifying this device.
    try {
      apiInstance.dcimDevicesDelete(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling DcimApi#dcimDevicesDelete");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **Integer**| A unique integer value identifying this device. | |

### Return type

null (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** |  |  -  |

<a id="dcimDevicesList"></a>
# **dcimDevicesList**
> DcimDevicesList200Response dcimDevicesList(serial, position, idIn, q, manufacturerId, manufacturer, deviceTypeId, roleId, role, tenantId, tenant, platformId, platform, name, assetTag, regionId, region, siteId, site, rackGroupId, rackId, clusterId, model, status, isFullDepth, isConsoleServer, isPdu, isNetworkDevice, macAddress, hasPrimaryIp, virtualChassisId, tag, limit, offset)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DcimApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    DcimApi apiInstance = new DcimApi(defaultClient);
    String serial = "serial_example"; // String | 
    BigDecimal position = new BigDecimal(78); // BigDecimal | 
    String idIn = "idIn_example"; // String | Multiple values may be separated by commas.
    String q = "q_example"; // String | 
    String manufacturerId = "manufacturerId_example"; // String | 
    String manufacturer = "manufacturer_example"; // String | 
    String deviceTypeId = "deviceTypeId_example"; // String | 
    String roleId = "roleId_example"; // String | 
    String role = "role_example"; // String | 
    String tenantId = "tenantId_example"; // String | 
    String tenant = "tenant_example"; // String | 
    String platformId = "platformId_example"; // String | 
    String platform = "platform_example"; // String | 
    String name = "name_example"; // String | 
    String assetTag = "assetTag_example"; // String | 
    BigDecimal regionId = new BigDecimal(78); // BigDecimal | 
    String region = "region_example"; // String | 
    String siteId = "siteId_example"; // String | 
    String site = "site_example"; // String | 
    String rackGroupId = "rackGroupId_example"; // String | 
    String rackId = "rackId_example"; // String | 
    String clusterId = "clusterId_example"; // String | 
    String model = "model_example"; // String | 
    String status = "status_example"; // String | 
    String isFullDepth = "isFullDepth_example"; // String | 
    String isConsoleServer = "isConsoleServer_example"; // String | 
    String isPdu = "isPdu_example"; // String | 
    String isNetworkDevice = "isNetworkDevice_example"; // String | 
    String macAddress = "macAddress_example"; // String | 
    String hasPrimaryIp = "hasPrimaryIp_example"; // String | 
    String virtualChassisId = "virtualChassisId_example"; // String | 
    String tag = "tag_example"; // String | 
    Integer limit = 56; // Integer | Number of results to return per page.
    Integer offset = 56; // Integer | The initial index from which to return the results.
    try {
      DcimDevicesList200Response result = apiInstance.dcimDevicesList(serial, position, idIn, q, manufacturerId, manufacturer, deviceTypeId, roleId, role, tenantId, tenant, platformId, platform, name, assetTag, regionId, region, siteId, site, rackGroupId, rackId, clusterId, model, status, isFullDepth, isConsoleServer, isPdu, isNetworkDevice, macAddress, hasPrimaryIp, virtualChassisId, tag, limit, offset);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DcimApi#dcimDevicesList");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **serial** | **String**|  | [optional] |
| **position** | **BigDecimal**|  | [optional] |
| **idIn** | **String**| Multiple values may be separated by commas. | [optional] |
| **q** | **String**|  | [optional] |
| **manufacturerId** | **String**|  | [optional] |
| **manufacturer** | **String**|  | [optional] |
| **deviceTypeId** | **String**|  | [optional] |
| **roleId** | **String**|  | [optional] |
| **role** | **String**|  | [optional] |
| **tenantId** | **String**|  | [optional] |
| **tenant** | **String**|  | [optional] |
| **platformId** | **String**|  | [optional] |
| **platform** | **String**|  | [optional] |
| **name** | **String**|  | [optional] |
| **assetTag** | **String**|  | [optional] |
| **regionId** | **BigDecimal**|  | [optional] |
| **region** | **String**|  | [optional] |
| **siteId** | **String**|  | [optional] |
| **site** | **String**|  | [optional] |
| **rackGroupId** | **String**|  | [optional] |
| **rackId** | **String**|  | [optional] |
| **clusterId** | **String**|  | [optional] |
| **model** | **String**|  | [optional] |
| **status** | **String**|  | [optional] |
| **isFullDepth** | **String**|  | [optional] |
| **isConsoleServer** | **String**|  | [optional] |
| **isPdu** | **String**|  | [optional] |
| **isNetworkDevice** | **String**|  | [optional] |
| **macAddress** | **String**|  | [optional] |
| **hasPrimaryIp** | **String**|  | [optional] |
| **virtualChassisId** | **String**|  | [optional] |
| **tag** | **String**|  | [optional] |
| **limit** | **Integer**| Number of results to return per page. | [optional] |
| **offset** | **Integer**| The initial index from which to return the results. | [optional] |

### Return type

[**DcimDevicesList200Response**](DcimDevicesList200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="dcimDevicesNapalm"></a>
# **dcimDevicesNapalm**
> Device dcimDevicesNapalm(id)



Execute a NAPALM method on a Device

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DcimApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    DcimApi apiInstance = new DcimApi(defaultClient);
    Integer id = 56; // Integer | A unique integer value identifying this device.
    try {
      Device result = apiInstance.dcimDevicesNapalm(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DcimApi#dcimDevicesNapalm");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **Integer**| A unique integer value identifying this device. | |

### Return type

[**Device**](Device.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="dcimDevicesPartialUpdate"></a>
# **dcimDevicesPartialUpdate**
> Device dcimDevicesPartialUpdate(id, writableDevice)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DcimApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    DcimApi apiInstance = new DcimApi(defaultClient);
    Integer id = 56; // Integer | A unique integer value identifying this device.
    WritableDevice writableDevice = new WritableDevice(); // WritableDevice | 
    try {
      Device result = apiInstance.dcimDevicesPartialUpdate(id, writableDevice);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DcimApi#dcimDevicesPartialUpdate");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **Integer**| A unique integer value identifying this device. | |
| **writableDevice** | [**WritableDevice**](WritableDevice.md)|  | |

### Return type

[**Device**](Device.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="dcimDevicesRead"></a>
# **dcimDevicesRead**
> DeviceWithConfigContext dcimDevicesRead(id)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DcimApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    DcimApi apiInstance = new DcimApi(defaultClient);
    Integer id = 56; // Integer | A unique integer value identifying this device.
    try {
      DeviceWithConfigContext result = apiInstance.dcimDevicesRead(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DcimApi#dcimDevicesRead");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **Integer**| A unique integer value identifying this device. | |

### Return type

[**DeviceWithConfigContext**](DeviceWithConfigContext.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="dcimDevicesUpdate"></a>
# **dcimDevicesUpdate**
> Device dcimDevicesUpdate(id, writableDevice)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DcimApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    DcimApi apiInstance = new DcimApi(defaultClient);
    Integer id = 56; // Integer | A unique integer value identifying this device.
    WritableDevice writableDevice = new WritableDevice(); // WritableDevice | 
    try {
      Device result = apiInstance.dcimDevicesUpdate(id, writableDevice);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DcimApi#dcimDevicesUpdate");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **Integer**| A unique integer value identifying this device. | |
| **writableDevice** | [**WritableDevice**](WritableDevice.md)|  | |

### Return type

[**Device**](Device.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="dcimInterfaceConnectionsCreate"></a>
# **dcimInterfaceConnectionsCreate**
> InterfaceConnection dcimInterfaceConnectionsCreate(writableInterfaceConnection)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DcimApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    DcimApi apiInstance = new DcimApi(defaultClient);
    WritableInterfaceConnection writableInterfaceConnection = new WritableInterfaceConnection(); // WritableInterfaceConnection | 
    try {
      InterfaceConnection result = apiInstance.dcimInterfaceConnectionsCreate(writableInterfaceConnection);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DcimApi#dcimInterfaceConnectionsCreate");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **writableInterfaceConnection** | [**WritableInterfaceConnection**](WritableInterfaceConnection.md)|  | |

### Return type

[**InterfaceConnection**](InterfaceConnection.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** |  |  -  |

<a id="dcimInterfaceConnectionsDelete"></a>
# **dcimInterfaceConnectionsDelete**
> dcimInterfaceConnectionsDelete(id)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DcimApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    DcimApi apiInstance = new DcimApi(defaultClient);
    Integer id = 56; // Integer | A unique integer value identifying this interface connection.
    try {
      apiInstance.dcimInterfaceConnectionsDelete(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling DcimApi#dcimInterfaceConnectionsDelete");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **Integer**| A unique integer value identifying this interface connection. | |

### Return type

null (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** |  |  -  |

<a id="dcimInterfaceConnectionsList"></a>
# **dcimInterfaceConnectionsList**
> DcimInterfaceConnectionsList200Response dcimInterfaceConnectionsList(connectionStatus, site, device, limit, offset)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DcimApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    DcimApi apiInstance = new DcimApi(defaultClient);
    String connectionStatus = "connectionStatus_example"; // String | 
    String site = "site_example"; // String | 
    String device = "device_example"; // String | 
    Integer limit = 56; // Integer | Number of results to return per page.
    Integer offset = 56; // Integer | The initial index from which to return the results.
    try {
      DcimInterfaceConnectionsList200Response result = apiInstance.dcimInterfaceConnectionsList(connectionStatus, site, device, limit, offset);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DcimApi#dcimInterfaceConnectionsList");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **connectionStatus** | **String**|  | [optional] |
| **site** | **String**|  | [optional] |
| **device** | **String**|  | [optional] |
| **limit** | **Integer**| Number of results to return per page. | [optional] |
| **offset** | **Integer**| The initial index from which to return the results. | [optional] |

### Return type

[**DcimInterfaceConnectionsList200Response**](DcimInterfaceConnectionsList200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="dcimInterfaceConnectionsPartialUpdate"></a>
# **dcimInterfaceConnectionsPartialUpdate**
> InterfaceConnection dcimInterfaceConnectionsPartialUpdate(id, writableInterfaceConnection)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DcimApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    DcimApi apiInstance = new DcimApi(defaultClient);
    Integer id = 56; // Integer | A unique integer value identifying this interface connection.
    WritableInterfaceConnection writableInterfaceConnection = new WritableInterfaceConnection(); // WritableInterfaceConnection | 
    try {
      InterfaceConnection result = apiInstance.dcimInterfaceConnectionsPartialUpdate(id, writableInterfaceConnection);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DcimApi#dcimInterfaceConnectionsPartialUpdate");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **Integer**| A unique integer value identifying this interface connection. | |
| **writableInterfaceConnection** | [**WritableInterfaceConnection**](WritableInterfaceConnection.md)|  | |

### Return type

[**InterfaceConnection**](InterfaceConnection.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="dcimInterfaceConnectionsRead"></a>
# **dcimInterfaceConnectionsRead**
> InterfaceConnection dcimInterfaceConnectionsRead(id)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DcimApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    DcimApi apiInstance = new DcimApi(defaultClient);
    Integer id = 56; // Integer | A unique integer value identifying this interface connection.
    try {
      InterfaceConnection result = apiInstance.dcimInterfaceConnectionsRead(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DcimApi#dcimInterfaceConnectionsRead");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **Integer**| A unique integer value identifying this interface connection. | |

### Return type

[**InterfaceConnection**](InterfaceConnection.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="dcimInterfaceConnectionsUpdate"></a>
# **dcimInterfaceConnectionsUpdate**
> InterfaceConnection dcimInterfaceConnectionsUpdate(id, writableInterfaceConnection)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DcimApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    DcimApi apiInstance = new DcimApi(defaultClient);
    Integer id = 56; // Integer | A unique integer value identifying this interface connection.
    WritableInterfaceConnection writableInterfaceConnection = new WritableInterfaceConnection(); // WritableInterfaceConnection | 
    try {
      InterfaceConnection result = apiInstance.dcimInterfaceConnectionsUpdate(id, writableInterfaceConnection);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DcimApi#dcimInterfaceConnectionsUpdate");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **Integer**| A unique integer value identifying this interface connection. | |
| **writableInterfaceConnection** | [**WritableInterfaceConnection**](WritableInterfaceConnection.md)|  | |

### Return type

[**InterfaceConnection**](InterfaceConnection.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="dcimInterfaceTemplatesCreate"></a>
# **dcimInterfaceTemplatesCreate**
> InterfaceTemplate dcimInterfaceTemplatesCreate(writableInterfaceTemplate)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DcimApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    DcimApi apiInstance = new DcimApi(defaultClient);
    WritableInterfaceTemplate writableInterfaceTemplate = new WritableInterfaceTemplate(); // WritableInterfaceTemplate | 
    try {
      InterfaceTemplate result = apiInstance.dcimInterfaceTemplatesCreate(writableInterfaceTemplate);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DcimApi#dcimInterfaceTemplatesCreate");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **writableInterfaceTemplate** | [**WritableInterfaceTemplate**](WritableInterfaceTemplate.md)|  | |

### Return type

[**InterfaceTemplate**](InterfaceTemplate.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** |  |  -  |

<a id="dcimInterfaceTemplatesDelete"></a>
# **dcimInterfaceTemplatesDelete**
> dcimInterfaceTemplatesDelete(id)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DcimApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    DcimApi apiInstance = new DcimApi(defaultClient);
    Integer id = 56; // Integer | A unique integer value identifying this interface template.
    try {
      apiInstance.dcimInterfaceTemplatesDelete(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling DcimApi#dcimInterfaceTemplatesDelete");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **Integer**| A unique integer value identifying this interface template. | |

### Return type

null (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** |  |  -  |

<a id="dcimInterfaceTemplatesList"></a>
# **dcimInterfaceTemplatesList**
> DcimInterfaceTemplatesList200Response dcimInterfaceTemplatesList(name, formFactor, mgmtOnly, devicetypeId, limit, offset)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DcimApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    DcimApi apiInstance = new DcimApi(defaultClient);
    String name = "name_example"; // String | 
    String formFactor = "formFactor_example"; // String | 
    String mgmtOnly = "mgmtOnly_example"; // String | 
    String devicetypeId = "devicetypeId_example"; // String | 
    Integer limit = 56; // Integer | Number of results to return per page.
    Integer offset = 56; // Integer | The initial index from which to return the results.
    try {
      DcimInterfaceTemplatesList200Response result = apiInstance.dcimInterfaceTemplatesList(name, formFactor, mgmtOnly, devicetypeId, limit, offset);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DcimApi#dcimInterfaceTemplatesList");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **name** | **String**|  | [optional] |
| **formFactor** | **String**|  | [optional] |
| **mgmtOnly** | **String**|  | [optional] |
| **devicetypeId** | **String**|  | [optional] |
| **limit** | **Integer**| Number of results to return per page. | [optional] |
| **offset** | **Integer**| The initial index from which to return the results. | [optional] |

### Return type

[**DcimInterfaceTemplatesList200Response**](DcimInterfaceTemplatesList200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="dcimInterfaceTemplatesPartialUpdate"></a>
# **dcimInterfaceTemplatesPartialUpdate**
> InterfaceTemplate dcimInterfaceTemplatesPartialUpdate(id, writableInterfaceTemplate)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DcimApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    DcimApi apiInstance = new DcimApi(defaultClient);
    Integer id = 56; // Integer | A unique integer value identifying this interface template.
    WritableInterfaceTemplate writableInterfaceTemplate = new WritableInterfaceTemplate(); // WritableInterfaceTemplate | 
    try {
      InterfaceTemplate result = apiInstance.dcimInterfaceTemplatesPartialUpdate(id, writableInterfaceTemplate);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DcimApi#dcimInterfaceTemplatesPartialUpdate");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **Integer**| A unique integer value identifying this interface template. | |
| **writableInterfaceTemplate** | [**WritableInterfaceTemplate**](WritableInterfaceTemplate.md)|  | |

### Return type

[**InterfaceTemplate**](InterfaceTemplate.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="dcimInterfaceTemplatesRead"></a>
# **dcimInterfaceTemplatesRead**
> InterfaceTemplate dcimInterfaceTemplatesRead(id)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DcimApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    DcimApi apiInstance = new DcimApi(defaultClient);
    Integer id = 56; // Integer | A unique integer value identifying this interface template.
    try {
      InterfaceTemplate result = apiInstance.dcimInterfaceTemplatesRead(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DcimApi#dcimInterfaceTemplatesRead");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **Integer**| A unique integer value identifying this interface template. | |

### Return type

[**InterfaceTemplate**](InterfaceTemplate.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="dcimInterfaceTemplatesUpdate"></a>
# **dcimInterfaceTemplatesUpdate**
> InterfaceTemplate dcimInterfaceTemplatesUpdate(id, writableInterfaceTemplate)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DcimApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    DcimApi apiInstance = new DcimApi(defaultClient);
    Integer id = 56; // Integer | A unique integer value identifying this interface template.
    WritableInterfaceTemplate writableInterfaceTemplate = new WritableInterfaceTemplate(); // WritableInterfaceTemplate | 
    try {
      InterfaceTemplate result = apiInstance.dcimInterfaceTemplatesUpdate(id, writableInterfaceTemplate);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DcimApi#dcimInterfaceTemplatesUpdate");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **Integer**| A unique integer value identifying this interface template. | |
| **writableInterfaceTemplate** | [**WritableInterfaceTemplate**](WritableInterfaceTemplate.md)|  | |

### Return type

[**InterfaceTemplate**](InterfaceTemplate.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="dcimInterfacesCreate"></a>
# **dcimInterfacesCreate**
> ModelInterface dcimInterfacesCreate(writableInterface)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DcimApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    DcimApi apiInstance = new DcimApi(defaultClient);
    WritableInterface writableInterface = new WritableInterface(); // WritableInterface | 
    try {
      ModelInterface result = apiInstance.dcimInterfacesCreate(writableInterface);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DcimApi#dcimInterfacesCreate");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **writableInterface** | [**WritableInterface**](WritableInterface.md)|  | |

### Return type

[**ModelInterface**](ModelInterface.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** |  |  -  |

<a id="dcimInterfacesDelete"></a>
# **dcimInterfacesDelete**
> dcimInterfacesDelete(id)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DcimApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    DcimApi apiInstance = new DcimApi(defaultClient);
    Integer id = 56; // Integer | A unique integer value identifying this interface.
    try {
      apiInstance.dcimInterfacesDelete(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling DcimApi#dcimInterfacesDelete");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **Integer**| A unique integer value identifying this interface. | |

### Return type

null (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** |  |  -  |

<a id="dcimInterfacesGraphs"></a>
# **dcimInterfacesGraphs**
> ModelInterface dcimInterfacesGraphs(id)



A convenience method for rendering graphs for a particular interface.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DcimApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    DcimApi apiInstance = new DcimApi(defaultClient);
    Integer id = 56; // Integer | A unique integer value identifying this interface.
    try {
      ModelInterface result = apiInstance.dcimInterfacesGraphs(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DcimApi#dcimInterfacesGraphs");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **Integer**| A unique integer value identifying this interface. | |

### Return type

[**ModelInterface**](ModelInterface.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="dcimInterfacesList"></a>
# **dcimInterfacesList**
> DcimInterfacesList200Response dcimInterfacesList(name, enabled, mtu, mgmtOnly, device, deviceId, type, lagId, macAddress, tag, vlanId, vlan, formFactor, limit, offset)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DcimApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    DcimApi apiInstance = new DcimApi(defaultClient);
    String name = "name_example"; // String | 
    String enabled = "enabled_example"; // String | 
    BigDecimal mtu = new BigDecimal(78); // BigDecimal | 
    String mgmtOnly = "mgmtOnly_example"; // String | 
    String device = "device_example"; // String | 
    BigDecimal deviceId = new BigDecimal(78); // BigDecimal | 
    String type = "type_example"; // String | 
    String lagId = "lagId_example"; // String | 
    String macAddress = "macAddress_example"; // String | 
    String tag = "tag_example"; // String | 
    String vlanId = "vlanId_example"; // String | 
    String vlan = "vlan_example"; // String | 
    String formFactor = "formFactor_example"; // String | 
    Integer limit = 56; // Integer | Number of results to return per page.
    Integer offset = 56; // Integer | The initial index from which to return the results.
    try {
      DcimInterfacesList200Response result = apiInstance.dcimInterfacesList(name, enabled, mtu, mgmtOnly, device, deviceId, type, lagId, macAddress, tag, vlanId, vlan, formFactor, limit, offset);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DcimApi#dcimInterfacesList");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **name** | **String**|  | [optional] |
| **enabled** | **String**|  | [optional] |
| **mtu** | **BigDecimal**|  | [optional] |
| **mgmtOnly** | **String**|  | [optional] |
| **device** | **String**|  | [optional] |
| **deviceId** | **BigDecimal**|  | [optional] |
| **type** | **String**|  | [optional] |
| **lagId** | **String**|  | [optional] |
| **macAddress** | **String**|  | [optional] |
| **tag** | **String**|  | [optional] |
| **vlanId** | **String**|  | [optional] |
| **vlan** | **String**|  | [optional] |
| **formFactor** | **String**|  | [optional] |
| **limit** | **Integer**| Number of results to return per page. | [optional] |
| **offset** | **Integer**| The initial index from which to return the results. | [optional] |

### Return type

[**DcimInterfacesList200Response**](DcimInterfacesList200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="dcimInterfacesPartialUpdate"></a>
# **dcimInterfacesPartialUpdate**
> ModelInterface dcimInterfacesPartialUpdate(id, writableInterface)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DcimApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    DcimApi apiInstance = new DcimApi(defaultClient);
    Integer id = 56; // Integer | A unique integer value identifying this interface.
    WritableInterface writableInterface = new WritableInterface(); // WritableInterface | 
    try {
      ModelInterface result = apiInstance.dcimInterfacesPartialUpdate(id, writableInterface);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DcimApi#dcimInterfacesPartialUpdate");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **Integer**| A unique integer value identifying this interface. | |
| **writableInterface** | [**WritableInterface**](WritableInterface.md)|  | |

### Return type

[**ModelInterface**](ModelInterface.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="dcimInterfacesRead"></a>
# **dcimInterfacesRead**
> ModelInterface dcimInterfacesRead(id)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DcimApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    DcimApi apiInstance = new DcimApi(defaultClient);
    Integer id = 56; // Integer | A unique integer value identifying this interface.
    try {
      ModelInterface result = apiInstance.dcimInterfacesRead(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DcimApi#dcimInterfacesRead");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **Integer**| A unique integer value identifying this interface. | |

### Return type

[**ModelInterface**](ModelInterface.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="dcimInterfacesUpdate"></a>
# **dcimInterfacesUpdate**
> ModelInterface dcimInterfacesUpdate(id, writableInterface)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DcimApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    DcimApi apiInstance = new DcimApi(defaultClient);
    Integer id = 56; // Integer | A unique integer value identifying this interface.
    WritableInterface writableInterface = new WritableInterface(); // WritableInterface | 
    try {
      ModelInterface result = apiInstance.dcimInterfacesUpdate(id, writableInterface);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DcimApi#dcimInterfacesUpdate");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **Integer**| A unique integer value identifying this interface. | |
| **writableInterface** | [**WritableInterface**](WritableInterface.md)|  | |

### Return type

[**ModelInterface**](ModelInterface.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="dcimInventoryItemsCreate"></a>
# **dcimInventoryItemsCreate**
> InventoryItem dcimInventoryItemsCreate(writableInventoryItem)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DcimApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    DcimApi apiInstance = new DcimApi(defaultClient);
    WritableInventoryItem writableInventoryItem = new WritableInventoryItem(); // WritableInventoryItem | 
    try {
      InventoryItem result = apiInstance.dcimInventoryItemsCreate(writableInventoryItem);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DcimApi#dcimInventoryItemsCreate");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **writableInventoryItem** | [**WritableInventoryItem**](WritableInventoryItem.md)|  | |

### Return type

[**InventoryItem**](InventoryItem.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** |  |  -  |

<a id="dcimInventoryItemsDelete"></a>
# **dcimInventoryItemsDelete**
> dcimInventoryItemsDelete(id)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DcimApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    DcimApi apiInstance = new DcimApi(defaultClient);
    Integer id = 56; // Integer | A unique integer value identifying this inventory item.
    try {
      apiInstance.dcimInventoryItemsDelete(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling DcimApi#dcimInventoryItemsDelete");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **Integer**| A unique integer value identifying this inventory item. | |

### Return type

null (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** |  |  -  |

<a id="dcimInventoryItemsList"></a>
# **dcimInventoryItemsList**
> DcimInventoryItemsList200Response dcimInventoryItemsList(name, partId, serial, assetTag, discovered, deviceId, device, tag, q, parentId, manufacturerId, manufacturer, limit, offset)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DcimApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    DcimApi apiInstance = new DcimApi(defaultClient);
    String name = "name_example"; // String | 
    String partId = "partId_example"; // String | 
    String serial = "serial_example"; // String | 
    String assetTag = "assetTag_example"; // String | 
    String discovered = "discovered_example"; // String | 
    String deviceId = "deviceId_example"; // String | 
    String device = "device_example"; // String | 
    String tag = "tag_example"; // String | 
    String q = "q_example"; // String | 
    String parentId = "parentId_example"; // String | 
    String manufacturerId = "manufacturerId_example"; // String | 
    String manufacturer = "manufacturer_example"; // String | 
    Integer limit = 56; // Integer | Number of results to return per page.
    Integer offset = 56; // Integer | The initial index from which to return the results.
    try {
      DcimInventoryItemsList200Response result = apiInstance.dcimInventoryItemsList(name, partId, serial, assetTag, discovered, deviceId, device, tag, q, parentId, manufacturerId, manufacturer, limit, offset);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DcimApi#dcimInventoryItemsList");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **name** | **String**|  | [optional] |
| **partId** | **String**|  | [optional] |
| **serial** | **String**|  | [optional] |
| **assetTag** | **String**|  | [optional] |
| **discovered** | **String**|  | [optional] |
| **deviceId** | **String**|  | [optional] |
| **device** | **String**|  | [optional] |
| **tag** | **String**|  | [optional] |
| **q** | **String**|  | [optional] |
| **parentId** | **String**|  | [optional] |
| **manufacturerId** | **String**|  | [optional] |
| **manufacturer** | **String**|  | [optional] |
| **limit** | **Integer**| Number of results to return per page. | [optional] |
| **offset** | **Integer**| The initial index from which to return the results. | [optional] |

### Return type

[**DcimInventoryItemsList200Response**](DcimInventoryItemsList200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="dcimInventoryItemsPartialUpdate"></a>
# **dcimInventoryItemsPartialUpdate**
> InventoryItem dcimInventoryItemsPartialUpdate(id, writableInventoryItem)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DcimApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    DcimApi apiInstance = new DcimApi(defaultClient);
    Integer id = 56; // Integer | A unique integer value identifying this inventory item.
    WritableInventoryItem writableInventoryItem = new WritableInventoryItem(); // WritableInventoryItem | 
    try {
      InventoryItem result = apiInstance.dcimInventoryItemsPartialUpdate(id, writableInventoryItem);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DcimApi#dcimInventoryItemsPartialUpdate");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **Integer**| A unique integer value identifying this inventory item. | |
| **writableInventoryItem** | [**WritableInventoryItem**](WritableInventoryItem.md)|  | |

### Return type

[**InventoryItem**](InventoryItem.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="dcimInventoryItemsRead"></a>
# **dcimInventoryItemsRead**
> InventoryItem dcimInventoryItemsRead(id)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DcimApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    DcimApi apiInstance = new DcimApi(defaultClient);
    Integer id = 56; // Integer | A unique integer value identifying this inventory item.
    try {
      InventoryItem result = apiInstance.dcimInventoryItemsRead(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DcimApi#dcimInventoryItemsRead");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **Integer**| A unique integer value identifying this inventory item. | |

### Return type

[**InventoryItem**](InventoryItem.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="dcimInventoryItemsUpdate"></a>
# **dcimInventoryItemsUpdate**
> InventoryItem dcimInventoryItemsUpdate(id, writableInventoryItem)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DcimApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    DcimApi apiInstance = new DcimApi(defaultClient);
    Integer id = 56; // Integer | A unique integer value identifying this inventory item.
    WritableInventoryItem writableInventoryItem = new WritableInventoryItem(); // WritableInventoryItem | 
    try {
      InventoryItem result = apiInstance.dcimInventoryItemsUpdate(id, writableInventoryItem);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DcimApi#dcimInventoryItemsUpdate");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **Integer**| A unique integer value identifying this inventory item. | |
| **writableInventoryItem** | [**WritableInventoryItem**](WritableInventoryItem.md)|  | |

### Return type

[**InventoryItem**](InventoryItem.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="dcimManufacturersCreate"></a>
# **dcimManufacturersCreate**
> Manufacturer dcimManufacturersCreate(manufacturer)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DcimApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    DcimApi apiInstance = new DcimApi(defaultClient);
    Manufacturer manufacturer = new Manufacturer(); // Manufacturer | 
    try {
      Manufacturer result = apiInstance.dcimManufacturersCreate(manufacturer);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DcimApi#dcimManufacturersCreate");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **manufacturer** | [**Manufacturer**](Manufacturer.md)|  | |

### Return type

[**Manufacturer**](Manufacturer.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** |  |  -  |

<a id="dcimManufacturersDelete"></a>
# **dcimManufacturersDelete**
> dcimManufacturersDelete(id)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DcimApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    DcimApi apiInstance = new DcimApi(defaultClient);
    Integer id = 56; // Integer | A unique integer value identifying this manufacturer.
    try {
      apiInstance.dcimManufacturersDelete(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling DcimApi#dcimManufacturersDelete");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **Integer**| A unique integer value identifying this manufacturer. | |

### Return type

null (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** |  |  -  |

<a id="dcimManufacturersList"></a>
# **dcimManufacturersList**
> DcimManufacturersList200Response dcimManufacturersList(name, slug, limit, offset)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DcimApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    DcimApi apiInstance = new DcimApi(defaultClient);
    String name = "name_example"; // String | 
    String slug = "slug_example"; // String | 
    Integer limit = 56; // Integer | Number of results to return per page.
    Integer offset = 56; // Integer | The initial index from which to return the results.
    try {
      DcimManufacturersList200Response result = apiInstance.dcimManufacturersList(name, slug, limit, offset);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DcimApi#dcimManufacturersList");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **name** | **String**|  | [optional] |
| **slug** | **String**|  | [optional] |
| **limit** | **Integer**| Number of results to return per page. | [optional] |
| **offset** | **Integer**| The initial index from which to return the results. | [optional] |

### Return type

[**DcimManufacturersList200Response**](DcimManufacturersList200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="dcimManufacturersPartialUpdate"></a>
# **dcimManufacturersPartialUpdate**
> Manufacturer dcimManufacturersPartialUpdate(id, manufacturer)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DcimApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    DcimApi apiInstance = new DcimApi(defaultClient);
    Integer id = 56; // Integer | A unique integer value identifying this manufacturer.
    Manufacturer manufacturer = new Manufacturer(); // Manufacturer | 
    try {
      Manufacturer result = apiInstance.dcimManufacturersPartialUpdate(id, manufacturer);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DcimApi#dcimManufacturersPartialUpdate");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **Integer**| A unique integer value identifying this manufacturer. | |
| **manufacturer** | [**Manufacturer**](Manufacturer.md)|  | |

### Return type

[**Manufacturer**](Manufacturer.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="dcimManufacturersRead"></a>
# **dcimManufacturersRead**
> Manufacturer dcimManufacturersRead(id)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DcimApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    DcimApi apiInstance = new DcimApi(defaultClient);
    Integer id = 56; // Integer | A unique integer value identifying this manufacturer.
    try {
      Manufacturer result = apiInstance.dcimManufacturersRead(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DcimApi#dcimManufacturersRead");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **Integer**| A unique integer value identifying this manufacturer. | |

### Return type

[**Manufacturer**](Manufacturer.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="dcimManufacturersUpdate"></a>
# **dcimManufacturersUpdate**
> Manufacturer dcimManufacturersUpdate(id, manufacturer)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DcimApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    DcimApi apiInstance = new DcimApi(defaultClient);
    Integer id = 56; // Integer | A unique integer value identifying this manufacturer.
    Manufacturer manufacturer = new Manufacturer(); // Manufacturer | 
    try {
      Manufacturer result = apiInstance.dcimManufacturersUpdate(id, manufacturer);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DcimApi#dcimManufacturersUpdate");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **Integer**| A unique integer value identifying this manufacturer. | |
| **manufacturer** | [**Manufacturer**](Manufacturer.md)|  | |

### Return type

[**Manufacturer**](Manufacturer.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="dcimPlatformsCreate"></a>
# **dcimPlatformsCreate**
> Platform dcimPlatformsCreate(writablePlatform)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DcimApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    DcimApi apiInstance = new DcimApi(defaultClient);
    WritablePlatform writablePlatform = new WritablePlatform(); // WritablePlatform | 
    try {
      Platform result = apiInstance.dcimPlatformsCreate(writablePlatform);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DcimApi#dcimPlatformsCreate");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **writablePlatform** | [**WritablePlatform**](WritablePlatform.md)|  | |

### Return type

[**Platform**](Platform.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** |  |  -  |

<a id="dcimPlatformsDelete"></a>
# **dcimPlatformsDelete**
> dcimPlatformsDelete(id)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DcimApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    DcimApi apiInstance = new DcimApi(defaultClient);
    Integer id = 56; // Integer | A unique integer value identifying this platform.
    try {
      apiInstance.dcimPlatformsDelete(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling DcimApi#dcimPlatformsDelete");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **Integer**| A unique integer value identifying this platform. | |

### Return type

null (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** |  |  -  |

<a id="dcimPlatformsList"></a>
# **dcimPlatformsList**
> DcimPlatformsList200Response dcimPlatformsList(name, slug, manufacturerId, manufacturer, limit, offset)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DcimApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    DcimApi apiInstance = new DcimApi(defaultClient);
    String name = "name_example"; // String | 
    String slug = "slug_example"; // String | 
    String manufacturerId = "manufacturerId_example"; // String | 
    String manufacturer = "manufacturer_example"; // String | 
    Integer limit = 56; // Integer | Number of results to return per page.
    Integer offset = 56; // Integer | The initial index from which to return the results.
    try {
      DcimPlatformsList200Response result = apiInstance.dcimPlatformsList(name, slug, manufacturerId, manufacturer, limit, offset);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DcimApi#dcimPlatformsList");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **name** | **String**|  | [optional] |
| **slug** | **String**|  | [optional] |
| **manufacturerId** | **String**|  | [optional] |
| **manufacturer** | **String**|  | [optional] |
| **limit** | **Integer**| Number of results to return per page. | [optional] |
| **offset** | **Integer**| The initial index from which to return the results. | [optional] |

### Return type

[**DcimPlatformsList200Response**](DcimPlatformsList200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="dcimPlatformsPartialUpdate"></a>
# **dcimPlatformsPartialUpdate**
> Platform dcimPlatformsPartialUpdate(id, writablePlatform)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DcimApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    DcimApi apiInstance = new DcimApi(defaultClient);
    Integer id = 56; // Integer | A unique integer value identifying this platform.
    WritablePlatform writablePlatform = new WritablePlatform(); // WritablePlatform | 
    try {
      Platform result = apiInstance.dcimPlatformsPartialUpdate(id, writablePlatform);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DcimApi#dcimPlatformsPartialUpdate");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **Integer**| A unique integer value identifying this platform. | |
| **writablePlatform** | [**WritablePlatform**](WritablePlatform.md)|  | |

### Return type

[**Platform**](Platform.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="dcimPlatformsRead"></a>
# **dcimPlatformsRead**
> Platform dcimPlatformsRead(id)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DcimApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    DcimApi apiInstance = new DcimApi(defaultClient);
    Integer id = 56; // Integer | A unique integer value identifying this platform.
    try {
      Platform result = apiInstance.dcimPlatformsRead(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DcimApi#dcimPlatformsRead");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **Integer**| A unique integer value identifying this platform. | |

### Return type

[**Platform**](Platform.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="dcimPlatformsUpdate"></a>
# **dcimPlatformsUpdate**
> Platform dcimPlatformsUpdate(id, writablePlatform)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DcimApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    DcimApi apiInstance = new DcimApi(defaultClient);
    Integer id = 56; // Integer | A unique integer value identifying this platform.
    WritablePlatform writablePlatform = new WritablePlatform(); // WritablePlatform | 
    try {
      Platform result = apiInstance.dcimPlatformsUpdate(id, writablePlatform);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DcimApi#dcimPlatformsUpdate");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **Integer**| A unique integer value identifying this platform. | |
| **writablePlatform** | [**WritablePlatform**](WritablePlatform.md)|  | |

### Return type

[**Platform**](Platform.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="dcimPowerConnectionsList"></a>
# **dcimPowerConnectionsList**
> DcimPowerConnectionsList200Response dcimPowerConnectionsList(name, connectionStatus, site, device, limit, offset)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DcimApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    DcimApi apiInstance = new DcimApi(defaultClient);
    String name = "name_example"; // String | 
    String connectionStatus = "connectionStatus_example"; // String | 
    String site = "site_example"; // String | 
    String device = "device_example"; // String | 
    Integer limit = 56; // Integer | Number of results to return per page.
    Integer offset = 56; // Integer | The initial index from which to return the results.
    try {
      DcimPowerConnectionsList200Response result = apiInstance.dcimPowerConnectionsList(name, connectionStatus, site, device, limit, offset);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DcimApi#dcimPowerConnectionsList");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **name** | **String**|  | [optional] |
| **connectionStatus** | **String**|  | [optional] |
| **site** | **String**|  | [optional] |
| **device** | **String**|  | [optional] |
| **limit** | **Integer**| Number of results to return per page. | [optional] |
| **offset** | **Integer**| The initial index from which to return the results. | [optional] |

### Return type

[**DcimPowerConnectionsList200Response**](DcimPowerConnectionsList200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="dcimPowerOutletTemplatesCreate"></a>
# **dcimPowerOutletTemplatesCreate**
> PowerOutletTemplate dcimPowerOutletTemplatesCreate(writablePowerOutletTemplate)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DcimApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    DcimApi apiInstance = new DcimApi(defaultClient);
    WritablePowerOutletTemplate writablePowerOutletTemplate = new WritablePowerOutletTemplate(); // WritablePowerOutletTemplate | 
    try {
      PowerOutletTemplate result = apiInstance.dcimPowerOutletTemplatesCreate(writablePowerOutletTemplate);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DcimApi#dcimPowerOutletTemplatesCreate");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **writablePowerOutletTemplate** | [**WritablePowerOutletTemplate**](WritablePowerOutletTemplate.md)|  | |

### Return type

[**PowerOutletTemplate**](PowerOutletTemplate.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** |  |  -  |

<a id="dcimPowerOutletTemplatesDelete"></a>
# **dcimPowerOutletTemplatesDelete**
> dcimPowerOutletTemplatesDelete(id)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DcimApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    DcimApi apiInstance = new DcimApi(defaultClient);
    Integer id = 56; // Integer | A unique integer value identifying this power outlet template.
    try {
      apiInstance.dcimPowerOutletTemplatesDelete(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling DcimApi#dcimPowerOutletTemplatesDelete");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **Integer**| A unique integer value identifying this power outlet template. | |

### Return type

null (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** |  |  -  |

<a id="dcimPowerOutletTemplatesList"></a>
# **dcimPowerOutletTemplatesList**
> DcimPowerOutletTemplatesList200Response dcimPowerOutletTemplatesList(name, devicetypeId, limit, offset)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DcimApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    DcimApi apiInstance = new DcimApi(defaultClient);
    String name = "name_example"; // String | 
    String devicetypeId = "devicetypeId_example"; // String | 
    Integer limit = 56; // Integer | Number of results to return per page.
    Integer offset = 56; // Integer | The initial index from which to return the results.
    try {
      DcimPowerOutletTemplatesList200Response result = apiInstance.dcimPowerOutletTemplatesList(name, devicetypeId, limit, offset);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DcimApi#dcimPowerOutletTemplatesList");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **name** | **String**|  | [optional] |
| **devicetypeId** | **String**|  | [optional] |
| **limit** | **Integer**| Number of results to return per page. | [optional] |
| **offset** | **Integer**| The initial index from which to return the results. | [optional] |

### Return type

[**DcimPowerOutletTemplatesList200Response**](DcimPowerOutletTemplatesList200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="dcimPowerOutletTemplatesPartialUpdate"></a>
# **dcimPowerOutletTemplatesPartialUpdate**
> PowerOutletTemplate dcimPowerOutletTemplatesPartialUpdate(id, writablePowerOutletTemplate)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DcimApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    DcimApi apiInstance = new DcimApi(defaultClient);
    Integer id = 56; // Integer | A unique integer value identifying this power outlet template.
    WritablePowerOutletTemplate writablePowerOutletTemplate = new WritablePowerOutletTemplate(); // WritablePowerOutletTemplate | 
    try {
      PowerOutletTemplate result = apiInstance.dcimPowerOutletTemplatesPartialUpdate(id, writablePowerOutletTemplate);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DcimApi#dcimPowerOutletTemplatesPartialUpdate");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **Integer**| A unique integer value identifying this power outlet template. | |
| **writablePowerOutletTemplate** | [**WritablePowerOutletTemplate**](WritablePowerOutletTemplate.md)|  | |

### Return type

[**PowerOutletTemplate**](PowerOutletTemplate.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="dcimPowerOutletTemplatesRead"></a>
# **dcimPowerOutletTemplatesRead**
> PowerOutletTemplate dcimPowerOutletTemplatesRead(id)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DcimApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    DcimApi apiInstance = new DcimApi(defaultClient);
    Integer id = 56; // Integer | A unique integer value identifying this power outlet template.
    try {
      PowerOutletTemplate result = apiInstance.dcimPowerOutletTemplatesRead(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DcimApi#dcimPowerOutletTemplatesRead");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **Integer**| A unique integer value identifying this power outlet template. | |

### Return type

[**PowerOutletTemplate**](PowerOutletTemplate.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="dcimPowerOutletTemplatesUpdate"></a>
# **dcimPowerOutletTemplatesUpdate**
> PowerOutletTemplate dcimPowerOutletTemplatesUpdate(id, writablePowerOutletTemplate)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DcimApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    DcimApi apiInstance = new DcimApi(defaultClient);
    Integer id = 56; // Integer | A unique integer value identifying this power outlet template.
    WritablePowerOutletTemplate writablePowerOutletTemplate = new WritablePowerOutletTemplate(); // WritablePowerOutletTemplate | 
    try {
      PowerOutletTemplate result = apiInstance.dcimPowerOutletTemplatesUpdate(id, writablePowerOutletTemplate);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DcimApi#dcimPowerOutletTemplatesUpdate");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **Integer**| A unique integer value identifying this power outlet template. | |
| **writablePowerOutletTemplate** | [**WritablePowerOutletTemplate**](WritablePowerOutletTemplate.md)|  | |

### Return type

[**PowerOutletTemplate**](PowerOutletTemplate.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="dcimPowerOutletsCreate"></a>
# **dcimPowerOutletsCreate**
> PowerOutlet dcimPowerOutletsCreate(writablePowerOutlet)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DcimApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    DcimApi apiInstance = new DcimApi(defaultClient);
    WritablePowerOutlet writablePowerOutlet = new WritablePowerOutlet(); // WritablePowerOutlet | 
    try {
      PowerOutlet result = apiInstance.dcimPowerOutletsCreate(writablePowerOutlet);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DcimApi#dcimPowerOutletsCreate");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **writablePowerOutlet** | [**WritablePowerOutlet**](WritablePowerOutlet.md)|  | |

### Return type

[**PowerOutlet**](PowerOutlet.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** |  |  -  |

<a id="dcimPowerOutletsDelete"></a>
# **dcimPowerOutletsDelete**
> dcimPowerOutletsDelete(id)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DcimApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    DcimApi apiInstance = new DcimApi(defaultClient);
    Integer id = 56; // Integer | A unique integer value identifying this power outlet.
    try {
      apiInstance.dcimPowerOutletsDelete(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling DcimApi#dcimPowerOutletsDelete");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **Integer**| A unique integer value identifying this power outlet. | |

### Return type

null (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** |  |  -  |

<a id="dcimPowerOutletsList"></a>
# **dcimPowerOutletsList**
> DcimPowerOutletsList200Response dcimPowerOutletsList(name, deviceId, device, tag, limit, offset)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DcimApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    DcimApi apiInstance = new DcimApi(defaultClient);
    String name = "name_example"; // String | 
    String deviceId = "deviceId_example"; // String | 
    String device = "device_example"; // String | 
    String tag = "tag_example"; // String | 
    Integer limit = 56; // Integer | Number of results to return per page.
    Integer offset = 56; // Integer | The initial index from which to return the results.
    try {
      DcimPowerOutletsList200Response result = apiInstance.dcimPowerOutletsList(name, deviceId, device, tag, limit, offset);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DcimApi#dcimPowerOutletsList");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **name** | **String**|  | [optional] |
| **deviceId** | **String**|  | [optional] |
| **device** | **String**|  | [optional] |
| **tag** | **String**|  | [optional] |
| **limit** | **Integer**| Number of results to return per page. | [optional] |
| **offset** | **Integer**| The initial index from which to return the results. | [optional] |

### Return type

[**DcimPowerOutletsList200Response**](DcimPowerOutletsList200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="dcimPowerOutletsPartialUpdate"></a>
# **dcimPowerOutletsPartialUpdate**
> PowerOutlet dcimPowerOutletsPartialUpdate(id, writablePowerOutlet)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DcimApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    DcimApi apiInstance = new DcimApi(defaultClient);
    Integer id = 56; // Integer | A unique integer value identifying this power outlet.
    WritablePowerOutlet writablePowerOutlet = new WritablePowerOutlet(); // WritablePowerOutlet | 
    try {
      PowerOutlet result = apiInstance.dcimPowerOutletsPartialUpdate(id, writablePowerOutlet);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DcimApi#dcimPowerOutletsPartialUpdate");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **Integer**| A unique integer value identifying this power outlet. | |
| **writablePowerOutlet** | [**WritablePowerOutlet**](WritablePowerOutlet.md)|  | |

### Return type

[**PowerOutlet**](PowerOutlet.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="dcimPowerOutletsRead"></a>
# **dcimPowerOutletsRead**
> PowerOutlet dcimPowerOutletsRead(id)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DcimApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    DcimApi apiInstance = new DcimApi(defaultClient);
    Integer id = 56; // Integer | A unique integer value identifying this power outlet.
    try {
      PowerOutlet result = apiInstance.dcimPowerOutletsRead(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DcimApi#dcimPowerOutletsRead");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **Integer**| A unique integer value identifying this power outlet. | |

### Return type

[**PowerOutlet**](PowerOutlet.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="dcimPowerOutletsUpdate"></a>
# **dcimPowerOutletsUpdate**
> PowerOutlet dcimPowerOutletsUpdate(id, writablePowerOutlet)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DcimApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    DcimApi apiInstance = new DcimApi(defaultClient);
    Integer id = 56; // Integer | A unique integer value identifying this power outlet.
    WritablePowerOutlet writablePowerOutlet = new WritablePowerOutlet(); // WritablePowerOutlet | 
    try {
      PowerOutlet result = apiInstance.dcimPowerOutletsUpdate(id, writablePowerOutlet);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DcimApi#dcimPowerOutletsUpdate");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **Integer**| A unique integer value identifying this power outlet. | |
| **writablePowerOutlet** | [**WritablePowerOutlet**](WritablePowerOutlet.md)|  | |

### Return type

[**PowerOutlet**](PowerOutlet.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="dcimPowerPortTemplatesCreate"></a>
# **dcimPowerPortTemplatesCreate**
> PowerPortTemplate dcimPowerPortTemplatesCreate(writablePowerPortTemplate)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DcimApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    DcimApi apiInstance = new DcimApi(defaultClient);
    WritablePowerPortTemplate writablePowerPortTemplate = new WritablePowerPortTemplate(); // WritablePowerPortTemplate | 
    try {
      PowerPortTemplate result = apiInstance.dcimPowerPortTemplatesCreate(writablePowerPortTemplate);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DcimApi#dcimPowerPortTemplatesCreate");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **writablePowerPortTemplate** | [**WritablePowerPortTemplate**](WritablePowerPortTemplate.md)|  | |

### Return type

[**PowerPortTemplate**](PowerPortTemplate.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** |  |  -  |

<a id="dcimPowerPortTemplatesDelete"></a>
# **dcimPowerPortTemplatesDelete**
> dcimPowerPortTemplatesDelete(id)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DcimApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    DcimApi apiInstance = new DcimApi(defaultClient);
    Integer id = 56; // Integer | A unique integer value identifying this power port template.
    try {
      apiInstance.dcimPowerPortTemplatesDelete(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling DcimApi#dcimPowerPortTemplatesDelete");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **Integer**| A unique integer value identifying this power port template. | |

### Return type

null (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** |  |  -  |

<a id="dcimPowerPortTemplatesList"></a>
# **dcimPowerPortTemplatesList**
> DcimPowerPortTemplatesList200Response dcimPowerPortTemplatesList(name, devicetypeId, limit, offset)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DcimApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    DcimApi apiInstance = new DcimApi(defaultClient);
    String name = "name_example"; // String | 
    String devicetypeId = "devicetypeId_example"; // String | 
    Integer limit = 56; // Integer | Number of results to return per page.
    Integer offset = 56; // Integer | The initial index from which to return the results.
    try {
      DcimPowerPortTemplatesList200Response result = apiInstance.dcimPowerPortTemplatesList(name, devicetypeId, limit, offset);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DcimApi#dcimPowerPortTemplatesList");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **name** | **String**|  | [optional] |
| **devicetypeId** | **String**|  | [optional] |
| **limit** | **Integer**| Number of results to return per page. | [optional] |
| **offset** | **Integer**| The initial index from which to return the results. | [optional] |

### Return type

[**DcimPowerPortTemplatesList200Response**](DcimPowerPortTemplatesList200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="dcimPowerPortTemplatesPartialUpdate"></a>
# **dcimPowerPortTemplatesPartialUpdate**
> PowerPortTemplate dcimPowerPortTemplatesPartialUpdate(id, writablePowerPortTemplate)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DcimApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    DcimApi apiInstance = new DcimApi(defaultClient);
    Integer id = 56; // Integer | A unique integer value identifying this power port template.
    WritablePowerPortTemplate writablePowerPortTemplate = new WritablePowerPortTemplate(); // WritablePowerPortTemplate | 
    try {
      PowerPortTemplate result = apiInstance.dcimPowerPortTemplatesPartialUpdate(id, writablePowerPortTemplate);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DcimApi#dcimPowerPortTemplatesPartialUpdate");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **Integer**| A unique integer value identifying this power port template. | |
| **writablePowerPortTemplate** | [**WritablePowerPortTemplate**](WritablePowerPortTemplate.md)|  | |

### Return type

[**PowerPortTemplate**](PowerPortTemplate.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="dcimPowerPortTemplatesRead"></a>
# **dcimPowerPortTemplatesRead**
> PowerPortTemplate dcimPowerPortTemplatesRead(id)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DcimApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    DcimApi apiInstance = new DcimApi(defaultClient);
    Integer id = 56; // Integer | A unique integer value identifying this power port template.
    try {
      PowerPortTemplate result = apiInstance.dcimPowerPortTemplatesRead(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DcimApi#dcimPowerPortTemplatesRead");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **Integer**| A unique integer value identifying this power port template. | |

### Return type

[**PowerPortTemplate**](PowerPortTemplate.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="dcimPowerPortTemplatesUpdate"></a>
# **dcimPowerPortTemplatesUpdate**
> PowerPortTemplate dcimPowerPortTemplatesUpdate(id, writablePowerPortTemplate)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DcimApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    DcimApi apiInstance = new DcimApi(defaultClient);
    Integer id = 56; // Integer | A unique integer value identifying this power port template.
    WritablePowerPortTemplate writablePowerPortTemplate = new WritablePowerPortTemplate(); // WritablePowerPortTemplate | 
    try {
      PowerPortTemplate result = apiInstance.dcimPowerPortTemplatesUpdate(id, writablePowerPortTemplate);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DcimApi#dcimPowerPortTemplatesUpdate");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **Integer**| A unique integer value identifying this power port template. | |
| **writablePowerPortTemplate** | [**WritablePowerPortTemplate**](WritablePowerPortTemplate.md)|  | |

### Return type

[**PowerPortTemplate**](PowerPortTemplate.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="dcimPowerPortsCreate"></a>
# **dcimPowerPortsCreate**
> PowerPort dcimPowerPortsCreate(writablePowerPort)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DcimApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    DcimApi apiInstance = new DcimApi(defaultClient);
    WritablePowerPort writablePowerPort = new WritablePowerPort(); // WritablePowerPort | 
    try {
      PowerPort result = apiInstance.dcimPowerPortsCreate(writablePowerPort);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DcimApi#dcimPowerPortsCreate");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **writablePowerPort** | [**WritablePowerPort**](WritablePowerPort.md)|  | |

### Return type

[**PowerPort**](PowerPort.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** |  |  -  |

<a id="dcimPowerPortsDelete"></a>
# **dcimPowerPortsDelete**
> dcimPowerPortsDelete(id)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DcimApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    DcimApi apiInstance = new DcimApi(defaultClient);
    Integer id = 56; // Integer | A unique integer value identifying this power port.
    try {
      apiInstance.dcimPowerPortsDelete(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling DcimApi#dcimPowerPortsDelete");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **Integer**| A unique integer value identifying this power port. | |

### Return type

null (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** |  |  -  |

<a id="dcimPowerPortsList"></a>
# **dcimPowerPortsList**
> DcimPowerConnectionsList200Response dcimPowerPortsList(name, deviceId, device, tag, limit, offset)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DcimApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    DcimApi apiInstance = new DcimApi(defaultClient);
    String name = "name_example"; // String | 
    String deviceId = "deviceId_example"; // String | 
    String device = "device_example"; // String | 
    String tag = "tag_example"; // String | 
    Integer limit = 56; // Integer | Number of results to return per page.
    Integer offset = 56; // Integer | The initial index from which to return the results.
    try {
      DcimPowerConnectionsList200Response result = apiInstance.dcimPowerPortsList(name, deviceId, device, tag, limit, offset);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DcimApi#dcimPowerPortsList");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **name** | **String**|  | [optional] |
| **deviceId** | **String**|  | [optional] |
| **device** | **String**|  | [optional] |
| **tag** | **String**|  | [optional] |
| **limit** | **Integer**| Number of results to return per page. | [optional] |
| **offset** | **Integer**| The initial index from which to return the results. | [optional] |

### Return type

[**DcimPowerConnectionsList200Response**](DcimPowerConnectionsList200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="dcimPowerPortsPartialUpdate"></a>
# **dcimPowerPortsPartialUpdate**
> PowerPort dcimPowerPortsPartialUpdate(id, writablePowerPort)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DcimApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    DcimApi apiInstance = new DcimApi(defaultClient);
    Integer id = 56; // Integer | A unique integer value identifying this power port.
    WritablePowerPort writablePowerPort = new WritablePowerPort(); // WritablePowerPort | 
    try {
      PowerPort result = apiInstance.dcimPowerPortsPartialUpdate(id, writablePowerPort);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DcimApi#dcimPowerPortsPartialUpdate");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **Integer**| A unique integer value identifying this power port. | |
| **writablePowerPort** | [**WritablePowerPort**](WritablePowerPort.md)|  | |

### Return type

[**PowerPort**](PowerPort.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="dcimPowerPortsRead"></a>
# **dcimPowerPortsRead**
> PowerPort dcimPowerPortsRead(id)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DcimApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    DcimApi apiInstance = new DcimApi(defaultClient);
    Integer id = 56; // Integer | A unique integer value identifying this power port.
    try {
      PowerPort result = apiInstance.dcimPowerPortsRead(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DcimApi#dcimPowerPortsRead");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **Integer**| A unique integer value identifying this power port. | |

### Return type

[**PowerPort**](PowerPort.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="dcimPowerPortsUpdate"></a>
# **dcimPowerPortsUpdate**
> PowerPort dcimPowerPortsUpdate(id, writablePowerPort)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DcimApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    DcimApi apiInstance = new DcimApi(defaultClient);
    Integer id = 56; // Integer | A unique integer value identifying this power port.
    WritablePowerPort writablePowerPort = new WritablePowerPort(); // WritablePowerPort | 
    try {
      PowerPort result = apiInstance.dcimPowerPortsUpdate(id, writablePowerPort);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DcimApi#dcimPowerPortsUpdate");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **Integer**| A unique integer value identifying this power port. | |
| **writablePowerPort** | [**WritablePowerPort**](WritablePowerPort.md)|  | |

### Return type

[**PowerPort**](PowerPort.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="dcimRackGroupsCreate"></a>
# **dcimRackGroupsCreate**
> RackGroup dcimRackGroupsCreate(writableRackGroup)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DcimApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    DcimApi apiInstance = new DcimApi(defaultClient);
    WritableRackGroup writableRackGroup = new WritableRackGroup(); // WritableRackGroup | 
    try {
      RackGroup result = apiInstance.dcimRackGroupsCreate(writableRackGroup);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DcimApi#dcimRackGroupsCreate");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **writableRackGroup** | [**WritableRackGroup**](WritableRackGroup.md)|  | |

### Return type

[**RackGroup**](RackGroup.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** |  |  -  |

<a id="dcimRackGroupsDelete"></a>
# **dcimRackGroupsDelete**
> dcimRackGroupsDelete(id)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DcimApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    DcimApi apiInstance = new DcimApi(defaultClient);
    Integer id = 56; // Integer | A unique integer value identifying this rack group.
    try {
      apiInstance.dcimRackGroupsDelete(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling DcimApi#dcimRackGroupsDelete");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **Integer**| A unique integer value identifying this rack group. | |

### Return type

null (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** |  |  -  |

<a id="dcimRackGroupsList"></a>
# **dcimRackGroupsList**
> DcimRackGroupsList200Response dcimRackGroupsList(siteId, name, slug, q, site, limit, offset)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DcimApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    DcimApi apiInstance = new DcimApi(defaultClient);
    String siteId = "siteId_example"; // String | 
    String name = "name_example"; // String | 
    String slug = "slug_example"; // String | 
    String q = "q_example"; // String | 
    String site = "site_example"; // String | 
    Integer limit = 56; // Integer | Number of results to return per page.
    Integer offset = 56; // Integer | The initial index from which to return the results.
    try {
      DcimRackGroupsList200Response result = apiInstance.dcimRackGroupsList(siteId, name, slug, q, site, limit, offset);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DcimApi#dcimRackGroupsList");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **siteId** | **String**|  | [optional] |
| **name** | **String**|  | [optional] |
| **slug** | **String**|  | [optional] |
| **q** | **String**|  | [optional] |
| **site** | **String**|  | [optional] |
| **limit** | **Integer**| Number of results to return per page. | [optional] |
| **offset** | **Integer**| The initial index from which to return the results. | [optional] |

### Return type

[**DcimRackGroupsList200Response**](DcimRackGroupsList200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="dcimRackGroupsPartialUpdate"></a>
# **dcimRackGroupsPartialUpdate**
> RackGroup dcimRackGroupsPartialUpdate(id, writableRackGroup)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DcimApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    DcimApi apiInstance = new DcimApi(defaultClient);
    Integer id = 56; // Integer | A unique integer value identifying this rack group.
    WritableRackGroup writableRackGroup = new WritableRackGroup(); // WritableRackGroup | 
    try {
      RackGroup result = apiInstance.dcimRackGroupsPartialUpdate(id, writableRackGroup);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DcimApi#dcimRackGroupsPartialUpdate");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **Integer**| A unique integer value identifying this rack group. | |
| **writableRackGroup** | [**WritableRackGroup**](WritableRackGroup.md)|  | |

### Return type

[**RackGroup**](RackGroup.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="dcimRackGroupsRead"></a>
# **dcimRackGroupsRead**
> RackGroup dcimRackGroupsRead(id)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DcimApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    DcimApi apiInstance = new DcimApi(defaultClient);
    Integer id = 56; // Integer | A unique integer value identifying this rack group.
    try {
      RackGroup result = apiInstance.dcimRackGroupsRead(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DcimApi#dcimRackGroupsRead");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **Integer**| A unique integer value identifying this rack group. | |

### Return type

[**RackGroup**](RackGroup.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="dcimRackGroupsUpdate"></a>
# **dcimRackGroupsUpdate**
> RackGroup dcimRackGroupsUpdate(id, writableRackGroup)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DcimApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    DcimApi apiInstance = new DcimApi(defaultClient);
    Integer id = 56; // Integer | A unique integer value identifying this rack group.
    WritableRackGroup writableRackGroup = new WritableRackGroup(); // WritableRackGroup | 
    try {
      RackGroup result = apiInstance.dcimRackGroupsUpdate(id, writableRackGroup);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DcimApi#dcimRackGroupsUpdate");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **Integer**| A unique integer value identifying this rack group. | |
| **writableRackGroup** | [**WritableRackGroup**](WritableRackGroup.md)|  | |

### Return type

[**RackGroup**](RackGroup.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="dcimRackReservationsCreate"></a>
# **dcimRackReservationsCreate**
> RackReservation dcimRackReservationsCreate(writableRackReservation)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DcimApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    DcimApi apiInstance = new DcimApi(defaultClient);
    WritableRackReservation writableRackReservation = new WritableRackReservation(); // WritableRackReservation | 
    try {
      RackReservation result = apiInstance.dcimRackReservationsCreate(writableRackReservation);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DcimApi#dcimRackReservationsCreate");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **writableRackReservation** | [**WritableRackReservation**](WritableRackReservation.md)|  | |

### Return type

[**RackReservation**](RackReservation.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** |  |  -  |

<a id="dcimRackReservationsDelete"></a>
# **dcimRackReservationsDelete**
> dcimRackReservationsDelete(id)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DcimApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    DcimApi apiInstance = new DcimApi(defaultClient);
    Integer id = 56; // Integer | A unique integer value identifying this rack reservation.
    try {
      apiInstance.dcimRackReservationsDelete(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling DcimApi#dcimRackReservationsDelete");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **Integer**| A unique integer value identifying this rack reservation. | |

### Return type

null (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** |  |  -  |

<a id="dcimRackReservationsList"></a>
# **dcimRackReservationsList**
> DcimRackReservationsList200Response dcimRackReservationsList(created, idIn, q, rackId, siteId, site, groupId, group, tenantId, tenant, userId, user, limit, offset)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DcimApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    DcimApi apiInstance = new DcimApi(defaultClient);
    String created = "created_example"; // String | 
    String idIn = "idIn_example"; // String | Multiple values may be separated by commas.
    String q = "q_example"; // String | 
    String rackId = "rackId_example"; // String | 
    String siteId = "siteId_example"; // String | 
    String site = "site_example"; // String | 
    String groupId = "groupId_example"; // String | 
    String group = "group_example"; // String | 
    String tenantId = "tenantId_example"; // String | 
    String tenant = "tenant_example"; // String | 
    String userId = "userId_example"; // String | 
    String user = "user_example"; // String | 
    Integer limit = 56; // Integer | Number of results to return per page.
    Integer offset = 56; // Integer | The initial index from which to return the results.
    try {
      DcimRackReservationsList200Response result = apiInstance.dcimRackReservationsList(created, idIn, q, rackId, siteId, site, groupId, group, tenantId, tenant, userId, user, limit, offset);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DcimApi#dcimRackReservationsList");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **created** | **String**|  | [optional] |
| **idIn** | **String**| Multiple values may be separated by commas. | [optional] |
| **q** | **String**|  | [optional] |
| **rackId** | **String**|  | [optional] |
| **siteId** | **String**|  | [optional] |
| **site** | **String**|  | [optional] |
| **groupId** | **String**|  | [optional] |
| **group** | **String**|  | [optional] |
| **tenantId** | **String**|  | [optional] |
| **tenant** | **String**|  | [optional] |
| **userId** | **String**|  | [optional] |
| **user** | **String**|  | [optional] |
| **limit** | **Integer**| Number of results to return per page. | [optional] |
| **offset** | **Integer**| The initial index from which to return the results. | [optional] |

### Return type

[**DcimRackReservationsList200Response**](DcimRackReservationsList200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="dcimRackReservationsPartialUpdate"></a>
# **dcimRackReservationsPartialUpdate**
> RackReservation dcimRackReservationsPartialUpdate(id, writableRackReservation)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DcimApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    DcimApi apiInstance = new DcimApi(defaultClient);
    Integer id = 56; // Integer | A unique integer value identifying this rack reservation.
    WritableRackReservation writableRackReservation = new WritableRackReservation(); // WritableRackReservation | 
    try {
      RackReservation result = apiInstance.dcimRackReservationsPartialUpdate(id, writableRackReservation);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DcimApi#dcimRackReservationsPartialUpdate");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **Integer**| A unique integer value identifying this rack reservation. | |
| **writableRackReservation** | [**WritableRackReservation**](WritableRackReservation.md)|  | |

### Return type

[**RackReservation**](RackReservation.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="dcimRackReservationsRead"></a>
# **dcimRackReservationsRead**
> RackReservation dcimRackReservationsRead(id)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DcimApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    DcimApi apiInstance = new DcimApi(defaultClient);
    Integer id = 56; // Integer | A unique integer value identifying this rack reservation.
    try {
      RackReservation result = apiInstance.dcimRackReservationsRead(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DcimApi#dcimRackReservationsRead");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **Integer**| A unique integer value identifying this rack reservation. | |

### Return type

[**RackReservation**](RackReservation.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="dcimRackReservationsUpdate"></a>
# **dcimRackReservationsUpdate**
> RackReservation dcimRackReservationsUpdate(id, writableRackReservation)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DcimApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    DcimApi apiInstance = new DcimApi(defaultClient);
    Integer id = 56; // Integer | A unique integer value identifying this rack reservation.
    WritableRackReservation writableRackReservation = new WritableRackReservation(); // WritableRackReservation | 
    try {
      RackReservation result = apiInstance.dcimRackReservationsUpdate(id, writableRackReservation);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DcimApi#dcimRackReservationsUpdate");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **Integer**| A unique integer value identifying this rack reservation. | |
| **writableRackReservation** | [**WritableRackReservation**](WritableRackReservation.md)|  | |

### Return type

[**RackReservation**](RackReservation.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="dcimRackRolesCreate"></a>
# **dcimRackRolesCreate**
> RackRole dcimRackRolesCreate(rackRole)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DcimApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    DcimApi apiInstance = new DcimApi(defaultClient);
    RackRole rackRole = new RackRole(); // RackRole | 
    try {
      RackRole result = apiInstance.dcimRackRolesCreate(rackRole);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DcimApi#dcimRackRolesCreate");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **rackRole** | [**RackRole**](RackRole.md)|  | |

### Return type

[**RackRole**](RackRole.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** |  |  -  |

<a id="dcimRackRolesDelete"></a>
# **dcimRackRolesDelete**
> dcimRackRolesDelete(id)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DcimApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    DcimApi apiInstance = new DcimApi(defaultClient);
    Integer id = 56; // Integer | A unique integer value identifying this rack role.
    try {
      apiInstance.dcimRackRolesDelete(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling DcimApi#dcimRackRolesDelete");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **Integer**| A unique integer value identifying this rack role. | |

### Return type

null (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** |  |  -  |

<a id="dcimRackRolesList"></a>
# **dcimRackRolesList**
> DcimRackRolesList200Response dcimRackRolesList(name, slug, color, limit, offset)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DcimApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    DcimApi apiInstance = new DcimApi(defaultClient);
    String name = "name_example"; // String | 
    String slug = "slug_example"; // String | 
    String color = "color_example"; // String | 
    Integer limit = 56; // Integer | Number of results to return per page.
    Integer offset = 56; // Integer | The initial index from which to return the results.
    try {
      DcimRackRolesList200Response result = apiInstance.dcimRackRolesList(name, slug, color, limit, offset);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DcimApi#dcimRackRolesList");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **name** | **String**|  | [optional] |
| **slug** | **String**|  | [optional] |
| **color** | **String**|  | [optional] |
| **limit** | **Integer**| Number of results to return per page. | [optional] |
| **offset** | **Integer**| The initial index from which to return the results. | [optional] |

### Return type

[**DcimRackRolesList200Response**](DcimRackRolesList200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="dcimRackRolesPartialUpdate"></a>
# **dcimRackRolesPartialUpdate**
> RackRole dcimRackRolesPartialUpdate(id, rackRole)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DcimApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    DcimApi apiInstance = new DcimApi(defaultClient);
    Integer id = 56; // Integer | A unique integer value identifying this rack role.
    RackRole rackRole = new RackRole(); // RackRole | 
    try {
      RackRole result = apiInstance.dcimRackRolesPartialUpdate(id, rackRole);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DcimApi#dcimRackRolesPartialUpdate");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **Integer**| A unique integer value identifying this rack role. | |
| **rackRole** | [**RackRole**](RackRole.md)|  | |

### Return type

[**RackRole**](RackRole.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="dcimRackRolesRead"></a>
# **dcimRackRolesRead**
> RackRole dcimRackRolesRead(id)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DcimApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    DcimApi apiInstance = new DcimApi(defaultClient);
    Integer id = 56; // Integer | A unique integer value identifying this rack role.
    try {
      RackRole result = apiInstance.dcimRackRolesRead(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DcimApi#dcimRackRolesRead");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **Integer**| A unique integer value identifying this rack role. | |

### Return type

[**RackRole**](RackRole.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="dcimRackRolesUpdate"></a>
# **dcimRackRolesUpdate**
> RackRole dcimRackRolesUpdate(id, rackRole)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DcimApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    DcimApi apiInstance = new DcimApi(defaultClient);
    Integer id = 56; // Integer | A unique integer value identifying this rack role.
    RackRole rackRole = new RackRole(); // RackRole | 
    try {
      RackRole result = apiInstance.dcimRackRolesUpdate(id, rackRole);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DcimApi#dcimRackRolesUpdate");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **Integer**| A unique integer value identifying this rack role. | |
| **rackRole** | [**RackRole**](RackRole.md)|  | |

### Return type

[**RackRole**](RackRole.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="dcimRacksCreate"></a>
# **dcimRacksCreate**
> Rack dcimRacksCreate(writableRack)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DcimApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    DcimApi apiInstance = new DcimApi(defaultClient);
    WritableRack writableRack = new WritableRack(); // WritableRack | 
    try {
      Rack result = apiInstance.dcimRacksCreate(writableRack);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DcimApi#dcimRacksCreate");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **writableRack** | [**WritableRack**](WritableRack.md)|  | |

### Return type

[**Rack**](Rack.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** |  |  -  |

<a id="dcimRacksDelete"></a>
# **dcimRacksDelete**
> dcimRacksDelete(id)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DcimApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    DcimApi apiInstance = new DcimApi(defaultClient);
    Integer id = 56; // Integer | A unique integer value identifying this rack.
    try {
      apiInstance.dcimRacksDelete(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling DcimApi#dcimRacksDelete");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **Integer**| A unique integer value identifying this rack. | |

### Return type

null (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** |  |  -  |

<a id="dcimRacksList"></a>
# **dcimRacksList**
> DcimRacksList200Response dcimRacksList(name, serial, type, width, uHeight, descUnits, idIn, q, facilityId, siteId, site, groupId, group, tenantId, tenant, roleId, role, tag, limit, offset)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DcimApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    DcimApi apiInstance = new DcimApi(defaultClient);
    String name = "name_example"; // String | 
    String serial = "serial_example"; // String | 
    String type = "type_example"; // String | 
    String width = "width_example"; // String | 
    BigDecimal uHeight = new BigDecimal(78); // BigDecimal | 
    String descUnits = "descUnits_example"; // String | 
    String idIn = "idIn_example"; // String | Multiple values may be separated by commas.
    String q = "q_example"; // String | 
    String facilityId = "facilityId_example"; // String | 
    String siteId = "siteId_example"; // String | 
    String site = "site_example"; // String | 
    String groupId = "groupId_example"; // String | 
    String group = "group_example"; // String | 
    String tenantId = "tenantId_example"; // String | 
    String tenant = "tenant_example"; // String | 
    String roleId = "roleId_example"; // String | 
    String role = "role_example"; // String | 
    String tag = "tag_example"; // String | 
    Integer limit = 56; // Integer | Number of results to return per page.
    Integer offset = 56; // Integer | The initial index from which to return the results.
    try {
      DcimRacksList200Response result = apiInstance.dcimRacksList(name, serial, type, width, uHeight, descUnits, idIn, q, facilityId, siteId, site, groupId, group, tenantId, tenant, roleId, role, tag, limit, offset);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DcimApi#dcimRacksList");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **name** | **String**|  | [optional] |
| **serial** | **String**|  | [optional] |
| **type** | **String**|  | [optional] |
| **width** | **String**|  | [optional] |
| **uHeight** | **BigDecimal**|  | [optional] |
| **descUnits** | **String**|  | [optional] |
| **idIn** | **String**| Multiple values may be separated by commas. | [optional] |
| **q** | **String**|  | [optional] |
| **facilityId** | **String**|  | [optional] |
| **siteId** | **String**|  | [optional] |
| **site** | **String**|  | [optional] |
| **groupId** | **String**|  | [optional] |
| **group** | **String**|  | [optional] |
| **tenantId** | **String**|  | [optional] |
| **tenant** | **String**|  | [optional] |
| **roleId** | **String**|  | [optional] |
| **role** | **String**|  | [optional] |
| **tag** | **String**|  | [optional] |
| **limit** | **Integer**| Number of results to return per page. | [optional] |
| **offset** | **Integer**| The initial index from which to return the results. | [optional] |

### Return type

[**DcimRacksList200Response**](DcimRacksList200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="dcimRacksPartialUpdate"></a>
# **dcimRacksPartialUpdate**
> Rack dcimRacksPartialUpdate(id, writableRack)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DcimApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    DcimApi apiInstance = new DcimApi(defaultClient);
    Integer id = 56; // Integer | A unique integer value identifying this rack.
    WritableRack writableRack = new WritableRack(); // WritableRack | 
    try {
      Rack result = apiInstance.dcimRacksPartialUpdate(id, writableRack);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DcimApi#dcimRacksPartialUpdate");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **Integer**| A unique integer value identifying this rack. | |
| **writableRack** | [**WritableRack**](WritableRack.md)|  | |

### Return type

[**Rack**](Rack.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="dcimRacksRead"></a>
# **dcimRacksRead**
> Rack dcimRacksRead(id)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DcimApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    DcimApi apiInstance = new DcimApi(defaultClient);
    Integer id = 56; // Integer | A unique integer value identifying this rack.
    try {
      Rack result = apiInstance.dcimRacksRead(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DcimApi#dcimRacksRead");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **Integer**| A unique integer value identifying this rack. | |

### Return type

[**Rack**](Rack.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="dcimRacksUnits"></a>
# **dcimRacksUnits**
> Rack dcimRacksUnits(id)



List rack units (by rack)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DcimApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    DcimApi apiInstance = new DcimApi(defaultClient);
    Integer id = 56; // Integer | A unique integer value identifying this rack.
    try {
      Rack result = apiInstance.dcimRacksUnits(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DcimApi#dcimRacksUnits");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **Integer**| A unique integer value identifying this rack. | |

### Return type

[**Rack**](Rack.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="dcimRacksUpdate"></a>
# **dcimRacksUpdate**
> Rack dcimRacksUpdate(id, writableRack)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DcimApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    DcimApi apiInstance = new DcimApi(defaultClient);
    Integer id = 56; // Integer | A unique integer value identifying this rack.
    WritableRack writableRack = new WritableRack(); // WritableRack | 
    try {
      Rack result = apiInstance.dcimRacksUpdate(id, writableRack);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DcimApi#dcimRacksUpdate");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **Integer**| A unique integer value identifying this rack. | |
| **writableRack** | [**WritableRack**](WritableRack.md)|  | |

### Return type

[**Rack**](Rack.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="dcimRegionsCreate"></a>
# **dcimRegionsCreate**
> Region dcimRegionsCreate(writableRegion)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DcimApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    DcimApi apiInstance = new DcimApi(defaultClient);
    WritableRegion writableRegion = new WritableRegion(); // WritableRegion | 
    try {
      Region result = apiInstance.dcimRegionsCreate(writableRegion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DcimApi#dcimRegionsCreate");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **writableRegion** | [**WritableRegion**](WritableRegion.md)|  | |

### Return type

[**Region**](Region.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** |  |  -  |

<a id="dcimRegionsDelete"></a>
# **dcimRegionsDelete**
> dcimRegionsDelete(id)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DcimApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    DcimApi apiInstance = new DcimApi(defaultClient);
    Integer id = 56; // Integer | A unique integer value identifying this region.
    try {
      apiInstance.dcimRegionsDelete(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling DcimApi#dcimRegionsDelete");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **Integer**| A unique integer value identifying this region. | |

### Return type

null (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** |  |  -  |

<a id="dcimRegionsList"></a>
# **dcimRegionsList**
> DcimRegionsList200Response dcimRegionsList(name, slug, q, parentId, parent, limit, offset)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DcimApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    DcimApi apiInstance = new DcimApi(defaultClient);
    String name = "name_example"; // String | 
    String slug = "slug_example"; // String | 
    String q = "q_example"; // String | 
    String parentId = "parentId_example"; // String | 
    String parent = "parent_example"; // String | 
    Integer limit = 56; // Integer | Number of results to return per page.
    Integer offset = 56; // Integer | The initial index from which to return the results.
    try {
      DcimRegionsList200Response result = apiInstance.dcimRegionsList(name, slug, q, parentId, parent, limit, offset);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DcimApi#dcimRegionsList");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **name** | **String**|  | [optional] |
| **slug** | **String**|  | [optional] |
| **q** | **String**|  | [optional] |
| **parentId** | **String**|  | [optional] |
| **parent** | **String**|  | [optional] |
| **limit** | **Integer**| Number of results to return per page. | [optional] |
| **offset** | **Integer**| The initial index from which to return the results. | [optional] |

### Return type

[**DcimRegionsList200Response**](DcimRegionsList200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="dcimRegionsPartialUpdate"></a>
# **dcimRegionsPartialUpdate**
> Region dcimRegionsPartialUpdate(id, writableRegion)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DcimApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    DcimApi apiInstance = new DcimApi(defaultClient);
    Integer id = 56; // Integer | A unique integer value identifying this region.
    WritableRegion writableRegion = new WritableRegion(); // WritableRegion | 
    try {
      Region result = apiInstance.dcimRegionsPartialUpdate(id, writableRegion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DcimApi#dcimRegionsPartialUpdate");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **Integer**| A unique integer value identifying this region. | |
| **writableRegion** | [**WritableRegion**](WritableRegion.md)|  | |

### Return type

[**Region**](Region.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="dcimRegionsRead"></a>
# **dcimRegionsRead**
> Region dcimRegionsRead(id)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DcimApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    DcimApi apiInstance = new DcimApi(defaultClient);
    Integer id = 56; // Integer | A unique integer value identifying this region.
    try {
      Region result = apiInstance.dcimRegionsRead(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DcimApi#dcimRegionsRead");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **Integer**| A unique integer value identifying this region. | |

### Return type

[**Region**](Region.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="dcimRegionsUpdate"></a>
# **dcimRegionsUpdate**
> Region dcimRegionsUpdate(id, writableRegion)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DcimApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    DcimApi apiInstance = new DcimApi(defaultClient);
    Integer id = 56; // Integer | A unique integer value identifying this region.
    WritableRegion writableRegion = new WritableRegion(); // WritableRegion | 
    try {
      Region result = apiInstance.dcimRegionsUpdate(id, writableRegion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DcimApi#dcimRegionsUpdate");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **Integer**| A unique integer value identifying this region. | |
| **writableRegion** | [**WritableRegion**](WritableRegion.md)|  | |

### Return type

[**Region**](Region.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="dcimSitesCreate"></a>
# **dcimSitesCreate**
> Site dcimSitesCreate(writableSite)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DcimApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    DcimApi apiInstance = new DcimApi(defaultClient);
    WritableSite writableSite = new WritableSite(); // WritableSite | 
    try {
      Site result = apiInstance.dcimSitesCreate(writableSite);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DcimApi#dcimSitesCreate");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **writableSite** | [**WritableSite**](WritableSite.md)|  | |

### Return type

[**Site**](Site.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** |  |  -  |

<a id="dcimSitesDelete"></a>
# **dcimSitesDelete**
> dcimSitesDelete(id)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DcimApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    DcimApi apiInstance = new DcimApi(defaultClient);
    Integer id = 56; // Integer | A unique integer value identifying this site.
    try {
      apiInstance.dcimSitesDelete(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling DcimApi#dcimSitesDelete");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **Integer**| A unique integer value identifying this site. | |

### Return type

null (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** |  |  -  |

<a id="dcimSitesGraphs"></a>
# **dcimSitesGraphs**
> Site dcimSitesGraphs(id)



A convenience method for rendering graphs for a particular site.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DcimApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    DcimApi apiInstance = new DcimApi(defaultClient);
    Integer id = 56; // Integer | A unique integer value identifying this site.
    try {
      Site result = apiInstance.dcimSitesGraphs(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DcimApi#dcimSitesGraphs");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **Integer**| A unique integer value identifying this site. | |

### Return type

[**Site**](Site.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="dcimSitesList"></a>
# **dcimSitesList**
> DcimSitesList200Response dcimSitesList(q, name, slug, facility, asn, contactName, contactPhone, contactEmail, idIn, status, regionId, region, tenantId, tenant, tag, limit, offset)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DcimApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    DcimApi apiInstance = new DcimApi(defaultClient);
    String q = "q_example"; // String | 
    String name = "name_example"; // String | 
    String slug = "slug_example"; // String | 
    String facility = "facility_example"; // String | 
    BigDecimal asn = new BigDecimal(78); // BigDecimal | 
    String contactName = "contactName_example"; // String | 
    String contactPhone = "contactPhone_example"; // String | 
    String contactEmail = "contactEmail_example"; // String | 
    String idIn = "idIn_example"; // String | Multiple values may be separated by commas.
    String status = "status_example"; // String | 
    String regionId = "regionId_example"; // String | 
    String region = "region_example"; // String | 
    String tenantId = "tenantId_example"; // String | 
    String tenant = "tenant_example"; // String | 
    String tag = "tag_example"; // String | 
    Integer limit = 56; // Integer | Number of results to return per page.
    Integer offset = 56; // Integer | The initial index from which to return the results.
    try {
      DcimSitesList200Response result = apiInstance.dcimSitesList(q, name, slug, facility, asn, contactName, contactPhone, contactEmail, idIn, status, regionId, region, tenantId, tenant, tag, limit, offset);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DcimApi#dcimSitesList");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **q** | **String**|  | [optional] |
| **name** | **String**|  | [optional] |
| **slug** | **String**|  | [optional] |
| **facility** | **String**|  | [optional] |
| **asn** | **BigDecimal**|  | [optional] |
| **contactName** | **String**|  | [optional] |
| **contactPhone** | **String**|  | [optional] |
| **contactEmail** | **String**|  | [optional] |
| **idIn** | **String**| Multiple values may be separated by commas. | [optional] |
| **status** | **String**|  | [optional] |
| **regionId** | **String**|  | [optional] |
| **region** | **String**|  | [optional] |
| **tenantId** | **String**|  | [optional] |
| **tenant** | **String**|  | [optional] |
| **tag** | **String**|  | [optional] |
| **limit** | **Integer**| Number of results to return per page. | [optional] |
| **offset** | **Integer**| The initial index from which to return the results. | [optional] |

### Return type

[**DcimSitesList200Response**](DcimSitesList200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="dcimSitesPartialUpdate"></a>
# **dcimSitesPartialUpdate**
> Site dcimSitesPartialUpdate(id, writableSite)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DcimApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    DcimApi apiInstance = new DcimApi(defaultClient);
    Integer id = 56; // Integer | A unique integer value identifying this site.
    WritableSite writableSite = new WritableSite(); // WritableSite | 
    try {
      Site result = apiInstance.dcimSitesPartialUpdate(id, writableSite);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DcimApi#dcimSitesPartialUpdate");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **Integer**| A unique integer value identifying this site. | |
| **writableSite** | [**WritableSite**](WritableSite.md)|  | |

### Return type

[**Site**](Site.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="dcimSitesRead"></a>
# **dcimSitesRead**
> Site dcimSitesRead(id)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DcimApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    DcimApi apiInstance = new DcimApi(defaultClient);
    Integer id = 56; // Integer | A unique integer value identifying this site.
    try {
      Site result = apiInstance.dcimSitesRead(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DcimApi#dcimSitesRead");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **Integer**| A unique integer value identifying this site. | |

### Return type

[**Site**](Site.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="dcimSitesUpdate"></a>
# **dcimSitesUpdate**
> Site dcimSitesUpdate(id, writableSite)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DcimApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    DcimApi apiInstance = new DcimApi(defaultClient);
    Integer id = 56; // Integer | A unique integer value identifying this site.
    WritableSite writableSite = new WritableSite(); // WritableSite | 
    try {
      Site result = apiInstance.dcimSitesUpdate(id, writableSite);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DcimApi#dcimSitesUpdate");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **Integer**| A unique integer value identifying this site. | |
| **writableSite** | [**WritableSite**](WritableSite.md)|  | |

### Return type

[**Site**](Site.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="dcimVirtualChassisCreate"></a>
# **dcimVirtualChassisCreate**
> VirtualChassis dcimVirtualChassisCreate(writableVirtualChassis)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DcimApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    DcimApi apiInstance = new DcimApi(defaultClient);
    WritableVirtualChassis writableVirtualChassis = new WritableVirtualChassis(); // WritableVirtualChassis | 
    try {
      VirtualChassis result = apiInstance.dcimVirtualChassisCreate(writableVirtualChassis);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DcimApi#dcimVirtualChassisCreate");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **writableVirtualChassis** | [**WritableVirtualChassis**](WritableVirtualChassis.md)|  | |

### Return type

[**VirtualChassis**](VirtualChassis.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** |  |  -  |

<a id="dcimVirtualChassisDelete"></a>
# **dcimVirtualChassisDelete**
> dcimVirtualChassisDelete(id)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DcimApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    DcimApi apiInstance = new DcimApi(defaultClient);
    Integer id = 56; // Integer | A unique integer value identifying this virtual chassis.
    try {
      apiInstance.dcimVirtualChassisDelete(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling DcimApi#dcimVirtualChassisDelete");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **Integer**| A unique integer value identifying this virtual chassis. | |

### Return type

null (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** |  |  -  |

<a id="dcimVirtualChassisList"></a>
# **dcimVirtualChassisList**
> DcimVirtualChassisList200Response dcimVirtualChassisList(limit, offset)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DcimApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    DcimApi apiInstance = new DcimApi(defaultClient);
    Integer limit = 56; // Integer | Number of results to return per page.
    Integer offset = 56; // Integer | The initial index from which to return the results.
    try {
      DcimVirtualChassisList200Response result = apiInstance.dcimVirtualChassisList(limit, offset);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DcimApi#dcimVirtualChassisList");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **limit** | **Integer**| Number of results to return per page. | [optional] |
| **offset** | **Integer**| The initial index from which to return the results. | [optional] |

### Return type

[**DcimVirtualChassisList200Response**](DcimVirtualChassisList200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="dcimVirtualChassisPartialUpdate"></a>
# **dcimVirtualChassisPartialUpdate**
> VirtualChassis dcimVirtualChassisPartialUpdate(id, writableVirtualChassis)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DcimApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    DcimApi apiInstance = new DcimApi(defaultClient);
    Integer id = 56; // Integer | A unique integer value identifying this virtual chassis.
    WritableVirtualChassis writableVirtualChassis = new WritableVirtualChassis(); // WritableVirtualChassis | 
    try {
      VirtualChassis result = apiInstance.dcimVirtualChassisPartialUpdate(id, writableVirtualChassis);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DcimApi#dcimVirtualChassisPartialUpdate");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **Integer**| A unique integer value identifying this virtual chassis. | |
| **writableVirtualChassis** | [**WritableVirtualChassis**](WritableVirtualChassis.md)|  | |

### Return type

[**VirtualChassis**](VirtualChassis.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="dcimVirtualChassisRead"></a>
# **dcimVirtualChassisRead**
> VirtualChassis dcimVirtualChassisRead(id)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DcimApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    DcimApi apiInstance = new DcimApi(defaultClient);
    Integer id = 56; // Integer | A unique integer value identifying this virtual chassis.
    try {
      VirtualChassis result = apiInstance.dcimVirtualChassisRead(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DcimApi#dcimVirtualChassisRead");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **Integer**| A unique integer value identifying this virtual chassis. | |

### Return type

[**VirtualChassis**](VirtualChassis.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="dcimVirtualChassisUpdate"></a>
# **dcimVirtualChassisUpdate**
> VirtualChassis dcimVirtualChassisUpdate(id, writableVirtualChassis)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DcimApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    DcimApi apiInstance = new DcimApi(defaultClient);
    Integer id = 56; // Integer | A unique integer value identifying this virtual chassis.
    WritableVirtualChassis writableVirtualChassis = new WritableVirtualChassis(); // WritableVirtualChassis | 
    try {
      VirtualChassis result = apiInstance.dcimVirtualChassisUpdate(id, writableVirtualChassis);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DcimApi#dcimVirtualChassisUpdate");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **Integer**| A unique integer value identifying this virtual chassis. | |
| **writableVirtualChassis** | [**WritableVirtualChassis**](WritableVirtualChassis.md)|  | |

### Return type

[**VirtualChassis**](VirtualChassis.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

