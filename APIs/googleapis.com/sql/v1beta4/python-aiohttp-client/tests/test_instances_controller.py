# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.database_instance import DatabaseInstance
from openapi_server.models.instances_clone_request import InstancesCloneRequest
from openapi_server.models.instances_demote_master_request import InstancesDemoteMasterRequest
from openapi_server.models.instances_demote_request import InstancesDemoteRequest
from openapi_server.models.instances_export_request import InstancesExportRequest
from openapi_server.models.instances_failover_request import InstancesFailoverRequest
from openapi_server.models.instances_import_request import InstancesImportRequest
from openapi_server.models.instances_list_response import InstancesListResponse
from openapi_server.models.instances_list_server_cas_response import InstancesListServerCasResponse
from openapi_server.models.instances_reencrypt_request import InstancesReencryptRequest
from openapi_server.models.instances_restore_backup_request import InstancesRestoreBackupRequest
from openapi_server.models.instances_rotate_server_ca_request import InstancesRotateServerCaRequest
from openapi_server.models.instances_truncate_log_request import InstancesTruncateLogRequest
from openapi_server.models.operation import Operation


pytestmark = pytest.mark.asyncio

async def test_sql_instances_add_server_ca(client):
    """Test case for sql_instances_add_server_ca

    
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
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/sql/v1beta4/projects/{project}/instances/{instance}/addServerCa'.format(project='project_example', instance='instance_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sql_instances_clone(client):
    """Test case for sql_instances_clone

    
    """
    body = {"cloneContext":{"preferredZone":"preferredZone","pointInTime":"pointInTime","destinationInstanceName":"destinationInstanceName","kind":"kind","pitrTimestampMs":"pitrTimestampMs","allocatedIpRange":"allocatedIpRange","databaseNames":["databaseNames","databaseNames"],"binLogCoordinates":{"kind":"kind","binLogPosition":"binLogPosition","binLogFileName":"binLogFileName"}}}
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
        path='/sql/v1beta4/projects/{project}/instances/{instance}/clone'.format(project='project_example', instance='instance_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sql_instances_delete(client):
    """Test case for sql_instances_delete

    
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
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/sql/v1beta4/projects/{project}/instances/{instance}'.format(project='project_example', instance='instance_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sql_instances_demote(client):
    """Test case for sql_instances_demote

    
    """
    body = {"demoteContext":{"kind":"kind","sourceRepresentativeInstanceName":"sourceRepresentativeInstanceName"}}
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
        path='/sql/v1beta4/projects/{project}/instances/{instance}/demote'.format(project='project_example', instance='instance_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sql_instances_demote_master(client):
    """Test case for sql_instances_demote_master

    
    """
    body = {"demoteMasterContext":{"skipReplicationSetup":True,"masterInstanceName":"masterInstanceName","kind":"kind","verifyGtidConsistency":True,"replicaConfiguration":{"kind":"kind","mysqlReplicaConfiguration":{"clientCertificate":"clientCertificate","password":"password","clientKey":"clientKey","kind":"kind","caCertificate":"caCertificate","username":"username"}}}}
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
        path='/sql/v1beta4/projects/{project}/instances/{instance}/demoteMaster'.format(project='project_example', instance='instance_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sql_instances_export(client):
    """Test case for sql_instances_export

    
    """
    body = {"exportContext":{"databases":["databases","databases"],"sqlExportOptions":{"tables":["tables","tables"],"parallel":True,"threads":1,"schemaOnly":True,"mysqlExportOptions":{"masterData":6}},"bakExportOptions":{"striped":True,"bakType":"BAK_TYPE_UNSPECIFIED","stripeCount":0,"copyOnly":True,"differentialBase":True},"csvExportOptions":{"fieldsTerminatedBy":"fieldsTerminatedBy","linesTerminatedBy":"linesTerminatedBy","quoteCharacter":"quoteCharacter","escapeCharacter":"escapeCharacter","selectQuery":"selectQuery"},"kind":"kind","offload":True,"uri":"uri","fileType":"SQL_FILE_TYPE_UNSPECIFIED"}}
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
        path='/sql/v1beta4/projects/{project}/instances/{instance}/export'.format(project='project_example', instance='instance_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sql_instances_failover(client):
    """Test case for sql_instances_failover

    
    """
    body = {"failoverContext":{"kind":"kind","settingsVersion":"settingsVersion"}}
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
        path='/sql/v1beta4/projects/{project}/instances/{instance}/failover'.format(project='project_example', instance='instance_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sql_instances_get(client):
    """Test case for sql_instances_get

    
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
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/sql/v1beta4/projects/{project}/instances/{instance}'.format(project='project_example', instance='instance_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sql_instances_import(client):
    """Test case for sql_instances_import

    
    """
    body = {"importContext":{"database":"database","kind":"kind","csvImportOptions":{"columns":["columns","columns"],"fieldsTerminatedBy":"fieldsTerminatedBy","linesTerminatedBy":"linesTerminatedBy","quoteCharacter":"quoteCharacter","escapeCharacter":"escapeCharacter","table":"table"},"bakImportOptions":{"recoveryOnly":True,"stopAt":"stopAt","striped":True,"bakType":"BAK_TYPE_UNSPECIFIED","noRecovery":True,"encryptionOptions":{"certPath":"certPath","pvkPath":"pvkPath","pvkPassword":"pvkPassword"},"stopAtMark":"stopAtMark"},"importUser":"importUser","uri":"uri","fileType":"SQL_FILE_TYPE_UNSPECIFIED"}}
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
        path='/sql/v1beta4/projects/{project}/instances/{instance}/import'.format(project='project_example', instance='instance_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sql_instances_insert(client):
    """Test case for sql_instances_insert

    
    """
    body = {"ipv6Address":"ipv6Address","failoverReplica":{"available":True,"name":"name"},"backendType":"SQL_BACKEND_TYPE_UNSPECIFIED","scheduledMaintenance":{"canDefer":True,"canReschedule":True,"startTime":"startTime","scheduleDeadlineTime":"scheduleDeadlineTime"},"maintenanceVersion":"maintenanceVersion","dnsName":"dnsName","project":"project","replicaNames":["replicaNames","replicaNames"],"satisfiesPzs":True,"diskEncryptionConfiguration":{"kind":"kind","kmsKeyName":"kmsKeyName"},"maxDiskSize":"maxDiskSize","databaseVersion":"SQL_DATABASE_VERSION_UNSPECIFIED","serviceAccountEmailAddress":"serviceAccountEmailAddress","replicaConfiguration":{"kind":"kind","cascadableReplica":True,"mysqlReplicaConfiguration":{"sslCipher":"sslCipher","verifyServerCertificate":True,"clientCertificate":"clientCertificate","password":"password","dumpFilePath":"dumpFilePath","clientKey":"clientKey","kind":"kind","masterHeartbeatPeriod":"masterHeartbeatPeriod","connectRetryInterval":6,"caCertificate":"caCertificate","username":"username"},"failoverTarget":True},"masterInstanceName":"masterInstanceName","onPremisesConfiguration":{"sourceInstance":{"name":"name","project":"project","region":"region"},"clientCertificate":"clientCertificate","password":"password","dumpFilePath":"dumpFilePath","clientKey":"clientKey","kind":"kind","hostPort":"hostPort","caCertificate":"caCertificate","username":"username"},"databaseInstalledVersion":"databaseInstalledVersion","secondaryGceZone":"secondaryGceZone","availableMaintenanceVersions":["availableMaintenanceVersions","availableMaintenanceVersions"],"state":"SQL_INSTANCE_STATE_UNSPECIFIED","primaryDnsName":"primaryDnsName","gceZone":"gceZone","rootPassword":"rootPassword","outOfDiskReport":{"sqlOutOfDiskState":"SQL_OUT_OF_DISK_STATE_UNSPECIFIED","sqlMinRecommendedIncreaseSizeGb":0},"settings":{"dataDiskSizeGb":"dataDiskSizeGb","databaseFlags":[{"name":"name","value":"value"},{"name":"name","value":"value"}],"dataDiskType":"SQL_DATA_DISK_TYPE_UNSPECIFIED","activationPolicy":"SQL_ACTIVATION_POLICY_UNSPECIFIED","edition":"EDITION_UNSPECIFIED","userLabels":{"key":"userLabels"},"deletionProtectionEnabled":True,"sqlServerAuditConfig":{"bucket":"bucket","retentionInterval":"retentionInterval","uploadInterval":"uploadInterval","kind":"kind"},"maintenanceWindow":{"hour":3,"kind":"kind","updateTrack":"SQL_UPDATE_TRACK_UNSPECIFIED","day":9},"availabilityType":"SQL_AVAILABILITY_TYPE_UNSPECIFIED","pricingPlan":"SQL_PRICING_PLAN_UNSPECIFIED","activeDirectoryConfig":{"kind":"kind","domain":"domain"},"tier":"tier","replicationType":"SQL_REPLICATION_TYPE_UNSPECIFIED","ipConfiguration":{"ipv4Enabled":True,"requireSsl":True,"privateNetwork":"privateNetwork","pscConfig":{"pscEnabled":True,"allowedConsumerProjects":["allowedConsumerProjects","allowedConsumerProjects"]},"allocatedIpRange":"allocatedIpRange","authorizedNetworks":[{"expirationTime":"expirationTime","kind":"kind","name":"name","value":"value"},{"expirationTime":"expirationTime","kind":"kind","name":"name","value":"value"}],"enablePrivatePathForGoogleCloudServices":True,"sslMode":"SSL_MODE_UNSPECIFIED"},"collation":"collation","crashSafeReplicationEnabled":True,"dataCacheConfig":{"dataCacheEnabled":True},"settingsVersion":"settingsVersion","advancedMachineFeatures":{"threadsPerCore":1},"backupConfiguration":{"backupRetentionSettings":{"retainedBackups":5,"retentionUnit":"RETENTION_UNIT_UNSPECIFIED"},"kind":"kind","transactionLogRetentionDays":5,"binaryLogEnabled":True,"replicationLogArchivingEnabled":True,"location":"location","startTime":"startTime","pointInTimeRecoveryEnabled":True,"enabled":True},"denyMaintenancePeriods":[{"endDate":"endDate","time":"time","startDate":"startDate"},{"endDate":"endDate","time":"time","startDate":"startDate"}],"locationPreference":{"secondaryZone":"secondaryZone","zone":"zone","kind":"kind","followGaeApplication":"followGaeApplication"},"storageAutoResizeLimit":"storageAutoResizeLimit","kind":"kind","timeZone":"timeZone","authorizedGaeApplications":["authorizedGaeApplications","authorizedGaeApplications"],"insightsConfig":{"recordClientAddress":True,"queryStringLength":7,"queryPlansPerMinute":2,"queryInsightsEnabled":True,"recordApplicationTags":True},"passwordValidationPolicy":{"complexity":"COMPLEXITY_UNSPECIFIED","disallowCompromisedCredentials":True,"reuseInterval":4,"minLength":2,"passwordChangeInterval":"passwordChangeInterval","disallowUsernameSubstring":True,"enablePasswordPolicy":True},"connectorEnforcement":"CONNECTOR_ENFORCEMENT_UNSPECIFIED","storageAutoResize":True,"databaseReplicationEnabled":True},"kind":"kind","suspensionReason":["SQL_SUSPENSION_REASON_UNSPECIFIED","SQL_SUSPENSION_REASON_UNSPECIFIED"],"instanceType":"SQL_INSTANCE_TYPE_UNSPECIFIED","currentDiskSize":"currentDiskSize","diskEncryptionStatus":{"kind":"kind","kmsKeyVersionName":"kmsKeyVersionName"},"sqlNetworkArchitecture":"SQL_NETWORK_ARCHITECTURE_UNSPECIFIED","writeEndpoint":"writeEndpoint","pscServiceAttachmentLink":"pscServiceAttachmentLink","selfLink":"selfLink","createTime":"createTime","serverCaCert":{"commonName":"commonName","instance":"instance","createTime":"createTime","expirationTime":"expirationTime","kind":"kind","certSerialNumber":"certSerialNumber","sha1Fingerprint":"sha1Fingerprint","cert":"cert","selfLink":"selfLink"},"name":"name","etag":"etag","ipAddresses":[{"ipAddress":"ipAddress","timeToRetire":"timeToRetire","type":"SQL_IP_ADDRESS_TYPE_UNSPECIFIED"},{"ipAddress":"ipAddress","timeToRetire":"timeToRetire","type":"SQL_IP_ADDRESS_TYPE_UNSPECIFIED"}],"connectionName":"connectionName","region":"region"}
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
        path='/sql/v1beta4/projects/{project}/instances'.format(project='project_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sql_instances_list(client):
    """Test case for sql_instances_list

    
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
                    ('maxResults', 56),
                    ('pageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/sql/v1beta4/projects/{project}/instances'.format(project='project_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sql_instances_list_server_cas(client):
    """Test case for sql_instances_list_server_cas

    
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
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/sql/v1beta4/projects/{project}/instances/{instance}/listServerCas'.format(project='project_example', instance='instance_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sql_instances_patch(client):
    """Test case for sql_instances_patch

    
    """
    body = {"ipv6Address":"ipv6Address","failoverReplica":{"available":True,"name":"name"},"backendType":"SQL_BACKEND_TYPE_UNSPECIFIED","scheduledMaintenance":{"canDefer":True,"canReschedule":True,"startTime":"startTime","scheduleDeadlineTime":"scheduleDeadlineTime"},"maintenanceVersion":"maintenanceVersion","dnsName":"dnsName","project":"project","replicaNames":["replicaNames","replicaNames"],"satisfiesPzs":True,"diskEncryptionConfiguration":{"kind":"kind","kmsKeyName":"kmsKeyName"},"maxDiskSize":"maxDiskSize","databaseVersion":"SQL_DATABASE_VERSION_UNSPECIFIED","serviceAccountEmailAddress":"serviceAccountEmailAddress","replicaConfiguration":{"kind":"kind","cascadableReplica":True,"mysqlReplicaConfiguration":{"sslCipher":"sslCipher","verifyServerCertificate":True,"clientCertificate":"clientCertificate","password":"password","dumpFilePath":"dumpFilePath","clientKey":"clientKey","kind":"kind","masterHeartbeatPeriod":"masterHeartbeatPeriod","connectRetryInterval":6,"caCertificate":"caCertificate","username":"username"},"failoverTarget":True},"masterInstanceName":"masterInstanceName","onPremisesConfiguration":{"sourceInstance":{"name":"name","project":"project","region":"region"},"clientCertificate":"clientCertificate","password":"password","dumpFilePath":"dumpFilePath","clientKey":"clientKey","kind":"kind","hostPort":"hostPort","caCertificate":"caCertificate","username":"username"},"databaseInstalledVersion":"databaseInstalledVersion","secondaryGceZone":"secondaryGceZone","availableMaintenanceVersions":["availableMaintenanceVersions","availableMaintenanceVersions"],"state":"SQL_INSTANCE_STATE_UNSPECIFIED","primaryDnsName":"primaryDnsName","gceZone":"gceZone","rootPassword":"rootPassword","outOfDiskReport":{"sqlOutOfDiskState":"SQL_OUT_OF_DISK_STATE_UNSPECIFIED","sqlMinRecommendedIncreaseSizeGb":0},"settings":{"dataDiskSizeGb":"dataDiskSizeGb","databaseFlags":[{"name":"name","value":"value"},{"name":"name","value":"value"}],"dataDiskType":"SQL_DATA_DISK_TYPE_UNSPECIFIED","activationPolicy":"SQL_ACTIVATION_POLICY_UNSPECIFIED","edition":"EDITION_UNSPECIFIED","userLabels":{"key":"userLabels"},"deletionProtectionEnabled":True,"sqlServerAuditConfig":{"bucket":"bucket","retentionInterval":"retentionInterval","uploadInterval":"uploadInterval","kind":"kind"},"maintenanceWindow":{"hour":3,"kind":"kind","updateTrack":"SQL_UPDATE_TRACK_UNSPECIFIED","day":9},"availabilityType":"SQL_AVAILABILITY_TYPE_UNSPECIFIED","pricingPlan":"SQL_PRICING_PLAN_UNSPECIFIED","activeDirectoryConfig":{"kind":"kind","domain":"domain"},"tier":"tier","replicationType":"SQL_REPLICATION_TYPE_UNSPECIFIED","ipConfiguration":{"ipv4Enabled":True,"requireSsl":True,"privateNetwork":"privateNetwork","pscConfig":{"pscEnabled":True,"allowedConsumerProjects":["allowedConsumerProjects","allowedConsumerProjects"]},"allocatedIpRange":"allocatedIpRange","authorizedNetworks":[{"expirationTime":"expirationTime","kind":"kind","name":"name","value":"value"},{"expirationTime":"expirationTime","kind":"kind","name":"name","value":"value"}],"enablePrivatePathForGoogleCloudServices":True,"sslMode":"SSL_MODE_UNSPECIFIED"},"collation":"collation","crashSafeReplicationEnabled":True,"dataCacheConfig":{"dataCacheEnabled":True},"settingsVersion":"settingsVersion","advancedMachineFeatures":{"threadsPerCore":1},"backupConfiguration":{"backupRetentionSettings":{"retainedBackups":5,"retentionUnit":"RETENTION_UNIT_UNSPECIFIED"},"kind":"kind","transactionLogRetentionDays":5,"binaryLogEnabled":True,"replicationLogArchivingEnabled":True,"location":"location","startTime":"startTime","pointInTimeRecoveryEnabled":True,"enabled":True},"denyMaintenancePeriods":[{"endDate":"endDate","time":"time","startDate":"startDate"},{"endDate":"endDate","time":"time","startDate":"startDate"}],"locationPreference":{"secondaryZone":"secondaryZone","zone":"zone","kind":"kind","followGaeApplication":"followGaeApplication"},"storageAutoResizeLimit":"storageAutoResizeLimit","kind":"kind","timeZone":"timeZone","authorizedGaeApplications":["authorizedGaeApplications","authorizedGaeApplications"],"insightsConfig":{"recordClientAddress":True,"queryStringLength":7,"queryPlansPerMinute":2,"queryInsightsEnabled":True,"recordApplicationTags":True},"passwordValidationPolicy":{"complexity":"COMPLEXITY_UNSPECIFIED","disallowCompromisedCredentials":True,"reuseInterval":4,"minLength":2,"passwordChangeInterval":"passwordChangeInterval","disallowUsernameSubstring":True,"enablePasswordPolicy":True},"connectorEnforcement":"CONNECTOR_ENFORCEMENT_UNSPECIFIED","storageAutoResize":True,"databaseReplicationEnabled":True},"kind":"kind","suspensionReason":["SQL_SUSPENSION_REASON_UNSPECIFIED","SQL_SUSPENSION_REASON_UNSPECIFIED"],"instanceType":"SQL_INSTANCE_TYPE_UNSPECIFIED","currentDiskSize":"currentDiskSize","diskEncryptionStatus":{"kind":"kind","kmsKeyVersionName":"kmsKeyVersionName"},"sqlNetworkArchitecture":"SQL_NETWORK_ARCHITECTURE_UNSPECIFIED","writeEndpoint":"writeEndpoint","pscServiceAttachmentLink":"pscServiceAttachmentLink","selfLink":"selfLink","createTime":"createTime","serverCaCert":{"commonName":"commonName","instance":"instance","createTime":"createTime","expirationTime":"expirationTime","kind":"kind","certSerialNumber":"certSerialNumber","sha1Fingerprint":"sha1Fingerprint","cert":"cert","selfLink":"selfLink"},"name":"name","etag":"etag","ipAddresses":[{"ipAddress":"ipAddress","timeToRetire":"timeToRetire","type":"SQL_IP_ADDRESS_TYPE_UNSPECIFIED"},{"ipAddress":"ipAddress","timeToRetire":"timeToRetire","type":"SQL_IP_ADDRESS_TYPE_UNSPECIFIED"}],"connectionName":"connectionName","region":"region"}
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
        method='PATCH',
        path='/sql/v1beta4/projects/{project}/instances/{instance}'.format(project='project_example', instance='instance_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sql_instances_promote_replica(client):
    """Test case for sql_instances_promote_replica

    
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
                    ('failover', True)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/sql/v1beta4/projects/{project}/instances/{instance}/promoteReplica'.format(project='project_example', instance='instance_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sql_instances_reencrypt(client):
    """Test case for sql_instances_reencrypt

    
    """
    body = {"backupReencryptionConfig":{"backupLimit":0,"backupType":"BACKUP_TYPE_UNSPECIFIED"}}
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
        path='/sql/v1beta4/projects/{project}/instances/{instance}/reencrypt'.format(project='project_example', instance='instance_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sql_instances_reset_ssl_config(client):
    """Test case for sql_instances_reset_ssl_config

    
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
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/sql/v1beta4/projects/{project}/instances/{instance}/resetSslConfig'.format(project='project_example', instance='instance_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sql_instances_restart(client):
    """Test case for sql_instances_restart

    
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
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/sql/v1beta4/projects/{project}/instances/{instance}/restart'.format(project='project_example', instance='instance_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sql_instances_restore_backup(client):
    """Test case for sql_instances_restore_backup

    
    """
    body = {"restoreBackupContext":{"backupRunId":"backupRunId","instanceId":"instanceId","kind":"kind","project":"project"}}
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
        path='/sql/v1beta4/projects/{project}/instances/{instance}/restoreBackup'.format(project='project_example', instance='instance_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sql_instances_rotate_server_ca(client):
    """Test case for sql_instances_rotate_server_ca

    
    """
    body = {"rotateServerCaContext":{"kind":"kind","nextVersion":"nextVersion"}}
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
        path='/sql/v1beta4/projects/{project}/instances/{instance}/rotateServerCa'.format(project='project_example', instance='instance_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sql_instances_start_replica(client):
    """Test case for sql_instances_start_replica

    
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
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/sql/v1beta4/projects/{project}/instances/{instance}/startReplica'.format(project='project_example', instance='instance_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sql_instances_stop_replica(client):
    """Test case for sql_instances_stop_replica

    
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
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/sql/v1beta4/projects/{project}/instances/{instance}/stopReplica'.format(project='project_example', instance='instance_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sql_instances_switchover(client):
    """Test case for sql_instances_switchover

    
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
                    ('dbTimeout', 'db_timeout_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/sql/v1beta4/projects/{project}/instances/{instance}/switchover'.format(project='project_example', instance='instance_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sql_instances_truncate_log(client):
    """Test case for sql_instances_truncate_log

    
    """
    body = {"truncateLogContext":{"logType":"logType","kind":"kind"}}
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
        path='/sql/v1beta4/projects/{project}/instances/{instance}/truncateLog'.format(project='project_example', instance='instance_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sql_instances_update(client):
    """Test case for sql_instances_update

    
    """
    body = {"ipv6Address":"ipv6Address","failoverReplica":{"available":True,"name":"name"},"backendType":"SQL_BACKEND_TYPE_UNSPECIFIED","scheduledMaintenance":{"canDefer":True,"canReschedule":True,"startTime":"startTime","scheduleDeadlineTime":"scheduleDeadlineTime"},"maintenanceVersion":"maintenanceVersion","dnsName":"dnsName","project":"project","replicaNames":["replicaNames","replicaNames"],"satisfiesPzs":True,"diskEncryptionConfiguration":{"kind":"kind","kmsKeyName":"kmsKeyName"},"maxDiskSize":"maxDiskSize","databaseVersion":"SQL_DATABASE_VERSION_UNSPECIFIED","serviceAccountEmailAddress":"serviceAccountEmailAddress","replicaConfiguration":{"kind":"kind","cascadableReplica":True,"mysqlReplicaConfiguration":{"sslCipher":"sslCipher","verifyServerCertificate":True,"clientCertificate":"clientCertificate","password":"password","dumpFilePath":"dumpFilePath","clientKey":"clientKey","kind":"kind","masterHeartbeatPeriod":"masterHeartbeatPeriod","connectRetryInterval":6,"caCertificate":"caCertificate","username":"username"},"failoverTarget":True},"masterInstanceName":"masterInstanceName","onPremisesConfiguration":{"sourceInstance":{"name":"name","project":"project","region":"region"},"clientCertificate":"clientCertificate","password":"password","dumpFilePath":"dumpFilePath","clientKey":"clientKey","kind":"kind","hostPort":"hostPort","caCertificate":"caCertificate","username":"username"},"databaseInstalledVersion":"databaseInstalledVersion","secondaryGceZone":"secondaryGceZone","availableMaintenanceVersions":["availableMaintenanceVersions","availableMaintenanceVersions"],"state":"SQL_INSTANCE_STATE_UNSPECIFIED","primaryDnsName":"primaryDnsName","gceZone":"gceZone","rootPassword":"rootPassword","outOfDiskReport":{"sqlOutOfDiskState":"SQL_OUT_OF_DISK_STATE_UNSPECIFIED","sqlMinRecommendedIncreaseSizeGb":0},"settings":{"dataDiskSizeGb":"dataDiskSizeGb","databaseFlags":[{"name":"name","value":"value"},{"name":"name","value":"value"}],"dataDiskType":"SQL_DATA_DISK_TYPE_UNSPECIFIED","activationPolicy":"SQL_ACTIVATION_POLICY_UNSPECIFIED","edition":"EDITION_UNSPECIFIED","userLabels":{"key":"userLabels"},"deletionProtectionEnabled":True,"sqlServerAuditConfig":{"bucket":"bucket","retentionInterval":"retentionInterval","uploadInterval":"uploadInterval","kind":"kind"},"maintenanceWindow":{"hour":3,"kind":"kind","updateTrack":"SQL_UPDATE_TRACK_UNSPECIFIED","day":9},"availabilityType":"SQL_AVAILABILITY_TYPE_UNSPECIFIED","pricingPlan":"SQL_PRICING_PLAN_UNSPECIFIED","activeDirectoryConfig":{"kind":"kind","domain":"domain"},"tier":"tier","replicationType":"SQL_REPLICATION_TYPE_UNSPECIFIED","ipConfiguration":{"ipv4Enabled":True,"requireSsl":True,"privateNetwork":"privateNetwork","pscConfig":{"pscEnabled":True,"allowedConsumerProjects":["allowedConsumerProjects","allowedConsumerProjects"]},"allocatedIpRange":"allocatedIpRange","authorizedNetworks":[{"expirationTime":"expirationTime","kind":"kind","name":"name","value":"value"},{"expirationTime":"expirationTime","kind":"kind","name":"name","value":"value"}],"enablePrivatePathForGoogleCloudServices":True,"sslMode":"SSL_MODE_UNSPECIFIED"},"collation":"collation","crashSafeReplicationEnabled":True,"dataCacheConfig":{"dataCacheEnabled":True},"settingsVersion":"settingsVersion","advancedMachineFeatures":{"threadsPerCore":1},"backupConfiguration":{"backupRetentionSettings":{"retainedBackups":5,"retentionUnit":"RETENTION_UNIT_UNSPECIFIED"},"kind":"kind","transactionLogRetentionDays":5,"binaryLogEnabled":True,"replicationLogArchivingEnabled":True,"location":"location","startTime":"startTime","pointInTimeRecoveryEnabled":True,"enabled":True},"denyMaintenancePeriods":[{"endDate":"endDate","time":"time","startDate":"startDate"},{"endDate":"endDate","time":"time","startDate":"startDate"}],"locationPreference":{"secondaryZone":"secondaryZone","zone":"zone","kind":"kind","followGaeApplication":"followGaeApplication"},"storageAutoResizeLimit":"storageAutoResizeLimit","kind":"kind","timeZone":"timeZone","authorizedGaeApplications":["authorizedGaeApplications","authorizedGaeApplications"],"insightsConfig":{"recordClientAddress":True,"queryStringLength":7,"queryPlansPerMinute":2,"queryInsightsEnabled":True,"recordApplicationTags":True},"passwordValidationPolicy":{"complexity":"COMPLEXITY_UNSPECIFIED","disallowCompromisedCredentials":True,"reuseInterval":4,"minLength":2,"passwordChangeInterval":"passwordChangeInterval","disallowUsernameSubstring":True,"enablePasswordPolicy":True},"connectorEnforcement":"CONNECTOR_ENFORCEMENT_UNSPECIFIED","storageAutoResize":True,"databaseReplicationEnabled":True},"kind":"kind","suspensionReason":["SQL_SUSPENSION_REASON_UNSPECIFIED","SQL_SUSPENSION_REASON_UNSPECIFIED"],"instanceType":"SQL_INSTANCE_TYPE_UNSPECIFIED","currentDiskSize":"currentDiskSize","diskEncryptionStatus":{"kind":"kind","kmsKeyVersionName":"kmsKeyVersionName"},"sqlNetworkArchitecture":"SQL_NETWORK_ARCHITECTURE_UNSPECIFIED","writeEndpoint":"writeEndpoint","pscServiceAttachmentLink":"pscServiceAttachmentLink","selfLink":"selfLink","createTime":"createTime","serverCaCert":{"commonName":"commonName","instance":"instance","createTime":"createTime","expirationTime":"expirationTime","kind":"kind","certSerialNumber":"certSerialNumber","sha1Fingerprint":"sha1Fingerprint","cert":"cert","selfLink":"selfLink"},"name":"name","etag":"etag","ipAddresses":[{"ipAddress":"ipAddress","timeToRetire":"timeToRetire","type":"SQL_IP_ADDRESS_TYPE_UNSPECIFIED"},{"ipAddress":"ipAddress","timeToRetire":"timeToRetire","type":"SQL_IP_ADDRESS_TYPE_UNSPECIFIED"}],"connectionName":"connectionName","region":"region"}
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
        method='PUT',
        path='/sql/v1beta4/projects/{project}/instances/{instance}'.format(project='project_example', instance='instance_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

