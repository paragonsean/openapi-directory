

# IpPermission

A range of IP addresses and port settings that allow inbound traffic to connect to server processes on an instance in a fleet. New game sessions are assigned an IP address/port number combination, which must fall into the fleet's allowed ranges. Fleets with custom game builds must have permissions explicitly set. For Realtime Servers fleets, Amazon GameLift automatically opens two port ranges, one for TCP messaging and one for UDP.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**fromPort** | [**Integer**](Integer.md) |  |  |
|**toPort** | [**Integer**](Integer.md) |  |  |
|**ipRange** | [**String**](String.md) |  |  |
|**protocol** | [**IpProtocol**](IpProtocol.md) |  |  |



