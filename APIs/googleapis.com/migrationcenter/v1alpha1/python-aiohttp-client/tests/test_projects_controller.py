# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.add_assets_to_group_request import AddAssetsToGroupRequest
from openapi_server.models.aggregate_assets_values_request import AggregateAssetsValuesRequest
from openapi_server.models.aggregate_assets_values_response import AggregateAssetsValuesResponse
from openapi_server.models.batch_delete_assets_request import BatchDeleteAssetsRequest
from openapi_server.models.batch_update_assets_request import BatchUpdateAssetsRequest
from openapi_server.models.batch_update_assets_response import BatchUpdateAssetsResponse
from openapi_server.models.error_frame import ErrorFrame
from openapi_server.models.frames import Frames
from openapi_server.models.group import Group
from openapi_server.models.import_data_file import ImportDataFile
from openapi_server.models.import_job import ImportJob
from openapi_server.models.list_assets_response import ListAssetsResponse
from openapi_server.models.list_error_frames_response import ListErrorFramesResponse
from openapi_server.models.list_groups_response import ListGroupsResponse
from openapi_server.models.list_import_data_files_response import ListImportDataFilesResponse
from openapi_server.models.list_import_jobs_response import ListImportJobsResponse
from openapi_server.models.list_locations_response import ListLocationsResponse
from openapi_server.models.list_operations_response import ListOperationsResponse
from openapi_server.models.list_preference_sets_response import ListPreferenceSetsResponse
from openapi_server.models.list_report_configs_response import ListReportConfigsResponse
from openapi_server.models.list_reports_response import ListReportsResponse
from openapi_server.models.list_sources_response import ListSourcesResponse
from openapi_server.models.operation import Operation
from openapi_server.models.preference_set import PreferenceSet
from openapi_server.models.remove_assets_from_group_request import RemoveAssetsFromGroupRequest
from openapi_server.models.report import Report
from openapi_server.models.report_config import ReportConfig
from openapi_server.models.run_import_job_request import RunImportJobRequest
from openapi_server.models.source import Source
from openapi_server.models.validate_import_job_request import ValidateImportJobRequest


pytestmark = pytest.mark.asyncio

