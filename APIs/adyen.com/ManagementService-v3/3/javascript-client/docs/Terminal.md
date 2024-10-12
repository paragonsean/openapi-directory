# ManagementApi.Terminal

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assignment** | [**TerminalAssignment**](TerminalAssignment.md) | Indicates the account level to which the terminal is assigned, the [assignment status](https://docs.adyen.com/point-of-sale/automating-terminal-management/assign-terminals-api), and where the terminals is in the process of being reassigned to. | [optional] 
**connectivity** | [**TerminalConnectivity**](TerminalConnectivity.md) | Information about bluetooth, cellular, ethernet and wifi connectivity for the terminal. | [optional] 
**firmwareVersion** | **String** | The software release currently in use on the terminal. | [optional] 
**id** | **String** | The unique identifier of the terminal. | [optional] 
**lastActivityAt** | **Date** | Date and time of the last activity on the terminal. Not included when the last activity was more than 14 days ago. | [optional] 
**lastTransactionAt** | **Date** | Date and time of the last transaction on the terminal. Not included when the last transaction was more than 14 days ago. | [optional] 
**model** | **String** | The model name of the terminal. | [optional] 
**serialNumber** | **String** | The serial number of the terminal. | [optional] 


