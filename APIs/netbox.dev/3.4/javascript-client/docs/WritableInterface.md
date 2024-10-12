# NetBoxApi.WritableInterface

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**occupied** | **Boolean** |  | [optional] [readonly] 
**bridge** | **Number** |  | [optional] 
**cable** | [**NestedCable**](NestedCable.md) |  | [optional] 
**cableEnd** | **String** |  | [optional] [readonly] 
**connectedEndpoints** | **[String]** |  Return the appropriate serializer for the type of connected object.  | [optional] [readonly] 
**connectedEndpointsReachable** | **Boolean** |  | [optional] [readonly] 
**connectedEndpointsType** | **String** |  | [optional] [readonly] 
**countFhrpGroups** | **Number** |  | [optional] [readonly] 
**countIpaddresses** | **Number** |  | [optional] [readonly] 
**created** | **Date** |  | [optional] [readonly] 
**customFields** | **Object** |  | [optional] 
**description** | **String** |  | [optional] 
**device** | **Number** |  | 
**display** | **String** |  | [optional] [readonly] 
**duplex** | **String** |  | [optional] 
**enabled** | **Boolean** |  | [optional] 
**id** | **Number** |  | [optional] [readonly] 
**l2vpnTermination** | **String** |  | [optional] [readonly] 
**label** | **String** | Physical label | [optional] 
**lag** | **Number** |  | [optional] 
**lastUpdated** | **Date** |  | [optional] [readonly] 
**linkPeers** | **[String]** |  Return the appropriate serializer for the link termination model.  | [optional] [readonly] 
**linkPeersType** | **String** |  | [optional] [readonly] 
**macAddress** | **String** |  | [optional] 
**markConnected** | **Boolean** | Treat as if a cable is connected | [optional] 
**mgmtOnly** | **Boolean** | This interface is used only for out-of-band management | [optional] 
**mode** | **String** |  | [optional] 
**module** | **Number** |  | [optional] 
**mtu** | **Number** |  | [optional] 
**name** | **String** |  | 
**parent** | **Number** |  | [optional] 
**poeMode** | **String** |  | [optional] 
**poeType** | **String** |  | [optional] 
**rfChannel** | **String** |  | [optional] 
**rfChannelFrequency** | **Number** |  | [optional] 
**rfChannelWidth** | **Number** |  | [optional] 
**rfRole** | **String** |  | [optional] 
**speed** | **Number** |  | [optional] 
**taggedVlans** | **[Number]** |  | [optional] 
**tags** | [**[NestedTag]**](NestedTag.md) |  | [optional] 
**txPower** | **Number** |  | [optional] 
**type** | **String** |  | 
**untaggedVlan** | **Number** |  | [optional] 
**url** | **String** |  | [optional] [readonly] 
**vdcs** | **[Number]** |  | 
**vrf** | **Number** |  | [optional] 
**wirelessLans** | **[Number]** |  | [optional] 
**wirelessLink** | **Number** |  | [optional] 
**wwn** | **String** | 64-bit World Wide Name | [optional] 



## Enum: DuplexEnum


* `half` (value: `"half"`)

* `full` (value: `"full"`)

* `auto` (value: `"auto"`)





## Enum: ModeEnum


* `access` (value: `"access"`)

* `tagged` (value: `"tagged"`)

* `tagged-all` (value: `"tagged-all"`)





## Enum: PoeModeEnum


* `pd` (value: `"pd"`)

* `pse` (value: `"pse"`)





## Enum: PoeTypeEnum


* `type1-ieee802.3af` (value: `"type1-ieee802.3af"`)

* `type2-ieee802.3at` (value: `"type2-ieee802.3at"`)

* `type2-ieee802.3az` (value: `"type2-ieee802.3az"`)

* `type3-ieee802.3bt` (value: `"type3-ieee802.3bt"`)

* `type4-ieee802.3bt` (value: `"type4-ieee802.3bt"`)

* `passive-24v-2pair` (value: `"passive-24v-2pair"`)

* `passive-24v-4pair` (value: `"passive-24v-4pair"`)

* `passive-48v-2pair` (value: `"passive-48v-2pair"`)

* `passive-48v-4pair` (value: `"passive-48v-4pair"`)





## Enum: RfChannelEnum


* `2.4g-1-2412-22` (value: `"2.4g-1-2412-22"`)

* `2.4g-2-2417-22` (value: `"2.4g-2-2417-22"`)