async def test_migrationcenter_projects_locations_assets_aggregate_values(client):
    """Test case for migrationcenter_projects_locations_assets_aggregate_values

    
    """
    body = {"filter":"filter","showHidden":True,"aggregations":[{"histogram":{"lowerBounds":[0.8008281904610115,0.8008281904610115]},"field":"field","count":"{}","sum":"{}","frequency":"{}"},{"histogram":{"lowerBounds":[0.8008281904610115,0.8008281904610115]},"field":"field","count":"{}","sum":"{}","frequency":"{}"}]}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1alpha1/{parent}/assets:aggregateValues'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_migrationcenter_projects_locations_assets_batch_delete(client):
    """Test case for migrationcenter_projects_locations_assets_batch_delete

    
    """
    body = {"names":["names","names"],"allowMissing":True}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1alpha1/{parent}/assets:batchDelete'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_migrationcenter_projects_locations_assets_batch_update(client):
    """Test case for migrationcenter_projects_locations_assets_batch_update

    
    """
    body = {"requests":[{"requestId":"requestId","asset":{"insightList":{"insights":[{"softwareInsight":{"detectedSoftware":{"softwareName":"softwareName","softwareFamily":"softwareFamily"}},"migrationInsight":{"fit":{"fitLevel":"FIT_LEVEL_UNSPECIFIED"},"vmwareEngineTarget":"{}","computeEngineSoleTenantTarget":"{}","computeEngineTarget":{"shape":{"memoryMb":6,"physicalCoreCount":1,"series":"series","logicalCoreCount":0,"storage":[{"sizeGb":5,"type":"PERSISTENT_DISK_TYPE_UNSPECIFIED"},{"sizeGb":5,"type":"PERSISTENT_DISK_TYPE_UNSPECIFIED"}],"machineType":"machineType"}},"gkeTarget":"{}"},"genericInsight":{"additionalInformation":["additionalInformation","additionalInformation"],"defaultMessage":"defaultMessage","messageId":"messageId"}},{"softwareInsight":{"detectedSoftware":{"softwareName":"softwareName","softwareFamily":"softwareFamily"}},"migrationInsight":{"fit":{"fitLevel":"FIT_LEVEL_UNSPECIFIED"},"vmwareEngineTarget":"{}","computeEngineSoleTenantTarget":"{}","computeEngineTarget":{"shape":{"memoryMb":6,"physicalCoreCount":1,"series":"series","logicalCoreCount":0,"storage":[{"sizeGb":5,"type":"PERSISTENT_DISK_TYPE_UNSPECIFIED"},{"sizeGb":5,"type":"PERSISTENT_DISK_TYPE_UNSPECIFIED"}],"machineType":"machineType"}},"gkeTarget":"{}"},"genericInsight":{"additionalInformation":["additionalInformation","additionalInformation"],"defaultMessage":"defaultMessage","messageId":"messageId"}}],"updateTime":"updateTime"},"hidden":True,"sources":["sources","sources"],"performanceData":{"dailyResourceUsageAggregations":[{"date":{"month":2,"year":4,"day":3},"disk":{"iops":{"average":5.637377,"median":2.302136,"ninteyFifthPercentile":7.0614014,"peak":9.301444}},"memory":{"utilizationPercentage":{"average":5.637377,"median":2.302136,"ninteyFifthPercentile":7.0614014,"peak":9.301444}},"cpu":{"utilizationPercentage":{"average":5.637377,"median":2.302136,"ninteyFifthPercentile":7.0614014,"peak":9.301444}},"network":{"egressBps":{"average":5.637377,"median":2.302136,"ninteyFifthPercentile":7.0614014,"peak":9.301444},"ingressBps":{"average":5.637377,"median":2.302136,"ninteyFifthPercentile":7.0614014,"peak":9.301444}}},{"date":{"month":2,"year":4,"day":3},"disk":{"iops":{"average":5.637377,"median":2.302136,"ninteyFifthPercentile":7.0614014,"peak":9.301444}},"memory":{"utilizationPercentage":{"average":5.637377,"median":2.302136,"ninteyFifthPercentile":7.0614014,"peak":9.301444}},"cpu":{"utilizationPercentage":{"average":5.637377,"median":2.302136,"ninteyFifthPercentile":7.0614014,"peak":9.301444}},"network":{"egressBps":{"average":5.637377,"median":2.302136,"ninteyFifthPercentile":7.0614014,"peak":9.301444},"ingressBps":{"average":5.637377,"median":2.302136,"ninteyFifthPercentile":7.0614014,"peak":9.301444}}}]},"updateTime":"updateTime","hideTime":"hideTime","labels":{"key":"labels"},"createTime":"createTime","name":"name","attributes":{"key":"attributes"},"hideReason":"hideReason","virtualMachineDetails":{"vmName":"vmName","osFamily":"OS_FAMILY_UNKNOWN","osName":"osName","coreCount":2,"platform":{"genericDetails":{"location":"location"},"vmwareDetails":{"vcenterVersion":"vcenterVersion","osid":"osid","esxVersion":"esxVersion"},"azureVmDetails":{"location":"location","provisioningState":"provisioningState","machineTypeLabel":"machineTypeLabel"},"physicalDetails":{"location":"location"},"awsEc2Details":{"location":"location","machineTypeLabel":"machineTypeLabel"}},"vcenterUrl":"vcenterUrl","vcenterVmId":"vcenterVmId","vmDisks":{"hddTotalFreeBytes":"hddTotalFreeBytes","disks":{"entries":[{"partitions":{"entries":[{"fileSystem":"fileSystem","mountPoint":"mountPoint","capacityBytes":"capacityBytes","freeBytes":"freeBytes","type":"type","uuid":"uuid"},{"fileSystem":"fileSystem","mountPoint":"mountPoint","capacityBytes":"capacityBytes","freeBytes":"freeBytes","type":"type","uuid":"uuid"}]},"diskLabel":"diskLabel","interfaceType":"interfaceType","diskLabelType":"diskLabelType","vmwareConfig":{"shared":True,"rdmCompatibilityMode":"rdmCompatibilityMode","backingType":"BACKING_TYPE_UNSPECIFIED","vmdkDiskMode":"vmdkDiskMode"},"totalCapacityBytes":"totalCapacityBytes","hwAddress":"hwAddress","totalFreeBytes":"totalFreeBytes","status":"status"},{"partitions":{"entries":[{"fileSystem":"fileSystem","mountPoint":"mountPoint","capacityBytes":"capacityBytes","freeBytes":"freeBytes","type":"type","uuid":"uuid"},{"fileSystem":"fileSystem","mountPoint":"mountPoint","capacityBytes":"capacityBytes","freeBytes":"freeBytes","type":"type","uuid":"uuid"}]},"diskLabel":"diskLabel","interfaceType":"interfaceType","diskLabelType":"diskLabelType","vmwareConfig":{"shared":True,"rdmCompatibilityMode":"rdmCompatibilityMode","backingType":"BACKING_TYPE_UNSPECIFIED","vmdkDiskMode":"vmdkDiskMode"},"totalCapacityBytes":"totalCapacityBytes","hwAddress":"hwAddress","totalFreeBytes":"totalFreeBytes","status":"status"}]},"hddTotalCapacityBytes":"hddTotalCapacityBytes","lsblkJson":"lsblkJson"},"memoryMb":9,"guestOs":{"runtime":{"openFileList":{"entries":[{"filePath":"filePath","user":"user","command":"command","fileType":"fileType"},{"filePath":"filePath","user":"user","command":"command","fileType":"fileType"}]},"installedApps":{"entries":[{"path":"path","licenses":["licenses","licenses"],"vendor":"vendor","name":"name","time":"time","version":"version"},{"path":"path","licenses":["licenses","licenses"],"vendor":"vendor","name":"name","time":"time","version":"version"}]},"processes":{"processes":[{"cmdline":"cmdline","exePath":"exePath","attributes":{"key":"attributes"},"pid":"pid","user":"user"},{"cmdline":"cmdline","exePath":"exePath","attributes":{"key":"attributes"},"pid":"pid","user":"user"}]},"networkInfo":{"netstatTime":{"hours":1,"seconds":4,"utcOffset":"utcOffset","month":7,"nanos":1,"year":5,"minutes":6,"timeZone":{"id":"id","version":"version"},"day":1},"connections":{"entries":[{"protocol":"protocol","localPort":7,"processName":"processName","remotePort":1,"pid":"pid","state":"state","localIpAddress":"localIpAddress","remoteIpAddress":"remoteIpAddress"},{"protocol":"protocol","localPort":7,"processName":"processName","remotePort":1,"pid":"pid","state":"state","localIpAddress":"localIpAddress","remoteIpAddress":"remoteIpAddress"}]},"netstat":"netstat"},"domain":"domain","services":{"services":[{"cmdline":"cmdline","exePath":"exePath","startMode":"startMode","name":"name","pid":"pid","state":"state","status":"status"},{"cmdline":"cmdline","exePath":"exePath","startMode":"startMode","name":"name","pid":"pid","state":"state","status":"status"}]},"lastUptime":{"month":2,"year":4,"day":3},"machineName":"machineName"},"config":{"issue":"issue","hosts":{"entries":[{"hostNames":["hostNames","hostNames"],"ip":"ip"},{"hostNames":["hostNames","hostNames"],"ip":"ip"}]},"fstab":{"entries":[{"file":"file","vfstype":"vfstype","freq":7,"passno":9,"mntops":"mntops","spec":"spec"},{"file":"file","vfstype":"vfstype","freq":7,"passno":9,"mntops":"mntops","spec":"spec"}]},"selinux":{"mode":"mode","enabled":True},"nfsExports":{"entries":[{"hosts":["hosts","hosts"],"exportDirectory":"exportDirectory"},{"hosts":["hosts","hosts"],"exportDirectory":"exportDirectory"}]}}},"vmNetwork":{"primaryMacAddress":"primaryMacAddress","publicIpAddress":"publicIpAddress","defaultGw":"defaultGw","primaryIpAddress":"primaryIpAddress","networkAdapters":{"networkAdapters":[{"addresses":{"addresses":[{"bcast":"bcast","fqdn":"fqdn","assignment":"ADDRESS_ASSIGNMENT_UNSPECIFIED","ipAddress":"ipAddress","subnetMask":"subnetMask"},{"bcast":"bcast","fqdn":"fqdn","assignment":"ADDRESS_ASSIGNMENT_UNSPECIFIED","ipAddress":"ipAddress","subnetMask":"subnetMask"}]},"macAddress":"macAddress","adapterType":"adapterType"},{"addresses":{"addresses":[{"bcast":"bcast","fqdn":"fqdn","assignment":"ADDRESS_ASSIGNMENT_UNSPECIFIED","ipAddress":"ipAddress","subnetMask":"subnetMask"},{"bcast":"bcast","fqdn":"fqdn","assignment":"ADDRESS_ASSIGNMENT_UNSPECIFIED","ipAddress":"ipAddress","subnetMask":"subnetMask"}]},"macAddress":"macAddress","adapterType":"adapterType"}]}},"powerState":"powerState","osVersion":"osVersion","createTime":"createTime","vmArchitecture":{"cpuSocketCount":9,"cpuThreadCount":6,"cpuManufacturer":"cpuManufacturer","bios":{"biosVersion":"biosVersion","biosName":"biosName","biosReleaseDate":"biosReleaseDate","biosManufacturer":"biosManufacturer","smbiosUuid":"smbiosUuid"},"vendor":"vendor","cpuArchitecture":"cpuArchitecture","firmware":"firmware","hyperthreading":"HYPER_THREADING_UNSPECIFIED","cpuName":"cpuName"},"vmUuid":"vmUuid","vcenterFolder":"vcenterFolder"},"assignedGroups":["assignedGroups","assignedGroups"]},"updateMask":"updateMask"},{"requestId":"requestId","asset":{"insightList":{"insights":[{"softwareInsight":{"detectedSoftware":{"softwareName":"softwareName","softwareFamily":"softwareFamily"}},"migrationInsight":{"fit":{"fitLevel":"FIT_LEVEL_UNSPECIFIED"},"vmwareEngineTarget":"{}","computeEngineSoleTenantTarget":"{}","computeEngineTarget":{"shape":{"memoryMb":6,"physicalCoreCount":1,"series":"series","logicalCoreCount":0,"storage":[{"sizeGb":5,"type":"PERSISTENT_DISK_TYPE_UNSPECIFIED"},{"sizeGb":5,"type":"PERSISTENT_DISK_TYPE_UNSPECIFIED"}],"machineType":"machineType"}},"gkeTarget":"{}"},"genericInsight":{"additionalInformation":["additionalInformation","additionalInformation"],"defaultMessage":"defaultMessage","messageId":"messageId"}},{"softwareInsight":{"detectedSoftware":{"softwareName":"softwareName","softwareFamily":"softwareFamily"}},"migrationInsight":{"fit":{"fitLevel":"FIT_LEVEL_UNSPECIFIED"},"vmwareEngineTarget":"{}","computeEngineSoleTenantTarget":"{}","computeEngineTarget":{"shape":{"memoryMb":6,"physicalCoreCount":1,"series":"series","logicalCoreCount":0,"storage":[{"sizeGb":5,"type":"PERSISTENT_DISK_TYPE_UNSPECIFIED"},{"sizeGb":5,"type":"PERSISTENT_DISK_TYPE_UNSPECIFIED"}],"machineType":"machineType"}},"gkeTarget":"{}"},"genericInsight":{"additionalInformation":["additionalInformation","additionalInformation"],"defaultMessage":"defaultMessage","messageId":"messageId"}}],"updateTime":"updateTime"},"hidden":True,"sources":["sources","sources"],"performanceData":{"dailyResourceUsageAggregations":[{"date":{"month":2,"year":4,"day":3},"disk":{"iops":{"average":5.637377,"median":2.302136,"ninteyFifthPercentile":7.0614014,"peak":9.301444}},"memory":{"utilizationPercentage":{"average":5.637377,"median":2.302136,"ninteyFifthPercentile":7.0614014,"peak":9.301444}},"cpu":{"utilizationPercentage":{"average":5.637377,"median":2.302136,"ninteyFifthPercentile":7.0614014,"peak":9.301444}},"network":{"egressBps":{"average":5.637377,"median":2.302136,"ninteyFifthPercentile":7.0614014,"peak":9.301444},"ingressBps":{"average":5.637377,"median":2.302136,"ninteyFifthPercentile":7.0614014,"peak":9.301444}}},{"date":{"month":2,"year":4,"day":3},"disk":{"iops":{"average":5.637377,"median":2.302136,"ninteyFifthPercentile":7.0614014,"peak":9.301444}},"memory":{"utilizationPercentage":{"average":5.637377,"median":2.302136,"ninteyFifthPercentile":7.0614014,"peak":9.301444}},"cpu":{"utilizationPercentage":{"average":5.637377,"median":2.302136,"ninteyFifthPercentile":7.0614014,"peak":9.301444}},"network":{"egressBps":{"average":5.637377,"median":2.302136,"ninteyFifthPercentile":7.0614014,"peak":9.301444},"ingressBps":{"average":5.637377,"median":2.302136,"ninteyFifthPercentile":7.0614014,"peak":9.301444}}}]},"updateTime":"updateTime","hideTime":"hideTime","labels":{"key":"labels"},"createTime":"createTime","name":"name","attributes":{"key":"attributes"},"hideReason":"hideReason","virtualMachineDetails":{"vmName":"vmName","osFamily":"OS_FAMILY_UNKNOWN","osName":"osName","coreCount":2,"platform":{"genericDetails":{"location":"location"},"vmwareDetails":{"vcenterVersion":"vcenterVersion","osid":"osid","esxVersion":"esxVersion"},"azureVmDetails":{"location":"location","provisioningState":"provisioningState","machineTypeLabel":"machineTypeLabel"},"physicalDetails":{"location":"location"},"awsEc2Details":{"location":"location","machineTypeLabel":"machineTypeLabel"}},"vcenterUrl":"vcenterUrl","vcenterVmId":"vcenterVmId","vmDisks":{"hddTotalFreeBytes":"hddTotalFreeBytes","disks":{"entries":[{"partitions":{"entries":[{"fileSystem":"fileSystem","mountPoint":"mountPoint","capacityBytes":"capacityBytes","freeBytes":"freeBytes","type":"type","uuid":"uuid"},{"fileSystem":"fileSystem","mountPoint":"mountPoint","capacityBytes":"capacityBytes","freeBytes":"freeBytes","type":"type","uuid":"uuid"}]},"diskLabel":"diskLabel","interfaceType":"interfaceType","diskLabelType":"diskLabelType","vmwareConfig":{"shared":True,"rdmCompatibilityMode":"rdmCompatibilityMode","backingType":"BACKING_TYPE_UNSPECIFIED","vmdkDiskMode":"vmdkDiskMode"},"totalCapacityBytes":"totalCapacityBytes","hwAddress":"hwAddress","totalFreeBytes":"totalFreeBytes","status":"status"},{"partitions":{"entries":[{"fileSystem":"fileSystem","mountPoint":"mountPoint","capacityBytes":"capacityBytes","freeBytes":"freeBytes","type":"type","uuid":"uuid"},{"fileSystem":"fileSystem","mountPoint":"mountPoint","capacityBytes":"capacityBytes","freeBytes":"freeBytes","type":"type","uuid":"uuid"}]},"diskLabel":"diskLabel","interfaceType":"interfaceType","diskLabelType":"diskLabelType","vmwareConfig":{"shared":True,"rdmCompatibilityMode":"rdmCompatibilityMode","backingType":"BACKING_TYPE_UNSPECIFIED","vmdkDiskMode":"vmdkDiskMode"},"totalCapacityBytes":"totalCapacityBytes","hwAddress":"hwAddress","totalFreeBytes":"totalFreeBytes","status":"status"}]},"hddTotalCapacityBytes":"hddTotalCapacityBytes","lsblkJson":"lsblkJson"},"memoryMb":9,"guestOs":{"runtime":{"openFileList":{"entries":[{"filePath":"filePath","user":"user","command":"command","fileType":"fileType"},{"filePath":"filePath","user":"user","command":"command","fileType":"fileType"}]},"installedApps":{"entries":[{"path":"path","licenses":["licenses","licenses"],"vendor":"vendor","name":"name","time":"time","version":"version"},{"path":"path","licenses":["licenses","licenses"],"vendor":"vendor","name":"name","time":"time","version":"version"}]},"processes":{"processes":[{"cmdline":"cmdline","exePath":"exePath","attributes":{"key":"attributes"},"pid":"pid","user":"user"},{"cmdline":"cmdline","exePath":"exePath","attributes":{"key":"attributes"},"pid":"pid","user":"user"}]},"networkInfo":{"netstatTime":{"hours":1,"seconds":4,"utcOffset":"utcOffset","month":7,"nanos":1,"year":5,"minutes":6,"timeZone":{"id":"id","version":"version"},"day":1},"connections":{"entries":[{"protocol":"protocol","localPort":7,"processName":"processName","remotePort":1,"pid":"pid","state":"state","localIpAddress":"localIpAddress","remoteIpAddress":"remoteIpAddress"},{"protocol":"protocol","localPort":7,"processName":"processName","remotePort":1,"pid":"pid","state":"state","localIpAddress":"localIpAddress","remoteIpAddress":"remoteIpAddress"}]},"netstat":"netstat"},"domain":"domain","services":{"services":[{"cmdline":"cmdline","exePath":"exePath","startMode":"startMode","name":"name","pid":"pid","state":"state","status":"status"},{"cmdline":"cmdline","exePath":"exePath","startMode":"startMode","name":"name","pid":"pid","state":"state","status":"status"}]},"lastUptime":{"month":2,"year":4,"day":3},"machineName":"machineName"},"config":{"issue":"issue","hosts":{"entries":[{"hostNames":["hostNames","hostNames"],"ip":"ip"},{"hostNames":["hostNames","hostNames"],"ip":"ip"}]},"fstab":{"entries":[{"file":"file","vfstype":"vfstype","freq":7,"passno":9,"mntops":"mntops","spec":"spec"},{"file":"file","vfstype":"vfstype","freq":7,"passno":9,"mntops":"mntops","spec":"spec"}]},"selinux":{"mode":"mode","enabled":True},"nfsExports":{"entries":[{"hosts":["hosts","hosts"],"exportDirectory":"exportDirectory"},{"hosts":["hosts","hosts"],"exportDirectory":"exportDirectory"}]}}},"vmNetwork":{"primaryMacAddress":"primaryMacAddress","publicIpAddress":"publicIpAddress","defaultGw":"defaultGw","primaryIpAddress":"primaryIpAddress","networkAdapters":{"networkAdapters":[{"addresses":{"addresses":[{"bcast":"bcast","fqdn":"fqdn","assignment":"ADDRESS_ASSIGNMENT_UNSPECIFIED","ipAddress":"ipAddress","subnetMask":"subnetMask"},{"bcast":"bcast","fqdn":"fqdn","assignment":"ADDRESS_ASSIGNMENT_UNSPECIFIED","ipAddress":"ipAddress","subnetMask":"subnetMask"}]},"macAddress":"macAddress","adapterType":"adapterType"},{"addresses":{"addresses":[{"bcast":"bcast","fqdn":"fqdn","assignment":"ADDRESS_ASSIGNMENT_UNSPECIFIED","ipAddress":"ipAddress","subnetMask":"subnetMask"},{"bcast":"bcast","fqdn":"fqdn","assignment":"ADDRESS_ASSIGNMENT_UNSPECIFIED","ipAddress":"ipAddress","subnetMask":"subnetMask"}]},"macAddress":"macAddress","adapterType":"adapterType"}]}},"powerState":"powerState","osVersion":"osVersion","createTime":"createTime","vmArchitecture":{"cpuSocketCount":9,"cpuThreadCount":6,"cpuManufacturer":"cpuManufacturer","bios":{"biosVersion":"biosVersion","biosName":"biosName","biosReleaseDate":"biosReleaseDate","biosManufacturer":"biosManufacturer","smbiosUuid":"smbiosUuid"},"vendor":"vendor","cpuArchitecture":"cpuArchitecture","firmware":"firmware","hyperthreading":"HYPER_THREADING_UNSPECIFIED","cpuName":"cpuName"},"vmUuid":"vmUuid","vcenterFolder":"vcenterFolder"},"assignedGroups":["assignedGroups","assignedGroups"]},"updateMask":"updateMask"}]}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1alpha1/{parent}/assets:batchUpdate'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_migrationcenter_projects_locations_assets_list(client):
    """Test case for migrationcenter_projects_locations_assets_list

    
    """
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example'),
                    ('filter', 'filter_example'),
                    ('orderBy', 'order_by_example'),
                    ('pageSize', 56),
                    ('pageToken', 'page_token_example'),
                    ('showHidden', True),
                    ('view', 'view_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1alpha1/{parent}/assets'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_migrationcenter_projects_locations_assets_report_asset_frames(client):
    """Test case for migrationcenter_projects_locations_assets_report_asset_frames

    
    """
    body = {"framesData":[{"attributes":{"key":"attributes"},"performanceSamples":[{"disk":{"averageIops":6.0274563},"memory":{"utilizedPercentage":1.4658129},"cpu":{"utilizedPercentage":0.8008282},"network":{"averageEgressBps":5.962134,"averageIngressBps":5.637377},"sampleTime":"sampleTime"},{"disk":{"averageIops":6.0274563},"memory":{"utilizedPercentage":1.4658129},"cpu":{"utilizedPercentage":0.8008282},"network":{"averageEgressBps":5.962134,"averageIngressBps":5.637377},"sampleTime":"sampleTime"}],"traceToken":"traceToken","virtualMachineDetails":{"vmName":"vmName","osFamily":"OS_FAMILY_UNKNOWN","osName":"osName","coreCount":2,"platform":{"genericDetails":{"location":"location"},"vmwareDetails":{"vcenterVersion":"vcenterVersion","osid":"osid","esxVersion":"esxVersion"},"azureVmDetails":{"location":"location","provisioningState":"provisioningState","machineTypeLabel":"machineTypeLabel"},"physicalDetails":{"location":"location"},"awsEc2Details":{"location":"location","machineTypeLabel":"machineTypeLabel"}},"vcenterUrl":"vcenterUrl","vcenterVmId":"vcenterVmId","vmDisks":{"hddTotalFreeBytes":"hddTotalFreeBytes","disks":{"entries":[{"partitions":{"entries":[{"fileSystem":"fileSystem","mountPoint":"mountPoint","capacityBytes":"capacityBytes","freeBytes":"freeBytes","type":"type","uuid":"uuid"},{"fileSystem":"fileSystem","mountPoint":"mountPoint","capacityBytes":"capacityBytes","freeBytes":"freeBytes","type":"type","uuid":"uuid"}]},"diskLabel":"diskLabel","interfaceType":"interfaceType","diskLabelType":"diskLabelType","vmwareConfig":{"shared":True,"rdmCompatibilityMode":"rdmCompatibilityMode","backingType":"BACKING_TYPE_UNSPECIFIED","vmdkDiskMode":"vmdkDiskMode"},"totalCapacityBytes":"totalCapacityBytes","hwAddress":"hwAddress","totalFreeBytes":"totalFreeBytes","status":"status"},{"partitions":{"entries":[{"fileSystem":"fileSystem","mountPoint":"mountPoint","capacityBytes":"capacityBytes","freeBytes":"freeBytes","type":"type","uuid":"uuid"},{"fileSystem":"fileSystem","mountPoint":"mountPoint","capacityBytes":"capacityBytes","freeBytes":"freeBytes","type":"type","uuid":"uuid"}]},"diskLabel":"diskLabel","interfaceType":"interfaceType","diskLabelType":"diskLabelType","vmwareConfig":{"shared":True,"rdmCompatibilityMode":"rdmCompatibilityMode","backingType":"BACKING_TYPE_UNSPECIFIED","vmdkDiskMode":"vmdkDiskMode"},"totalCapacityBytes":"totalCapacityBytes","hwAddress":"hwAddress","totalFreeBytes":"totalFreeBytes","status":"status"}]},"hddTotalCapacityBytes":"hddTotalCapacityBytes","lsblkJson":"lsblkJson"},"memoryMb":9,"guestOs":{"runtime":{"openFileList":{"entries":[{"filePath":"filePath","user":"user","command":"command","fileType":"fileType"},{"filePath":"filePath","user":"user","command":"command","fileType":"fileType"}]},"installedApps":{"entries":[{"path":"path","licenses":["licenses","licenses"],"vendor":"vendor","name":"name","time":"time","version":"version"},{"path":"path","licenses":["licenses","licenses"],"vendor":"vendor","name":"name","time":"time","version":"version"}]},"processes":{"processes":[{"cmdline":"cmdline","exePath":"exePath","attributes":{"key":"attributes"},"pid":"pid","user":"user"},{"cmdline":"cmdline","exePath":"exePath","attributes":{"key":"attributes"},"pid":"pid","user":"user"}]},"networkInfo":{"netstatTime":{"hours":1,"seconds":4,"utcOffset":"utcOffset","month":7,"nanos":1,"year":5,"minutes":6,"timeZone":{"id":"id","version":"version"},"day":1},"connections":{"entries":[{"protocol":"protocol","localPort":7,"processName":"processName","remotePort":1,"pid":"pid","state":"state","localIpAddress":"localIpAddress","remoteIpAddress":"remoteIpAddress"},{"protocol":"protocol","localPort":7,"processName":"processName","remotePort":1,"pid":"pid","state":"state","localIpAddress":"localIpAddress","remoteIpAddress":"remoteIpAddress"}]},"netstat":"netstat"},"domain":"domain","services":{"services":[{"cmdline":"cmdline","exePath":"exePath","startMode":"startMode","name":"name","pid":"pid","state":"state","status":"status"},{"cmdline":"cmdline","exePath":"exePath","startMode":"startMode","name":"name","pid":"pid","state":"state","status":"status"}]},"lastUptime":{"month":2,"year":4,"day":3},"machineName":"machineName"},"config":{"issue":"issue","hosts":{"entries":[{"hostNames":["hostNames","hostNames"],"ip":"ip"},{"hostNames":["hostNames","hostNames"],"ip":"ip"}]},"fstab":{"entries":[{"file":"file","vfstype":"vfstype","freq":7,"passno":9,"mntops":"mntops","spec":"spec"},{"file":"file","vfstype":"vfstype","freq":7,"passno":9,"mntops":"mntops","spec":"spec"}]},"selinux":{"mode":"mode","enabled":True},"nfsExports":{"entries":[{"hosts":["hosts","hosts"],"exportDirectory":"exportDirectory"},{"hosts":["hosts","hosts"],"exportDirectory":"exportDirectory"}]}}},"vmNetwork":{"primaryMacAddress":"primaryMacAddress","publicIpAddress":"publicIpAddress","defaultGw":"defaultGw","primaryIpAddress":"primaryIpAddress","networkAdapters":{"networkAdapters":[{"addresses":{"addresses":[{"bcast":"bcast","fqdn":"fqdn","assignment":"ADDRESS_ASSIGNMENT_UNSPECIFIED","ipAddress":"ipAddress","subnetMask":"subnetMask"},{"bcast":"bcast","fqdn":"fqdn","assignment":"ADDRESS_ASSIGNMENT_UNSPECIFIED","ipAddress":"ipAddress","subnetMask":"subnetMask"}]},"macAddress":"macAddress","adapterType":"adapterType"},{"addresses":{"addresses":[{"bcast":"bcast","fqdn":"fqdn","assignment":"ADDRESS_ASSIGNMENT_UNSPECIFIED","ipAddress":"ipAddress","subnetMask":"subnetMask"},{"bcast":"bcast","fqdn":"fqdn","assignment":"ADDRESS_ASSIGNMENT_UNSPECIFIED","ipAddress":"ipAddress","subnetMask":"subnetMask"}]},"macAddress":"macAddress","adapterType":"adapterType"}]}},"powerState":"powerState","osVersion":"osVersion","createTime":"createTime","vmArchitecture":{"cpuSocketCount":9,"cpuThreadCount":6,"cpuManufacturer":"cpuManufacturer","bios":{"biosVersion":"biosVersion","biosName":"biosName","biosReleaseDate":"biosReleaseDate","biosManufacturer":"biosManufacturer","smbiosUuid":"smbiosUuid"},"vendor":"vendor","cpuArchitecture":"cpuArchitecture","firmware":"firmware","hyperthreading":"HYPER_THREADING_UNSPECIFIED","cpuName":"cpuName"},"vmUuid":"vmUuid","vcenterFolder":"vcenterFolder"},"labels":{"key":"labels"},"reportTime":"reportTime"},{"attributes":{"key":"attributes"},"performanceSamples":[{"disk":{"averageIops":6.0274563},"memory":{"utilizedPercentage":1.4658129},"cpu":{"utilizedPercentage":0.8008282},"network":{"averageEgressBps":5.962134,"averageIngressBps":5.637377},"sampleTime":"sampleTime"},{"disk":{"averageIops":6.0274563},"memory":{"utilizedPercentage":1.4658129},"cpu":{"utilizedPercentage":0.8008282},"network":{"averageEgressBps":5.962134,"averageIngressBps":5.637377},"sampleTime":"sampleTime"}],"traceToken":"traceToken","virtualMachineDetails":{"vmName":"vmName","osFamily":"OS_FAMILY_UNKNOWN","osName":"osName","coreCount":2,"platform":{"genericDetails":{"location":"location"},"vmwareDetails":{"vcenterVersion":"vcenterVersion","osid":"osid","esxVersion":"esxVersion"},"azureVmDetails":{"location":"location","provisioningState":"provisioningState","machineTypeLabel":"machineTypeLabel"},"physicalDetails":{"location":"location"},"awsEc2Details":{"location":"location","machineTypeLabel":"machineTypeLabel"}},"vcenterUrl":"vcenterUrl","vcenterVmId":"vcenterVmId","vmDisks":{"hddTotalFreeBytes":"hddTotalFreeBytes","disks":{"entries":[{"partitions":{"entries":[{"fileSystem":"fileSystem","mountPoint":"mountPoint","capacityBytes":"capacityBytes","freeBytes":"freeBytes","type":"type","uuid":"uuid"},{"fileSystem":"fileSystem","mountPoint":"mountPoint","capacityBytes":"capacityBytes","freeBytes":"freeBytes","type":"type","uuid":"uuid"}]},"diskLabel":"diskLabel","interfaceType":"interfaceType","diskLabelType":"diskLabelType","vmwareConfig":{"shared":True,"rdmCompatibilityMode":"rdmCompatibilityMode","backingType":"BACKING_TYPE_UNSPECIFIED","vmdkDiskMode":"vmdkDiskMode"},"totalCapacityBytes":"totalCapacityBytes","hwAddress":"hwAddress","totalFreeBytes":"totalFreeBytes","status":"status"},{"partitions":{"entries":[{"fileSystem":"fileSystem","mountPoint":"mountPoint","capacityBytes":"capacityBytes","freeBytes":"freeBytes","type":"type","uuid":"uuid"},{"fileSystem":"fileSystem","mountPoint":"mountPoint","capacityBytes":"capacityBytes","freeBytes":"freeBytes","type":"type","uuid":"uuid"}]},"diskLabel":"diskLabel","interfaceType":"interfaceType","diskLabelType":"diskLabelType","vmwareConfig":{"shared":True,"rdmCompatibilityMode":"rdmCompatibilityMode","backingType":"BACKING_TYPE_UNSPECIFIED","vmdkDiskMode":"vmdkDiskMode"},"totalCapacityBytes":"totalCapacityBytes","hwAddress":"hwAddress","totalFreeBytes":"totalFreeBytes","status":"status"}]},"hddTotalCapacityBytes":"hddTotalCapacityBytes","lsblkJson":"lsblkJson"},"memoryMb":9,"guestOs":{"runtime":{"openFileList":{"entries":[{"filePath":"filePath","user":"user","command":"command","fileType":"fileType"},{"filePath":"filePath","user":"user","command":"command","fileType":"fileType"}]},"installedApps":{"entries":[{"path":"path","licenses":["licenses","licenses"],"vendor":"vendor","name":"name","time":"time","version":"version"},{"path":"path","licenses":["licenses","licenses"],"vendor":"vendor","name":"name","time":"time","version":"version"}]},"processes":{"processes":[{"cmdline":"cmdline","exePath":"exePath","attributes":{"key":"attributes"},"pid":"pid","user":"user"},{"cmdline":"cmdline","exePath":"exePath","attributes":{"key":"attributes"},"pid":"pid","user":"user"}]},"networkInfo":{"netstatTime":{"hours":1,"seconds":4,"utcOffset":"utcOffset","month":7,"nanos":1,"year":5,"minutes":6,"timeZone":{"id":"id","version":"version"},"day":1},"connections":{"entries":[{"protocol":"protocol","localPort":7,"processName":"processName","remotePort":1,"pid":"pid","state":"state","localIpAddress":"localIpAddress","remoteIpAddress":"remoteIpAddress"},{"protocol":"protocol","localPort":7,"processName":"processName","remotePort":1,"pid":"pid","state":"state","localIpAddress":"localIpAddress","remoteIpAddress":"remoteIpAddress"}]},"netstat":"netstat"},"domain":"domain","services":{"services":[{"cmdline":"cmdline","exePath":"exePath","startMode":"startMode","name":"name","pid":"pid","state":"state","status":"status"},{"cmdline":"cmdline","exePath":"exePath","startMode":"startMode","name":"name","pid":"pid","state":"state","status":"status"}]},"lastUptime":{"month":2,"year":4,"day":3},"machineName":"machineName"},"config":{"issue":"issue","hosts":{"entries":[{"hostNames":["hostNames","hostNames"],"ip":"ip"},{"hostNames":["hostNames","hostNames"],"ip":"ip"}]},"fstab":{"entries":[{"file":"file","vfstype":"vfstype","freq":7,"passno":9,"mntops":"mntops","spec":"spec"},{"file":"file","vfstype":"vfstype","freq":7,"passno":9,"mntops":"mntops","spec":"spec"}]},"selinux":{"mode":"mode","enabled":True},"nfsExports":{"entries":[{"hosts":["hosts","hosts"],"exportDirectory":"exportDirectory"},{"hosts":["hosts","hosts"],"exportDirectory":"exportDirectory"}]}}},"vmNetwork":{"primaryMacAddress":"primaryMacAddress","publicIpAddress":"publicIpAddress","defaultGw":"defaultGw","primaryIpAddress":"primaryIpAddress","networkAdapters":{"networkAdapters":[{"addresses":{"addresses":[{"bcast":"bcast","fqdn":"fqdn","assignment":"ADDRESS_ASSIGNMENT_UNSPECIFIED","ipAddress":"ipAddress","subnetMask":"subnetMask"},{"bcast":"bcast","fqdn":"fqdn","assignment":"ADDRESS_ASSIGNMENT_UNSPECIFIED","ipAddress":"ipAddress","subnetMask":"subnetMask"}]},"macAddress":"macAddress","adapterType":"adapterType"},{"addresses":{"addresses":[{"bcast":"bcast","fqdn":"fqdn","assignment":"ADDRESS_ASSIGNMENT_UNSPECIFIED","ipAddress":"ipAddress","subnetMask":"subnetMask"},{"bcast":"bcast","fqdn":"fqdn","assignment":"ADDRESS_ASSIGNMENT_UNSPECIFIED","ipAddress":"ipAddress","subnetMask":"subnetMask"}]},"macAddress":"macAddress","adapterType":"adapterType"}]}},"powerState":"powerState","osVersion":"osVersion","createTime":"createTime","vmArchitecture":{"cpuSocketCount":9,"cpuThreadCount":6,"cpuManufacturer":"cpuManufacturer","bios":{"biosVersion":"biosVersion","biosName":"biosName","biosReleaseDate":"biosReleaseDate","biosManufacturer":"biosManufacturer","smbiosUuid":"smbiosUuid"},"vendor":"vendor","cpuArchitecture":"cpuArchitecture","firmware":"firmware","hyperthreading":"HYPER_THREADING_UNSPECIFIED","cpuName":"cpuName"},"vmUuid":"vmUuid","vcenterFolder":"vcenterFolder"},"labels":{"key":"labels"},"reportTime":"reportTime"}]}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example'),
                    ('source', 'source_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1alpha1/{parent}/assets:reportAssetFrames'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_migrationcenter_projects_locations_groups_add_assets(client):
    """Test case for migrationcenter_projects_locations_groups_add_assets

    
    """
    body = {"assets":{"assetIds":["assetIds","assetIds"]},"requestId":"requestId","allowExisting":True}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1alpha1/{groupadd_asset}'.format(group='group_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_migrationcenter_projects_locations_groups_create(client):
    """Test case for migrationcenter_projects_locations_groups_create

    
    """
    body = {"createTime":"createTime","displayName":"displayName","name":"name","description":"description","updateTime":"updateTime","labels":{"key":"labels"}}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example'),
                    ('groupId', 'group_id_example'),
                    ('requestId', 'request_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1alpha1/{parent}/groups'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_migrationcenter_projects_locations_groups_list(client):
    """Test case for migrationcenter_projects_locations_groups_list

    
    """
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example'),
                    ('filter', 'filter_example'),
                    ('orderBy', 'order_by_example'),
                    ('pageSize', 56),
                    ('pageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1alpha1/{parent}/groups'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_migrationcenter_projects_locations_groups_remove_assets(client):
    """Test case for migrationcenter_projects_locations_groups_remove_assets

    
    """
    body = {"assets":{"assetIds":["assetIds","assetIds"]},"requestId":"requestId","allowMissing":True}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1alpha1/{groupremove_asset}'.format(group='group_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_migrationcenter_projects_locations_import_jobs_create(client):
    """Test case for migrationcenter_projects_locations_import_jobs_create

    
    """
    body = {"createTime":"createTime","inlinePayload":{"payload":[{"data":"data","name":"name"},{"data":"data","name":"name"}],"format":"IMPORT_JOB_FORMAT_UNSPECIFIED"},"displayName":"displayName","executionReport":{"totalRowsCount":1,"executionErrors":{"fileValidations":[{"fileName":"fileName","partialReport":True,"fileErrors":[{"severity":"SEVERITY_UNSPECIFIED","errorDetails":"errorDetails"},{"severity":"SEVERITY_UNSPECIFIED","errorDetails":"errorDetails"}],"rowErrors":[{"vmName":"vmName","vmUuid":"vmUuid","rowNumber":0,"errors":[{"severity":"SEVERITY_UNSPECIFIED","errorDetails":"errorDetails"},{"severity":"SEVERITY_UNSPECIFIED","errorDetails":"errorDetails"}]},{"vmName":"vmName","vmUuid":"vmUuid","rowNumber":0,"errors":[{"severity":"SEVERITY_UNSPECIFIED","errorDetails":"errorDetails"},{"severity":"SEVERITY_UNSPECIFIED","errorDetails":"errorDetails"}]}]},{"fileName":"fileName","partialReport":True,"fileErrors":[{"severity":"SEVERITY_UNSPECIFIED","errorDetails":"errorDetails"},{"severity":"SEVERITY_UNSPECIFIED","errorDetails":"errorDetails"}],"rowErrors":[{"vmName":"vmName","vmUuid":"vmUuid","rowNumber":0,"errors":[{"severity":"SEVERITY_UNSPECIFIED","errorDetails":"errorDetails"},{"severity":"SEVERITY_UNSPECIFIED","errorDetails":"errorDetails"}]},{"vmName":"vmName","vmUuid":"vmUuid","rowNumber":0,"errors":[{"severity":"SEVERITY_UNSPECIFIED","errorDetails":"errorDetails"},{"severity":"SEVERITY_UNSPECIFIED","errorDetails":"errorDetails"}]}]}],"jobErrors":[{"severity":"SEVERITY_UNSPECIFIED","errorDetails":"errorDetails"},{"severity":"SEVERITY_UNSPECIFIED","errorDetails":"errorDetails"}]},"framesReported":6,"jobErrors":[{"severity":"SEVERITY_UNSPECIFIED","errorDetails":"errorDetails"},{"severity":"SEVERITY_UNSPECIFIED","errorDetails":"errorDetails"}]},"gcsPayload":{"path":"path","format":"IMPORT_JOB_FORMAT_UNSPECIFIED"},"name":"name","assetSource":"assetSource","completeTime":"completeTime","validationReport":{"fileValidations":[{"fileName":"fileName","partialReport":True,"fileErrors":[{"severity":"SEVERITY_UNSPECIFIED","errorDetails":"errorDetails"},{"severity":"SEVERITY_UNSPECIFIED","errorDetails":"errorDetails"}],"rowErrors":[{"vmName":"vmName","vmUuid":"vmUuid","rowNumber":0,"errors":[{"severity":"SEVERITY_UNSPECIFIED","errorDetails":"errorDetails"},{"severity":"SEVERITY_UNSPECIFIED","errorDetails":"errorDetails"}]},{"vmName":"vmName","vmUuid":"vmUuid","rowNumber":0,"errors":[{"severity":"SEVERITY_UNSPECIFIED","errorDetails":"errorDetails"},{"severity":"SEVERITY_UNSPECIFIED","errorDetails":"errorDetails"}]}]},{"fileName":"fileName","partialReport":True,"fileErrors":[{"severity":"SEVERITY_UNSPECIFIED","errorDetails":"errorDetails"},{"severity":"SEVERITY_UNSPECIFIED","errorDetails":"errorDetails"}],"rowErrors":[{"vmName":"vmName","vmUuid":"vmUuid","rowNumber":0,"errors":[{"severity":"SEVERITY_UNSPECIFIED","errorDetails":"errorDetails"},{"severity":"SEVERITY_UNSPECIFIED","errorDetails":"errorDetails"}]},{"vmName":"vmName","vmUuid":"vmUuid","rowNumber":0,"errors":[{"severity":"SEVERITY_UNSPECIFIED","errorDetails":"errorDetails"},{"severity":"SEVERITY_UNSPECIFIED","errorDetails":"errorDetails"}]}]}],"jobErrors":[{"severity":"SEVERITY_UNSPECIFIED","errorDetails":"errorDetails"},{"severity":"SEVERITY_UNSPECIFIED","errorDetails":"errorDetails"}]},"updateTime":"updateTime","state":"IMPORT_JOB_STATE_UNSPECIFIED","labels":{"key":"labels"}}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example'),
                    ('importJobId', 'import_job_id_example'),
                    ('requestId', 'request_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1alpha1/{parent}/importJobs'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_migrationcenter_projects_locations_import_jobs_import_data_files_create(client):
    """Test case for migrationcenter_projects_locations_import_jobs_import_data_files_create

    
    """
    body = {"uploadFileInfo":{"headers":{"key":"headers"},"signedUri":"signedUri","uriExpirationTime":"uriExpirationTime"},"createTime":"createTime","displayName":"displayName","format":"IMPORT_JOB_FORMAT_UNSPECIFIED","name":"name","state":"STATE_UNSPECIFIED"}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example'),
                    ('importDataFileId', 'import_data_file_id_example'),
                    ('requestId', 'request_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1alpha1/{parent}/importDataFiles'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_migrationcenter_projects_locations_import_jobs_import_data_files_list(client):
    """Test case for migrationcenter_projects_locations_import_jobs_import_data_files_list

    
    """
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example'),
                    ('filter', 'filter_example'),
                    ('orderBy', 'order_by_example'),
                    ('pageSize', 56),
                    ('pageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1alpha1/{parent}/importDataFiles'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_migrationcenter_projects_locations_import_jobs_list(client):
    """Test case for migrationcenter_projects_locations_import_jobs_list

    
    """
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example'),
                    ('filter', 'filter_example'),
                    ('orderBy', 'order_by_example'),
                    ('pageSize', 56),
                    ('pageToken', 'page_token_example'),
                    ('view', 'view_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1alpha1/{parent}/importJobs'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_migrationcenter_projects_locations_import_jobs_run(client):
    """Test case for migrationcenter_projects_locations_import_jobs_run

    
    """
    body = {"requestId":"requestId"}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1alpha1/{nameru}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_migrationcenter_projects_locations_import_jobs_validate(client):
    """Test case for migrationcenter_projects_locations_import_jobs_validate

    
    """
    body = {"requestId":"requestId"}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1alpha1/{namevalidat}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_migrationcenter_projects_locations_list(client):
    """Test case for migrationcenter_projects_locations_list

    
    """
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example'),
                    ('filter', 'filter_example'),
                    ('pageSize', 56),
                    ('pageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1alpha1/{name}/locations'.format(name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_migrationcenter_projects_locations_operations_cancel(client):
    """Test case for migrationcenter_projects_locations_operations_cancel

    
    """
    body = None
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1alpha1/{namecance}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_migrationcenter_projects_locations_operations_list(client):
    """Test case for migrationcenter_projects_locations_operations_list

    
    """
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example'),
                    ('filter', 'filter_example'),
                    ('pageSize', 56),
                    ('pageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1alpha1/{name}/operations'.format(name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_migrationcenter_projects_locations_preference_sets_create(client):
    """Test case for migrationcenter_projects_locations_preference_sets_create

    
    """
    body = {"createTime":"createTime","displayName":"displayName","virtualMachinePreferences":{"computeEnginePreferences":{"licenseType":"LICENSE_TYPE_UNSPECIFIED","machinePreferences":{"allowedMachineSeries":[{"code":"code"},{"code":"code"}]},"persistentDiskType":"PERSISTENT_DISK_TYPE_UNSPECIFIED"},"commitmentPlan":"COMMITMENT_PLAN_UNSPECIFIED","soleTenancyPreferences":{"hostMaintenancePolicy":"HOST_MAINTENANCE_POLICY_UNSPECIFIED","commitmentPlan":"COMMITMENT_PLAN_UNSPECIFIED","cpuOvercommitRatio":5.637376656633329,"nodeTypes":[{"nodeName":"nodeName"},{"nodeName":"nodeName"}]},"vmwareEnginePreferences":{"commitmentPlan":"COMMITMENT_PLAN_UNSPECIFIED","memoryOvercommitRatio":7.061401241503109,"storageDeduplicationCompressionRatio":9.301444243932576,"cpuOvercommitRatio":2.3021358869347655},"networkCostParameters":{"estimatedEgressTrafficPercentage":0},"sizingOptimizationCustomParameters":{"cpuUsagePercentage":6,"memoryUsagePercentage":1,"aggregationMethod":"AGGREGATION_METHOD_UNSPECIFIED","storageMultiplier":5.962133916683182},"regionPreferences":{"preferredRegions":["preferredRegions","preferredRegions"]},"sizingOptimizationStrategy":"SIZING_OPTIMIZATION_STRATEGY_UNSPECIFIED","targetProduct":"COMPUTE_MIGRATION_TARGET_PRODUCT_UNSPECIFIED"},"name":"name","description":"description","updateTime":"updateTime"}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example'),
                    ('preferenceSetId', 'preference_set_id_example'),
                    ('requestId', 'request_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1alpha1/{parent}/preferenceSets'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_migrationcenter_projects_locations_preference_sets_list(client):
    """Test case for migrationcenter_projects_locations_preference_sets_list

    
    """
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example'),
                    ('orderBy', 'order_by_example'),
                    ('pageSize', 56),
                    ('pageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1alpha1/{parent}/preferenceSets'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_migrationcenter_projects_locations_report_configs_create(client):
    """Test case for migrationcenter_projects_locations_report_configs_create

    
    """
    body = {"createTime":"createTime","groupPreferencesetAssignments":[{"preferenceSet":"preferenceSet","group":"group"},{"preferenceSet":"preferenceSet","group":"group"}],"displayName":"displayName","name":"name","description":"description","updateTime":"updateTime"}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example'),
                    ('reportConfigId', 'report_config_id_example'),
                    ('requestId', 'request_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1alpha1/{parent}/reportConfigs'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_migrationcenter_projects_locations_report_configs_list(client):
    """Test case for migrationcenter_projects_locations_report_configs_list

    
    """
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example'),
                    ('filter', 'filter_example'),
                    ('orderBy', 'order_by_example'),
                    ('pageSize', 56),
                    ('pageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1alpha1/{parent}/reportConfigs'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_migrationcenter_projects_locations_report_configs_reports_create(client):
    """Test case for migrationcenter_projects_locations_report_configs_reports_create

    
    """
    body = {"summary":{"allAssetsStats":{"coreCountHistogram":{"buckets":[{"upperBound":"upperBound","count":"count","lowerBound":"lowerBound"},{"upperBound":"upperBound","count":"count","lowerBound":"lowerBound"}]},"totalAssets":"totalAssets","operatingSystem":{"dataPoints":[{"label":"label","value":0.8008281904610115},{"label":"label","value":0.8008281904610115}]},"storageBytesHistogram":{"buckets":[{"upperBound":"upperBound","count":"count","lowerBound":"lowerBound"},{"upperBound":"upperBound","count":"count","lowerBound":"lowerBound"}]},"assetAge":{"dataPoints":[{"label":"label","value":0.8008281904610115},{"label":"label","value":0.8008281904610115}]},"storageUtilizationChart":{"used":"used","free":"free"},"totalMemoryBytes":"totalMemoryBytes","memoryBytesHistogram":{"buckets":[{"upperBound":"upperBound","count":"count","lowerBound":"lowerBound"},{"upperBound":"upperBound","count":"count","lowerBound":"lowerBound"}]},"totalStorageBytes":"totalStorageBytes","totalCores":"totalCores","memoryUtilization":{"dataPoints":[{"label":"label","value":0.8008281904610115},{"label":"label","value":0.8008281904610115}]},"storageUtilization":{"dataPoints":[{"label":"label","value":0.8008281904610115},{"label":"label","value":0.8008281904610115}]},"memoryUtilizationChart":{"used":"used","free":"free"}},"groupFindings":[{"assetAggregateStats":{"coreCountHistogram":{"buckets":[{"upperBound":"upperBound","count":"count","lowerBound":"lowerBound"},{"upperBound":"upperBound","count":"count","lowerBound":"lowerBound"}]},"totalAssets":"totalAssets","operatingSystem":{"dataPoints":[{"label":"label","value":0.8008281904610115},{"label":"label","value":0.8008281904610115}]},"storageBytesHistogram":{"buckets":[{"upperBound":"upperBound","count":"count","lowerBound":"lowerBound"},{"upperBound":"upperBound","count":"count","lowerBound":"lowerBound"}]},"assetAge":{"dataPoints":[{"label":"label","value":0.8008281904610115},{"label":"label","value":0.8008281904610115}]},"storageUtilizationChart":{"used":"used","free":"free"},"totalMemoryBytes":"totalMemoryBytes","memoryBytesHistogram":{"buckets":[{"upperBound":"upperBound","count":"count","lowerBound":"lowerBound"},{"upperBound":"upperBound","count":"count","lowerBound":"lowerBound"}]},"totalStorageBytes":"totalStorageBytes","totalCores":"totalCores","memoryUtilization":{"dataPoints":[{"label":"label","value":0.8008281904610115},{"label":"label","value":0.8008281904610115}]},"storageUtilization":{"dataPoints":[{"label":"label","value":0.8008281904610115},{"label":"label","value":0.8008281904610115}]},"memoryUtilizationChart":{"used":"used","free":"free"}},"overlappingAssetCount":"overlappingAssetCount","displayName":"displayName","description":"description","preferenceSetFindings":[{"pricingTrack":"pricingTrack","preferredRegion":"preferredRegion","displayName":"displayName","description":"description","machineFinding":{"allocatedDiskTypes":["PERSISTENT_DISK_TYPE_UNSPECIFIED","PERSISTENT_DISK_TYPE_UNSPECIFIED"],"machineSeriesAllocations":[{"machineSeries":{"code":"code"},"allocatedAssetCount":"allocatedAssetCount"},{"machineSeries":{"code":"code"},"allocatedAssetCount":"allocatedAssetCount"}],"allocatedRegions":["allocatedRegions","allocatedRegions"],"allocatedAssetCount":"allocatedAssetCount"},"vmwareEngineFinding":{"nodeAllocations":[{"vmwareNode":{"code":"code"},"nodeCount":"nodeCount","allocatedAssetCount":"allocatedAssetCount"},{"vmwareNode":{"code":"code"},"nodeCount":"nodeCount","allocatedAssetCount":"allocatedAssetCount"}],"allocatedRegions":["allocatedRegions","allocatedRegions"],"allocatedAssetCount":"allocatedAssetCount"},"monthlyCostTotal":{"nanos":6,"units":"units","currencyCode":"currencyCode"},"soleTenantFinding":{"nodeAllocations":[{"node":{"nodeName":"nodeName"},"nodeCount":"nodeCount","allocatedAssetCount":"allocatedAssetCount"},{"node":{"nodeName":"nodeName"},"nodeCount":"nodeCount","allocatedAssetCount":"allocatedAssetCount"}],"allocatedRegions":["allocatedRegions","allocatedRegions"],"allocatedAssetCount":"allocatedAssetCount"},"monthlyCostCompute":{"nanos":6,"units":"units","currencyCode":"currencyCode"},"machinePreferences":{"computeEnginePreferences":{"licenseType":"LICENSE_TYPE_UNSPECIFIED","machinePreferences":{"allowedMachineSeries":[{"code":"code"},{"code":"code"}]},"persistentDiskType":"PERSISTENT_DISK_TYPE_UNSPECIFIED"},"commitmentPlan":"COMMITMENT_PLAN_UNSPECIFIED","soleTenancyPreferences":{"hostMaintenancePolicy":"HOST_MAINTENANCE_POLICY_UNSPECIFIED","commitmentPlan":"COMMITMENT_PLAN_UNSPECIFIED","cpuOvercommitRatio":5.637376656633329,"nodeTypes":[{"nodeName":"nodeName"},{"nodeName":"nodeName"}]},"vmwareEnginePreferences":{"commitmentPlan":"COMMITMENT_PLAN_UNSPECIFIED","memoryOvercommitRatio":7.061401241503109,"storageDeduplicationCompressionRatio":9.301444243932576,"cpuOvercommitRatio":2.3021358869347655},"networkCostParameters":{"estimatedEgressTrafficPercentage":0},"sizingOptimizationCustomParameters":{"cpuUsagePercentage":6,"memoryUsagePercentage":1,"aggregationMethod":"AGGREGATION_METHOD_UNSPECIFIED","storageMultiplier":5.962133916683182},"regionPreferences":{"preferredRegions":["preferredRegions","preferredRegions"]},"sizingOptimizationStrategy":"SIZING_OPTIMIZATION_STRATEGY_UNSPECIFIED","targetProduct":"COMPUTE_MIGRATION_TARGET_PRODUCT_UNSPECIFIED"},"monthlyCostNetworkEgress":{"nanos":6,"units":"units","currencyCode":"currencyCode"},"topPriority":"topPriority","monthlyCostStorage":{"nanos":6,"units":"units","currencyCode":"currencyCode"},"monthlyCostOther":{"nanos":6,"units":"units","currencyCode":"currencyCode"},"monthlyCostOsLicense":{"nanos":6,"units":"units","currencyCode":"currencyCode"}},{"pricingTrack":"pricingTrack","preferredRegion":"preferredRegion","displayName":"displayName","description":"description","machineFinding":{"allocatedDiskTypes":["PERSISTENT_DISK_TYPE_UNSPECIFIED","PERSISTENT_DISK_TYPE_UNSPECIFIED"],"machineSeriesAllocations":[{"machineSeries":{"code":"code"},"allocatedAssetCount":"allocatedAssetCount"},{"machineSeries":{"code":"code"},"allocatedAssetCount":"allocatedAssetCount"}],"allocatedRegions":["allocatedRegions","allocatedRegions"],"allocatedAssetCount":"allocatedAssetCount"},"vmwareEngineFinding":{"nodeAllocations":[{"vmwareNode":{"code":"code"},"nodeCount":"nodeCount","allocatedAssetCount":"allocatedAssetCount"},{"vmwareNode":{"code":"code"},"nodeCount":"nodeCount","allocatedAssetCount":"allocatedAssetCount"}],"allocatedRegions":["allocatedRegions","allocatedRegions"],"allocatedAssetCount":"allocatedAssetCount"},"monthlyCostTotal":{"nanos":6,"units":"units","currencyCode":"currencyCode"},"soleTenantFinding":{"nodeAllocations":[{"node":{"nodeName":"nodeName"},"nodeCount":"nodeCount","allocatedAssetCount":"allocatedAssetCount"},{"node":{"nodeName":"nodeName"},"nodeCount":"nodeCount","allocatedAssetCount":"allocatedAssetCount"}],"allocatedRegions":["allocatedRegions","allocatedRegions"],"allocatedAssetCount":"allocatedAssetCount"},"monthlyCostCompute":{"nanos":6,"units":"units","currencyCode":"currencyCode"},"machinePreferences":{"computeEnginePreferences":{"licenseType":"LICENSE_TYPE_UNSPECIFIED","machinePreferences":{"allowedMachineSeries":[{"code":"code"},{"code":"code"}]},"persistentDiskType":"PERSISTENT_DISK_TYPE_UNSPECIFIED"},"commitmentPlan":"COMMITMENT_PLAN_UNSPECIFIED","soleTenancyPreferences":{"hostMaintenancePolicy":"HOST_MAINTENANCE_POLICY_UNSPECIFIED","commitmentPlan":"COMMITMENT_PLAN_UNSPECIFIED","cpuOvercommitRatio":5.637376656633329,"nodeTypes":[{"nodeName":"nodeName"},{"nodeName":"nodeName"}]},"vmwareEnginePreferences":{"commitmentPlan":"COMMITMENT_PLAN_UNSPECIFIED","memoryOvercommitRatio":7.061401241503109,"storageDeduplicationCompressionRatio":9.301444243932576,"cpuOvercommitRatio":2.3021358869347655},"networkCostParameters":{"estimatedEgressTrafficPercentage":0},"sizingOptimizationCustomParameters":{"cpuUsagePercentage":6,"memoryUsagePercentage":1,"aggregationMethod":"AGGREGATION_METHOD_UNSPECIFIED","storageMultiplier":5.962133916683182},"regionPreferences":{"preferredRegions":["preferredRegions","preferredRegions"]},"sizingOptimizationStrategy":"SIZING_OPTIMIZATION_STRATEGY_UNSPECIFIED","targetProduct":"COMPUTE_MIGRATION_TARGET_PRODUCT_UNSPECIFIED"},"monthlyCostNetworkEgress":{"nanos":6,"units":"units","currencyCode":"currencyCode"},"topPriority":"topPriority","monthlyCostStorage":{"nanos":6,"units":"units","currencyCode":"currencyCode"},"monthlyCostOther":{"nanos":6,"units":"units","currencyCode":"currencyCode"},"monthlyCostOsLicense":{"nanos":6,"units":"units","currencyCode":"currencyCode"}}]},{"assetAggregateStats":{"coreCountHistogram":{"buckets":[{"upperBound":"upperBound","count":"count","lowerBound":"lowerBound"},{"upperBound":"upperBound","count":"count","lowerBound":"lowerBound"}]},"totalAssets":"totalAssets","operatingSystem":{"dataPoints":[{"label":"label","value":0.8008281904610115},{"label":"label","value":0.8008281904610115}]},"storageBytesHistogram":{"buckets":[{"upperBound":"upperBound","count":"count","lowerBound":"lowerBound"},{"upperBound":"upperBound","count":"count","lowerBound":"lowerBound"}]},"assetAge":{"dataPoints":[{"label":"label","value":0.8008281904610115},{"label":"label","value":0.8008281904610115}]},"storageUtilizationChart":{"used":"used","free":"free"},"totalMemoryBytes":"totalMemoryBytes","memoryBytesHistogram":{"buckets":[{"upperBound":"upperBound","count":"count","lowerBound":"lowerBound"},{"upperBound":"upperBound","count":"count","lowerBound":"lowerBound"}]},"totalStorageBytes":"totalStorageBytes","totalCores":"totalCores","memoryUtilization":{"dataPoints":[{"label":"label","value":0.8008281904610115},{"label":"label","value":0.8008281904610115}]},"storageUtilization":{"dataPoints":[{"label":"label","value":0.8008281904610115},{"label":"label","value":0.8008281904610115}]},"memoryUtilizationChart":{"used":"used","free":"free"}},"overlappingAssetCount":"overlappingAssetCount","displayName":"displayName","description":"description","preferenceSetFindings":[{"pricingTrack":"pricingTrack","preferredRegion":"preferredRegion","displayName":"displayName","description":"description","machineFinding":{"allocatedDiskTypes":["PERSISTENT_DISK_TYPE_UNSPECIFIED","PERSISTENT_DISK_TYPE_UNSPECIFIED"],"machineSeriesAllocations":[{"machineSeries":{"code":"code"},"allocatedAssetCount":"allocatedAssetCount"},{"machineSeries":{"code":"code"},"allocatedAssetCount":"allocatedAssetCount"}],"allocatedRegions":["allocatedRegions","allocatedRegions"],"allocatedAssetCount":"allocatedAssetCount"},"vmwareEngineFinding":{"nodeAllocations":[{"vmwareNode":{"code":"code"},"nodeCount":"nodeCount","allocatedAssetCount":"allocatedAssetCount"},{"vmwareNode":{"code":"code"},"nodeCount":"nodeCount","allocatedAssetCount":"allocatedAssetCount"}],"allocatedRegions":["allocatedRegions","allocatedRegions"],"allocatedAssetCount":"allocatedAssetCount"},"monthlyCostTotal":{"nanos":6,"units":"units","currencyCode":"currencyCode"},"soleTenantFinding":{"nodeAllocations":[{"node":{"nodeName":"nodeName"},"nodeCount":"nodeCount","allocatedAssetCount":"allocatedAssetCount"},{"node":{"nodeName":"nodeName"},"nodeCount":"nodeCount","allocatedAssetCount":"allocatedAssetCount"}],"allocatedRegions":["allocatedRegions","allocatedRegions"],"allocatedAssetCount":"allocatedAssetCount"},"monthlyCostCompute":{"nanos":6,"units":"units","currencyCode":"currencyCode"},"machinePreferences":{"computeEnginePreferences":{"licenseType":"LICENSE_TYPE_UNSPECIFIED","machinePreferences":{"allowedMachineSeries":[{"code":"code"},{"code":"code"}]},"persistentDiskType":"PERSISTENT_DISK_TYPE_UNSPECIFIED"},"commitmentPlan":"COMMITMENT_PLAN_UNSPECIFIED","soleTenancyPreferences":{"hostMaintenancePolicy":"HOST_MAINTENANCE_POLICY_UNSPECIFIED","commitmentPlan":"COMMITMENT_PLAN_UNSPECIFIED","cpuOvercommitRatio":5.637376656633329,"nodeTypes":[{"nodeName":"nodeName"},{"nodeName":"nodeName"}]},"vmwareEnginePreferences":{"commitmentPlan":"COMMITMENT_PLAN_UNSPECIFIED","memoryOvercommitRatio":7.061401241503109,"storageDeduplicationCompressionRatio":9.301444243932576,"cpuOvercommitRatio":2.3021358869347655},"networkCostParameters":{"estimatedEgressTrafficPercentage":0},"sizingOptimizationCustomParameters":{"cpuUsagePercentage":6,"memoryUsagePercentage":1,"aggregationMethod":"AGGREGATION_METHOD_UNSPECIFIED","storageMultiplier":5.962133916683182},"regionPreferences":{"preferredRegions":["preferredRegions","preferredRegions"]},"sizingOptimizationStrategy":"SIZING_OPTIMIZATION_STRATEGY_UNSPECIFIED","targetProduct":"COMPUTE_MIGRATION_TARGET_PRODUCT_UNSPECIFIED"},"monthlyCostNetworkEgress":{"nanos":6,"units":"units","currencyCode":"currencyCode"},"topPriority":"topPriority","monthlyCostStorage":{"nanos":6,"units":"units","currencyCode":"currencyCode"},"monthlyCostOther":{"nanos":6,"units":"units","currencyCode":"currencyCode"},"monthlyCostOsLicense":{"nanos":6,"units":"units","currencyCode":"currencyCode"}},{"pricingTrack":"pricingTrack","preferredRegion":"preferredRegion","displayName":"displayName","description":"description","machineFinding":{"allocatedDiskTypes":["PERSISTENT_DISK_TYPE_UNSPECIFIED","PERSISTENT_DISK_TYPE_UNSPECIFIED"],"machineSeriesAllocations":[{"machineSeries":{"code":"code"},"allocatedAssetCount":"allocatedAssetCount"},{"machineSeries":{"code":"code"},"allocatedAssetCount":"allocatedAssetCount"}],"allocatedRegions":["allocatedRegions","allocatedRegions"],"allocatedAssetCount":"allocatedAssetCount"},"vmwareEngineFinding":{"nodeAllocations":[{"vmwareNode":{"code":"code"},"nodeCount":"nodeCount","allocatedAssetCount":"allocatedAssetCount"},{"vmwareNode":{"code":"code"},"nodeCount":"nodeCount","allocatedAssetCount":"allocatedAssetCount"}],"allocatedRegions":["allocatedRegions","allocatedRegions"],"allocatedAssetCount":"allocatedAssetCount"},"monthlyCostTotal":{"nanos":6,"units":"units","currencyCode":"currencyCode"},"soleTenantFinding":{"nodeAllocations":[{"node":{"nodeName":"nodeName"},"nodeCount":"nodeCount","allocatedAssetCount":"allocatedAssetCount"},{"node":{"nodeName":"nodeName"},"nodeCount":"nodeCount","allocatedAssetCount":"allocatedAssetCount"}],"allocatedRegions":["allocatedRegions","allocatedRegions"],"allocatedAssetCount":"allocatedAssetCount"},"monthlyCostCompute":{"nanos":6,"units":"units","currencyCode":"currencyCode"},"machinePreferences":{"computeEnginePreferences":{"licenseType":"LICENSE_TYPE_UNSPECIFIED","machinePreferences":{"allowedMachineSeries":[{"code":"code"},{"code":"code"}]},"persistentDiskType":"PERSISTENT_DISK_TYPE_UNSPECIFIED"},"commitmentPlan":"COMMITMENT_PLAN_UNSPECIFIED","soleTenancyPreferences":{"hostMaintenancePolicy":"HOST_MAINTENANCE_POLICY_UNSPECIFIED","commitmentPlan":"COMMITMENT_PLAN_UNSPECIFIED","cpuOvercommitRatio":5.637376656633329,"nodeTypes":[{"nodeName":"nodeName"},{"nodeName":"nodeName"}]},"vmwareEnginePreferences":{"commitmentPlan":"COMMITMENT_PLAN_UNSPECIFIED","memoryOvercommitRatio":7.061401241503109,"storageDeduplicationCompressionRatio":9.301444243932576,"cpuOvercommitRatio":2.3021358869347655},"networkCostParameters":{"estimatedEgressTrafficPercentage":0},"sizingOptimizationCustomParameters":{"cpuUsagePercentage":6,"memoryUsagePercentage":1,"aggregationMethod":"AGGREGATION_METHOD_UNSPECIFIED","storageMultiplier":5.962133916683182},"regionPreferences":{"preferredRegions":["preferredRegions","preferredRegions"]},"sizingOptimizationStrategy":"SIZING_OPTIMIZATION_STRATEGY_UNSPECIFIED","targetProduct":"COMPUTE_MIGRATION_TARGET_PRODUCT_UNSPECIFIED"},"monthlyCostNetworkEgress":{"nanos":6,"units":"units","currencyCode":"currencyCode"},"topPriority":"topPriority","monthlyCostStorage":{"nanos":6,"units":"units","currencyCode":"currencyCode"},"monthlyCostOther":{"nanos":6,"units":"units","currencyCode":"currencyCode"},"monthlyCostOsLicense":{"nanos":6,"units":"units","currencyCode":"currencyCode"}}]}]},"createTime":"createTime","displayName":"displayName","name":"name","description":"description","updateTime":"updateTime","state":"STATE_UNSPECIFIED","type":"TYPE_UNSPECIFIED"}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example'),
                    ('reportId', 'report_id_example'),
                    ('requestId', 'request_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1alpha1/{parent}/reports'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_migrationcenter_projects_locations_report_configs_reports_list(client):
    """Test case for migrationcenter_projects_locations_report_configs_reports_list

    
    """
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example'),
                    ('filter', 'filter_example'),
                    ('orderBy', 'order_by_example'),
                    ('pageSize', 56),
                    ('pageToken', 'page_token_example'),
                    ('view', 'view_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1alpha1/{parent}/reports'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_migrationcenter_projects_locations_sources_create(client):
    """Test case for migrationcenter_projects_locations_sources_create

    
    """
    body = {"createTime":"createTime","displayName":"displayName","name":"name","description":"description","updateTime":"updateTime","errorFrameCount":0,"state":"STATE_UNSPECIFIED","priority":1,"type":"SOURCE_TYPE_UNKNOWN","pendingFrameCount":6,"isManaged":True}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example'),
                    ('requestId', 'request_id_example'),
                    ('sourceId', 'source_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1alpha1/{parent}/sources'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_migrationcenter_projects_locations_sources_delete(client):
    """Test case for migrationcenter_projects_locations_sources_delete

    
    """
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example'),
                    ('requestId', 'request_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v1alpha1/{name}'.format(name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_migrationcenter_projects_locations_sources_error_frames_get(client):
    """Test case for migrationcenter_projects_locations_sources_error_frames_get

    
    """
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example'),
                    ('view', 'view_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1alpha1/{name}'.format(name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_migrationcenter_projects_locations_sources_error_frames_list(client):
    """Test case for migrationcenter_projects_locations_sources_error_frames_list

    
    """
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example'),
                    ('pageSize', 56),
                    ('pageToken', 'page_token_example'),
                    ('view', 'view_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1alpha1/{parent}/errorFrames'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_migrationcenter_projects_locations_sources_list(client):
    """Test case for migrationcenter_projects_locations_sources_list

    
    """
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example'),
                    ('filter', 'filter_example'),
                    ('orderBy', 'order_by_example'),
                    ('pageSize', 56),
                    ('pageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1alpha1/{parent}/sources'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_migrationcenter_projects_locations_sources_patch(client):
    """Test case for migrationcenter_projects_locations_sources_patch

    
    """
    body = {"createTime":"createTime","displayName":"displayName","name":"name","description":"description","updateTime":"updateTime","errorFrameCount":0,"state":"STATE_UNSPECIFIED","priority":1,"type":"SOURCE_TYPE_UNKNOWN","pendingFrameCount":6,"isManaged":True}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example'),
                    ('requestId', 'request_id_example'),
                    ('updateMask', 'update_mask_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/v1alpha1/{name}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

