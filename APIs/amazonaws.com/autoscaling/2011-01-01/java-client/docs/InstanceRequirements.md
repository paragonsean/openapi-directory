

# InstanceRequirements

<p>The attributes for the instance types for a mixed instances policy. Amazon EC2 Auto Scaling uses your specified requirements to identify instance types. Then, it uses your On-Demand and Spot allocation strategies to launch instances from these instance types.</p> <p>When you specify multiple attributes, you get instance types that satisfy all of the specified attributes. If you specify multiple values for an attribute, you get instance types that satisfy any of the specified values.</p> <p>To limit the list of instance types from which Amazon EC2 Auto Scaling can identify matching instance types, you can use one of the following parameters, but not both in the same request:</p> <ul> <li> <p> <code>AllowedInstanceTypes</code> - The instance types to include in the list. All other instance types are ignored, even if they match your specified attributes.</p> </li> <li> <p> <code>ExcludedInstanceTypes</code> - The instance types to exclude from the list, even if they match your specified attributes.</p> </li> </ul> <note> <p>You must specify <code>VCpuCount</code> and <code>MemoryMiB</code>. All other attributes are optional. Any unspecified optional attribute is set to its default.</p> </note> <p>For more information, see <a href=\"https://docs.aws.amazon.com/autoscaling/ec2/userguide/create-asg-instance-type-requirements.html\">Creating an Auto Scaling group using attribute-based instance type selection</a> in the <i>Amazon EC2 Auto Scaling User Guide</i>. For help determining which instance types match your attributes before you apply them to your Auto Scaling group, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-fleet-attribute-based-instance-type-selection.html#ec2fleet-get-instance-types-from-instance-requirements\">Preview instance types with specified attributes</a> in the <i>Amazon EC2 User Guide for Linux Instances</i>.</p>

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**vcpuCount** | [**InstanceRequirementsVCpuCount**](InstanceRequirementsVCpuCount.md) |  |  |
|**memoryMiB** | [**InstanceRequirementsMemoryMiB**](InstanceRequirementsMemoryMiB.md) |  |  |
|**cpuManufacturers** | [**List**](List.md) |  |  [optional] |
|**memoryGiBPerVCpu** | [**InstanceRequirementsMemoryGiBPerVCpu**](InstanceRequirementsMemoryGiBPerVCpu.md) |  |  [optional] |
|**excludedInstanceTypes** | [**List**](List.md) |  |  [optional] |
|**instanceGenerations** | [**List**](List.md) |  |  [optional] |
|**spotMaxPricePercentageOverLowestPrice** | [**Integer**](Integer.md) |  |  [optional] |
|**onDemandMaxPricePercentageOverLowestPrice** | [**Integer**](Integer.md) |  |  [optional] |
|**bareMetal** | [**BareMetal**](BareMetal.md) |  |  [optional] |
|**burstablePerformance** | [**BurstablePerformance**](BurstablePerformance.md) |  |  [optional] |
|**requireHibernateSupport** | [**Boolean**](Boolean.md) |  |  [optional] |
|**networkInterfaceCount** | [**InstanceRequirementsNetworkInterfaceCount**](InstanceRequirementsNetworkInterfaceCount.md) |  |  [optional] |
|**localStorage** | [**LocalStorage**](LocalStorage.md) |  |  [optional] |
|**localStorageTypes** | [**List**](List.md) |  |  [optional] |
|**totalLocalStorageGB** | [**InstanceRequirementsTotalLocalStorageGB**](InstanceRequirementsTotalLocalStorageGB.md) |  |  [optional] |
|**baselineEbsBandwidthMbps** | [**InstanceRequirementsBaselineEbsBandwidthMbps**](InstanceRequirementsBaselineEbsBandwidthMbps.md) |  |  [optional] |
|**acceleratorTypes** | [**List**](List.md) |  |  [optional] |
|**acceleratorCount** | [**InstanceRequirementsAcceleratorCount**](InstanceRequirementsAcceleratorCount.md) |  |  [optional] |
|**acceleratorManufacturers** | [**List**](List.md) |  |  [optional] |
|**acceleratorNames** | [**List**](List.md) |  |  [optional] |
|**acceleratorTotalMemoryMiB** | [**InstanceRequirementsAcceleratorTotalMemoryMiB**](InstanceRequirementsAcceleratorTotalMemoryMiB.md) |  |  [optional] |
|**networkBandwidthGbps** | [**InstanceRequirementsNetworkBandwidthGbps**](InstanceRequirementsNetworkBandwidthGbps.md) |  |  [optional] |
|**allowedInstanceTypes** | [**List**](List.md) |  |  [optional] |