* `2.4g-3-2422-22` (value: `"2.4g-3-2422-22"`)

* `2.4g-4-2427-22` (value: `"2.4g-4-2427-22"`)

* `2.4g-5-2432-22` (value: `"2.4g-5-2432-22"`)

* `2.4g-6-2437-22` (value: `"2.4g-6-2437-22"`)

* `2.4g-7-2442-22` (value: `"2.4g-7-2442-22"`)

* `2.4g-8-2447-22` (value: `"2.4g-8-2447-22"`)

* `2.4g-9-2452-22` (value: `"2.4g-9-2452-22"`)

* `2.4g-10-2457-22` (value: `"2.4g-10-2457-22"`)

* `2.4g-11-2462-22` (value: `"2.4g-11-2462-22"`)

* `2.4g-12-2467-22` (value: `"2.4g-12-2467-22"`)

* `2.4g-13-2472-22` (value: `"2.4g-13-2472-22"`)

* `5g-32-5160-20` (value: `"5g-32-5160-20"`)

* `5g-34-5170-40` (value: `"5g-34-5170-40"`)

* `5g-36-5180-20` (value: `"5g-36-5180-20"`)

* `5g-38-5190-40` (value: `"5g-38-5190-40"`)

* `5g-40-5200-20` (value: `"5g-40-5200-20"`)

* `5g-42-5210-80` (value: `"5g-42-5210-80"`)

* `5g-44-5220-20` (value: `"5g-44-5220-20"`)

* `5g-46-5230-40` (value: `"5g-46-5230-40"`)

* `5g-48-5240-20` (value: `"5g-48-5240-20"`)

* `5g-50-5250-160` (value: `"5g-50-5250-160"`)

* `5g-52-5260-20` (value: `"5g-52-5260-20"`)

* `5g-54-5270-40` (value: `"5g-54-5270-40"`)

* `5g-56-5280-20` (value: `"5g-56-5280-20"`)

* `5g-58-5290-80` (value: `"5g-58-5290-80"`)

* `5g-60-5300-20` (value: `"5g-60-5300-20"`)

* `5g-62-5310-40` (value: `"5g-62-5310-40"`)

* `5g-64-5320-20` (value: `"5g-64-5320-20"`)

* `5g-100-5500-20` (value: `"5g-100-5500-20"`)

* `5g-102-5510-40` (value: `"5g-102-5510-40"`)

* `5g-104-5520-20` (value: `"5g-104-5520-20"`)

* `5g-106-5530-80` (value: `"5g-106-5530-80"`)

* `5g-108-5540-20` (value: `"5g-108-5540-20"`)

* `5g-110-5550-40` (value: `"5g-110-5550-40"`)

* `5g-112-5560-20` (value: `"5g-112-5560-20"`)

* `5g-114-5570-160` (value: `"5g-114-5570-160"`)

* `5g-116-5580-20` (value: `"5g-116-5580-20"`)

* `5g-118-5590-40` (value: `"5g-118-5590-40"`)

* `5g-120-5600-20` (value: `"5g-120-5600-20"`)

* `5g-122-5610-80` (value: `"5g-122-5610-80"`)

* `5g-124-5620-20` (value: `"5g-124-5620-20"`)

* `5g-126-5630-40` (value: `"5g-126-5630-40"`)

* `5g-128-5640-20` (value: `"5g-128-5640-20"`)

* `5g-132-5660-20` (value: `"5g-132-5660-20"`)

* `5g-134-5670-40` (value: `"5g-134-5670-40"`)

* `5g-136-5680-20` (value: `"5g-136-5680-20"`)

* `5g-138-5690-80` (value: `"5g-138-5690-80"`)

* `5g-140-5700-20` (value: `"5g-140-5700-20"`)

* `5g-142-5710-40` (value: `"5g-142-5710-40"`)

* `5g-144-5720-20` (value: `"5g-144-5720-20"`)

* `5g-149-5745-20` (value: `"5g-149-5745-20"`)

* `5g-151-5755-40` (value: `"5g-151-5755-40"`)

* `5g-153-5765-20` (value: `"5g-153-5765-20"`)

* `5g-155-5775-80` (value: `"5g-155-5775-80"`)

* `5g-157-5785-20` (value: `"5g-157-5785-20"`)

* `5g-159-5795-40` (value: `"5g-159-5795-40"`)

* `5g-161-5805-20` (value: `"5g-161-5805-20"`)

* `5g-163-5815-160` (value: `"5g-163-5815-160"`)

