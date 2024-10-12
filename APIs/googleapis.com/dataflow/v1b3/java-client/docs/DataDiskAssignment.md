

# DataDiskAssignment

Data disk assignment for a given VM instance.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**dataDisks** | **List&lt;String&gt;** | Mounted data disks. The order is important a data disk&#39;s 0-based index in this list defines which persistent directory the disk is mounted to, for example the list of { \&quot;myproject-1014-104817-4c2-harness-0-disk-0\&quot; }, { \&quot;myproject-1014-104817-4c2-harness-0-disk-1\&quot; }. |  [optional] |
|**vmInstance** | **String** | VM instance name the data disks mounted to, for example \&quot;myproject-1014-104817-4c2-harness-0\&quot;. |  [optional] |



