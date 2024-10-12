# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.activate_certificate_authority_request import ActivateCertificateAuthorityRequest
from openapi_server.models.ca_pool import CaPool
from openapi_server.models.certificate import Certificate
from openapi_server.models.certificate_authority import CertificateAuthority
from openapi_server.models.certificate_template import CertificateTemplate
from openapi_server.models.disable_certificate_authority_request import DisableCertificateAuthorityRequest
from openapi_server.models.enable_certificate_authority_request import EnableCertificateAuthorityRequest
from openapi_server.models.fetch_ca_certs_request import FetchCaCertsRequest
from openapi_server.models.fetch_ca_certs_response import FetchCaCertsResponse
from openapi_server.models.fetch_certificate_authority_csr_response import FetchCertificateAuthorityCsrResponse
from openapi_server.models.list_ca_pools_response import ListCaPoolsResponse
from openapi_server.models.list_certificate_authorities_response import ListCertificateAuthoritiesResponse
from openapi_server.models.list_certificate_revocation_lists_response import ListCertificateRevocationListsResponse
from openapi_server.models.list_certificate_templates_response import ListCertificateTemplatesResponse
from openapi_server.models.list_certificates_response import ListCertificatesResponse
from openapi_server.models.list_locations_response import ListLocationsResponse
from openapi_server.models.list_operations_response import ListOperationsResponse
from openapi_server.models.operation import Operation
from openapi_server.models.policy import Policy
from openapi_server.models.revoke_certificate_request import RevokeCertificateRequest
from openapi_server.models.set_iam_policy_request import SetIamPolicyRequest
from openapi_server.models.test_iam_permissions_request import TestIamPermissionsRequest
from openapi_server.models.test_iam_permissions_response import TestIamPermissionsResponse
from openapi_server.models.undelete_certificate_authority_request import UndeleteCertificateAuthorityRequest


pytestmark = pytest.mark.asyncio