* `5g-165-5825-20` (value: `"5g-165-5825-20"`)

* `5g-167-5835-40` (value: `"5g-167-5835-40"`)

* `5g-169-5845-20` (value: `"5g-169-5845-20"`)

* `5g-171-5855-80` (value: `"5g-171-5855-80"`)

* `5g-173-5865-20` (value: `"5g-173-5865-20"`)

* `5g-175-5875-40` (value: `"5g-175-5875-40"`)

* `5g-177-5885-20` (value: `"5g-177-5885-20"`)

* `6g-1-5955-20` (value: `"6g-1-5955-20"`)

* `6g-3-5965-40` (value: `"6g-3-5965-40"`)

* `6g-5-5975-20` (value: `"6g-5-5975-20"`)

* `6g-7-5985-80` (value: `"6g-7-5985-80"`)

* `6g-9-5995-20` (value: `"6g-9-5995-20"`)

* `6g-11-6005-40` (value: `"6g-11-6005-40"`)

* `6g-13-6015-20` (value: `"6g-13-6015-20"`)

* `6g-15-6025-160` (value: `"6g-15-6025-160"`)

* `6g-17-6035-20` (value: `"6g-17-6035-20"`)

* `6g-19-6045-40` (value: `"6g-19-6045-40"`)

* `6g-21-6055-20` (value: `"6g-21-6055-20"`)

* `6g-23-6065-80` (value: `"6g-23-6065-80"`)

* `6g-25-6075-20` (value: `"6g-25-6075-20"`)

* `6g-27-6085-40` (value: `"6g-27-6085-40"`)

* `6g-29-6095-20` (value: `"6g-29-6095-20"`)

* `6g-31-6105-320` (value: `"6g-31-6105-320"`)

* `6g-33-6115-20` (value: `"6g-33-6115-20"`)

* `6g-35-6125-40` (value: `"6g-35-6125-40"`)

* `6g-37-6135-20` (value: `"6g-37-6135-20"`)

* `6g-39-6145-80` (value: `"6g-39-6145-80"`)

* `6g-41-6155-20` (value: `"6g-41-6155-20"`)

* `6g-43-6165-40` (value: `"6g-43-6165-40"`)

* `6g-45-6175-20` (value: `"6g-45-6175-20"`)

* `6g-47-6185-160` (value: `"6g-47-6185-160"`)

* `6g-49-6195-20` (value: `"6g-49-6195-20"`)

* `6g-51-6205-40` (value: `"6g-51-6205-40"`)

* `6g-53-6215-20` (value: `"6g-53-6215-20"`)

* `6g-55-6225-80` (value: `"6g-55-6225-80"`)

* `6g-57-6235-20` (value: `"6g-57-6235-20"`)

* `6g-59-6245-40` (value: `"6g-59-6245-40"`)

* `6g-61-6255-20` (value: `"6g-61-6255-20"`)

* `6g-65-6275-20` (value: `"6g-65-6275-20"`)

* `6g-67-6285-40` (value: `"6g-67-6285-40"`)

* `6g-69-6295-20` (value: `"6g-69-6295-20"`)

* `6g-71-6305-80` (value: `"6g-71-6305-80"`)

* `6g-73-6315-20` (value: `"6g-73-6315-20"`)

* `6g-75-6325-40` (value: `"6g-75-6325-40"`)

* `6g-77-6335-20` (value: `"6g-77-6335-20"`)

* `6g-79-6345-160` (value: `"6g-79-6345-160"`)

* `6g-81-6355-20` (value: `"6g-81-6355-20"`)

* `6g-83-6365-40` (value: `"6g-83-6365-40"`)

* `6g-85-6375-20` (value: `"6g-85-6375-20"`)

* `6g-87-6385-80` (value: `"6g-87-6385-80"`)

* `6g-89-6395-20` (value: `"6g-89-6395-20"`)

* `6g-91-6405-40` (value: `"6g-91-6405-40"`)

* `6g-93-6415-20` (value: `"6g-93-6415-20"`)

* `6g-95-6425-320` (value: `"6g-95-6425-320"`)

* `6g-97-6435-20` (value: `"6g-97-6435-20"`)

* `6g-99-6445-40` (value: `"6g-99-6445-40"`)

* `6g-101-6455-20` (value: `"6g-101-6455-20"`)

* `6g-103-6465-80` (value: `"6g-103-6465-80"`)

* `6g-105-6475-20` (value: `"6g-105-6475-20"`)

