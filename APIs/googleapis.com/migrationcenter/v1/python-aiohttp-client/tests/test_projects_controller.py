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
    body = {"filter":"filter","aggregations":[{"histogram":{"lowerBounds":[0.8008281904610115,0.8008281904610115]},"field":"field","count":"{}","sum":"{}","frequency":"{}"},{"histogram":{"lowerBounds":[0.8008281904610115,0.8008281904610115]},"field":"field","count":"{}","sum":"{}","frequency":"{}"}]}
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
        path='/v1/{parent}/assets:aggregateValues'.format(parent='parent_example'),
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
        path='/v1/{parent}/assets:batchDelete'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_migrationcenter_projects_locations_assets_batch_update(client):
    """Test case for migrationcenter_projects_locations_assets_batch_update

    
    """
    body = {"requests":[{"requestId":"requestId","asset":{"insightList":{"insights":[{"migrationInsight":{"fit":{"fitLevel":"FIT_LEVEL_UNSPECIFIED"},"computeEngineTarget":{"shape":{"memoryMb":6,"physicalCoreCount":1,"series":"series","logicalCoreCount":0,"storage":[{"sizeGb":5,"type":"PERSISTENT_DISK_TYPE_UNSPECIFIED"},{"sizeGb":5,"type":"PERSISTENT_DISK_TYPE_UNSPECIFIED"}],"machineType":"machineType"}}},"genericInsight":{"additionalInformation":["additionalInformation","additionalInformation"],"defaultMessage":"defaultMessage","messageId":"messageId"}},{"migrationInsight":{"fit":{"fitLevel":"FIT_LEVEL_UNSPECIFIED"},"computeEngineTarget":{"shape":{"memoryMb":6,"physicalCoreCount":1,"series":"series","logicalCoreCount":0,"storage":[{"sizeGb":5,"type":"PERSISTENT_DISK_TYPE_UNSPECIFIED"},{"sizeGb":5,"type":"PERSISTENT_DISK_TYPE_UNSPECIFIED"}],"machineType":"machineType"}}},"genericInsight":{"additionalInformation":["additionalInformation","additionalInformation"],"defaultMessage":"defaultMessage","messageId":"messageId"}}],"updateTime":"updateTime"},"machineDetails":{"memoryMb":4,"guestOs":{"runtime":{"openFileList":{"entries":[{"filePath":"filePath","user":"user","command":"command","fileType":"fileType"},{"filePath":"filePath","user":"user","command":"command","fileType":"fileType"}]},"installedApps":{"entries":[{"path":"path","licenses":["licenses","licenses"],"vendor":"vendor","installTime":"installTime","version":"version","applicationName":"applicationName"},{"path":"path","licenses":["licenses","licenses"],"vendor":"vendor","installTime":"installTime","version":"version","applicationName":"applicationName"}]},"processes":{"entries":[{"cmdline":"cmdline","exePath":"exePath","attributes":{"key":"attributes"},"pid":"pid","user":"user"},{"cmdline":"cmdline","exePath":"exePath","attributes":{"key":"attributes"},"pid":"pid","user":"user"}]},"domain":"domain","lastBootTime":"lastBootTime","services":{"entries":[{"cmdline":"cmdline","exePath":"exePath","startMode":"START_MODE_UNSPECIFIED","pid":"pid","state":"STATE_UNSPECIFIED","serviceName":"serviceName"},{"cmdline":"cmdline","exePath":"exePath","startMode":"START_MODE_UNSPECIFIED","pid":"pid","state":"STATE_UNSPECIFIED","serviceName":"serviceName"}]},"machineName":"machineName","network":{"scanTime":"scanTime","connections":{"entries":[{"protocol":"protocol","localPort":3,"processName":"processName","remotePort":2,"pid":"pid","state":"STATE_UNSPECIFIED","localIpAddress":"localIpAddress","remoteIpAddress":"remoteIpAddress"},{"protocol":"protocol","localPort":3,"processName":"processName","remotePort":2,"pid":"pid","state":"STATE_UNSPECIFIED","localIpAddress":"localIpAddress","remoteIpAddress":"remoteIpAddress"}]}}},"family":"OS_FAMILY_UNKNOWN","osName":"osName","config":{"selinuxMode":"SE_LINUX_MODE_UNSPECIFIED","issue":"issue","hosts":{"entries":[{"hostNames":["hostNames","hostNames"],"ip":"ip"},{"hostNames":["hostNames","hostNames"],"ip":"ip"}]},"fstab":{"entries":[{"file":"file","vfstype":"vfstype","freq":7,"passno":9,"mntops":"mntops","spec":"spec"},{"file":"file","vfstype":"vfstype","freq":7,"passno":9,"mntops":"mntops","spec":"spec"}]},"nfsExports":{"entries":[{"hosts":["hosts","hosts"],"exportDirectory":"exportDirectory"},{"hosts":["hosts","hosts"],"exportDirectory":"exportDirectory"}]}},"version":"version"},"powerState":"POWER_STATE_UNSPECIFIED","disks":{"disks":{"entries":[{"partitions":{"entries":[{"fileSystem":"fileSystem","mountPoint":"mountPoint","capacityBytes":"capacityBytes","freeBytes":"freeBytes","type":"type","uuid":"uuid"},{"fileSystem":"fileSystem","mountPoint":"mountPoint","capacityBytes":"capacityBytes","freeBytes":"freeBytes","type":"type","uuid":"uuid"}]},"diskLabel":"diskLabel","interfaceType":"INTERFACE_TYPE_UNSPECIFIED","diskLabelType":"diskLabelType","capacityBytes":"capacityBytes","vmware":{"shared":True,"rdmCompatibility":"RDM_COMPATIBILITY_UNSPECIFIED","backingType":"BACKING_TYPE_UNSPECIFIED","vmdkMode":"VMDK_MODE_UNSPECIFIED"},"freeBytes":"freeBytes","hwAddress":"hwAddress"},{"partitions":{"entries":[{"fileSystem":"fileSystem","mountPoint":"mountPoint","capacityBytes":"capacityBytes","freeBytes":"freeBytes","type":"type","uuid":"uuid"},{"fileSystem":"fileSystem","mountPoint":"mountPoint","capacityBytes":"capacityBytes","freeBytes":"freeBytes","type":"type","uuid":"uuid"}]},"diskLabel":"diskLabel","interfaceType":"INTERFACE_TYPE_UNSPECIFIED","diskLabelType":"diskLabelType","capacityBytes":"capacityBytes","vmware":{"shared":True,"rdmCompatibility":"RDM_COMPATIBILITY_UNSPECIFIED","backingType":"BACKING_TYPE_UNSPECIFIED","vmdkMode":"VMDK_MODE_UNSPECIFIED"},"freeBytes":"freeBytes","hwAddress":"hwAddress"}]},"totalCapacityBytes":"totalCapacityBytes","totalFreeBytes":"totalFreeBytes"},"createTime":"createTime","coreCount":2,"uuid":"uuid","machineName":"machineName","platform":{"genericDetails":{"location":"location"},"vmwareDetails":{"vcenterVmId":"vcenterVmId","vcenterVersion":"vcenterVersion","vcenterUri":"vcenterUri","osid":"osid","vcenterFolder":"vcenterFolder","esxVersion":"esxVersion"},"azureVmDetails":{"location":"location","provisioningState":"provisioningState","machineTypeLabel":"machineTypeLabel"},"physicalDetails":{"location":"location"},"awsEc2Details":{"location":"location","machineTypeLabel":"machineTypeLabel"}},"architecture":{"firmwareType":"FIRMWARE_TYPE_UNSPECIFIED","cpuSocketCount":5,"cpuThreadCount":5,"bios":{"biosName":"biosName","releaseDate":{"month":6,"year":1,"day":0},"smbiosUuid":"smbiosUuid","id":"id","version":"version","manufacturer":"manufacturer"},"vendor":"vendor","cpuArchitecture":"cpuArchitecture","hyperthreading":"CPU_HYPER_THREADING_UNSPECIFIED","cpuName":"cpuName"},"network":{"primaryMacAddress":"primaryMacAddress","adapters":{"entries":[{"addresses":{"entries":[{"bcast":"bcast","fqdn":"fqdn","assignment":"ADDRESS_ASSIGNMENT_UNSPECIFIED","ipAddress":"ipAddress","subnetMask":"subnetMask"},{"bcast":"bcast","fqdn":"fqdn","assignment":"ADDRESS_ASSIGNMENT_UNSPECIFIED","ipAddress":"ipAddress","subnetMask":"subnetMask"}]},"macAddress":"macAddress","adapterType":"adapterType"},{"addresses":{"entries":[{"bcast":"bcast","fqdn":"fqdn","assignment":"ADDRESS_ASSIGNMENT_UNSPECIFIED","ipAddress":"ipAddress","subnetMask":"subnetMask"},{"bcast":"bcast","fqdn":"fqdn","assignment":"ADDRESS_ASSIGNMENT_UNSPECIFIED","ipAddress":"ipAddress","subnetMask":"subnetMask"}]},"macAddress":"macAddress","adapterType":"adapterType"}]},"publicIpAddress":"publicIpAddress","primaryIpAddress":"primaryIpAddress"}},"sources":["sources","sources"],"createTime":"createTime","performanceData":{"dailyResourceUsageAggregations":[{"date":{"month":6,"year":1,"day":0},"disk":{"iops":{"average":5.637377,"median":2.302136,"ninteyFifthPercentile":7.0614014,"peak":9.301444}},"memory":{"utilizationPercentage":{"average":5.637377,"median":2.302136,"ninteyFifthPercentile":7.0614014,"peak":9.301444}},"cpu":{"utilizationPercentage":{"average":5.637377,"median":2.302136,"ninteyFifthPercentile":7.0614014,"peak":9.301444}},"network":{"egressBps":{"average":5.637377,"median":2.302136,"ninteyFifthPercentile":7.0614014,"peak":9.301444},"ingressBps":{"average":5.637377,"median":2.302136,"ninteyFifthPercentile":7.0614014,"peak":9.301444}}},{"date":{"month":6,"year":1,"day":0},"disk":{"iops":{"average":5.637377,"median":2.302136,"ninteyFifthPercentile":7.0614014,"peak":9.301444}},"memory":{"utilizationPercentage":{"average":5.637377,"median":2.302136,"ninteyFifthPercentile":7.0614014,"peak":9.301444}},"cpu":{"utilizationPercentage":{"average":5.637377,"median":2.302136,"ninteyFifthPercentile":7.0614014,"peak":9.301444}},"network":{"egressBps":{"average":5.637377,"median":2.302136,"ninteyFifthPercentile":7.0614014,"peak":9.301444},"ingressBps":{"average":5.637377,"median":2.302136,"ninteyFifthPercentile":7.0614014,"peak":9.301444}}}]},"name":"name","attributes":{"key":"attributes"},"updateTime":"updateTime","assignedGroups":["assignedGroups","assignedGroups"],"labels":{"key":"labels"}},"updateMask":"updateMask"},{"requestId":"requestId","asset":{"insightList":{"insights":[{"migrationInsight":{"fit":{"fitLevel":"FIT_LEVEL_UNSPECIFIED"},"computeEngineTarget":{"shape":{"memoryMb":6,"physicalCoreCount":1,"series":"series","logicalCoreCount":0,"storage":[{"sizeGb":5,"type":"PERSISTENT_DISK_TYPE_UNSPECIFIED"},{"sizeGb":5,"type":"PERSISTENT_DISK_TYPE_UNSPECIFIED"}],"machineType":"machineType"}}},"genericInsight":{"additionalInformation":["additionalInformation","additionalInformation"],"defaultMessage":"defaultMessage","messageId":"messageId"}},{"migrationInsight":{"fit":{"fitLevel":"FIT_LEVEL_UNSPECIFIED"},"computeEngineTarget":{"shape":{"memoryMb":6,"physicalCoreCount":1,"series":"series","logicalCoreCount":0,"storage":[{"sizeGb":5,"type":"PERSISTENT_DISK_TYPE_UNSPECIFIED"},{"sizeGb":5,"type":"PERSISTENT_DISK_TYPE_UNSPECIFIED"}],"machineType":"machineType"}}},"genericInsight":{"additionalInformation":["additionalInformation","additionalInformation"],"defaultMessage":"defaultMessage","messageId":"messageId"}}],"updateTime":"updateTime"},"machineDetails":{"memoryMb":4,"guestOs":{"runtime":{"openFileList":{"entries":[{"filePath":"filePath","user":"user","command":"command","fileType":"fileType"},{"filePath":"filePath","user":"user","command":"command","fileType":"fileType"}]},"installedApps":{"entries":[{"path":"path","licenses":["licenses","licenses"],"vendor":"vendor","installTime":"installTime","version":"version","applicationName":"applicationName"},{"path":"path","licenses":["licenses","licenses"],"vendor":"vendor","installTime":"installTime","version":"version","applicationName":"applicationName"}]},"processes":{"entries":[{"cmdline":"cmdline","exePath":"exePath","attributes":{"key":"attributes"},"pid":"pid","user":"user"},{"cmdline":"cmdline","exePath":"exePath","attributes":{"key":"attributes"},"pid":"pid","user":"user"}]},"domain":"domain","lastBootTime":"lastBootTime","services":{"entries":[{"cmdline":"cmdline","exePath":"exePath","startMode":"START_MODE_UNSPECIFIED","pid":"pid","state":"STATE_UNSPECIFIED","serviceName":"serviceName"},{"cmdline":"cmdline","exePath":"exePath","startMode":"START_MODE_UNSPECIFIED","pid":"pid","state":"STATE_UNSPECIFIED","serviceName":"serviceName"}]},"machineName":"machineName","network":{"scanTime":"scanTime","connections":{"entries":[{"protocol":"protocol","localPort":3,"processName":"processName","remotePort":2,"pid":"pid","state":"STATE_UNSPECIFIED","localIpAddress":"localIpAddress","remoteIpAddress":"remoteIpAddress"},{"protocol":"protocol","localPort":3,"processName":"processName","remotePort":2,"pid":"pid","state":"STATE_UNSPECIFIED","localIpAddress":"localIpAddress","remoteIpAddress":"remoteIpAddress"}]}}},"family":"OS_FAMILY_UNKNOWN","osName":"osName","config":{"selinuxMode":"SE_LINUX_MODE_UNSPECIFIED","issue":"issue","hosts":{"entries":[{"hostNames":["hostNames","hostNames"],"ip":"ip"},{"hostNames":["hostNames","hostNames"],"ip":"ip"}]},"fstab":{"entries":[{"file":"file","vfstype":"vfstype","freq":7,"passno":9,"mntops":"mntops","spec":"spec"},{"file":"file","vfstype":"vfstype","freq":7,"passno":9,"mntops":"mntops","spec":"spec"}]},"nfsExports":{"entries":[{"hosts":["hosts","hosts"],"exportDirectory":"exportDirectory"},{"hosts":["hosts","hosts"],"exportDirectory":"exportDirectory"}]}},"version":"version"},"powerState":"POWER_STATE_UNSPECIFIED","disks":{"disks":{"entries":[{"partitions":{"entries":[{"fileSystem":"fileSystem","mountPoint":"mountPoint","capacityBytes":"capacityBytes","freeBytes":"freeBytes","type":"type","uuid":"uuid"},{"fileSystem":"fileSystem","mountPoint":"mountPoint","capacityBytes":"capacityBytes","freeBytes":"freeBytes","type":"type","uuid":"uuid"}]},"diskLabel":"diskLabel","interfaceType":"INTERFACE_TYPE_UNSPECIFIED","diskLabelType":"diskLabelType","capacityBytes":"capacityBytes","vmware":{"shared":True,"rdmCompatibility":"RDM_COMPATIBILITY_UNSPECIFIED","backingType":"BACKING_TYPE_UNSPECIFIED","vmdkMode":"VMDK_MODE_UNSPECIFIED"},"freeBytes":"freeBytes","hwAddress":"hwAddress"},{"partitions":{"entries":[{"fileSystem":"fileSystem","mountPoint":"mountPoint","capacityBytes":"capacityBytes","freeBytes":"freeBytes","type":"type","uuid":"uuid"},{"fileSystem":"fileSystem","mountPoint":"mountPoint","capacityBytes":"capacityBytes","freeBytes":"freeBytes","type":"type","uuid":"uuid"}]},"diskLabel":"diskLabel","interfaceType":"INTERFACE_TYPE_UNSPECIFIED","diskLabelType":"diskLabelType","capacityBytes":"capacityBytes","vmware":{"shared":True,"rdmCompatibility":"RDM_COMPATIBILITY_UNSPECIFIED","backingType":"BACKING_TYPE_UNSPECIFIED","vmdkMode":"VMDK_MODE_UNSPECIFIED"},"freeBytes":"freeBytes","hwAddress":"hwAddress"}]},"totalCapacityBytes":"totalCapacityBytes","totalFreeBytes":"totalFreeBytes"},"createTime":"createTime","coreCount":2,"uuid":"uuid","machineName":"machineName","platform":{"genericDetails":{"location":"location"},"vmwareDetails":{"vcenterVmId":"vcenterVmId","vcenterVersion":"vcenterVersion","vcenterUri":"vcenterUri","osid":"osid","vcenterFolder":"vcenterFolder","esxVersion":"esxVersion"},"azureVmDetails":{"location":"location","provisioningState":"provisioningState","machineTypeLabel":"machineTypeLabel"},"physicalDetails":{"location":"location"},"awsEc2Details":{"location":"location","machineTypeLabel":"machineTypeLabel"}},"architecture":{"firmwareType":"FIRMWARE_TYPE_UNSPECIFIED","cpuSocketCount":5,"cpuThreadCount":5,"bios":{"biosName":"biosName","releaseDate":{"month":6,"year":1,"day":0},"smbiosUuid":"smbiosUuid","id":"id","version":"version","manufacturer":"manufacturer"},"vendor":"vendor","cpuArchitecture":"cpuArchitecture","hyperthreading":"CPU_HYPER_THREADING_UNSPECIFIED","cpuName":"cpuName"},"network":{"primaryMacAddress":"primaryMacAddress","adapters":{"entries":[{"addresses":{"entries":[{"bcast":"bcast","fqdn":"fqdn","assignment":"ADDRESS_ASSIGNMENT_UNSPECIFIED","ipAddress":"ipAddress","subnetMask":"subnetMask"},{"bcast":"bcast","fqdn":"fqdn","assignment":"ADDRESS_ASSIGNMENT_UNSPECIFIED","ipAddress":"ipAddress","subnetMask":"subnetMask"}]},"macAddress":"macAddress","adapterType":"adapterType"},{"addresses":{"entries":[{"bcast":"bcast","fqdn":"fqdn","assignment":"ADDRESS_ASSIGNMENT_UNSPECIFIED","ipAddress":"ipAddress","subnetMask":"subnetMask"},{"bcast":"bcast","fqdn":"fqdn","assignment":"ADDRESS_ASSIGNMENT_UNSPECIFIED","ipAddress":"ipAddress","subnetMask":"subnetMask"}]},"macAddress":"macAddress","adapterType":"adapterType"}]},"publicIpAddress":"publicIpAddress","primaryIpAddress":"primaryIpAddress"}},"sources":["sources","sources"],"createTime":"createTime","performanceData":{"dailyResourceUsageAggregations":[{"date":{"month":6,"year":1,"day":0},"disk":{"iops":{"average":5.637377,"median":2.302136,"ninteyFifthPercentile":7.0614014,"peak":9.301444}},"memory":{"utilizationPercentage":{"average":5.637377,"median":2.302136,"ninteyFifthPercentile":7.0614014,"peak":9.301444}},"cpu":{"utilizationPercentage":{"average":5.637377,"median":2.302136,"ninteyFifthPercentile":7.0614014,"peak":9.301444}},"network":{"egressBps":{"average":5.637377,"median":2.302136,"ninteyFifthPercentile":7.0614014,"peak":9.301444},"ingressBps":{"average":5.637377,"median":2.302136,"ninteyFifthPercentile":7.0614014,"peak":9.301444}}},{"date":{"month":6,"year":1,"day":0},"disk":{"iops":{"average":5.637377,"median":2.302136,"ninteyFifthPercentile":7.0614014,"peak":9.301444}},"memory":{"utilizationPercentage":{"average":5.637377,"median":2.302136,"ninteyFifthPercentile":7.0614014,"peak":9.301444}},"cpu":{"utilizationPercentage":{"average":5.637377,"median":2.302136,"ninteyFifthPercentile":7.0614014,"peak":9.301444}},"network":{"egressBps":{"average":5.637377,"median":2.302136,"ninteyFifthPercentile":7.0614014,"peak":9.301444},"ingressBps":{"average":5.637377,"median":2.302136,"ninteyFifthPercentile":7.0614014,"peak":9.301444}}}]},"name":"name","attributes":{"key":"attributes"},"updateTime":"updateTime","assignedGroups":["assignedGroups","assignedGroups"],"labels":{"key":"labels"}},"updateMask":"updateMask"}]}
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
        path='/v1/{parent}/assets:batchUpdate'.format(parent='parent_example'),
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
                    ('view', 'view_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/{parent}/assets'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_migrationcenter_projects_locations_assets_report_asset_frames(client):
    """Test case for migrationcenter_projects_locations_assets_report_asset_frames

    
    """
    body = {"framesData":[{"machineDetails":{"memoryMb":4,"guestOs":{"runtime":{"openFileList":{"entries":[{"filePath":"filePath","user":"user","command":"command","fileType":"fileType"},{"filePath":"filePath","user":"user","command":"command","fileType":"fileType"}]},"installedApps":{"entries":[{"path":"path","licenses":["licenses","licenses"],"vendor":"vendor","installTime":"installTime","version":"version","applicationName":"applicationName"},{"path":"path","licenses":["licenses","licenses"],"vendor":"vendor","installTime":"installTime","version":"version","applicationName":"applicationName"}]},"processes":{"entries":[{"cmdline":"cmdline","exePath":"exePath","attributes":{"key":"attributes"},"pid":"pid","user":"user"},{"cmdline":"cmdline","exePath":"exePath","attributes":{"key":"attributes"},"pid":"pid","user":"user"}]},"domain":"domain","lastBootTime":"lastBootTime","services":{"entries":[{"cmdline":"cmdline","exePath":"exePath","startMode":"START_MODE_UNSPECIFIED","pid":"pid","state":"STATE_UNSPECIFIED","serviceName":"serviceName"},{"cmdline":"cmdline","exePath":"exePath","startMode":"START_MODE_UNSPECIFIED","pid":"pid","state":"STATE_UNSPECIFIED","serviceName":"serviceName"}]},"machineName":"machineName","network":{"scanTime":"scanTime","connections":{"entries":[{"protocol":"protocol","localPort":3,"processName":"processName","remotePort":2,"pid":"pid","state":"STATE_UNSPECIFIED","localIpAddress":"localIpAddress","remoteIpAddress":"remoteIpAddress"},{"protocol":"protocol","localPort":3,"processName":"processName","remotePort":2,"pid":"pid","state":"STATE_UNSPECIFIED","localIpAddress":"localIpAddress","remoteIpAddress":"remoteIpAddress"}]}}},"family":"OS_FAMILY_UNKNOWN","osName":"osName","config":{"selinuxMode":"SE_LINUX_MODE_UNSPECIFIED","issue":"issue","hosts":{"entries":[{"hostNames":["hostNames","hostNames"],"ip":"ip"},{"hostNames":["hostNames","hostNames"],"ip":"ip"}]},"fstab":{"entries":[{"file":"file","vfstype":"vfstype","freq":7,"passno":9,"mntops":"mntops","spec":"spec"},{"file":"file","vfstype":"vfstype","freq":7,"passno":9,"mntops":"mntops","spec":"spec"}]},"nfsExports":{"entries":[{"hosts":["hosts","hosts"],"exportDirectory":"exportDirectory"},{"hosts":["hosts","hosts"],"exportDirectory":"exportDirectory"}]}},"version":"version"},"powerState":"POWER_STATE_UNSPECIFIED","disks":{"disks":{"entries":[{"partitions":{"entries":[{"fileSystem":"fileSystem","mountPoint":"mountPoint","capacityBytes":"capacityBytes","freeBytes":"freeBytes","type":"type","uuid":"uuid"},{"fileSystem":"fileSystem","mountPoint":"mountPoint","capacityBytes":"capacityBytes","freeBytes":"freeBytes","type":"type","uuid":"uuid"}]},"diskLabel":"diskLabel","interfaceType":"INTERFACE_TYPE_UNSPECIFIED","diskLabelType":"diskLabelType","capacityBytes":"capacityBytes","vmware":{"shared":True,"rdmCompatibility":"RDM_COMPATIBILITY_UNSPECIFIED","backingType":"BACKING_TYPE_UNSPECIFIED","vmdkMode":"VMDK_MODE_UNSPECIFIED"},"freeBytes":"freeBytes","hwAddress":"hwAddress"},{"partitions":{"entries":[{"fileSystem":"fileSystem","mountPoint":"mountPoint","capacityBytes":"capacityBytes","freeBytes":"freeBytes","type":"type","uuid":"uuid"},{"fileSystem":"fileSystem","mountPoint":"mountPoint","capacityBytes":"capacityBytes","freeBytes":"freeBytes","type":"type","uuid":"uuid"}]},"diskLabel":"diskLabel","interfaceType":"INTERFACE_TYPE_UNSPECIFIED","diskLabelType":"diskLabelType","capacityBytes":"capacityBytes","vmware":{"shared":True,"rdmCompatibility":"RDM_COMPATIBILITY_UNSPECIFIED","backingType":"BACKING_TYPE_UNSPECIFIED","vmdkMode":"VMDK_MODE_UNSPECIFIED"},"freeBytes":"freeBytes","hwAddress":"hwAddress"}]},"totalCapacityBytes":"totalCapacityBytes","totalFreeBytes":"totalFreeBytes"},"createTime":"createTime","coreCount":2,"uuid":"uuid","machineName":"machineName","platform":{"genericDetails":{"location":"location"},"vmwareDetails":{"vcenterVmId":"vcenterVmId","vcenterVersion":"vcenterVersion","vcenterUri":"vcenterUri","osid":"osid","vcenterFolder":"vcenterFolder","esxVersion":"esxVersion"},"azureVmDetails":{"location":"location","provisioningState":"provisioningState","machineTypeLabel":"machineTypeLabel"},"physicalDetails":{"location":"location"},"awsEc2Details":{"location":"location","machineTypeLabel":"machineTypeLabel"}},"architecture":{"firmwareType":"FIRMWARE_TYPE_UNSPECIFIED","cpuSocketCount":5,"cpuThreadCount":5,"bios":{"biosName":"biosName","releaseDate":{"month":6,"year":1,"day":0},"smbiosUuid":"smbiosUuid","id":"id","version":"version","manufacturer":"manufacturer"},"vendor":"vendor","cpuArchitecture":"cpuArchitecture","hyperthreading":"CPU_HYPER_THREADING_UNSPECIFIED","cpuName":"cpuName"},"network":{"primaryMacAddress":"primaryMacAddress","adapters":{"entries":[{"addresses":{"entries":[{"bcast":"bcast","fqdn":"fqdn","assignment":"ADDRESS_ASSIGNMENT_UNSPECIFIED","ipAddress":"ipAddress","subnetMask":"subnetMask"},{"bcast":"bcast","fqdn":"fqdn","assignment":"ADDRESS_ASSIGNMENT_UNSPECIFIED","ipAddress":"ipAddress","subnetMask":"subnetMask"}]},"macAddress":"macAddress","adapterType":"adapterType"},{"addresses":{"entries":[{"bcast":"bcast","fqdn":"fqdn","assignment":"ADDRESS_ASSIGNMENT_UNSPECIFIED","ipAddress":"ipAddress","subnetMask":"subnetMask"},{"bcast":"bcast","fqdn":"fqdn","assignment":"ADDRESS_ASSIGNMENT_UNSPECIFIED","ipAddress":"ipAddress","subnetMask":"subnetMask"}]},"macAddress":"macAddress","adapterType":"adapterType"}]},"publicIpAddress":"publicIpAddress","primaryIpAddress":"primaryIpAddress"}},"attributes":{"key":"attributes"},"performanceSamples":[{"disk":{"averageIops":1.2315135},"memory":{"utilizedPercentage":1.0246457},"cpu":{"utilizedPercentage":7.386282},"network":{"averageEgressBps":1.4894159,"averageIngressBps":6.846853},"sampleTime":"sampleTime"},{"disk":{"averageIops":1.2315135},"memory":{"utilizedPercentage":1.0246457},"cpu":{"utilizedPercentage":7.386282},"network":{"averageEgressBps":1.4894159,"averageIngressBps":6.846853},"sampleTime":"sampleTime"}],"traceToken":"traceToken","labels":{"key":"labels"},"reportTime":"reportTime"},{"machineDetails":{"memoryMb":4,"guestOs":{"runtime":{"openFileList":{"entries":[{"filePath":"filePath","user":"user","command":"command","fileType":"fileType"},{"filePath":"filePath","user":"user","command":"command","fileType":"fileType"}]},"installedApps":{"entries":[{"path":"path","licenses":["licenses","licenses"],"vendor":"vendor","installTime":"installTime","version":"version","applicationName":"applicationName"},{"path":"path","licenses":["licenses","licenses"],"vendor":"vendor","installTime":"installTime","version":"version","applicationName":"applicationName"}]},"processes":{"entries":[{"cmdline":"cmdline","exePath":"exePath","attributes":{"key":"attributes"},"pid":"pid","user":"user"},{"cmdline":"cmdline","exePath":"exePath","attributes":{"key":"attributes"},"pid":"pid","user":"user"}]},"domain":"domain","lastBootTime":"lastBootTime","services":{"entries":[{"cmdline":"cmdline","exePath":"exePath","startMode":"START_MODE_UNSPECIFIED","pid":"pid","state":"STATE_UNSPECIFIED","serviceName":"serviceName"},{"cmdline":"cmdline","exePath":"exePath","startMode":"START_MODE_UNSPECIFIED","pid":"pid","state":"STATE_UNSPECIFIED","serviceName":"serviceName"}]},"machineName":"machineName","network":{"scanTime":"scanTime","connections":{"entries":[{"protocol":"protocol","localPort":3,"processName":"processName","remotePort":2,"pid":"pid","state":"STATE_UNSPECIFIED","localIpAddress":"localIpAddress","remoteIpAddress":"remoteIpAddress"},{"protocol":"protocol","localPort":3,"processName":"processName","remotePort":2,"pid":"pid","state":"STATE_UNSPECIFIED","localIpAddress":"localIpAddress","remoteIpAddress":"remoteIpAddress"}]}}},"family":"OS_FAMILY_UNKNOWN","osName":"osName","config":{"selinuxMode":"SE_LINUX_MODE_UNSPECIFIED","issue":"issue","hosts":{"entries":[{"hostNames":["hostNames","hostNames"],"ip":"ip"},{"hostNames":["hostNames","hostNames"],"ip":"ip"}]},"fstab":{"entries":[{"file":"file","vfstype":"vfstype","freq":7,"passno":9,"mntops":"mntops","spec":"spec"},{"file":"file","vfstype":"vfstype","freq":7,"passno":9,"mntops":"mntops","spec":"spec"}]},"nfsExports":{"entries":[{"hosts":["hosts","hosts"],"exportDirectory":"exportDirectory"},{"hosts":["hosts","hosts"],"exportDirectory":"exportDirectory"}]}},"version":"version"},"powerState":"POWER_STATE_UNSPECIFIED","disks":{"disks":{"entries":[{"partitions":{"entries":[{"fileSystem":"fileSystem","mountPoint":"mountPoint","capacityBytes":"capacityBytes","freeBytes":"freeBytes","type":"type","uuid":"uuid"},{"fileSystem":"fileSystem","mountPoint":"mountPoint","capacityBytes":"capacityBytes","freeBytes":"freeBytes","type":"type","uuid":"uuid"}]},"diskLabel":"diskLabel","interfaceType":"INTERFACE_TYPE_UNSPECIFIED","diskLabelType":"diskLabelType","capacityBytes":"capacityBytes","vmware":{"shared":True,"rdmCompatibility":"RDM_COMPATIBILITY_UNSPECIFIED","backingType":"BACKING_TYPE_UNSPECIFIED","vmdkMode":"VMDK_MODE_UNSPECIFIED"},"freeBytes":"freeBytes","hwAddress":"hwAddress"},{"partitions":{"entries":[{"fileSystem":"fileSystem","mountPoint":"mountPoint","capacityBytes":"capacityBytes","freeBytes":"freeBytes","type":"type","uuid":"uuid"},{"fileSystem":"fileSystem","mountPoint":"mountPoint","capacityBytes":"capacityBytes","freeBytes":"freeBytes","type":"type","uuid":"uuid"}]},"diskLabel":"diskLabel","interfaceType":"INTERFACE_TYPE_UNSPECIFIED","diskLabelType":"diskLabelType","capacityBytes":"capacityBytes","vmware":{"shared":True,"rdmCompatibility":"RDM_COMPATIBILITY_UNSPECIFIED","backingType":"BACKING_TYPE_UNSPECIFIED","vmdkMode":"VMDK_MODE_UNSPECIFIED"},"freeBytes":"freeBytes","hwAddress":"hwAddress"}]},"totalCapacityBytes":"totalCapacityBytes","totalFreeBytes":"totalFreeBytes"},"createTime":"createTime","coreCount":2,"uuid":"uuid","machineName":"machineName","platform":{"genericDetails":{"location":"location"},"vmwareDetails":{"vcenterVmId":"vcenterVmId","vcenterVersion":"vcenterVersion","vcenterUri":"vcenterUri","osid":"osid","vcenterFolder":"vcenterFolder","esxVersion":"esxVersion"},"azureVmDetails":{"location":"location","provisioningState":"provisioningState","machineTypeLabel":"machineTypeLabel"},"physicalDetails":{"location":"location"},"awsEc2Details":{"location":"location","machineTypeLabel":"machineTypeLabel"}},"architecture":{"firmwareType":"FIRMWARE_TYPE_UNSPECIFIED","cpuSocketCount":5,"cpuThreadCount":5,"bios":{"biosName":"biosName","releaseDate":{"month":6,"year":1,"day":0},"smbiosUuid":"smbiosUuid","id":"id","version":"version","manufacturer":"manufacturer"},"vendor":"vendor","cpuArchitecture":"cpuArchitecture","hyperthreading":"CPU_HYPER_THREADING_UNSPECIFIED","cpuName":"cpuName"},"network":{"primaryMacAddress":"primaryMacAddress","adapters":{"entries":[{"addresses":{"entries":[{"bcast":"bcast","fqdn":"fqdn","assignment":"ADDRESS_ASSIGNMENT_UNSPECIFIED","ipAddress":"ipAddress","subnetMask":"subnetMask"},{"bcast":"bcast","fqdn":"fqdn","assignment":"ADDRESS_ASSIGNMENT_UNSPECIFIED","ipAddress":"ipAddress","subnetMask":"subnetMask"}]},"macAddress":"macAddress","adapterType":"adapterType"},{"addresses":{"entries":[{"bcast":"bcast","fqdn":"fqdn","assignment":"ADDRESS_ASSIGNMENT_UNSPECIFIED","ipAddress":"ipAddress","subnetMask":"subnetMask"},{"bcast":"bcast","fqdn":"fqdn","assignment":"ADDRESS_ASSIGNMENT_UNSPECIFIED","ipAddress":"ipAddress","subnetMask":"subnetMask"}]},"macAddress":"macAddress","adapterType":"adapterType"}]},"publicIpAddress":"publicIpAddress","primaryIpAddress":"primaryIpAddress"}},"attributes":{"key":"attributes"},"performanceSamples":[{"disk":{"averageIops":1.2315135},"memory":{"utilizedPercentage":1.0246457},"cpu":{"utilizedPercentage":7.386282},"network":{"averageEgressBps":1.4894159,"averageIngressBps":6.846853},"sampleTime":"sampleTime"},{"disk":{"averageIops":1.2315135},"memory":{"utilizedPercentage":1.0246457},"cpu":{"utilizedPercentage":7.386282},"network":{"averageEgressBps":1.4894159,"averageIngressBps":6.846853},"sampleTime":"sampleTime"}],"traceToken":"traceToken","labels":{"key":"labels"},"reportTime":"reportTime"}]}
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
        path='/v1/{parent}/assets:reportAssetFrames'.format(parent='parent_example'),
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
        path='/v1/{groupadd_asset}'.format(group='group_example'),
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
        path='/v1/{parent}/groups'.format(parent='parent_example'),
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
        path='/v1/{parent}/groups'.format(parent='parent_example'),
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
        path='/v1/{groupremove_asset}'.format(group='group_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_migrationcenter_projects_locations_import_jobs_create(client):
    """Test case for migrationcenter_projects_locations_import_jobs_create

    
    """
    body = {"createTime":"createTime","displayName":"displayName","executionReport":{"totalRowsCount":1,"executionErrors":{"fileValidations":[{"fileName":"fileName","partialReport":True,"fileErrors":[{"severity":"SEVERITY_UNSPECIFIED","errorDetails":"errorDetails"},{"severity":"SEVERITY_UNSPECIFIED","errorDetails":"errorDetails"}],"rowErrors":[{"vmName":"vmName","vmUuid":"vmUuid","rowNumber":0,"errors":[{"severity":"SEVERITY_UNSPECIFIED","errorDetails":"errorDetails"},{"severity":"SEVERITY_UNSPECIFIED","errorDetails":"errorDetails"}]},{"vmName":"vmName","vmUuid":"vmUuid","rowNumber":0,"errors":[{"severity":"SEVERITY_UNSPECIFIED","errorDetails":"errorDetails"},{"severity":"SEVERITY_UNSPECIFIED","errorDetails":"errorDetails"}]}]},{"fileName":"fileName","partialReport":True,"fileErrors":[{"severity":"SEVERITY_UNSPECIFIED","errorDetails":"errorDetails"},{"severity":"SEVERITY_UNSPECIFIED","errorDetails":"errorDetails"}],"rowErrors":[{"vmName":"vmName","vmUuid":"vmUuid","rowNumber":0,"errors":[{"severity":"SEVERITY_UNSPECIFIED","errorDetails":"errorDetails"},{"severity":"SEVERITY_UNSPECIFIED","errorDetails":"errorDetails"}]},{"vmName":"vmName","vmUuid":"vmUuid","rowNumber":0,"errors":[{"severity":"SEVERITY_UNSPECIFIED","errorDetails":"errorDetails"},{"severity":"SEVERITY_UNSPECIFIED","errorDetails":"errorDetails"}]}]}],"jobErrors":[{"severity":"SEVERITY_UNSPECIFIED","errorDetails":"errorDetails"},{"severity":"SEVERITY_UNSPECIFIED","errorDetails":"errorDetails"}]},"framesReported":6},"name":"name","assetSource":"assetSource","completeTime":"completeTime","validationReport":{"fileValidations":[{"fileName":"fileName","partialReport":True,"fileErrors":[{"severity":"SEVERITY_UNSPECIFIED","errorDetails":"errorDetails"},{"severity":"SEVERITY_UNSPECIFIED","errorDetails":"errorDetails"}],"rowErrors":[{"vmName":"vmName","vmUuid":"vmUuid","rowNumber":0,"errors":[{"severity":"SEVERITY_UNSPECIFIED","errorDetails":"errorDetails"},{"severity":"SEVERITY_UNSPECIFIED","errorDetails":"errorDetails"}]},{"vmName":"vmName","vmUuid":"vmUuid","rowNumber":0,"errors":[{"severity":"SEVERITY_UNSPECIFIED","errorDetails":"errorDetails"},{"severity":"SEVERITY_UNSPECIFIED","errorDetails":"errorDetails"}]}]},{"fileName":"fileName","partialReport":True,"fileErrors":[{"severity":"SEVERITY_UNSPECIFIED","errorDetails":"errorDetails"},{"severity":"SEVERITY_UNSPECIFIED","errorDetails":"errorDetails"}],"rowErrors":[{"vmName":"vmName","vmUuid":"vmUuid","rowNumber":0,"errors":[{"severity":"SEVERITY_UNSPECIFIED","errorDetails":"errorDetails"},{"severity":"SEVERITY_UNSPECIFIED","errorDetails":"errorDetails"}]},{"vmName":"vmName","vmUuid":"vmUuid","rowNumber":0,"errors":[{"severity":"SEVERITY_UNSPECIFIED","errorDetails":"errorDetails"},{"severity":"SEVERITY_UNSPECIFIED","errorDetails":"errorDetails"}]}]}],"jobErrors":[{"severity":"SEVERITY_UNSPECIFIED","errorDetails":"errorDetails"},{"severity":"SEVERITY_UNSPECIFIED","errorDetails":"errorDetails"}]},"updateTime":"updateTime","state":"IMPORT_JOB_STATE_UNSPECIFIED","labels":{"key":"labels"}}
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
        path='/v1/{parent}/importJobs'.format(parent='parent_example'),
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
        path='/v1/{parent}/importDataFiles'.format(parent='parent_example'),
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
        path='/v1/{parent}/importDataFiles'.format(parent='parent_example'),
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
        path='/v1/{parent}/importJobs'.format(parent='parent_example'),
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
        path='/v1/{nameru}'.format(name='name_example'),
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
        path='/v1/{namevalidat}'.format(name='name_example'),
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
        path='/v1/{name}/locations'.format(name='name_example'),
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
        path='/v1/{namecance}'.format(name='name_example'),
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
        path='/v1/{name}/operations'.format(name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_migrationcenter_projects_locations_preference_sets_create(client):
    """Test case for migrationcenter_projects_locations_preference_sets_create

    
    """
    body = {"createTime":"createTime","displayName":"displayName","virtualMachinePreferences":{"computeEnginePreferences":{"licenseType":"LICENSE_TYPE_UNSPECIFIED","machinePreferences":{"allowedMachineSeries":[{"code":"code"},{"code":"code"}]},"persistentDiskType":"PERSISTENT_DISK_TYPE_UNSPECIFIED"},"commitmentPlan":"COMMITMENT_PLAN_UNSPECIFIED","soleTenancyPreferences":{"hostMaintenancePolicy":"HOST_MAINTENANCE_POLICY_UNSPECIFIED","commitmentPlan":"COMMITMENT_PLAN_UNSPECIFIED","cpuOvercommitRatio":0.8008281904610115,"nodeTypes":[{"nodeName":"nodeName"},{"nodeName":"nodeName"}]},"vmwareEnginePreferences":{"commitmentPlan":"COMMITMENT_PLAN_UNSPECIFIED","memoryOvercommitRatio":1.4658129805029452,"storageDeduplicationCompressionRatio":5.962133916683182,"cpuOvercommitRatio":6.027456183070403},"regionPreferences":{"preferredRegions":["preferredRegions","preferredRegions"]},"sizingOptimizationStrategy":"SIZING_OPTIMIZATION_STRATEGY_UNSPECIFIED","targetProduct":"COMPUTE_MIGRATION_TARGET_PRODUCT_UNSPECIFIED"},"name":"name","description":"description","updateTime":"updateTime"}
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
        path='/v1/{parent}/preferenceSets'.format(parent='parent_example'),
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
        path='/v1/{parent}/preferenceSets'.format(parent='parent_example'),
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
        path='/v1/{parent}/reportConfigs'.format(parent='parent_example'),
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
        path='/v1/{parent}/reportConfigs'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_migrationcenter_projects_locations_report_configs_reports_create(client):
    """Test case for migrationcenter_projects_locations_report_configs_reports_create

    
    """
    body = {"summary":{"allAssetsStats":{"totalMemoryBytes":"totalMemoryBytes","coreCountHistogram":{"buckets":[{"upperBound":"upperBound","count":"count","lowerBound":"lowerBound"},{"upperBound":"upperBound","count":"count","lowerBound":"lowerBound"}]},"memoryBytesHistogram":{"buckets":[{"upperBound":"upperBound","count":"count","lowerBound":"lowerBound"},{"upperBound":"upperBound","count":"count","lowerBound":"lowerBound"}]},"totalStorageBytes":"totalStorageBytes","totalAssets":"totalAssets","totalCores":"totalCores","memoryUtilizationChart":{"used":"used","free":"free"},"operatingSystem":{"dataPoints":[{"label":"label","value":0.8008281904610115},{"label":"label","value":0.8008281904610115}]},"storageBytesHistogram":{"buckets":[{"upperBound":"upperBound","count":"count","lowerBound":"lowerBound"},{"upperBound":"upperBound","count":"count","lowerBound":"lowerBound"}]},"storageUtilizationChart":{"used":"used","free":"free"}},"groupFindings":[{"assetAggregateStats":{"totalMemoryBytes":"totalMemoryBytes","coreCountHistogram":{"buckets":[{"upperBound":"upperBound","count":"count","lowerBound":"lowerBound"},{"upperBound":"upperBound","count":"count","lowerBound":"lowerBound"}]},"memoryBytesHistogram":{"buckets":[{"upperBound":"upperBound","count":"count","lowerBound":"lowerBound"},{"upperBound":"upperBound","count":"count","lowerBound":"lowerBound"}]},"totalStorageBytes":"totalStorageBytes","totalAssets":"totalAssets","totalCores":"totalCores","memoryUtilizationChart":{"used":"used","free":"free"},"operatingSystem":{"dataPoints":[{"label":"label","value":0.8008281904610115},{"label":"label","value":0.8008281904610115}]},"storageBytesHistogram":{"buckets":[{"upperBound":"upperBound","count":"count","lowerBound":"lowerBound"},{"upperBound":"upperBound","count":"count","lowerBound":"lowerBound"}]},"storageUtilizationChart":{"used":"used","free":"free"}},"overlappingAssetCount":"overlappingAssetCount","displayName":"displayName","description":"description","preferenceSetFindings":[{"soleTenantFinding":{"nodeAllocations":[{"node":{"nodeName":"nodeName"},"nodeCount":"nodeCount","allocatedAssetCount":"allocatedAssetCount"},{"node":{"nodeName":"nodeName"},"nodeCount":"nodeCount","allocatedAssetCount":"allocatedAssetCount"}],"allocatedRegions":["allocatedRegions","allocatedRegions"],"allocatedAssetCount":"allocatedAssetCount"},"computeEngineFinding":{"allocatedDiskTypes":["PERSISTENT_DISK_TYPE_UNSPECIFIED","PERSISTENT_DISK_TYPE_UNSPECIFIED"],"machineSeriesAllocations":[{"machineSeries":{"code":"code"},"allocatedAssetCount":"allocatedAssetCount"},{"machineSeries":{"code":"code"},"allocatedAssetCount":"allocatedAssetCount"}],"allocatedRegions":["allocatedRegions","allocatedRegions"],"allocatedAssetCount":"allocatedAssetCount"},"monthlyCostCompute":{"nanos":6,"units":"units","currencyCode":"currencyCode"},"machinePreferences":{"computeEnginePreferences":{"licenseType":"LICENSE_TYPE_UNSPECIFIED","machinePreferences":{"allowedMachineSeries":[{"code":"code"},{"code":"code"}]},"persistentDiskType":"PERSISTENT_DISK_TYPE_UNSPECIFIED"},"commitmentPlan":"COMMITMENT_PLAN_UNSPECIFIED","soleTenancyPreferences":{"hostMaintenancePolicy":"HOST_MAINTENANCE_POLICY_UNSPECIFIED","commitmentPlan":"COMMITMENT_PLAN_UNSPECIFIED","cpuOvercommitRatio":0.8008281904610115,"nodeTypes":[{"nodeName":"nodeName"},{"nodeName":"nodeName"}]},"vmwareEnginePreferences":{"commitmentPlan":"COMMITMENT_PLAN_UNSPECIFIED","memoryOvercommitRatio":1.4658129805029452,"storageDeduplicationCompressionRatio":5.962133916683182,"cpuOvercommitRatio":6.027456183070403},"regionPreferences":{"preferredRegions":["preferredRegions","preferredRegions"]},"sizingOptimizationStrategy":"SIZING_OPTIMIZATION_STRATEGY_UNSPECIFIED","targetProduct":"COMPUTE_MIGRATION_TARGET_PRODUCT_UNSPECIFIED"},"monthlyCostNetworkEgress":{"nanos":6,"units":"units","currencyCode":"currencyCode"},"displayName":"displayName","monthlyCostStorage":{"nanos":6,"units":"units","currencyCode":"currencyCode"},"monthlyCostOther":{"nanos":6,"units":"units","currencyCode":"currencyCode"},"monthlyCostOsLicense":{"nanos":6,"units":"units","currencyCode":"currencyCode"},"description":"description","vmwareEngineFinding":{"nodeAllocations":[{"vmwareNode":{"code":"code"},"nodeCount":"nodeCount","allocatedAssetCount":"allocatedAssetCount"},{"vmwareNode":{"code":"code"},"nodeCount":"nodeCount","allocatedAssetCount":"allocatedAssetCount"}],"allocatedRegions":["allocatedRegions","allocatedRegions"],"allocatedAssetCount":"allocatedAssetCount"},"monthlyCostTotal":{"nanos":6,"units":"units","currencyCode":"currencyCode"}},{"soleTenantFinding":{"nodeAllocations":[{"node":{"nodeName":"nodeName"},"nodeCount":"nodeCount","allocatedAssetCount":"allocatedAssetCount"},{"node":{"nodeName":"nodeName"},"nodeCount":"nodeCount","allocatedAssetCount":"allocatedAssetCount"}],"allocatedRegions":["allocatedRegions","allocatedRegions"],"allocatedAssetCount":"allocatedAssetCount"},"computeEngineFinding":{"allocatedDiskTypes":["PERSISTENT_DISK_TYPE_UNSPECIFIED","PERSISTENT_DISK_TYPE_UNSPECIFIED"],"machineSeriesAllocations":[{"machineSeries":{"code":"code"},"allocatedAssetCount":"allocatedAssetCount"},{"machineSeries":{"code":"code"},"allocatedAssetCount":"allocatedAssetCount"}],"allocatedRegions":["allocatedRegions","allocatedRegions"],"allocatedAssetCount":"allocatedAssetCount"},"monthlyCostCompute":{"nanos":6,"units":"units","currencyCode":"currencyCode"},"machinePreferences":{"computeEnginePreferences":{"licenseType":"LICENSE_TYPE_UNSPECIFIED","machinePreferences":{"allowedMachineSeries":[{"code":"code"},{"code":"code"}]},"persistentDiskType":"PERSISTENT_DISK_TYPE_UNSPECIFIED"},"commitmentPlan":"COMMITMENT_PLAN_UNSPECIFIED","soleTenancyPreferences":{"hostMaintenancePolicy":"HOST_MAINTENANCE_POLICY_UNSPECIFIED","commitmentPlan":"COMMITMENT_PLAN_UNSPECIFIED","cpuOvercommitRatio":0.8008281904610115,"nodeTypes":[{"nodeName":"nodeName"},{"nodeName":"nodeName"}]},"vmwareEnginePreferences":{"commitmentPlan":"COMMITMENT_PLAN_UNSPECIFIED","memoryOvercommitRatio":1.4658129805029452,"storageDeduplicationCompressionRatio":5.962133916683182,"cpuOvercommitRatio":6.027456183070403},"regionPreferences":{"preferredRegions":["preferredRegions","preferredRegions"]},"sizingOptimizationStrategy":"SIZING_OPTIMIZATION_STRATEGY_UNSPECIFIED","targetProduct":"COMPUTE_MIGRATION_TARGET_PRODUCT_UNSPECIFIED"},"monthlyCostNetworkEgress":{"nanos":6,"units":"units","currencyCode":"currencyCode"},"displayName":"displayName","monthlyCostStorage":{"nanos":6,"units":"units","currencyCode":"currencyCode"},"monthlyCostOther":{"nanos":6,"units":"units","currencyCode":"currencyCode"},"monthlyCostOsLicense":{"nanos":6,"units":"units","currencyCode":"currencyCode"},"description":"description","vmwareEngineFinding":{"nodeAllocations":[{"vmwareNode":{"code":"code"},"nodeCount":"nodeCount","allocatedAssetCount":"allocatedAssetCount"},{"vmwareNode":{"code":"code"},"nodeCount":"nodeCount","allocatedAssetCount":"allocatedAssetCount"}],"allocatedRegions":["allocatedRegions","allocatedRegions"],"allocatedAssetCount":"allocatedAssetCount"},"monthlyCostTotal":{"nanos":6,"units":"units","currencyCode":"currencyCode"}}]},{"assetAggregateStats":{"totalMemoryBytes":"totalMemoryBytes","coreCountHistogram":{"buckets":[{"upperBound":"upperBound","count":"count","lowerBound":"lowerBound"},{"upperBound":"upperBound","count":"count","lowerBound":"lowerBound"}]},"memoryBytesHistogram":{"buckets":[{"upperBound":"upperBound","count":"count","lowerBound":"lowerBound"},{"upperBound":"upperBound","count":"count","lowerBound":"lowerBound"}]},"totalStorageBytes":"totalStorageBytes","totalAssets":"totalAssets","totalCores":"totalCores","memoryUtilizationChart":{"used":"used","free":"free"},"operatingSystem":{"dataPoints":[{"label":"label","value":0.8008281904610115},{"label":"label","value":0.8008281904610115}]},"storageBytesHistogram":{"buckets":[{"upperBound":"upperBound","count":"count","lowerBound":"lowerBound"},{"upperBound":"upperBound","count":"count","lowerBound":"lowerBound"}]},"storageUtilizationChart":{"used":"used","free":"free"}},"overlappingAssetCount":"overlappingAssetCount","displayName":"displayName","description":"description","preferenceSetFindings":[{"soleTenantFinding":{"nodeAllocations":[{"node":{"nodeName":"nodeName"},"nodeCount":"nodeCount","allocatedAssetCount":"allocatedAssetCount"},{"node":{"nodeName":"nodeName"},"nodeCount":"nodeCount","allocatedAssetCount":"allocatedAssetCount"}],"allocatedRegions":["allocatedRegions","allocatedRegions"],"allocatedAssetCount":"allocatedAssetCount"},"computeEngineFinding":{"allocatedDiskTypes":["PERSISTENT_DISK_TYPE_UNSPECIFIED","PERSISTENT_DISK_TYPE_UNSPECIFIED"],"machineSeriesAllocations":[{"machineSeries":{"code":"code"},"allocatedAssetCount":"allocatedAssetCount"},{"machineSeries":{"code":"code"},"allocatedAssetCount":"allocatedAssetCount"}],"allocatedRegions":["allocatedRegions","allocatedRegions"],"allocatedAssetCount":"allocatedAssetCount"},"monthlyCostCompute":{"nanos":6,"units":"units","currencyCode":"currencyCode"},"machinePreferences":{"computeEnginePreferences":{"licenseType":"LICENSE_TYPE_UNSPECIFIED","machinePreferences":{"allowedMachineSeries":[{"code":"code"},{"code":"code"}]},"persistentDiskType":"PERSISTENT_DISK_TYPE_UNSPECIFIED"},"commitmentPlan":"COMMITMENT_PLAN_UNSPECIFIED","soleTenancyPreferences":{"hostMaintenancePolicy":"HOST_MAINTENANCE_POLICY_UNSPECIFIED","commitmentPlan":"COMMITMENT_PLAN_UNSPECIFIED","cpuOvercommitRatio":0.8008281904610115,"nodeTypes":[{"nodeName":"nodeName"},{"nodeName":"nodeName"}]},"vmwareEnginePreferences":{"commitmentPlan":"COMMITMENT_PLAN_UNSPECIFIED","memoryOvercommitRatio":1.4658129805029452,"storageDeduplicationCompressionRatio":5.962133916683182,"cpuOvercommitRatio":6.027456183070403},"regionPreferences":{"preferredRegions":["preferredRegions","preferredRegions"]},"sizingOptimizationStrategy":"SIZING_OPTIMIZATION_STRATEGY_UNSPECIFIED","targetProduct":"COMPUTE_MIGRATION_TARGET_PRODUCT_UNSPECIFIED"},"monthlyCostNetworkEgress":{"nanos":6,"units":"units","currencyCode":"currencyCode"},"displayName":"displayName","monthlyCostStorage":{"nanos":6,"units":"units","currencyCode":"currencyCode"},"monthlyCostOther":{"nanos":6,"units":"units","currencyCode":"currencyCode"},"monthlyCostOsLicense":{"nanos":6,"units":"units","currencyCode":"currencyCode"},"description":"description","vmwareEngineFinding":{"nodeAllocations":[{"vmwareNode":{"code":"code"},"nodeCount":"nodeCount","allocatedAssetCount":"allocatedAssetCount"},{"vmwareNode":{"code":"code"},"nodeCount":"nodeCount","allocatedAssetCount":"allocatedAssetCount"}],"allocatedRegions":["allocatedRegions","allocatedRegions"],"allocatedAssetCount":"allocatedAssetCount"},"monthlyCostTotal":{"nanos":6,"units":"units","currencyCode":"currencyCode"}},{"soleTenantFinding":{"nodeAllocations":[{"node":{"nodeName":"nodeName"},"nodeCount":"nodeCount","allocatedAssetCount":"allocatedAssetCount"},{"node":{"nodeName":"nodeName"},"nodeCount":"nodeCount","allocatedAssetCount":"allocatedAssetCount"}],"allocatedRegions":["allocatedRegions","allocatedRegions"],"allocatedAssetCount":"allocatedAssetCount"},"computeEngineFinding":{"allocatedDiskTypes":["PERSISTENT_DISK_TYPE_UNSPECIFIED","PERSISTENT_DISK_TYPE_UNSPECIFIED"],"machineSeriesAllocations":[{"machineSeries":{"code":"code"},"allocatedAssetCount":"allocatedAssetCount"},{"machineSeries":{"code":"code"},"allocatedAssetCount":"allocatedAssetCount"}],"allocatedRegions":["allocatedRegions","allocatedRegions"],"allocatedAssetCount":"allocatedAssetCount"},"monthlyCostCompute":{"nanos":6,"units":"units","currencyCode":"currencyCode"},"machinePreferences":{"computeEnginePreferences":{"licenseType":"LICENSE_TYPE_UNSPECIFIED","machinePreferences":{"allowedMachineSeries":[{"code":"code"},{"code":"code"}]},"persistentDiskType":"PERSISTENT_DISK_TYPE_UNSPECIFIED"},"commitmentPlan":"COMMITMENT_PLAN_UNSPECIFIED","soleTenancyPreferences":{"hostMaintenancePolicy":"HOST_MAINTENANCE_POLICY_UNSPECIFIED","commitmentPlan":"COMMITMENT_PLAN_UNSPECIFIED","cpuOvercommitRatio":0.8008281904610115,"nodeTypes":[{"nodeName":"nodeName"},{"nodeName":"nodeName"}]},"vmwareEnginePreferences":{"commitmentPlan":"COMMITMENT_PLAN_UNSPECIFIED","memoryOvercommitRatio":1.4658129805029452,"storageDeduplicationCompressionRatio":5.962133916683182,"cpuOvercommitRatio":6.027456183070403},"regionPreferences":{"preferredRegions":["preferredRegions","preferredRegions"]},"sizingOptimizationStrategy":"SIZING_OPTIMIZATION_STRATEGY_UNSPECIFIED","targetProduct":"COMPUTE_MIGRATION_TARGET_PRODUCT_UNSPECIFIED"},"monthlyCostNetworkEgress":{"nanos":6,"units":"units","currencyCode":"currencyCode"},"displayName":"displayName","monthlyCostStorage":{"nanos":6,"units":"units","currencyCode":"currencyCode"},"monthlyCostOther":{"nanos":6,"units":"units","currencyCode":"currencyCode"},"monthlyCostOsLicense":{"nanos":6,"units":"units","currencyCode":"currencyCode"},"description":"description","vmwareEngineFinding":{"nodeAllocations":[{"vmwareNode":{"code":"code"},"nodeCount":"nodeCount","allocatedAssetCount":"allocatedAssetCount"},{"vmwareNode":{"code":"code"},"nodeCount":"nodeCount","allocatedAssetCount":"allocatedAssetCount"}],"allocatedRegions":["allocatedRegions","allocatedRegions"],"allocatedAssetCount":"allocatedAssetCount"},"monthlyCostTotal":{"nanos":6,"units":"units","currencyCode":"currencyCode"}}]}]},"createTime":"createTime","displayName":"displayName","name":"name","description":"description","updateTime":"updateTime","state":"STATE_UNSPECIFIED","type":"TYPE_UNSPECIFIED"}
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
        path='/v1/{parent}/reports'.format(parent='parent_example'),
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
        path='/v1/{parent}/reports'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_migrationcenter_projects_locations_sources_create(client):
    """Test case for migrationcenter_projects_locations_sources_create

    
    """
    body = {"createTime":"createTime","displayName":"displayName","managed":True,"name":"name","description":"description","updateTime":"updateTime","errorFrameCount":0,"state":"STATE_UNSPECIFIED","priority":1,"type":"SOURCE_TYPE_UNKNOWN","pendingFrameCount":6}
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
        path='/v1/{parent}/sources'.format(parent='parent_example'),
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
        path='/v1/{name}'.format(name='name_example'),
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
        path='/v1/{name}'.format(name='name_example'),
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
        path='/v1/{parent}/errorFrames'.format(parent='parent_example'),
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
        path='/v1/{parent}/sources'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_migrationcenter_projects_locations_sources_patch(client):
    """Test case for migrationcenter_projects_locations_sources_patch

    
    """
    body = {"createTime":"createTime","displayName":"displayName","managed":True,"name":"name","description":"description","updateTime":"updateTime","errorFrameCount":0,"state":"STATE_UNSPECIFIED","priority":1,"type":"SOURCE_TYPE_UNKNOWN","pendingFrameCount":6}
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
        path='/v1/{name}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

