

# WritableInterface


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**occupied** | **Boolean** |  |  [optional] [readonly] |
|**bridge** | **Integer** |  |  [optional] |
|**cable** | [**NestedCable**](NestedCable.md) |  |  [optional] |
|**cableEnd** | **String** |  |  [optional] [readonly] |
|**connectedEndpoints** | **List&lt;String&gt;** |  Return the appropriate serializer for the type of connected object.  |  [optional] [readonly] |
|**connectedEndpointsReachable** | **Boolean** |  |  [optional] [readonly] |
|**connectedEndpointsType** | **String** |  |  [optional] [readonly] |
|**countFhrpGroups** | **Integer** |  |  [optional] [readonly] |
|**countIpaddresses** | **Integer** |  |  [optional] [readonly] |
|**created** | **OffsetDateTime** |  |  [optional] [readonly] |
|**customFields** | **Object** |  |  [optional] |
|**description** | **String** |  |  [optional] |
|**device** | **Integer** |  |  |
|**display** | **String** |  |  [optional] [readonly] |
|**duplex** | [**DuplexEnum**](#DuplexEnum) |  |  [optional] |
|**enabled** | **Boolean** |  |  [optional] |
|**id** | **Integer** |  |  [optional] [readonly] |
|**l2vpnTermination** | **String** |  |  [optional] [readonly] |
|**label** | **String** | Physical label |  [optional] |
|**lag** | **Integer** |  |  [optional] |
|**lastUpdated** | **OffsetDateTime** |  |  [optional] [readonly] |
|**linkPeers** | **List&lt;String&gt;** |  Return the appropriate serializer for the link termination model.  |  [optional] [readonly] |
|**linkPeersType** | **String** |  |  [optional] [readonly] |
|**macAddress** | **String** |  |  [optional] |
|**markConnected** | **Boolean** | Treat as if a cable is connected |  [optional] |
|**mgmtOnly** | **Boolean** | This interface is used only for out-of-band management |  [optional] |
|**mode** | [**ModeEnum**](#ModeEnum) |  |  [optional] |
|**module** | **Integer** |  |  [optional] |
|**mtu** | **Integer** |  |  [optional] |
|**name** | **String** |  |  |
|**parent** | **Integer** |  |  [optional] |
|**poeMode** | [**PoeModeEnum**](#PoeModeEnum) |  |  [optional] |
|**poeType** | [**PoeTypeEnum**](#PoeTypeEnum) |  |  [optional] |
|**rfChannel** | [**RfChannelEnum**](#RfChannelEnum) |  |  [optional] |
|**rfChannelFrequency** | **BigDecimal** |  |  [optional] |
|**rfChannelWidth** | **BigDecimal** |  |  [optional] |
|**rfRole** | [**RfRoleEnum**](#RfRoleEnum) |  |  [optional] |
|**speed** | **Integer** |  |  [optional] |
|**taggedVlans** | **Set&lt;Integer&gt;** |  |  [optional] |
|**tags** | [**List&lt;NestedTag&gt;**](NestedTag.md) |  |  [optional] |
|**txPower** | **Integer** |  |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) |  |  |
|**untaggedVlan** | **Integer** |  |  [optional] |
|**url** | **URI** |  |  [optional] [readonly] |
|**vdcs** | **Set&lt;Integer&gt;** |  |  |
|**vrf** | **Integer** |  |  [optional] |
|**wirelessLans** | **Set&lt;Integer&gt;** |  |  [optional] |
|**wirelessLink** | **Integer** |  |  [optional] |
|**wwn** | **String** | 64-bit World Wide Name |  [optional] |



## Enum: DuplexEnum

| Name | Value |
|---- | -----|
| HALF | &quot;half&quot; |
| FULL | &quot;full&quot; |
| AUTO | &quot;auto&quot; |



## Enum: ModeEnum

| Name | Value |
|---- | -----|
| ACCESS | &quot;access&quot; |
| TAGGED | &quot;tagged&quot; |
| TAGGED_ALL | &quot;tagged-all&quot; |



## Enum: PoeModeEnum

| Name | Value |
|---- | -----|
| PD | &quot;pd&quot; |
| PSE | &quot;pse&quot; |



## Enum: PoeTypeEnum

| Name | Value |
|---- | -----|
| TYPE1_IEEE802_3AF | &quot;type1-ieee802.3af&quot; |
| TYPE2_IEEE802_3AT | &quot;type2-ieee802.3at&quot; |
| TYPE2_IEEE802_3AZ | &quot;type2-ieee802.3az&quot; |
| TYPE3_IEEE802_3BT | &quot;type3-ieee802.3bt&quot; |
| TYPE4_IEEE802_3BT | &quot;type4-ieee802.3bt&quot; |
| PASSIVE_24V_2PAIR | &quot;passive-24v-2pair&quot; |
| PASSIVE_24V_4PAIR | &quot;passive-24v-4pair&quot; |
| PASSIVE_48V_2PAIR | &quot;passive-48v-2pair&quot; |
| PASSIVE_48V_4PAIR | &quot;passive-48v-4pair&quot; |



## Enum: RfChannelEnum

| Name | Value |
|---- | -----|
| _2_4G_1_2412_22 | &quot;2.4g-1-2412-22&quot; |
| _2_4G_2_2417_22 | &quot;2.4g-2-2417-22&quot; |
| _2_4G_3_2422_22 | &quot;2.4g-3-2422-22&quot; |
| _2_4G_4_2427_22 | &quot;2.4g-4-2427-22&quot; |
| _2_4G_5_2432_22 | &quot;2.4g-5-2432-22&quot; |
| _2_4G_6_2437_22 | &quot;2.4g-6-2437-22&quot; |
| _2_4G_7_2442_22 | &quot;2.4g-7-2442-22&quot; |
| _2_4G_8_2447_22 | &quot;2.4g-8-2447-22&quot; |
| _2_4G_9_2452_22 | &quot;2.4g-9-2452-22&quot; |
| _2_4G_10_2457_22 | &quot;2.4g-10-2457-22&quot; |
| _2_4G_11_2462_22 | &quot;2.4g-11-2462-22&quot; |
| _2_4G_12_2467_22 | &quot;2.4g-12-2467-22&quot; |
| _2_4G_13_2472_22 | &quot;2.4g-13-2472-22&quot; |
| _5G_32_5160_20 | &quot;5g-32-5160-20&quot; |
| _5G_34_5170_40 | &quot;5g-34-5170-40&quot; |
| _5G_36_5180_20 | &quot;5g-36-5180-20&quot; |
| _5G_38_5190_40 | &quot;5g-38-5190-40&quot; |
| _5G_40_5200_20 | &quot;5g-40-5200-20&quot; |
| _5G_42_5210_80 | &quot;5g-42-5210-80&quot; |
| _5G_44_5220_20 | &quot;5g-44-5220-20&quot; |
| _5G_46_5230_40 | &quot;5g-46-5230-40&quot; |
| _5G_48_5240_20 | &quot;5g-48-5240-20&quot; |
| _5G_50_5250_160 | &quot;5g-50-5250-160&quot; |
| _5G_52_5260_20 | &quot;5g-52-5260-20&quot; |
| _5G_54_5270_40 | &quot;5g-54-5270-40&quot; |
| _5G_56_5280_20 | &quot;5g-56-5280-20&quot; |
| _5G_58_5290_80 | &quot;5g-58-5290-80&quot; |
| _5G_60_5300_20 | &quot;5g-60-5300-20&quot; |
| _5G_62_5310_40 | &quot;5g-62-5310-40&quot; |
| _5G_64_5320_20 | &quot;5g-64-5320-20&quot; |
| _5G_100_5500_20 | &quot;5g-100-5500-20&quot; |
| _5G_102_5510_40 | &quot;5g-102-5510-40&quot; |
| _5G_104_5520_20 | &quot;5g-104-5520-20&quot; |
| _5G_106_5530_80 | &quot;5g-106-5530-80&quot; |
| _5G_108_5540_20 | &quot;5g-108-5540-20&quot; |
| _5G_110_5550_40 | &quot;5g-110-5550-40&quot; |
| _5G_112_5560_20 | &quot;5g-112-5560-20&quot; |
| _5G_114_5570_160 | &quot;5g-114-5570-160&quot; |
| _5G_116_5580_20 | &quot;5g-116-5580-20&quot; |
| _5G_118_5590_40 | &quot;5g-118-5590-40&quot; |
| _5G_120_5600_20 | &quot;5g-120-5600-20&quot; |
| _5G_122_5610_80 | &quot;5g-122-5610-80&quot; |
| _5G_124_5620_20 | &quot;5g-124-5620-20&quot; |
| _5G_126_5630_40 | &quot;5g-126-5630-40&quot; |
| _5G_128_5640_20 | &quot;5g-128-5640-20&quot; |
| _5G_132_5660_20 | &quot;5g-132-5660-20&quot; |
| _5G_134_5670_40 | &quot;5g-134-5670-40&quot; |
| _5G_136_5680_20 | &quot;5g-136-5680-20&quot; |
| _5G_138_5690_80 | &quot;5g-138-5690-80&quot; |
| _5G_140_5700_20 | &quot;5g-140-5700-20&quot; |
| _5G_142_5710_40 | &quot;5g-142-5710-40&quot; |
| _5G_144_5720_20 | &quot;5g-144-5720-20&quot; |
| _5G_149_5745_20 | &quot;5g-149-5745-20&quot; |
| _5G_151_5755_40 | &quot;5g-151-5755-40&quot; |
| _5G_153_5765_20 | &quot;5g-153-5765-20&quot; |
| _5G_155_5775_80 | &quot;5g-155-5775-80&quot; |
| _5G_157_5785_20 | &quot;5g-157-5785-20&quot; |
| _5G_159_5795_40 | &quot;5g-159-5795-40&quot; |
| _5G_161_5805_20 | &quot;5g-161-5805-20&quot; |
| _5G_163_5815_160 | &quot;5g-163-5815-160&quot; |
| _5G_165_5825_20 | &quot;5g-165-5825-20&quot; |
| _5G_167_5835_40 | &quot;5g-167-5835-40&quot; |
| _5G_169_5845_20 | &quot;5g-169-5845-20&quot; |
| _5G_171_5855_80 | &quot;5g-171-5855-80&quot; |
| _5G_173_5865_20 | &quot;5g-173-5865-20&quot; |
| _5G_175_5875_40 | &quot;5g-175-5875-40&quot; |
| _5G_177_5885_20 | &quot;5g-177-5885-20&quot; |
| _6G_1_5955_20 | &quot;6g-1-5955-20&quot; |
| _6G_3_5965_40 | &quot;6g-3-5965-40&quot; |
| _6G_5_5975_20 | &quot;6g-5-5975-20&quot; |
| _6G_7_5985_80 | &quot;6g-7-5985-80&quot; |
| _6G_9_5995_20 | &quot;6g-9-5995-20&quot; |
| _6G_11_6005_40 | &quot;6g-11-6005-40&quot; |
| _6G_13_6015_20 | &quot;6g-13-6015-20&quot; |
| _6G_15_6025_160 | &quot;6g-15-6025-160&quot; |
| _6G_17_6035_20 | &quot;6g-17-6035-20&quot; |
| _6G_19_6045_40 | &quot;6g-19-6045-40&quot; |
| _6G_21_6055_20 | &quot;6g-21-6055-20&quot; |
| _6G_23_6065_80 | &quot;6g-23-6065-80&quot; |
| _6G_25_6075_20 | &quot;6g-25-6075-20&quot; |
| _6G_27_6085_40 | &quot;6g-27-6085-40&quot; |
| _6G_29_6095_20 | &quot;6g-29-6095-20&quot; |
| _6G_31_6105_320 | &quot;6g-31-6105-320&quot; |
| _6G_33_6115_20 | &quot;6g-33-6115-20&quot; |
| _6G_35_6125_40 | &quot;6g-35-6125-40&quot; |
| _6G_37_6135_20 | &quot;6g-37-6135-20&quot; |
| _6G_39_6145_80 | &quot;6g-39-6145-80&quot; |
| _6G_41_6155_20 | &quot;6g-41-6155-20&quot; |
| _6G_43_6165_40 | &quot;6g-43-6165-40&quot; |
| _6G_45_6175_20 | &quot;6g-45-6175-20&quot; |
| _6G_47_6185_160 | &quot;6g-47-6185-160&quot; |
| _6G_49_6195_20 | &quot;6g-49-6195-20&quot; |
| _6G_51_6205_40 | &quot;6g-51-6205-40&quot; |
| _6G_53_6215_20 | &quot;6g-53-6215-20&quot; |
| _6G_55_6225_80 | &quot;6g-55-6225-80&quot; |
| _6G_57_6235_20 | &quot;6g-57-6235-20&quot; |
| _6G_59_6245_40 | &quot;6g-59-6245-40&quot; |
| _6G_61_6255_20 | &quot;6g-61-6255-20&quot; |
| _6G_65_6275_20 | &quot;6g-65-6275-20&quot; |
| _6G_67_6285_40 | &quot;6g-67-6285-40&quot; |
| _6G_69_6295_20 | &quot;6g-69-6295-20&quot; |
| _6G_71_6305_80 | &quot;6g-71-6305-80&quot; |
| _6G_73_6315_20 | &quot;6g-73-6315-20&quot; |
| _6G_75_6325_40 | &quot;6g-75-6325-40&quot; |
| _6G_77_6335_20 | &quot;6g-77-6335-20&quot; |
| _6G_79_6345_160 | &quot;6g-79-6345-160&quot; |
| _6G_81_6355_20 | &quot;6g-81-6355-20&quot; |
| _6G_83_6365_40 | &quot;6g-83-6365-40&quot; |
| _6G_85_6375_20 | &quot;6g-85-6375-20&quot; |
| _6G_87_6385_80 | &quot;6g-87-6385-80&quot; |
| _6G_89_6395_20 | &quot;6g-89-6395-20&quot; |
| _6G_91_6405_40 | &quot;6g-91-6405-40&quot; |
| _6G_93_6415_20 | &quot;6g-93-6415-20&quot; |
| _6G_95_6425_320 | &quot;6g-95-6425-320&quot; |
| _6G_97_6435_20 | &quot;6g-97-6435-20&quot; |
| _6G_99_6445_40 | &quot;6g-99-6445-40&quot; |
| _6G_101_6455_20 | &quot;6g-101-6455-20&quot; |
| _6G_103_6465_80 | &quot;6g-103-6465-80&quot; |
| _6G_105_6475_20 | &quot;6g-105-6475-20&quot; |
| _6G_107_6485_40 | &quot;6g-107-6485-40&quot; |
| _6G_109_6495_20 | &quot;6g-109-6495-20&quot; |
| _6G_111_6505_160 | &quot;6g-111-6505-160&quot; |
| _6G_113_6515_20 | &quot;6g-113-6515-20&quot; |
| _6G_115_6525_40 | &quot;6g-115-6525-40&quot; |
| _6G_117_6535_20 | &quot;6g-117-6535-20&quot; |
| _6G_119_6545_80 | &quot;6g-119-6545-80&quot; |
| _6G_121_6555_20 | &quot;6g-121-6555-20&quot; |
| _6G_123_6565_40 | &quot;6g-123-6565-40&quot; |
| _6G_125_6575_20 | &quot;6g-125-6575-20&quot; |
| _6G_129_6595_20 | &quot;6g-129-6595-20&quot; |
| _6G_131_6605_40 | &quot;6g-131-6605-40&quot; |
| _6G_133_6615_20 | &quot;6g-133-6615-20&quot; |
| _6G_135_6625_80 | &quot;6g-135-6625-80&quot; |
| _6G_137_6635_20 | &quot;6g-137-6635-20&quot; |
| _6G_139_6645_40 | &quot;6g-139-6645-40&quot; |
| _6G_141_6655_20 | &quot;6g-141-6655-20&quot; |
| _6G_143_6665_160 | &quot;6g-143-6665-160&quot; |
| _6G_145_6675_20 | &quot;6g-145-6675-20&quot; |
| _6G_147_6685_40 | &quot;6g-147-6685-40&quot; |
| _6G_149_6695_20 | &quot;6g-149-6695-20&quot; |
| _6G_151_6705_80 | &quot;6g-151-6705-80&quot; |
| _6G_153_6715_20 | &quot;6g-153-6715-20&quot; |
| _6G_155_6725_40 | &quot;6g-155-6725-40&quot; |
| _6G_157_6735_20 | &quot;6g-157-6735-20&quot; |
| _6G_159_6745_320 | &quot;6g-159-6745-320&quot; |
| _6G_161_6755_20 | &quot;6g-161-6755-20&quot; |
| _6G_163_6765_40 | &quot;6g-163-6765-40&quot; |
| _6G_165_6775_20 | &quot;6g-165-6775-20&quot; |
| _6G_167_6785_80 | &quot;6g-167-6785-80&quot; |
| _6G_169_6795_20 | &quot;6g-169-6795-20&quot; |
| _6G_171_6805_40 | &quot;6g-171-6805-40&quot; |
| _6G_173_6815_20 | &quot;6g-173-6815-20&quot; |
| _6G_175_6825_160 | &quot;6g-175-6825-160&quot; |
| _6G_177_6835_20 | &quot;6g-177-6835-20&quot; |
| _6G_179_6845_40 | &quot;6g-179-6845-40&quot; |
| _6G_181_6855_20 | &quot;6g-181-6855-20&quot; |
| _6G_183_6865_80 | &quot;6g-183-6865-80&quot; |
| _6G_185_6875_20 | &quot;6g-185-6875-20&quot; |
| _6G_187_6885_40 | &quot;6g-187-6885-40&quot; |
| _6G_189_6895_20 | &quot;6g-189-6895-20&quot; |
| _6G_193_6915_20 | &quot;6g-193-6915-20&quot; |
| _6G_195_6925_40 | &quot;6g-195-6925-40&quot; |
| _6G_197_6935_20 | &quot;6g-197-6935-20&quot; |
| _6G_199_6945_80 | &quot;6g-199-6945-80&quot; |
| _6G_201_6955_20 | &quot;6g-201-6955-20&quot; |
| _6G_203_6965_40 | &quot;6g-203-6965-40&quot; |
| _6G_205_6975_20 | &quot;6g-205-6975-20&quot; |
| _6G_207_6985_160 | &quot;6g-207-6985-160&quot; |
| _6G_209_6995_20 | &quot;6g-209-6995-20&quot; |
| _6G_211_7005_40 | &quot;6g-211-7005-40&quot; |
| _6G_213_7015_20 | &quot;6g-213-7015-20&quot; |
| _6G_215_7025_80 | &quot;6g-215-7025-80&quot; |
| _6G_217_7035_20 | &quot;6g-217-7035-20&quot; |
| _6G_219_7045_40 | &quot;6g-219-7045-40&quot; |
| _6G_221_7055_20 | &quot;6g-221-7055-20&quot; |
| _6G_225_7075_20 | &quot;6g-225-7075-20&quot; |
| _6G_227_7085_40 | &quot;6g-227-7085-40&quot; |
| _6G_229_7095_20 | &quot;6g-229-7095-20&quot; |
| _6G_233_7115_20 | &quot;6g-233-7115-20&quot; |
| _60G_1_58320_2160 | &quot;60g-1-58320-2160&quot; |
| _60G_2_60480_2160 | &quot;60g-2-60480-2160&quot; |
| _60G_3_62640_2160 | &quot;60g-3-62640-2160&quot; |
| _60G_4_64800_2160 | &quot;60g-4-64800-2160&quot; |
| _60G_5_66960_2160 | &quot;60g-5-66960-2160&quot; |
| _60G_6_69120_2160 | &quot;60g-6-69120-2160&quot; |
| _60G_9_59400_4320 | &quot;60g-9-59400-4320&quot; |
| _60G_10_61560_4320 | &quot;60g-10-61560-4320&quot; |
| _60G_11_63720_4320 | &quot;60g-11-63720-4320&quot; |
| _60G_12_65880_4320 | &quot;60g-12-65880-4320&quot; |
| _60G_13_68040_4320 | &quot;60g-13-68040-4320&quot; |
| _60G_17_60480_6480 | &quot;60g-17-60480-6480&quot; |
| _60G_18_62640_6480 | &quot;60g-18-62640-6480&quot; |
| _60G_19_64800_6480 | &quot;60g-19-64800-6480&quot; |
| _60G_20_66960_6480 | &quot;60g-20-66960-6480&quot; |
| _60G_25_61560_6480 | &quot;60g-25-61560-6480&quot; |
| _60G_26_63720_6480 | &quot;60g-26-63720-6480&quot; |
| _60G_27_65880_6480 | &quot;60g-27-65880-6480&quot; |



## Enum: RfRoleEnum

| Name | Value |
|---- | -----|
| AP | &quot;ap&quot; |
| STATION | &quot;station&quot; |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| VIRTUAL | &quot;virtual&quot; |
| BRIDGE | &quot;bridge&quot; |
| LAG | &quot;lag&quot; |
| _100BASE_FX | &quot;100base-fx&quot; |
| _100BASE_LFX | &quot;100base-lfx&quot; |
| _100BASE_TX | &quot;100base-tx&quot; |
| _100BASE_T1 | &quot;100base-t1&quot; |
| _1000BASE_T | &quot;1000base-t&quot; |
| _2_5GBASE_T | &quot;2.5gbase-t&quot; |
| _5GBASE_T | &quot;5gbase-t&quot; |
| _10GBASE_T | &quot;10gbase-t&quot; |
| _10GBASE_CX4 | &quot;10gbase-cx4&quot; |
| _1000BASE_X_GBIC | &quot;1000base-x-gbic&quot; |
| _1000BASE_X_SFP | &quot;1000base-x-sfp&quot; |
| _10GBASE_X_SFPP | &quot;10gbase-x-sfpp&quot; |
| _10GBASE_X_XFP | &quot;10gbase-x-xfp&quot; |
| _10GBASE_X_XENPAK | &quot;10gbase-x-xenpak&quot; |
| _10GBASE_X_X2 | &quot;10gbase-x-x2&quot; |
| _25GBASE_X_SFP28 | &quot;25gbase-x-sfp28&quot; |
| _50GBASE_X_SFP56 | &quot;50gbase-x-sfp56&quot; |
| _40GBASE_X_QSFPP | &quot;40gbase-x-qsfpp&quot; |
| _50GBASE_X_SFP28 | &quot;50gbase-x-sfp28&quot; |
| _100GBASE_X_CFP | &quot;100gbase-x-cfp&quot; |
| _100GBASE_X_CFP2 | &quot;100gbase-x-cfp2&quot; |
| _200GBASE_X_CFP2 | &quot;200gbase-x-cfp2&quot; |
| _100GBASE_X_CFP4 | &quot;100gbase-x-cfp4&quot; |
| _100GBASE_X_CPAK | &quot;100gbase-x-cpak&quot; |
| _100GBASE_X_QSFP28 | &quot;100gbase-x-qsfp28&quot; |
| _200GBASE_X_QSFP56 | &quot;200gbase-x-qsfp56&quot; |
| _400GBASE_X_QSFPDD | &quot;400gbase-x-qsfpdd&quot; |
| _400GBASE_X_OSFP | &quot;400gbase-x-osfp&quot; |
| _800GBASE_X_QSFPDD | &quot;800gbase-x-qsfpdd&quot; |
| _800GBASE_X_OSFP | &quot;800gbase-x-osfp&quot; |
| _1000BASE_KX | &quot;1000base-kx&quot; |
| _10GBASE_KR | &quot;10gbase-kr&quot; |
| _10GBASE_KX4 | &quot;10gbase-kx4&quot; |
| _25GBASE_KR | &quot;25gbase-kr&quot; |
| _40GBASE_KR4 | &quot;40gbase-kr4&quot; |
| _50GBASE_KR | &quot;50gbase-kr&quot; |
| _100GBASE_KP4 | &quot;100gbase-kp4&quot; |
| _100GBASE_KR2 | &quot;100gbase-kr2&quot; |
| _100GBASE_KR4 | &quot;100gbase-kr4&quot; |
| IEEE802_11A | &quot;ieee802.11a&quot; |
| IEEE802_11G | &quot;ieee802.11g&quot; |
| IEEE802_11N | &quot;ieee802.11n&quot; |
| IEEE802_11AC | &quot;ieee802.11ac&quot; |
| IEEE802_11AD | &quot;ieee802.11ad&quot; |
| IEEE802_11AX | &quot;ieee802.11ax&quot; |
| IEEE802_11AY | &quot;ieee802.11ay&quot; |
| IEEE802_15_1 | &quot;ieee802.15.1&quot; |
| OTHER_WIRELESS | &quot;other-wireless&quot; |
| GSM | &quot;gsm&quot; |
| CDMA | &quot;cdma&quot; |
| LTE | &quot;lte&quot; |
| SONET_OC3 | &quot;sonet-oc3&quot; |
| SONET_OC12 | &quot;sonet-oc12&quot; |
| SONET_OC48 | &quot;sonet-oc48&quot; |
| SONET_OC192 | &quot;sonet-oc192&quot; |
| SONET_OC768 | &quot;sonet-oc768&quot; |
| SONET_OC1920 | &quot;sonet-oc1920&quot; |
| SONET_OC3840 | &quot;sonet-oc3840&quot; |
| _1GFC_SFP | &quot;1gfc-sfp&quot; |
| _2GFC_SFP | &quot;2gfc-sfp&quot; |
| _4GFC_SFP | &quot;4gfc-sfp&quot; |
| _8GFC_SFPP | &quot;8gfc-sfpp&quot; |
| _16GFC_SFPP | &quot;16gfc-sfpp&quot; |
| _32GFC_SFP28 | &quot;32gfc-sfp28&quot; |
| _64GFC_QSFPP | &quot;64gfc-qsfpp&quot; |
| _128GFC_QSFP28 | &quot;128gfc-qsfp28&quot; |
| INFINIBAND_SDR | &quot;infiniband-sdr&quot; |
| INFINIBAND_DDR | &quot;infiniband-ddr&quot; |
| INFINIBAND_QDR | &quot;infiniband-qdr&quot; |
| INFINIBAND_FDR10 | &quot;infiniband-fdr10&quot; |
| INFINIBAND_FDR | &quot;infiniband-fdr&quot; |
| INFINIBAND_EDR | &quot;infiniband-edr&quot; |
| INFINIBAND_HDR | &quot;infiniband-hdr&quot; |
| INFINIBAND_NDR | &quot;infiniband-ndr&quot; |
| INFINIBAND_XDR | &quot;infiniband-xdr&quot; |
| T1 | &quot;t1&quot; |
| E1 | &quot;e1&quot; |
| T3 | &quot;t3&quot; |
| E3 | &quot;e3&quot; |
| XDSL | &quot;xdsl&quot; |
| DOCSIS | &quot;docsis&quot; |
| GPON | &quot;gpon&quot; |
| XG_PON | &quot;xg-pon&quot; |
| XGS_PON | &quot;xgs-pon&quot; |
| NG_PON2 | &quot;ng-pon2&quot; |
| EPON | &quot;epon&quot; |
| _10G_EPON | &quot;10g-epon&quot; |
| CISCO_STACKWISE | &quot;cisco-stackwise&quot; |
| CISCO_STACKWISE_PLUS | &quot;cisco-stackwise-plus&quot; |
| CISCO_FLEXSTACK | &quot;cisco-flexstack&quot; |
| CISCO_FLEXSTACK_PLUS | &quot;cisco-flexstack-plus&quot; |
| CISCO_STACKWISE_80 | &quot;cisco-stackwise-80&quot; |
| CISCO_STACKWISE_160 | &quot;cisco-stackwise-160&quot; |
| CISCO_STACKWISE_320 | &quot;cisco-stackwise-320&quot; |
| CISCO_STACKWISE_480 | &quot;cisco-stackwise-480&quot; |
| CISCO_STACKWISE_1T | &quot;cisco-stackwise-1t&quot; |
| JUNIPER_VCP | &quot;juniper-vcp&quot; |
| EXTREME_SUMMITSTACK | &quot;extreme-summitstack&quot; |
| EXTREME_SUMMITSTACK_128 | &quot;extreme-summitstack-128&quot; |
| EXTREME_SUMMITSTACK_256 | &quot;extreme-summitstack-256&quot; |
| EXTREME_SUMMITSTACK_512 | &quot;extreme-summitstack-512&quot; |
| OTHER | &quot;other&quot; |