* `6g-107-6485-40` (value: `"6g-107-6485-40"`)

* `6g-109-6495-20` (value: `"6g-109-6495-20"`)

* `6g-111-6505-160` (value: `"6g-111-6505-160"`)

* `6g-113-6515-20` (value: `"6g-113-6515-20"`)

* `6g-115-6525-40` (value: `"6g-115-6525-40"`)

* `6g-117-6535-20` (value: `"6g-117-6535-20"`)

* `6g-119-6545-80` (value: `"6g-119-6545-80"`)

* `6g-121-6555-20` (value: `"6g-121-6555-20"`)

* `6g-123-6565-40` (value: `"6g-123-6565-40"`)

* `6g-125-6575-20` (value: `"6g-125-6575-20"`)

* `6g-129-6595-20` (value: `"6g-129-6595-20"`)

* `6g-131-6605-40` (value: `"6g-131-6605-40"`)

* `6g-133-6615-20` (value: `"6g-133-6615-20"`)

* `6g-135-6625-80` (value: `"6g-135-6625-80"`)

* `6g-137-6635-20` (value: `"6g-137-6635-20"`)

* `6g-139-6645-40` (value: `"6g-139-6645-40"`)

* `6g-141-6655-20` (value: `"6g-141-6655-20"`)

* `6g-143-6665-160` (value: `"6g-143-6665-160"`)

* `6g-145-6675-20` (value: `"6g-145-6675-20"`)

* `6g-147-6685-40` (value: `"6g-147-6685-40"`)

* `6g-149-6695-20` (value: `"6g-149-6695-20"`)

* `6g-151-6705-80` (value: `"6g-151-6705-80"`)

* `6g-153-6715-20` (value: `"6g-153-6715-20"`)

* `6g-155-6725-40` (value: `"6g-155-6725-40"`)

* `6g-157-6735-20` (value: `"6g-157-6735-20"`)

* `6g-159-6745-320` (value: `"6g-159-6745-320"`)

* `6g-161-6755-20` (value: `"6g-161-6755-20"`)

* `6g-163-6765-40` (value: `"6g-163-6765-40"`)

* `6g-165-6775-20` (value: `"6g-165-6775-20"`)

* `6g-167-6785-80` (value: `"6g-167-6785-80"`)

* `6g-169-6795-20` (value: `"6g-169-6795-20"`)

* `6g-171-6805-40` (value: `"6g-171-6805-40"`)

* `6g-173-6815-20` (value: `"6g-173-6815-20"`)

* `6g-175-6825-160` (value: `"6g-175-6825-160"`)

* `6g-177-6835-20` (value: `"6g-177-6835-20"`)

* `6g-179-6845-40` (value: `"6g-179-6845-40"`)

* `6g-181-6855-20` (value: `"6g-181-6855-20"`)

* `6g-183-6865-80` (value: `"6g-183-6865-80"`)

* `6g-185-6875-20` (value: `"6g-185-6875-20"`)

* `6g-187-6885-40` (value: `"6g-187-6885-40"`)

* `6g-189-6895-20` (value: `"6g-189-6895-20"`)

* `6g-193-6915-20` (value: `"6g-193-6915-20"`)

* `6g-195-6925-40` (value: `"6g-195-6925-40"`)

* `6g-197-6935-20` (value: `"6g-197-6935-20"`)

* `6g-199-6945-80` (value: `"6g-199-6945-80"`)

* `6g-201-6955-20` (value: `"6g-201-6955-20"`)

* `6g-203-6965-40` (value: `"6g-203-6965-40"`)

* `6g-205-6975-20` (value: `"6g-205-6975-20"`)

* `6g-207-6985-160` (value: `"6g-207-6985-160"`)

* `6g-209-6995-20` (value: `"6g-209-6995-20"`)

* `6g-211-7005-40` (value: `"6g-211-7005-40"`)

* `6g-213-7015-20` (value: `"6g-213-7015-20"`)

* `6g-215-7025-80` (value: `"6g-215-7025-80"`)

* `6g-217-7035-20` (value: `"6g-217-7035-20"`)

* `6g-219-7045-40` (value: `"6g-219-7045-40"`)

* `6g-221-7055-20` (value: `"6g-221-7055-20"`)

* `6g-225-7075-20` (value: `"6g-225-7075-20"`)

* `6g-227-7085-40` (value: `"6g-227-7085-40"`)

* `6g-229-7095-20` (value: `"6g-229-7095-20"`)