async def test_privateca_projects_locations_ca_pools_certificate_authorities_activate(client):
    """Test case for privateca_projects_locations_ca_pools_certificate_authorities_activate

    
    """
    body = {"pemCaCertificate":"pemCaCertificate","subordinateConfig":{"pemIssuerChain":{"pemCertificates":["pemCertificates","pemCertificates"]},"certificateAuthority":"certificateAuthority"},"requestId":"requestId"}
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
        path='/v1/{nameactivat}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_privateca_projects_locations_ca_pools_certificate_authorities_certificate_revocation_lists_list(client):
    """Test case for privateca_projects_locations_ca_pools_certificate_authorities_certificate_revocation_lists_list

    
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
        path='/v1/{parent}/certificateRevocationLists'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_privateca_projects_locations_ca_pools_certificate_authorities_create(client):
    """Test case for privateca_projects_locations_ca_pools_certificate_authorities_create

    
    """
    body = {"subordinateConfig":{"pemIssuerChain":{"pemCertificates":["pemCertificates","pemCertificates"]},"certificateAuthority":"certificateAuthority"},"accessUrls":{"crlAccessUrls":["crlAccessUrls","crlAccessUrls"],"caCertificateAccessUrl":"caCertificateAccessUrl"},"lifetime":"lifetime","gcsBucket":"gcsBucket","updateTime":"updateTime","type":"TYPE_UNSPECIFIED","labels":{"key":"labels"},"expireTime":"expireTime","tier":"TIER_UNSPECIFIED","createTime":"createTime","deleteTime":"deleteTime","caCertificateDescriptions":[{"x509Description":{"additionalExtensions":[{"critical":True,"value":"value","objectId":{"objectIdPath":[0,0]}},{"critical":True,"value":"value","objectId":{"objectIdPath":[0,0]}}],"keyUsage":{"baseKeyUsage":{"crlSign":True,"decipherOnly":True,"keyEncipherment":True,"contentCommitment":True,"encipherOnly":True,"digitalSignature":True,"keyAgreement":True,"dataEncipherment":True,"certSign":True},"unknownExtendedKeyUsages":[{"objectIdPath":[0,0]},{"objectIdPath":[0,0]}],"extendedKeyUsage":{"codeSigning":True,"ocspSigning":True,"emailProtection":True,"serverAuth":True,"timeStamping":True,"clientAuth":True}},"aiaOcspServers":["aiaOcspServers","aiaOcspServers"],"caOptions":{"isCa":True,"maxIssuerPathLength":6},"policyIds":[{"objectIdPath":[0,0]},{"objectIdPath":[0,0]}],"nameConstraints":{"permittedEmailAddresses":["permittedEmailAddresses","permittedEmailAddresses"],"excludedEmailAddresses":["excludedEmailAddresses","excludedEmailAddresses"],"excludedIpRanges":["excludedIpRanges","excludedIpRanges"],"critical":True,"excludedDnsNames":["excludedDnsNames","excludedDnsNames"],"excludedUris":["excludedUris","excludedUris"],"permittedUris":["permittedUris","permittedUris"],"permittedIpRanges":["permittedIpRanges","permittedIpRanges"],"permittedDnsNames":["permittedDnsNames","permittedDnsNames"]}},"aiaIssuingCertificateUrls":["aiaIssuingCertificateUrls","aiaIssuingCertificateUrls"],"subjectDescription":{"hexSerialNumber":"hexSerialNumber","notBeforeTime":"notBeforeTime","subject":{"commonName":"commonName","province":"province","streetAddress":"streetAddress","countryCode":"countryCode","organization":"organization","postalCode":"postalCode","locality":"locality","organizationalUnit":"organizationalUnit"},"lifetime":"lifetime","notAfterTime":"notAfterTime","subjectAltName":{"uris":["uris","uris"],"emailAddresses":["emailAddresses","emailAddresses"],"dnsNames":["dnsNames","dnsNames"],"ipAddresses":["ipAddresses","ipAddresses"],"customSans":[{"critical":True,"value":"value","objectId":{"objectIdPath":[0,0]}},{"critical":True,"value":"value","objectId":{"objectIdPath":[0,0]}}]}},"subjectKeyId":{"keyId":"keyId"},"certFingerprint":{"sha256Hash":"sha256Hash"},"authorityKeyId":{"keyId":"keyId"},"publicKey":{"format":"KEY_FORMAT_UNSPECIFIED","key":"key"},"crlDistributionPoints":["crlDistributionPoints","crlDistributionPoints"]},{"x509Description":{"additionalExtensions":[{"critical":True,"value":"value","objectId":{"objectIdPath":[0,0]}},{"critical":True,"value":"value","objectId":{"objectIdPath":[0,0]}}],"keyUsage":{"baseKeyUsage":{"crlSign":True,"decipherOnly":True,"keyEncipherment":True,"contentCommitment":True,"encipherOnly":True,"digitalSignature":True,"keyAgreement":True,"dataEncipherment":True,"certSign":True},"unknownExtendedKeyUsages":[{"objectIdPath":[0,0]},{"objectIdPath":[0,0]}],"extendedKeyUsage":{"codeSigning":True,"ocspSigning":True,"emailProtection":True,"serverAuth":True,"timeStamping":True,"clientAuth":True}},"aiaOcspServers":["aiaOcspServers","aiaOcspServers"],"caOptions":{"isCa":True,"maxIssuerPathLength":6},"policyIds":[{"objectIdPath":[0,0]},{"objectIdPath":[0,0]}],"nameConstraints":{"permittedEmailAddresses":["permittedEmailAddresses","permittedEmailAddresses"],"excludedEmailAddresses":["excludedEmailAddresses","excludedEmailAddresses"],"excludedIpRanges":["excludedIpRanges","excludedIpRanges"],"critical":True,"excludedDnsNames":["excludedDnsNames","excludedDnsNames"],"excludedUris":["excludedUris","excludedUris"],"permittedUris":["permittedUris","permittedUris"],"permittedIpRanges":["permittedIpRanges","permittedIpRanges"],"permittedDnsNames":["permittedDnsNames","permittedDnsNames"]}},"aiaIssuingCertificateUrls":["aiaIssuingCertificateUrls","aiaIssuingCertificateUrls"],"subjectDescription":{"hexSerialNumber":"hexSerialNumber","notBeforeTime":"notBeforeTime","subject":{"commonName":"commonName","province":"province","streetAddress":"streetAddress","countryCode":"countryCode","organization":"organization","postalCode":"postalCode","locality":"locality","organizationalUnit":"organizationalUnit"},"lifetime":"lifetime","notAfterTime":"notAfterTime","subjectAltName":{"uris":["uris","uris"],"emailAddresses":["emailAddresses","emailAddresses"],"dnsNames":["dnsNames","dnsNames"],"ipAddresses":["ipAddresses","ipAddresses"],"customSans":[{"critical":True,"value":"value","objectId":{"objectIdPath":[0,0]}},{"critical":True,"value":"value","objectId":{"objectIdPath":[0,0]}}]}},"subjectKeyId":{"keyId":"keyId"},"certFingerprint":{"sha256Hash":"sha256Hash"},"authorityKeyId":{"keyId":"keyId"},"publicKey":{"format":"KEY_FORMAT_UNSPECIFIED","key":"key"},"crlDistributionPoints":["crlDistributionPoints","crlDistributionPoints"]}],"name":"name","state":"STATE_UNSPECIFIED","config":{"x509Config":{"additionalExtensions":[{"critical":True,"value":"value","objectId":{"objectIdPath":[0,0]}},{"critical":True,"value":"value","objectId":{"objectIdPath":[0,0]}}],"keyUsage":{"baseKeyUsage":{"crlSign":True,"decipherOnly":True,"keyEncipherment":True,"contentCommitment":True,"encipherOnly":True,"digitalSignature":True,"keyAgreement":True,"dataEncipherment":True,"certSign":True},"unknownExtendedKeyUsages":[{"objectIdPath":[0,0]},{"objectIdPath":[0,0]}],"extendedKeyUsage":{"codeSigning":True,"ocspSigning":True,"emailProtection":True,"serverAuth":True,"timeStamping":True,"clientAuth":True}},"aiaOcspServers":["aiaOcspServers","aiaOcspServers"],"caOptions":{"isCa":True,"maxIssuerPathLength":6},"policyIds":[{"objectIdPath":[0,0]},{"objectIdPath":[0,0]}],"nameConstraints":{"permittedEmailAddresses":["permittedEmailAddresses","permittedEmailAddresses"],"excludedEmailAddresses":["excludedEmailAddresses","excludedEmailAddresses"],"excludedIpRanges":["excludedIpRanges","excludedIpRanges"],"critical":True,"excludedDnsNames":["excludedDnsNames","excludedDnsNames"],"excludedUris":["excludedUris","excludedUris"],"permittedUris":["permittedUris","permittedUris"],"permittedIpRanges":["permittedIpRanges","permittedIpRanges"],"permittedDnsNames":["permittedDnsNames","permittedDnsNames"]}},"subjectConfig":{"subject":{"commonName":"commonName","province":"province","streetAddress":"streetAddress","countryCode":"countryCode","organization":"organization","postalCode":"postalCode","locality":"locality","organizationalUnit":"organizationalUnit"},"subjectAltName":{"uris":["uris","uris"],"emailAddresses":["emailAddresses","emailAddresses"],"dnsNames":["dnsNames","dnsNames"],"ipAddresses":["ipAddresses","ipAddresses"],"customSans":[{"critical":True,"value":"value","objectId":{"objectIdPath":[0,0]}},{"critical":True,"value":"value","objectId":{"objectIdPath":[0,0]}}]}},"subjectKeyId":{"keyId":"keyId"},"publicKey":{"format":"KEY_FORMAT_UNSPECIFIED","key":"key"}},"pemCaCertificates":["pemCaCertificates","pemCaCertificates"],"keySpec":{"cloudKmsKeyVersion":"cloudKmsKeyVersion","algorithm":"SIGN_HASH_ALGORITHM_UNSPECIFIED"}}
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
                    ('certificateAuthorityId', 'certificate_authority_id_example'),
                    ('requestId', 'request_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/{parent}/certificateAuthorities'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_privateca_projects_locations_ca_pools_certificate_authorities_disable(client):
    """Test case for privateca_projects_locations_ca_pools_certificate_authorities_disable

    
    """
    body = {"ignoreDependentResources":True,"requestId":"requestId"}
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
        path='/v1/{namedisabl}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_privateca_projects_locations_ca_pools_certificate_authorities_enable(client):
    """Test case for privateca_projects_locations_ca_pools_certificate_authorities_enable

    
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
        path='/v1/{nameenabl}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_privateca_projects_locations_ca_pools_certificate_authorities_fetch(client):
    """Test case for privateca_projects_locations_ca_pools_certificate_authorities_fetch

    
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
        path='/v1/{namefetc}'.format(name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_privateca_projects_locations_ca_pools_certificate_authorities_list(client):
    """Test case for privateca_projects_locations_ca_pools_certificate_authorities_list

    
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
        path='/v1/{parent}/certificateAuthorities'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_privateca_projects_locations_ca_pools_certificate_authorities_undelete(client):
    """Test case for privateca_projects_locations_ca_pools_certificate_authorities_undelete

    
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
        path='/v1/{nameundelet}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_privateca_projects_locations_ca_pools_certificates_create(client):
    """Test case for privateca_projects_locations_ca_pools_certificates_create

    
    """
    body = {"certificateDescription":{"x509Description":{"additionalExtensions":[{"critical":True,"value":"value","objectId":{"objectIdPath":[0,0]}},{"critical":True,"value":"value","objectId":{"objectIdPath":[0,0]}}],"keyUsage":{"baseKeyUsage":{"crlSign":True,"decipherOnly":True,"keyEncipherment":True,"contentCommitment":True,"encipherOnly":True,"digitalSignature":True,"keyAgreement":True,"dataEncipherment":True,"certSign":True},"unknownExtendedKeyUsages":[{"objectIdPath":[0,0]},{"objectIdPath":[0,0]}],"extendedKeyUsage":{"codeSigning":True,"ocspSigning":True,"emailProtection":True,"serverAuth":True,"timeStamping":True,"clientAuth":True}},"aiaOcspServers":["aiaOcspServers","aiaOcspServers"],"caOptions":{"isCa":True,"maxIssuerPathLength":6},"policyIds":[{"objectIdPath":[0,0]},{"objectIdPath":[0,0]}],"nameConstraints":{"permittedEmailAddresses":["permittedEmailAddresses","permittedEmailAddresses"],"excludedEmailAddresses":["excludedEmailAddresses","excludedEmailAddresses"],"excludedIpRanges":["excludedIpRanges","excludedIpRanges"],"critical":True,"excludedDnsNames":["excludedDnsNames","excludedDnsNames"],"excludedUris":["excludedUris","excludedUris"],"permittedUris":["permittedUris","permittedUris"],"permittedIpRanges":["permittedIpRanges","permittedIpRanges"],"permittedDnsNames":["permittedDnsNames","permittedDnsNames"]}},"aiaIssuingCertificateUrls":["aiaIssuingCertificateUrls","aiaIssuingCertificateUrls"],"subjectDescription":{"hexSerialNumber":"hexSerialNumber","notBeforeTime":"notBeforeTime","subject":{"commonName":"commonName","province":"province","streetAddress":"streetAddress","countryCode":"countryCode","organization":"organization","postalCode":"postalCode","locality":"locality","organizationalUnit":"organizationalUnit"},"lifetime":"lifetime","notAfterTime":"notAfterTime","subjectAltName":{"uris":["uris","uris"],"emailAddresses":["emailAddresses","emailAddresses"],"dnsNames":["dnsNames","dnsNames"],"ipAddresses":["ipAddresses","ipAddresses"],"customSans":[{"critical":True,"value":"value","objectId":{"objectIdPath":[0,0]}},{"critical":True,"value":"value","objectId":{"objectIdPath":[0,0]}}]}},"subjectKeyId":{"keyId":"keyId"},"certFingerprint":{"sha256Hash":"sha256Hash"},"authorityKeyId":{"keyId":"keyId"},"publicKey":{"format":"KEY_FORMAT_UNSPECIFIED","key":"key"},"crlDistributionPoints":["crlDistributionPoints","crlDistributionPoints"]},"subjectMode":"SUBJECT_REQUEST_MODE_UNSPECIFIED","lifetime":"lifetime","pemCsr":"pemCsr","updateTime":"updateTime","issuerCertificateAuthority":"issuerCertificateAuthority","labels":{"key":"labels"},"certificateTemplate":"certificateTemplate","createTime":"createTime","name":"name","pemCertificate":"pemCertificate","pemCertificateChain":["pemCertificateChain","pemCertificateChain"],"config":{"x509Config":{"additionalExtensions":[{"critical":True,"value":"value","objectId":{"objectIdPath":[0,0]}},{"critical":True,"value":"value","objectId":{"objectIdPath":[0,0]}}],"keyUsage":{"baseKeyUsage":{"crlSign":True,"decipherOnly":True,"keyEncipherment":True,"contentCommitment":True,"encipherOnly":True,"digitalSignature":True,"keyAgreement":True,"dataEncipherment":True,"certSign":True},"unknownExtendedKeyUsages":[{"objectIdPath":[0,0]},{"objectIdPath":[0,0]}],"extendedKeyUsage":{"codeSigning":True,"ocspSigning":True,"emailProtection":True,"serverAuth":True,"timeStamping":True,"clientAuth":True}},"aiaOcspServers":["aiaOcspServers","aiaOcspServers"],"caOptions":{"isCa":True,"maxIssuerPathLength":6},"policyIds":[{"objectIdPath":[0,0]},{"objectIdPath":[0,0]}],"nameConstraints":{"permittedEmailAddresses":["permittedEmailAddresses","permittedEmailAddresses"],"excludedEmailAddresses":["excludedEmailAddresses","excludedEmailAddresses"],"excludedIpRanges":["excludedIpRanges","excludedIpRanges"],"critical":True,"excludedDnsNames":["excludedDnsNames","excludedDnsNames"],"excludedUris":["excludedUris","excludedUris"],"permittedUris":["permittedUris","permittedUris"],"permittedIpRanges":["permittedIpRanges","permittedIpRanges"],"permittedDnsNames":["permittedDnsNames","permittedDnsNames"]}},"subjectConfig":{"subject":{"commonName":"commonName","province":"province","streetAddress":"streetAddress","countryCode":"countryCode","organization":"organization","postalCode":"postalCode","locality":"locality","organizationalUnit":"organizationalUnit"},"subjectAltName":{"uris":["uris","uris"],"emailAddresses":["emailAddresses","emailAddresses"],"dnsNames":["dnsNames","dnsNames"],"ipAddresses":["ipAddresses","ipAddresses"],"customSans":[{"critical":True,"value":"value","objectId":{"objectIdPath":[0,0]}},{"critical":True,"value":"value","objectId":{"objectIdPath":[0,0]}}]}},"subjectKeyId":{"keyId":"keyId"},"publicKey":{"format":"KEY_FORMAT_UNSPECIFIED","key":"key"}},"revocationDetails":{"revocationState":"REVOCATION_REASON_UNSPECIFIED","revocationTime":"revocationTime"}}
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
                    ('certificateId', 'certificate_id_example'),
                    ('issuingCertificateAuthorityId', 'issuing_certificate_authority_id_example'),
                    ('requestId', 'request_id_example'),
                    ('validateOnly', True)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/{parent}/certificates'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_privateca_projects_locations_ca_pools_certificates_list(client):
    """Test case for privateca_projects_locations_ca_pools_certificates_list

    
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
        path='/v1/{parent}/certificates'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_privateca_projects_locations_ca_pools_certificates_revoke(client):
    """Test case for privateca_projects_locations_ca_pools_certificates_revoke

    
    """
    body = {"reason":"REVOCATION_REASON_UNSPECIFIED","requestId":"requestId"}
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
        path='/v1/{namerevok}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_privateca_projects_locations_ca_pools_create(client):
    """Test case for privateca_projects_locations_ca_pools_create

    
    """
    body = {"issuancePolicy":{"allowedKeyTypes":[{"ellipticCurve":{"signatureAlgorithm":"EC_SIGNATURE_ALGORITHM_UNSPECIFIED"},"rsa":{"maxModulusSize":"maxModulusSize","minModulusSize":"minModulusSize"}},{"ellipticCurve":{"signatureAlgorithm":"EC_SIGNATURE_ALGORITHM_UNSPECIFIED"},"rsa":{"maxModulusSize":"maxModulusSize","minModulusSize":"minModulusSize"}}],"maximumLifetime":"maximumLifetime","baselineValues":{"additionalExtensions":[{"critical":True,"value":"value","objectId":{"objectIdPath":[0,0]}},{"critical":True,"value":"value","objectId":{"objectIdPath":[0,0]}}],"keyUsage":{"baseKeyUsage":{"crlSign":True,"decipherOnly":True,"keyEncipherment":True,"contentCommitment":True,"encipherOnly":True,"digitalSignature":True,"keyAgreement":True,"dataEncipherment":True,"certSign":True},"unknownExtendedKeyUsages":[{"objectIdPath":[0,0]},{"objectIdPath":[0,0]}],"extendedKeyUsage":{"codeSigning":True,"ocspSigning":True,"emailProtection":True,"serverAuth":True,"timeStamping":True,"clientAuth":True}},"aiaOcspServers":["aiaOcspServers","aiaOcspServers"],"caOptions":{"isCa":True,"maxIssuerPathLength":6},"policyIds":[{"objectIdPath":[0,0]},{"objectIdPath":[0,0]}],"nameConstraints":{"permittedEmailAddresses":["permittedEmailAddresses","permittedEmailAddresses"],"excludedEmailAddresses":["excludedEmailAddresses","excludedEmailAddresses"],"excludedIpRanges":["excludedIpRanges","excludedIpRanges"],"critical":True,"excludedDnsNames":["excludedDnsNames","excludedDnsNames"],"excludedUris":["excludedUris","excludedUris"],"permittedUris":["permittedUris","permittedUris"],"permittedIpRanges":["permittedIpRanges","permittedIpRanges"],"permittedDnsNames":["permittedDnsNames","permittedDnsNames"]}},"identityConstraints":{"celExpression":{"expression":"expression","description":"description","location":"location","title":"title"},"allowSubjectAltNamesPassthrough":True,"allowSubjectPassthrough":True},"allowedIssuanceModes":{"allowConfigBasedIssuance":True,"allowCsrBasedIssuance":True},"passthroughExtensions":{"additionalExtensions":[{"objectIdPath":[0,0]},{"objectIdPath":[0,0]}],"knownExtensions":["KNOWN_CERTIFICATE_EXTENSION_UNSPECIFIED","KNOWN_CERTIFICATE_EXTENSION_UNSPECIFIED"]}},"tier":"TIER_UNSPECIFIED","publishingOptions":{"publishCrl":True,"publishCaCert":True,"encodingFormat":"ENCODING_FORMAT_UNSPECIFIED"},"name":"name","labels":{"key":"labels"}}
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
                    ('caPoolId', 'ca_pool_id_example'),
                    ('requestId', 'request_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/{parent}/caPools'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_privateca_projects_locations_ca_pools_fetch_ca_certs(client):
    """Test case for privateca_projects_locations_ca_pools_fetch_ca_certs

    
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
        path='/v1/{ca_poolfetch_ca_cert}'.format(ca_pool='ca_pool_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_privateca_projects_locations_ca_pools_list(client):
    """Test case for privateca_projects_locations_ca_pools_list

    
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
        path='/v1/{parent}/caPools'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_privateca_projects_locations_certificate_templates_create(client):
    """Test case for privateca_projects_locations_certificate_templates_create

    
    """
    body = {"maximumLifetime":"maximumLifetime","createTime":"createTime","identityConstraints":{"celExpression":{"expression":"expression","description":"description","location":"location","title":"title"},"allowSubjectAltNamesPassthrough":True,"allowSubjectPassthrough":True},"name":"name","description":"description","predefinedValues":{"additionalExtensions":[{"critical":True,"value":"value","objectId":{"objectIdPath":[0,0]}},{"critical":True,"value":"value","objectId":{"objectIdPath":[0,0]}}],"keyUsage":{"baseKeyUsage":{"crlSign":True,"decipherOnly":True,"keyEncipherment":True,"contentCommitment":True,"encipherOnly":True,"digitalSignature":True,"keyAgreement":True,"dataEncipherment":True,"certSign":True},"unknownExtendedKeyUsages":[{"objectIdPath":[0,0]},{"objectIdPath":[0,0]}],"extendedKeyUsage":{"codeSigning":True,"ocspSigning":True,"emailProtection":True,"serverAuth":True,"timeStamping":True,"clientAuth":True}},"aiaOcspServers":["aiaOcspServers","aiaOcspServers"],"caOptions":{"isCa":True,"maxIssuerPathLength":6},"policyIds":[{"objectIdPath":[0,0]},{"objectIdPath":[0,0]}],"nameConstraints":{"permittedEmailAddresses":["permittedEmailAddresses","permittedEmailAddresses"],"excludedEmailAddresses":["excludedEmailAddresses","excludedEmailAddresses"],"excludedIpRanges":["excludedIpRanges","excludedIpRanges"],"critical":True,"excludedDnsNames":["excludedDnsNames","excludedDnsNames"],"excludedUris":["excludedUris","excludedUris"],"permittedUris":["permittedUris","permittedUris"],"permittedIpRanges":["permittedIpRanges","permittedIpRanges"],"permittedDnsNames":["permittedDnsNames","permittedDnsNames"]}},"updateTime":"updateTime","labels":{"key":"labels"},"passthroughExtensions":{"additionalExtensions":[{"objectIdPath":[0,0]},{"objectIdPath":[0,0]}],"knownExtensions":["KNOWN_CERTIFICATE_EXTENSION_UNSPECIFIED","KNOWN_CERTIFICATE_EXTENSION_UNSPECIFIED"]}}
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
                    ('certificateTemplateId', 'certificate_template_id_example'),
                    ('requestId', 'request_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/{parent}/certificateTemplates'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_privateca_projects_locations_certificate_templates_get_iam_policy(client):
    """Test case for privateca_projects_locations_certificate_templates_get_iam_policy

    
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
                    ('options.requestedPolicyVersion', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/{resourceget_iam_polic}'.format(resource='resource_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_privateca_projects_locations_certificate_templates_list(client):
    """Test case for privateca_projects_locations_certificate_templates_list

    
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
        path='/v1/{parent}/certificateTemplates'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_privateca_projects_locations_certificate_templates_patch(client):
    """Test case for privateca_projects_locations_certificate_templates_patch

    
    """
    body = {"maximumLifetime":"maximumLifetime","createTime":"createTime","identityConstraints":{"celExpression":{"expression":"expression","description":"description","location":"location","title":"title"},"allowSubjectAltNamesPassthrough":True,"allowSubjectPassthrough":True},"name":"name","description":"description","predefinedValues":{"additionalExtensions":[{"critical":True,"value":"value","objectId":{"objectIdPath":[0,0]}},{"critical":True,"value":"value","objectId":{"objectIdPath":[0,0]}}],"keyUsage":{"baseKeyUsage":{"crlSign":True,"decipherOnly":True,"keyEncipherment":True,"contentCommitment":True,"encipherOnly":True,"digitalSignature":True,"keyAgreement":True,"dataEncipherment":True,"certSign":True},"unknownExtendedKeyUsages":[{"objectIdPath":[0,0]},{"objectIdPath":[0,0]}],"extendedKeyUsage":{"codeSigning":True,"ocspSigning":True,"emailProtection":True,"serverAuth":True,"timeStamping":True,"clientAuth":True}},"aiaOcspServers":["aiaOcspServers","aiaOcspServers"],"caOptions":{"isCa":True,"maxIssuerPathLength":6},"policyIds":[{"objectIdPath":[0,0]},{"objectIdPath":[0,0]}],"nameConstraints":{"permittedEmailAddresses":["permittedEmailAddresses","permittedEmailAddresses"],"excludedEmailAddresses":["excludedEmailAddresses","excludedEmailAddresses"],"excludedIpRanges":["excludedIpRanges","excludedIpRanges"],"critical":True,"excludedDnsNames":["excludedDnsNames","excludedDnsNames"],"excludedUris":["excludedUris","excludedUris"],"permittedUris":["permittedUris","permittedUris"],"permittedIpRanges":["permittedIpRanges","permittedIpRanges"],"permittedDnsNames":["permittedDnsNames","permittedDnsNames"]}},"updateTime":"updateTime","labels":{"key":"labels"},"passthroughExtensions":{"additionalExtensions":[{"objectIdPath":[0,0]},{"objectIdPath":[0,0]}],"knownExtensions":["KNOWN_CERTIFICATE_EXTENSION_UNSPECIFIED","KNOWN_CERTIFICATE_EXTENSION_UNSPECIFIED"]}}
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


pytestmark = pytest.mark.asyncio

async def test_privateca_projects_locations_certificate_templates_set_iam_policy(client):
    """Test case for privateca_projects_locations_certificate_templates_set_iam_policy

    
    """
    body = {"updateMask":"updateMask","policy":{"bindings":[{"condition":{"expression":"expression","description":"description","location":"location","title":"title"},"role":"role","members":["members","members"]},{"condition":{"expression":"expression","description":"description","location":"location","title":"title"},"role":"role","members":["members","members"]}],"etag":"etag","version":0,"auditConfigs":[{"auditLogConfigs":[{"logType":"LOG_TYPE_UNSPECIFIED","exemptedMembers":["exemptedMembers","exemptedMembers"]},{"logType":"LOG_TYPE_UNSPECIFIED","exemptedMembers":["exemptedMembers","exemptedMembers"]}],"service":"service"},{"auditLogConfigs":[{"logType":"LOG_TYPE_UNSPECIFIED","exemptedMembers":["exemptedMembers","exemptedMembers"]},{"logType":"LOG_TYPE_UNSPECIFIED","exemptedMembers":["exemptedMembers","exemptedMembers"]}],"service":"service"}]}}
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
        path='/v1/{resourceset_iam_polic}'.format(resource='resource_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_privateca_projects_locations_certificate_templates_test_iam_permissions(client):
    """Test case for privateca_projects_locations_certificate_templates_test_iam_permissions

    
    """
    body = {"permissions":["permissions","permissions"]}
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
        path='/v1/{resourcetest_iam_permission}'.format(resource='resource_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_privateca_projects_locations_list(client):
    """Test case for privateca_projects_locations_list

    
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

async def test_privateca_projects_locations_operations_cancel(client):
    """Test case for privateca_projects_locations_operations_cancel

    
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

async def test_privateca_projects_locations_operations_delete(client):
    """Test case for privateca_projects_locations_operations_delete

    
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
                    ('requestId', 'request_id_example'),
                    ('ignoreDependentResources', True),
                    ('skipGracePeriod', True)]
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

async def test_privateca_projects_locations_operations_get(client):
    """Test case for privateca_projects_locations_operations_get

    
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
        path='/v1/{name}'.format(name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_privateca_projects_locations_operations_list(client):
    """Test case for privateca_projects_locations_operations_list

    
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

