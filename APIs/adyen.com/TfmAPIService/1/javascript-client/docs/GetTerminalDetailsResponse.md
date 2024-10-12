# PosTerminalManagementApi.GetTerminalDetailsResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bluetoothIp** | **String** | The Bluetooth IP address of the terminal. | [optional] 
**bluetoothMac** | **String** | The Bluetooth MAC address of the terminal. | [optional] 
**companyAccount** | **String** | The company account that the terminal is associated with. If this is the only account level shown in the response, the terminal is assigned to the inventory of the company account. | 
**country** | **String** | The country where the terminal is used. | [optional] 
**deviceModel** | **String** | The model name of the terminal. | [optional] 
**dhcpEnabled** | **Boolean** | Indicates whether assigning IP addresses through a DHCP server is enabled on the terminal. | [optional] 
**displayLabel** | **String** | The label shown on the status bar of the display. This label (if any) is specified in your Customer Area. | [optional] 
**ethernetIp** | **String** | The terminal&#39;s IP address in your Ethernet network. | [optional] 
**ethernetMac** | **String** | The terminal&#39;s MAC address in your Ethernet network. | [optional] 
**firmwareVersion** | **String** | The software release currently in use on the terminal. | [optional] 
**iccid** | **String** | The integrated circuit card identifier (ICCID) of the SIM card in the terminal. | [optional] 
**lastActivityDateTime** | **Date** | Date and time of the last activity on the terminal. Not included when the last activity was more than 14 days ago. | [optional] 
**lastTransactionDateTime** | **Date** | Date and time of the last transaction on the terminal. Not included when the last transaction was more than 14 days ago. | [optional] 
**linkNegotiation** | **String** | The Ethernet link negotiation that the terminal uses:   - &#x60;auto&#x60;: Auto-negotiation  - &#x60;100full&#x60;: 100 Mbps full duplex | [optional] 
**merchantAccount** | **String** | The merchant account that the terminal is associated with. If the response doesn&#39;t contain a &#x60;store&#x60; the terminal is assigned to this merchant account. | [optional] 
**merchantInventory** | **Boolean** | Boolean that indicates if the terminal is assigned to the merchant inventory. This is returned when the terminal is assigned to a merchant account.  - If **true**, this indicates that the terminal is in the merchant inventory. This also means that the terminal cannot be boarded.  - If **false**, this indicates that the terminal is assigned to the merchant account as an in-store terminal. This means that the terminal is ready to be boarded, or is already boarded. | [optional] 
**permanentTerminalId** | **String** | The permanent terminal ID. | [optional] 
**serialNumber** | **String** | The serial number of the terminal. | [optional] 
**simStatus** | **String** | On a terminal that supports 3G or 4G connectivity, indicates the status of the SIM card in the terminal: ACTIVE or INVENTORY. | [optional] 
**store** | **String** | The store code of the store that the terminal is assigned to. | [optional] 
**storeDetails** | [**Store**](Store.md) | The store that the terminal is assigned to. | [optional] 
**terminal** | **String** | The unique terminal ID. | 
**terminalStatus** | **String** | The status of the terminal:   - &#x60;OnlineToday&#x60;, &#x60;OnlineLast1Day&#x60;, &#x60;OnlineLast2Days&#x60; etcetera to &#x60;OnlineLast7Days&#x60;: Indicates when in the past week the terminal was last online.   - &#x60;SwitchedOff&#x60;: Indicates it was more than a week ago that the terminal was last online.   - &#x60;ReAssignToInventoryPending&#x60;, &#x60;ReAssignToStorePending&#x60;, &#x60;ReAssignToMerchantInventoryPending&#x60;: Indicates the terminal is scheduled to be reassigned. | [optional] 
**wifiIp** | **String** | The terminal&#39;s IP address in your Wi-Fi network. | [optional] 
**wifiMac** | **String** | The terminal&#39;s MAC address in your Wi-Fi network. | [optional] 



## Enum: TerminalStatusEnum


* `OnlineLast1Day` (value: `"OnlineLast1Day"`)

* `OnlineLast2Days` (value: `"OnlineLast2Days"`)

* `OnlineLast3Days` (value: `"OnlineLast3Days"`)

* `OnlineLast4Days` (value: `"OnlineLast4Days"`)

* `OnlineLast5Days` (value: `"OnlineLast5Days"`)

* `OnlineLast6Days` (value: `"OnlineLast6Days"`)

* `OnlineLast7Days` (value: `"OnlineLast7Days"`)

* `OnlineToday` (value: `"OnlineToday"`)

* `ReAssignToInventoryPending` (value: `"ReAssignToInventoryPending"`)

* `ReAssignToMerchantInventoryPending` (value: `"ReAssignToMerchantInventoryPending"`)

* `ReAssignToStorePending` (value: `"ReAssignToStorePending"`)

* `SwitchedOff` (value: `"SwitchedOff"`)