* `6g-233-7115-20` (value: `"6g-233-7115-20"`)

* `60g-1-58320-2160` (value: `"60g-1-58320-2160"`)

* `60g-2-60480-2160` (value: `"60g-2-60480-2160"`)

* `60g-3-62640-2160` (value: `"60g-3-62640-2160"`)

* `60g-4-64800-2160` (value: `"60g-4-64800-2160"`)

* `60g-5-66960-2160` (value: `"60g-5-66960-2160"`)

* `60g-6-69120-2160` (value: `"60g-6-69120-2160"`)

* `60g-9-59400-4320` (value: `"60g-9-59400-4320"`)

* `60g-10-61560-4320` (value: `"60g-10-61560-4320"`)

* `60g-11-63720-4320` (value: `"60g-11-63720-4320"`)

* `60g-12-65880-4320` (value: `"60g-12-65880-4320"`)

* `60g-13-68040-4320` (value: `"60g-13-68040-4320"`)

* `60g-17-60480-6480` (value: `"60g-17-60480-6480"`)

* `60g-18-62640-6480` (value: `"60g-18-62640-6480"`)

* `60g-19-64800-6480` (value: `"60g-19-64800-6480"`)

* `60g-20-66960-6480` (value: `"60g-20-66960-6480"`)

* `60g-25-61560-6480` (value: `"60g-25-61560-6480"`)

* `60g-26-63720-6480` (value: `"60g-26-63720-6480"`)

* `60g-27-65880-6480` (value: `"60g-27-65880-6480"`)





## Enum: RfRoleEnum


* `ap` (value: `"ap"`)

* `station` (value: `"station"`)





## Enum: TypeEnum


* `virtual` (value: `"virtual"`)

* `bridge` (value: `"bridge"`)

* `lag` (value: `"lag"`)

* `100base-fx` (value: `"100base-fx"`)

* `100base-lfx` (value: `"100base-lfx"`)

* `100base-tx` (value: `"100base-tx"`)

* `100base-t1` (value: `"100base-t1"`)

* `1000base-t` (value: `"1000base-t"`)

* `2.5gbase-t` (value: `"2.5gbase-t"`)

* `5gbase-t` (value: `"5gbase-t"`)

* `10gbase-t` (value: `"10gbase-t"`)

* `10gbase-cx4` (value: `"10gbase-cx4"`)

* `1000base-x-gbic` (value: `"1000base-x-gbic"`)

* `1000base-x-sfp` (value: `"1000base-x-sfp"`)

* `10gbase-x-sfpp` (value: `"10gbase-x-sfpp"`)

* `10gbase-x-xfp` (value: `"10gbase-x-xfp"`)

* `10gbase-x-xenpak` (value: `"10gbase-x-xenpak"`)

* `10gbase-x-x2` (value: `"10gbase-x-x2"`)

* `25gbase-x-sfp28` (value: `"25gbase-x-sfp28"`)

* `50gbase-x-sfp56` (value: `"50gbase-x-sfp56"`)

* `40gbase-x-qsfpp` (value: `"40gbase-x-qsfpp"`)

* `50gbase-x-sfp28` (value: `"50gbase-x-sfp28"`)

* `100gbase-x-cfp` (value: `"100gbase-x-cfp"`)

* `100gbase-x-cfp2` (value: `"100gbase-x-cfp2"`)

* `200gbase-x-cfp2` (value: `"200gbase-x-cfp2"`)

* `100gbase-x-cfp4` (value: `"100gbase-x-cfp4"`)

* `100gbase-x-cpak` (value: `"100gbase-x-cpak"`)

* `100gbase-x-qsfp28` (value: `"100gbase-x-qsfp28"`)

* `200gbase-x-qsfp56` (value: `"200gbase-x-qsfp56"`)

* `400gbase-x-qsfpdd` (value: `"400gbase-x-qsfpdd"`)

* `400gbase-x-osfp` (value: `"400gbase-x-osfp"`)

* `800gbase-x-qsfpdd` (value: `"800gbase-x-qsfpdd"`)

* `800gbase-x-osfp` (value: `"800gbase-x-osfp"`)

* `1000base-kx` (value: `"1000base-kx"`)

* `10gbase-kr` (value: `"10gbase-kr"`)

* `10gbase-kx4` (value: `"10gbase-kx4"`)

* `25gbase-kr` (value: `"25gbase-kr"`)

* `40gbase-kr4` (value: `"40gbase-kr4"`)

* `50gbase-kr` (value: `"50gbase-kr"`)

* `100gbase-kp4` (value: `"100gbase-kp4"`)

* `100gbase-kr2` (value: `"100gbase-kr2"`)

* `100gbase-kr4` (value: `"100gbase-kr4"`)

* `ieee802.11a` (value: `"ieee802.11a"`)

* `ieee802.11g` (value: `"ieee802.11g"`)

* `ieee802.11n` (value: `"ieee802.11n"`)

* `ieee802.11ac` (value: `"ieee802.11ac"`)

* `ieee802.11ad` (value: `"ieee802.11ad"`)

* `ieee802.11ax` (value: `"ieee802.11ax"`)

* `ieee802.11ay` (value: `"ieee802.11ay"`)

* `ieee802.15.1` (value: `"ieee802.15.1"`)

* `other-wireless` (value: `"other-wireless"`)

* `gsm` (value: `"gsm"`)

* `cdma` (value: `"cdma"`)

* `lte` (value: `"lte"`)

* `sonet-oc3` (value: `"sonet-oc3"`)

* `sonet-oc12` (value: `"sonet-oc12"`)

* `sonet-oc48` (value: `"sonet-oc48"`)

* `sonet-oc192` (value: `"sonet-oc192"`)

* `sonet-oc768` (value: `"sonet-oc768"`)

* `sonet-oc1920` (value: `"sonet-oc1920"`)

* `sonet-oc3840` (value: `"sonet-oc3840"`)

* `1gfc-sfp` (value: `"1gfc-sfp"`)

* `2gfc-sfp` (value: `"2gfc-sfp"`)

* `4gfc-sfp` (value: `"4gfc-sfp"`)

* `8gfc-sfpp` (value: `"8gfc-sfpp"`)

* `16gfc-sfpp` (value: `"16gfc-sfpp"`)

* `32gfc-sfp28` (value: `"32gfc-sfp28"`)

* `64gfc-qsfpp` (value: `"64gfc-qsfpp"`)

* `128gfc-qsfp28` (value: `"128gfc-qsfp28"`)

* `infiniband-sdr` (value: `"infiniband-sdr"`)

* `infiniband-ddr` (value: `"infiniband-ddr"`)

* `infiniband-qdr` (value: `"infiniband-qdr"`)

* `infiniband-fdr10` (value: `"infiniband-fdr10"`)

* `infiniband-fdr` (value: `"infiniband-fdr"`)

* `infiniband-edr` (value: `"infiniband-edr"`)

* `infiniband-hdr` (value: `"infiniband-hdr"`)

* `infiniband-ndr` (value: `"infiniband-ndr"`)

* `infiniband-xdr` (value: `"infiniband-xdr"`)

* `t1` (value: `"t1"`)

* `e1` (value: `"e1"`)

* `t3` (value: `"t3"`)

* `e3` (value: `"e3"`)

* `xdsl` (value: `"xdsl"`)

* `docsis` (value: `"docsis"`)

* `gpon` (value: `"gpon"`)

* `xg-pon` (value: `"xg-pon"`)

* `xgs-pon` (value: `"xgs-pon"`)

* `ng-pon2` (value: `"ng-pon2"`)

* `epon` (value: `"epon"`)

* `10g-epon` (value: `"10g-epon"`)

* `cisco-stackwise` (value: `"cisco-stackwise"`)

* `cisco-stackwise-plus` (value: `"cisco-stackwise-plus"`)

* `cisco-flexstack` (value: `"cisco-flexstack"`)

* `cisco-flexstack-plus` (value: `"cisco-flexstack-plus"`)

* `cisco-stackwise-80` (value: `"cisco-stackwise-80"`)

* `cisco-stackwise-160` (value: `"cisco-stackwise-160"`)

* `cisco-stackwise-320` (value: `"cisco-stackwise-320"`)

* `cisco-stackwise-480` (value: `"cisco-stackwise-480"`)

* `cisco-stackwise-1t` (value: `"cisco-stackwise-1t"`)

* `juniper-vcp` (value: `"juniper-vcp"`)

* `extreme-summitstack` (value: `"extreme-summitstack"`)

* `extreme-summitstack-128` (value: `"extreme-summitstack-128"`)

* `extreme-summitstack-256` (value: `"extreme-summitstack-256"`)

* `extreme-summitstack-512` (value: `"extreme-summitstack-512"`)

* `other` (value: `"other"`)




