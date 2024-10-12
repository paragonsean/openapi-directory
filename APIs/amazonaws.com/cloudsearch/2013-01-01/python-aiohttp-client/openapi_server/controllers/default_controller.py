from typing import List, Dict
from aiohttp import web

from openapi_server.models.build_suggesters_request import BuildSuggestersRequest
from openapi_server.models.build_suggesters_response import BuildSuggestersResponse
from openapi_server.models.create_domain_request import CreateDomainRequest
from openapi_server.models.create_domain_response import CreateDomainResponse
from openapi_server.models.define_analysis_scheme_request import DefineAnalysisSchemeRequest
from openapi_server.models.define_analysis_scheme_response import DefineAnalysisSchemeResponse
from openapi_server.models.define_expression_request import DefineExpressionRequest
from openapi_server.models.define_expression_response import DefineExpressionResponse
from openapi_server.models.define_index_field_request import DefineIndexFieldRequest
from openapi_server.models.define_index_field_response import DefineIndexFieldResponse
from openapi_server.models.define_suggester_request import DefineSuggesterRequest
from openapi_server.models.define_suggester_response import DefineSuggesterResponse
from openapi_server.models.delete_analysis_scheme_request import DeleteAnalysisSchemeRequest
from openapi_server.models.delete_analysis_scheme_response import DeleteAnalysisSchemeResponse
from openapi_server.models.delete_domain_request import DeleteDomainRequest
from openapi_server.models.delete_domain_response import DeleteDomainResponse
from openapi_server.models.delete_expression_request import DeleteExpressionRequest
from openapi_server.models.delete_expression_response import DeleteExpressionResponse
from openapi_server.models.delete_index_field_request import DeleteIndexFieldRequest
from openapi_server.models.delete_index_field_response import DeleteIndexFieldResponse
from openapi_server.models.delete_suggester_request import DeleteSuggesterRequest
from openapi_server.models.delete_suggester_response import DeleteSuggesterResponse
from openapi_server.models.describe_analysis_schemes_request import DescribeAnalysisSchemesRequest
from openapi_server.models.describe_analysis_schemes_response import DescribeAnalysisSchemesResponse
from openapi_server.models.describe_availability_options_request import DescribeAvailabilityOptionsRequest
from openapi_server.models.describe_availability_options_response import DescribeAvailabilityOptionsResponse
from openapi_server.models.describe_domain_endpoint_options_request import DescribeDomainEndpointOptionsRequest
from openapi_server.models.describe_domain_endpoint_options_response import DescribeDomainEndpointOptionsResponse
from openapi_server.models.describe_domains_request import DescribeDomainsRequest
from openapi_server.models.describe_domains_response import DescribeDomainsResponse
from openapi_server.models.describe_expressions_request import DescribeExpressionsRequest
from openapi_server.models.describe_expressions_response import DescribeExpressionsResponse
from openapi_server.models.describe_index_fields_request import DescribeIndexFieldsRequest
from openapi_server.models.describe_index_fields_response import DescribeIndexFieldsResponse
from openapi_server.models.describe_scaling_parameters_request import DescribeScalingParametersRequest
from openapi_server.models.describe_scaling_parameters_response import DescribeScalingParametersResponse
from openapi_server.models.describe_service_access_policies_request import DescribeServiceAccessPoliciesRequest
from openapi_server.models.describe_service_access_policies_response import DescribeServiceAccessPoliciesResponse
from openapi_server.models.describe_suggesters_request import DescribeSuggestersRequest
from openapi_server.models.describe_suggesters_response import DescribeSuggestersResponse
from openapi_server.models.get_define_analysis_scheme_analysis_scheme_parameter import GETDefineAnalysisSchemeAnalysisSchemeParameter
from openapi_server.models.get_define_expression_expression_parameter import GETDefineExpressionExpressionParameter
from openapi_server.models.get_define_index_field_index_field_parameter import GETDefineIndexFieldIndexFieldParameter
from openapi_server.models.get_define_suggester_suggester_parameter import GETDefineSuggesterSuggesterParameter
from openapi_server.models.get_update_domain_endpoint_options_domain_endpoint_options_parameter import GETUpdateDomainEndpointOptionsDomainEndpointOptionsParameter
from openapi_server.models.get_update_scaling_parameters_scaling_parameters_parameter import GETUpdateScalingParametersScalingParametersParameter
from openapi_server.models.index_documents_request import IndexDocumentsRequest
from openapi_server.models.index_documents_response import IndexDocumentsResponse
from openapi_server.models.list_domain_names_response import ListDomainNamesResponse
from openapi_server.models.update_availability_options_request import UpdateAvailabilityOptionsRequest
from openapi_server.models.update_availability_options_response import UpdateAvailabilityOptionsResponse
from openapi_server.models.update_domain_endpoint_options_request import UpdateDomainEndpointOptionsRequest
from openapi_server.models.update_domain_endpoint_options_response import UpdateDomainEndpointOptionsResponse
from openapi_server.models.update_scaling_parameters_request import UpdateScalingParametersRequest
from openapi_server.models.update_scaling_parameters_response import UpdateScalingParametersResponse
from openapi_server.models.update_service_access_policies_request import UpdateServiceAccessPoliciesRequest
from openapi_server.models.update_service_access_policies_response import UpdateServiceAccessPoliciesResponse
from openapi_server import util


async def g_et_build_suggesters(request: web.Request, domain_name, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """g_et_build_suggesters

    Indexes the search suggestions. For more information, see &lt;a href&#x3D;\&quot;http://docs.aws.amazon.com/cloudsearch/latest/developerguide/getting-suggestions.html#configuring-suggesters\&quot;&gt;Configuring Suggesters&lt;/a&gt; in the &lt;i&gt;Amazon CloudSearch Developer Guide&lt;/i&gt;.

    :param domain_name: 
    :type domain_name: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def g_et_create_domain(request: web.Request, domain_name, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """g_et_create_domain

    Creates a new search domain. For more information, see &lt;a href&#x3D;\&quot;http://docs.aws.amazon.com/cloudsearch/latest/developerguide/creating-domains.html\&quot; target&#x3D;\&quot;_blank\&quot;&gt;Creating a Search Domain&lt;/a&gt; in the &lt;i&gt;Amazon CloudSearch Developer Guide&lt;/i&gt;.

    :param domain_name: A name for the domain you are creating. Allowed characters are a-z (lower-case letters), 0-9, and hyphen (-). Domain names must start with a letter or number and be at least 3 and no more than 28 characters long.
    :type domain_name: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def g_et_define_analysis_scheme(request: web.Request, domain_name, analysis_scheme, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """g_et_define_analysis_scheme

    Configures an analysis scheme that can be applied to a &lt;code&gt;text&lt;/code&gt; or &lt;code&gt;text-array&lt;/code&gt; field to define language-specific text processing options. For more information, see &lt;a href&#x3D;\&quot;http://docs.aws.amazon.com/cloudsearch/latest/developerguide/configuring-analysis-schemes.html\&quot; target&#x3D;\&quot;_blank\&quot;&gt;Configuring Analysis Schemes&lt;/a&gt; in the &lt;i&gt;Amazon CloudSearch Developer Guide&lt;/i&gt;.

    :param domain_name: 
    :type domain_name: str
    :param analysis_scheme: 
    :type analysis_scheme: dict | bytes
    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    analysis_scheme = .from_dict(analysis_scheme)
    return web.Response(status=200)


async def g_et_define_expression(request: web.Request, domain_name, expression, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """g_et_define_expression

    Configures an &lt;code&gt;&lt;a&gt;Expression&lt;/a&gt;&lt;/code&gt; for the search domain. Used to create new expressions and modify existing ones. If the expression exists, the new configuration replaces the old one. For more information, see &lt;a href&#x3D;\&quot;http://docs.aws.amazon.com/cloudsearch/latest/developerguide/configuring-expressions.html\&quot; target&#x3D;\&quot;_blank\&quot;&gt;Configuring Expressions&lt;/a&gt; in the &lt;i&gt;Amazon CloudSearch Developer Guide&lt;/i&gt;.

    :param domain_name: 
    :type domain_name: str
    :param expression: 
    :type expression: dict | bytes
    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    expression = .from_dict(expression)
    return web.Response(status=200)


async def g_et_define_index_field(request: web.Request, domain_name, index_field, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """g_et_define_index_field

    Configures an &lt;code&gt;&lt;a&gt;IndexField&lt;/a&gt;&lt;/code&gt; for the search domain. Used to create new fields and modify existing ones. You must specify the name of the domain you are configuring and an index field configuration. The index field configuration specifies a unique name, the index field type, and the options you want to configure for the field. The options you can specify depend on the &lt;code&gt;&lt;a&gt;IndexFieldType&lt;/a&gt;&lt;/code&gt;. If the field exists, the new configuration replaces the old one. For more information, see &lt;a href&#x3D;\&quot;http://docs.aws.amazon.com/cloudsearch/latest/developerguide/configuring-index-fields.html\&quot; target&#x3D;\&quot;_blank\&quot;&gt;Configuring Index Fields&lt;/a&gt; in the &lt;i&gt;Amazon CloudSearch Developer Guide&lt;/i&gt;. 

    :param domain_name: 
    :type domain_name: str
    :param index_field: The index field and field options you want to configure. 
    :type index_field: dict | bytes
    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    index_field = .from_dict(index_field)
    return web.Response(status=200)


async def g_et_define_suggester(request: web.Request, domain_name, suggester, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """g_et_define_suggester

    Configures a suggester for a domain. A suggester enables you to display possible matches before users finish typing their queries. When you configure a suggester, you must specify the name of the text field you want to search for possible matches and a unique name for the suggester. For more information, see &lt;a href&#x3D;\&quot;http://docs.aws.amazon.com/cloudsearch/latest/developerguide/getting-suggestions.html\&quot; target&#x3D;\&quot;_blank\&quot;&gt;Getting Search Suggestions&lt;/a&gt; in the &lt;i&gt;Amazon CloudSearch Developer Guide&lt;/i&gt;.

    :param domain_name: 
    :type domain_name: str
    :param suggester: 
    :type suggester: dict | bytes
    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    suggester = .from_dict(suggester)
    return web.Response(status=200)


async def g_et_delete_analysis_scheme(request: web.Request, domain_name, analysis_scheme_name, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """g_et_delete_analysis_scheme

    Deletes an analysis scheme. For more information, see &lt;a href&#x3D;\&quot;http://docs.aws.amazon.com/cloudsearch/latest/developerguide/configuring-analysis-schemes.html\&quot; target&#x3D;\&quot;_blank\&quot;&gt;Configuring Analysis Schemes&lt;/a&gt; in the &lt;i&gt;Amazon CloudSearch Developer Guide&lt;/i&gt;. 

    :param domain_name: 
    :type domain_name: str
    :param analysis_scheme_name: The name of the analysis scheme you want to delete.
    :type analysis_scheme_name: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def g_et_delete_domain(request: web.Request, domain_name, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """g_et_delete_domain

    Permanently deletes a search domain and all of its data. Once a domain has been deleted, it cannot be recovered. For more information, see &lt;a href&#x3D;\&quot;http://docs.aws.amazon.com/cloudsearch/latest/developerguide/deleting-domains.html\&quot; target&#x3D;\&quot;_blank\&quot;&gt;Deleting a Search Domain&lt;/a&gt; in the &lt;i&gt;Amazon CloudSearch Developer Guide&lt;/i&gt;. 

    :param domain_name: The name of the domain you want to permanently delete.
    :type domain_name: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def g_et_delete_expression(request: web.Request, domain_name, expression_name, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """g_et_delete_expression

    Removes an &lt;code&gt;&lt;a&gt;Expression&lt;/a&gt;&lt;/code&gt; from the search domain. For more information, see &lt;a href&#x3D;\&quot;http://docs.aws.amazon.com/cloudsearch/latest/developerguide/configuring-expressions.html\&quot; target&#x3D;\&quot;_blank\&quot;&gt;Configuring Expressions&lt;/a&gt; in the &lt;i&gt;Amazon CloudSearch Developer Guide&lt;/i&gt;.

    :param domain_name: 
    :type domain_name: str
    :param expression_name: The name of the &lt;code&gt;&lt;a&gt;Expression&lt;/a&gt;&lt;/code&gt; to delete.
    :type expression_name: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def g_et_delete_index_field(request: web.Request, domain_name, index_field_name, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """g_et_delete_index_field

    Removes an &lt;code&gt;&lt;a&gt;IndexField&lt;/a&gt;&lt;/code&gt; from the search domain. For more information, see &lt;a href&#x3D;\&quot;http://docs.aws.amazon.com/cloudsearch/latest/developerguide/configuring-index-fields.html\&quot; target&#x3D;\&quot;_blank\&quot;&gt;Configuring Index Fields&lt;/a&gt; in the &lt;i&gt;Amazon CloudSearch Developer Guide&lt;/i&gt;.

    :param domain_name: 
    :type domain_name: str
    :param index_field_name: The name of the index field your want to remove from the domain&#39;s indexing options.
    :type index_field_name: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def g_et_delete_suggester(request: web.Request, domain_name, suggester_name, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """g_et_delete_suggester

    Deletes a suggester. For more information, see &lt;a href&#x3D;\&quot;http://docs.aws.amazon.com/cloudsearch/latest/developerguide/getting-suggestions.html\&quot; target&#x3D;\&quot;_blank\&quot;&gt;Getting Search Suggestions&lt;/a&gt; in the &lt;i&gt;Amazon CloudSearch Developer Guide&lt;/i&gt;.

    :param domain_name: 
    :type domain_name: str
    :param suggester_name: Specifies the name of the suggester you want to delete.
    :type suggester_name: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def g_et_describe_analysis_schemes(request: web.Request, domain_name, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, analysis_scheme_names=None, deployed=None) -> web.Response:
    """g_et_describe_analysis_schemes

    Gets the analysis schemes configured for a domain. An analysis scheme defines language-specific text processing options for a &lt;code&gt;text&lt;/code&gt; field. Can be limited to specific analysis schemes by name. By default, shows all analysis schemes and includes any pending changes to the configuration. Set the &lt;code&gt;Deployed&lt;/code&gt; option to &lt;code&gt;true&lt;/code&gt; to show the active configuration and exclude pending changes. For more information, see &lt;a href&#x3D;\&quot;http://docs.aws.amazon.com/cloudsearch/latest/developerguide/configuring-analysis-schemes.html\&quot; target&#x3D;\&quot;_blank\&quot;&gt;Configuring Analysis Schemes&lt;/a&gt; in the &lt;i&gt;Amazon CloudSearch Developer Guide&lt;/i&gt;.

    :param domain_name: The name of the domain you want to describe.
    :type domain_name: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param analysis_scheme_names: The analysis schemes you want to describe.
    :type analysis_scheme_names: List[str]
    :param deployed: Whether to display the deployed configuration (&lt;code&gt;true&lt;/code&gt;) or include any pending changes (&lt;code&gt;false&lt;/code&gt;). Defaults to &lt;code&gt;false&lt;/code&gt;.
    :type deployed: bool

    """
    return web.Response(status=200)


async def g_et_describe_availability_options(request: web.Request, domain_name, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, deployed=None) -> web.Response:
    """g_et_describe_availability_options

    Gets the availability options configured for a domain. By default, shows the configuration with any pending changes. Set the &lt;code&gt;Deployed&lt;/code&gt; option to &lt;code&gt;true&lt;/code&gt; to show the active configuration and exclude pending changes. For more information, see &lt;a href&#x3D;\&quot;http://docs.aws.amazon.com/cloudsearch/latest/developerguide/configuring-availability-options.html\&quot; target&#x3D;\&quot;_blank\&quot;&gt;Configuring Availability Options&lt;/a&gt; in the &lt;i&gt;Amazon CloudSearch Developer Guide&lt;/i&gt;.

    :param domain_name: The name of the domain you want to describe.
    :type domain_name: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param deployed: Whether to display the deployed configuration (&lt;code&gt;true&lt;/code&gt;) or include any pending changes (&lt;code&gt;false&lt;/code&gt;). Defaults to &lt;code&gt;false&lt;/code&gt;.
    :type deployed: bool

    """
    return web.Response(status=200)


async def g_et_describe_domain_endpoint_options(request: web.Request, domain_name, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, deployed=None) -> web.Response:
    """g_et_describe_domain_endpoint_options

    Returns the domain&#39;s endpoint options, specifically whether all requests to the domain must arrive over HTTPS. For more information, see &lt;a href&#x3D;\&quot;http://docs.aws.amazon.com/cloudsearch/latest/developerguide/configuring-domain-endpoint-options.html\&quot; target&#x3D;\&quot;_blank\&quot;&gt;Configuring Domain Endpoint Options&lt;/a&gt; in the &lt;i&gt;Amazon CloudSearch Developer Guide&lt;/i&gt;.

    :param domain_name: A string that represents the name of a domain.
    :type domain_name: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param deployed: Whether to retrieve the latest configuration (which might be in a Processing state) or the current, active configuration. Defaults to &lt;code&gt;false&lt;/code&gt;.
    :type deployed: bool

    """
    return web.Response(status=200)


async def g_et_describe_domains(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, domain_names=None) -> web.Response:
    """g_et_describe_domains

    Gets information about the search domains owned by this account. Can be limited to specific domains. Shows all domains by default. To get the number of searchable documents in a domain, use the console or submit a &lt;code&gt;matchall&lt;/code&gt; request to your domain&#39;s search endpoint: &lt;code&gt;q&#x3D;matchall&amp;amp;amp;q.parser&#x3D;structured&amp;amp;amp;size&#x3D;0&lt;/code&gt;. For more information, see &lt;a href&#x3D;\&quot;http://docs.aws.amazon.com/cloudsearch/latest/developerguide/getting-domain-info.html\&quot; target&#x3D;\&quot;_blank\&quot;&gt;Getting Information about a Search Domain&lt;/a&gt; in the &lt;i&gt;Amazon CloudSearch Developer Guide&lt;/i&gt;.

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param domain_names: The names of the domains you want to include in the response.
    :type domain_names: List[str]

    """
    return web.Response(status=200)


async def g_et_describe_expressions(request: web.Request, domain_name, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, expression_names=None, deployed=None) -> web.Response:
    """g_et_describe_expressions

    Gets the expressions configured for the search domain. Can be limited to specific expressions by name. By default, shows all expressions and includes any pending changes to the configuration. Set the &lt;code&gt;Deployed&lt;/code&gt; option to &lt;code&gt;true&lt;/code&gt; to show the active configuration and exclude pending changes. For more information, see &lt;a href&#x3D;\&quot;http://docs.aws.amazon.com/cloudsearch/latest/developerguide/configuring-expressions.html\&quot; target&#x3D;\&quot;_blank\&quot;&gt;Configuring Expressions&lt;/a&gt; in the &lt;i&gt;Amazon CloudSearch Developer Guide&lt;/i&gt;.

    :param domain_name: The name of the domain you want to describe.
    :type domain_name: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param expression_names: Limits the &lt;code&gt;&lt;a&gt;DescribeExpressions&lt;/a&gt;&lt;/code&gt; response to the specified expressions. If not specified, all expressions are shown.
    :type expression_names: List[str]
    :param deployed: Whether to display the deployed configuration (&lt;code&gt;true&lt;/code&gt;) or include any pending changes (&lt;code&gt;false&lt;/code&gt;). Defaults to &lt;code&gt;false&lt;/code&gt;.
    :type deployed: bool

    """
    return web.Response(status=200)


async def g_et_describe_index_fields(request: web.Request, domain_name, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, field_names=None, deployed=None) -> web.Response:
    """g_et_describe_index_fields

    Gets information about the index fields configured for the search domain. Can be limited to specific fields by name. By default, shows all fields and includes any pending changes to the configuration. Set the &lt;code&gt;Deployed&lt;/code&gt; option to &lt;code&gt;true&lt;/code&gt; to show the active configuration and exclude pending changes. For more information, see &lt;a href&#x3D;\&quot;http://docs.aws.amazon.com/cloudsearch/latest/developerguide/getting-domain-info.html\&quot; target&#x3D;\&quot;_blank\&quot;&gt;Getting Domain Information&lt;/a&gt; in the &lt;i&gt;Amazon CloudSearch Developer Guide&lt;/i&gt;.

    :param domain_name: The name of the domain you want to describe.
    :type domain_name: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param field_names: A list of the index fields you want to describe. If not specified, information is returned for all configured index fields.
    :type field_names: List[str]
    :param deployed: Whether to display the deployed configuration (&lt;code&gt;true&lt;/code&gt;) or include any pending changes (&lt;code&gt;false&lt;/code&gt;). Defaults to &lt;code&gt;false&lt;/code&gt;.
    :type deployed: bool

    """
    return web.Response(status=200)


async def g_et_describe_scaling_parameters(request: web.Request, domain_name, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """g_et_describe_scaling_parameters

    Gets the scaling parameters configured for a domain. A domain&#39;s scaling parameters specify the desired search instance type and replication count. For more information, see &lt;a href&#x3D;\&quot;http://docs.aws.amazon.com/cloudsearch/latest/developerguide/configuring-scaling-options.html\&quot; target&#x3D;\&quot;_blank\&quot;&gt;Configuring Scaling Options&lt;/a&gt; in the &lt;i&gt;Amazon CloudSearch Developer Guide&lt;/i&gt;.

    :param domain_name: 
    :type domain_name: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def g_et_describe_service_access_policies(request: web.Request, domain_name, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, deployed=None) -> web.Response:
    """g_et_describe_service_access_policies

    Gets information about the access policies that control access to the domain&#39;s document and search endpoints. By default, shows the configuration with any pending changes. Set the &lt;code&gt;Deployed&lt;/code&gt; option to &lt;code&gt;true&lt;/code&gt; to show the active configuration and exclude pending changes. For more information, see &lt;a href&#x3D;\&quot;http://docs.aws.amazon.com/cloudsearch/latest/developerguide/configuring-access.html\&quot; target&#x3D;\&quot;_blank\&quot;&gt;Configuring Access for a Search Domain&lt;/a&gt; in the &lt;i&gt;Amazon CloudSearch Developer Guide&lt;/i&gt;.

    :param domain_name: The name of the domain you want to describe.
    :type domain_name: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param deployed: Whether to display the deployed configuration (&lt;code&gt;true&lt;/code&gt;) or include any pending changes (&lt;code&gt;false&lt;/code&gt;). Defaults to &lt;code&gt;false&lt;/code&gt;.
    :type deployed: bool

    """
    return web.Response(status=200)


async def g_et_describe_suggesters(request: web.Request, domain_name, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, suggester_names=None, deployed=None) -> web.Response:
    """g_et_describe_suggesters

    Gets the suggesters configured for a domain. A suggester enables you to display possible matches before users finish typing their queries. Can be limited to specific suggesters by name. By default, shows all suggesters and includes any pending changes to the configuration. Set the &lt;code&gt;Deployed&lt;/code&gt; option to &lt;code&gt;true&lt;/code&gt; to show the active configuration and exclude pending changes. For more information, see &lt;a href&#x3D;\&quot;http://docs.aws.amazon.com/cloudsearch/latest/developerguide/getting-suggestions.html\&quot; target&#x3D;\&quot;_blank\&quot;&gt;Getting Search Suggestions&lt;/a&gt; in the &lt;i&gt;Amazon CloudSearch Developer Guide&lt;/i&gt;.

    :param domain_name: The name of the domain you want to describe.
    :type domain_name: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param suggester_names: The suggesters you want to describe.
    :type suggester_names: List[str]
    :param deployed: Whether to display the deployed configuration (&lt;code&gt;true&lt;/code&gt;) or include any pending changes (&lt;code&gt;false&lt;/code&gt;). Defaults to &lt;code&gt;false&lt;/code&gt;.
    :type deployed: bool

    """
    return web.Response(status=200)


async def g_et_index_documents(request: web.Request, domain_name, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """g_et_index_documents

    Tells the search domain to start indexing its documents using the latest indexing options. This operation must be invoked to activate options whose &lt;a&gt;OptionStatus&lt;/a&gt; is &lt;code&gt;RequiresIndexDocuments&lt;/code&gt;.

    :param domain_name: 
    :type domain_name: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def g_et_list_domain_names(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """g_et_list_domain_names

    Lists all search domains owned by an account.

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def g_et_update_availability_options(request: web.Request, domain_name, multi_az, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """g_et_update_availability_options

    Configures the availability options for a domain. Enabling the Multi-AZ option expands an Amazon CloudSearch domain to an additional Availability Zone in the same Region to increase fault tolerance in the event of a service disruption. Changes to the Multi-AZ option can take about half an hour to become active. For more information, see &lt;a href&#x3D;\&quot;http://docs.aws.amazon.com/cloudsearch/latest/developerguide/configuring-availability-options.html\&quot; target&#x3D;\&quot;_blank\&quot;&gt;Configuring Availability Options&lt;/a&gt; in the &lt;i&gt;Amazon CloudSearch Developer Guide&lt;/i&gt;.

    :param domain_name: 
    :type domain_name: str
    :param multi_az: You expand an existing search domain to a second Availability Zone by setting the Multi-AZ option to true. Similarly, you can turn off the Multi-AZ option to downgrade the domain to a single Availability Zone by setting the Multi-AZ option to &lt;code&gt;false&lt;/code&gt;. 
    :type multi_az: bool
    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def g_et_update_domain_endpoint_options(request: web.Request, domain_name, domain_endpoint_options, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """g_et_update_domain_endpoint_options

    Updates the domain&#39;s endpoint options, specifically whether all requests to the domain must arrive over HTTPS. For more information, see &lt;a href&#x3D;\&quot;http://docs.aws.amazon.com/cloudsearch/latest/developerguide/configuring-domain-endpoint-options.html\&quot; target&#x3D;\&quot;_blank\&quot;&gt;Configuring Domain Endpoint Options&lt;/a&gt; in the &lt;i&gt;Amazon CloudSearch Developer Guide&lt;/i&gt;.

    :param domain_name: A string that represents the name of a domain.
    :type domain_name: str
    :param domain_endpoint_options: Whether to require that all requests to the domain arrive over HTTPS. We recommend Policy-Min-TLS-1-2-2019-07 for TLSSecurityPolicy. For compatibility with older clients, the default is Policy-Min-TLS-1-0-2019-07. 
    :type domain_endpoint_options: dict | bytes
    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    domain_endpoint_options = .from_dict(domain_endpoint_options)
    return web.Response(status=200)


async def g_et_update_scaling_parameters(request: web.Request, domain_name, scaling_parameters, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """g_et_update_scaling_parameters

    Configures scaling parameters for a domain. A domain&#39;s scaling parameters specify the desired search instance type and replication count. Amazon CloudSearch will still automatically scale your domain based on the volume of data and traffic, but not below the desired instance type and replication count. If the Multi-AZ option is enabled, these values control the resources used per Availability Zone. For more information, see &lt;a href&#x3D;\&quot;http://docs.aws.amazon.com/cloudsearch/latest/developerguide/configuring-scaling-options.html\&quot; target&#x3D;\&quot;_blank\&quot;&gt;Configuring Scaling Options&lt;/a&gt; in the &lt;i&gt;Amazon CloudSearch Developer Guide&lt;/i&gt;. 

    :param domain_name: 
    :type domain_name: str
    :param scaling_parameters: 
    :type scaling_parameters: dict | bytes
    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    scaling_parameters = .from_dict(scaling_parameters)
    return web.Response(status=200)


async def g_et_update_service_access_policies(request: web.Request, domain_name, access_policies, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """g_et_update_service_access_policies

    Configures the access rules that control access to the domain&#39;s document and search endpoints. For more information, see &lt;a href&#x3D;\&quot;http://docs.aws.amazon.com/cloudsearch/latest/developerguide/configuring-access.html\&quot; target&#x3D;\&quot;_blank\&quot;&gt; Configuring Access for an Amazon CloudSearch Domain&lt;/a&gt;.

    :param domain_name: 
    :type domain_name: str
    :param access_policies: The access rules you want to configure. These rules replace any existing rules. 
    :type access_policies: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def p_ost_build_suggesters(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_build_suggesters

    Indexes the search suggestions. For more information, see &lt;a href&#x3D;\&quot;http://docs.aws.amazon.com/cloudsearch/latest/developerguide/getting-suggestions.html#configuring-suggesters\&quot;&gt;Configuring Suggesters&lt;/a&gt; in the &lt;i&gt;Amazon CloudSearch Developer Guide&lt;/i&gt;.

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param body: 
    :type body: dict | bytes

    """
    body = BuildSuggestersRequest.from_dict(body)
    return web.Response(status=200)


async def p_ost_create_domain(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_create_domain

    Creates a new search domain. For more information, see &lt;a href&#x3D;\&quot;http://docs.aws.amazon.com/cloudsearch/latest/developerguide/creating-domains.html\&quot; target&#x3D;\&quot;_blank\&quot;&gt;Creating a Search Domain&lt;/a&gt; in the &lt;i&gt;Amazon CloudSearch Developer Guide&lt;/i&gt;.

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param body: 
    :type body: dict | bytes

    """
    body = CreateDomainRequest.from_dict(body)
    return web.Response(status=200)


async def p_ost_define_analysis_scheme(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_define_analysis_scheme

    Configures an analysis scheme that can be applied to a &lt;code&gt;text&lt;/code&gt; or &lt;code&gt;text-array&lt;/code&gt; field to define language-specific text processing options. For more information, see &lt;a href&#x3D;\&quot;http://docs.aws.amazon.com/cloudsearch/latest/developerguide/configuring-analysis-schemes.html\&quot; target&#x3D;\&quot;_blank\&quot;&gt;Configuring Analysis Schemes&lt;/a&gt; in the &lt;i&gt;Amazon CloudSearch Developer Guide&lt;/i&gt;.

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param body: 
    :type body: dict | bytes

    """
    body = DefineAnalysisSchemeRequest.from_dict(body)
    return web.Response(status=200)


async def p_ost_define_expression(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_define_expression

    Configures an &lt;code&gt;&lt;a&gt;Expression&lt;/a&gt;&lt;/code&gt; for the search domain. Used to create new expressions and modify existing ones. If the expression exists, the new configuration replaces the old one. For more information, see &lt;a href&#x3D;\&quot;http://docs.aws.amazon.com/cloudsearch/latest/developerguide/configuring-expressions.html\&quot; target&#x3D;\&quot;_blank\&quot;&gt;Configuring Expressions&lt;/a&gt; in the &lt;i&gt;Amazon CloudSearch Developer Guide&lt;/i&gt;.

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param body: 
    :type body: dict | bytes

    """
    body = DefineExpressionRequest.from_dict(body)
    return web.Response(status=200)


async def p_ost_define_index_field(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_define_index_field

    Configures an &lt;code&gt;&lt;a&gt;IndexField&lt;/a&gt;&lt;/code&gt; for the search domain. Used to create new fields and modify existing ones. You must specify the name of the domain you are configuring and an index field configuration. The index field configuration specifies a unique name, the index field type, and the options you want to configure for the field. The options you can specify depend on the &lt;code&gt;&lt;a&gt;IndexFieldType&lt;/a&gt;&lt;/code&gt;. If the field exists, the new configuration replaces the old one. For more information, see &lt;a href&#x3D;\&quot;http://docs.aws.amazon.com/cloudsearch/latest/developerguide/configuring-index-fields.html\&quot; target&#x3D;\&quot;_blank\&quot;&gt;Configuring Index Fields&lt;/a&gt; in the &lt;i&gt;Amazon CloudSearch Developer Guide&lt;/i&gt;. 

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param body: 
    :type body: dict | bytes

    """
    body = DefineIndexFieldRequest.from_dict(body)
    return web.Response(status=200)


async def p_ost_define_suggester(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_define_suggester

    Configures a suggester for a domain. A suggester enables you to display possible matches before users finish typing their queries. When you configure a suggester, you must specify the name of the text field you want to search for possible matches and a unique name for the suggester. For more information, see &lt;a href&#x3D;\&quot;http://docs.aws.amazon.com/cloudsearch/latest/developerguide/getting-suggestions.html\&quot; target&#x3D;\&quot;_blank\&quot;&gt;Getting Search Suggestions&lt;/a&gt; in the &lt;i&gt;Amazon CloudSearch Developer Guide&lt;/i&gt;.

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param body: 
    :type body: dict | bytes

    """
    body = DefineSuggesterRequest.from_dict(body)
    return web.Response(status=200)


async def p_ost_delete_analysis_scheme(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_delete_analysis_scheme

    Deletes an analysis scheme. For more information, see &lt;a href&#x3D;\&quot;http://docs.aws.amazon.com/cloudsearch/latest/developerguide/configuring-analysis-schemes.html\&quot; target&#x3D;\&quot;_blank\&quot;&gt;Configuring Analysis Schemes&lt;/a&gt; in the &lt;i&gt;Amazon CloudSearch Developer Guide&lt;/i&gt;. 

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param body: 
    :type body: dict | bytes

    """
    body = DeleteAnalysisSchemeRequest.from_dict(body)
    return web.Response(status=200)


async def p_ost_delete_domain(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_delete_domain

    Permanently deletes a search domain and all of its data. Once a domain has been deleted, it cannot be recovered. For more information, see &lt;a href&#x3D;\&quot;http://docs.aws.amazon.com/cloudsearch/latest/developerguide/deleting-domains.html\&quot; target&#x3D;\&quot;_blank\&quot;&gt;Deleting a Search Domain&lt;/a&gt; in the &lt;i&gt;Amazon CloudSearch Developer Guide&lt;/i&gt;. 

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param body: 
    :type body: dict | bytes

    """
    body = DeleteDomainRequest.from_dict(body)
    return web.Response(status=200)


async def p_ost_delete_expression(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_delete_expression

    Removes an &lt;code&gt;&lt;a&gt;Expression&lt;/a&gt;&lt;/code&gt; from the search domain. For more information, see &lt;a href&#x3D;\&quot;http://docs.aws.amazon.com/cloudsearch/latest/developerguide/configuring-expressions.html\&quot; target&#x3D;\&quot;_blank\&quot;&gt;Configuring Expressions&lt;/a&gt; in the &lt;i&gt;Amazon CloudSearch Developer Guide&lt;/i&gt;.

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param body: 
    :type body: dict | bytes

    """
    body = DeleteExpressionRequest.from_dict(body)
    return web.Response(status=200)


async def p_ost_delete_index_field(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_delete_index_field

    Removes an &lt;code&gt;&lt;a&gt;IndexField&lt;/a&gt;&lt;/code&gt; from the search domain. For more information, see &lt;a href&#x3D;\&quot;http://docs.aws.amazon.com/cloudsearch/latest/developerguide/configuring-index-fields.html\&quot; target&#x3D;\&quot;_blank\&quot;&gt;Configuring Index Fields&lt;/a&gt; in the &lt;i&gt;Amazon CloudSearch Developer Guide&lt;/i&gt;.

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param body: 
    :type body: dict | bytes

    """
    body = DeleteIndexFieldRequest.from_dict(body)
    return web.Response(status=200)


async def p_ost_delete_suggester(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_delete_suggester

    Deletes a suggester. For more information, see &lt;a href&#x3D;\&quot;http://docs.aws.amazon.com/cloudsearch/latest/developerguide/getting-suggestions.html\&quot; target&#x3D;\&quot;_blank\&quot;&gt;Getting Search Suggestions&lt;/a&gt; in the &lt;i&gt;Amazon CloudSearch Developer Guide&lt;/i&gt;.

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param body: 
    :type body: dict | bytes

    """
    body = DeleteSuggesterRequest.from_dict(body)
    return web.Response(status=200)


async def p_ost_describe_analysis_schemes(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_describe_analysis_schemes

    Gets the analysis schemes configured for a domain. An analysis scheme defines language-specific text processing options for a &lt;code&gt;text&lt;/code&gt; field. Can be limited to specific analysis schemes by name. By default, shows all analysis schemes and includes any pending changes to the configuration. Set the &lt;code&gt;Deployed&lt;/code&gt; option to &lt;code&gt;true&lt;/code&gt; to show the active configuration and exclude pending changes. For more information, see &lt;a href&#x3D;\&quot;http://docs.aws.amazon.com/cloudsearch/latest/developerguide/configuring-analysis-schemes.html\&quot; target&#x3D;\&quot;_blank\&quot;&gt;Configuring Analysis Schemes&lt;/a&gt; in the &lt;i&gt;Amazon CloudSearch Developer Guide&lt;/i&gt;.

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param body: 
    :type body: dict | bytes

    """
    body = DescribeAnalysisSchemesRequest.from_dict(body)
    return web.Response(status=200)


async def p_ost_describe_availability_options(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_describe_availability_options

    Gets the availability options configured for a domain. By default, shows the configuration with any pending changes. Set the &lt;code&gt;Deployed&lt;/code&gt; option to &lt;code&gt;true&lt;/code&gt; to show the active configuration and exclude pending changes. For more information, see &lt;a href&#x3D;\&quot;http://docs.aws.amazon.com/cloudsearch/latest/developerguide/configuring-availability-options.html\&quot; target&#x3D;\&quot;_blank\&quot;&gt;Configuring Availability Options&lt;/a&gt; in the &lt;i&gt;Amazon CloudSearch Developer Guide&lt;/i&gt;.

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param body: 
    :type body: dict | bytes

    """
    body = DescribeAvailabilityOptionsRequest.from_dict(body)
    return web.Response(status=200)


async def p_ost_describe_domain_endpoint_options(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_describe_domain_endpoint_options

    Returns the domain&#39;s endpoint options, specifically whether all requests to the domain must arrive over HTTPS. For more information, see &lt;a href&#x3D;\&quot;http://docs.aws.amazon.com/cloudsearch/latest/developerguide/configuring-domain-endpoint-options.html\&quot; target&#x3D;\&quot;_blank\&quot;&gt;Configuring Domain Endpoint Options&lt;/a&gt; in the &lt;i&gt;Amazon CloudSearch Developer Guide&lt;/i&gt;.

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param body: 
    :type body: dict | bytes

    """
    body = DescribeDomainEndpointOptionsRequest.from_dict(body)
    return web.Response(status=200)


async def p_ost_describe_domains(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_describe_domains

    Gets information about the search domains owned by this account. Can be limited to specific domains. Shows all domains by default. To get the number of searchable documents in a domain, use the console or submit a &lt;code&gt;matchall&lt;/code&gt; request to your domain&#39;s search endpoint: &lt;code&gt;q&#x3D;matchall&amp;amp;amp;q.parser&#x3D;structured&amp;amp;amp;size&#x3D;0&lt;/code&gt;. For more information, see &lt;a href&#x3D;\&quot;http://docs.aws.amazon.com/cloudsearch/latest/developerguide/getting-domain-info.html\&quot; target&#x3D;\&quot;_blank\&quot;&gt;Getting Information about a Search Domain&lt;/a&gt; in the &lt;i&gt;Amazon CloudSearch Developer Guide&lt;/i&gt;.

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param body: 
    :type body: dict | bytes

    """
    body = DescribeDomainsRequest.from_dict(body)
    return web.Response(status=200)


async def p_ost_describe_expressions(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_describe_expressions

    Gets the expressions configured for the search domain. Can be limited to specific expressions by name. By default, shows all expressions and includes any pending changes to the configuration. Set the &lt;code&gt;Deployed&lt;/code&gt; option to &lt;code&gt;true&lt;/code&gt; to show the active configuration and exclude pending changes. For more information, see &lt;a href&#x3D;\&quot;http://docs.aws.amazon.com/cloudsearch/latest/developerguide/configuring-expressions.html\&quot; target&#x3D;\&quot;_blank\&quot;&gt;Configuring Expressions&lt;/a&gt; in the &lt;i&gt;Amazon CloudSearch Developer Guide&lt;/i&gt;.

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param body: 
    :type body: dict | bytes

    """
    body = DescribeExpressionsRequest.from_dict(body)
    return web.Response(status=200)


async def p_ost_describe_index_fields(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_describe_index_fields

    Gets information about the index fields configured for the search domain. Can be limited to specific fields by name. By default, shows all fields and includes any pending changes to the configuration. Set the &lt;code&gt;Deployed&lt;/code&gt; option to &lt;code&gt;true&lt;/code&gt; to show the active configuration and exclude pending changes. For more information, see &lt;a href&#x3D;\&quot;http://docs.aws.amazon.com/cloudsearch/latest/developerguide/getting-domain-info.html\&quot; target&#x3D;\&quot;_blank\&quot;&gt;Getting Domain Information&lt;/a&gt; in the &lt;i&gt;Amazon CloudSearch Developer Guide&lt;/i&gt;.

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param body: 
    :type body: dict | bytes

    """
    body = DescribeIndexFieldsRequest.from_dict(body)
    return web.Response(status=200)


async def p_ost_describe_scaling_parameters(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_describe_scaling_parameters

    Gets the scaling parameters configured for a domain. A domain&#39;s scaling parameters specify the desired search instance type and replication count. For more information, see &lt;a href&#x3D;\&quot;http://docs.aws.amazon.com/cloudsearch/latest/developerguide/configuring-scaling-options.html\&quot; target&#x3D;\&quot;_blank\&quot;&gt;Configuring Scaling Options&lt;/a&gt; in the &lt;i&gt;Amazon CloudSearch Developer Guide&lt;/i&gt;.

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param body: 
    :type body: dict | bytes

    """
    body = DescribeScalingParametersRequest.from_dict(body)
    return web.Response(status=200)


async def p_ost_describe_service_access_policies(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_describe_service_access_policies

    Gets information about the access policies that control access to the domain&#39;s document and search endpoints. By default, shows the configuration with any pending changes. Set the &lt;code&gt;Deployed&lt;/code&gt; option to &lt;code&gt;true&lt;/code&gt; to show the active configuration and exclude pending changes. For more information, see &lt;a href&#x3D;\&quot;http://docs.aws.amazon.com/cloudsearch/latest/developerguide/configuring-access.html\&quot; target&#x3D;\&quot;_blank\&quot;&gt;Configuring Access for a Search Domain&lt;/a&gt; in the &lt;i&gt;Amazon CloudSearch Developer Guide&lt;/i&gt;.

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param body: 
    :type body: dict | bytes

    """
    body = DescribeServiceAccessPoliciesRequest.from_dict(body)
    return web.Response(status=200)


async def p_ost_describe_suggesters(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_describe_suggesters

    Gets the suggesters configured for a domain. A suggester enables you to display possible matches before users finish typing their queries. Can be limited to specific suggesters by name. By default, shows all suggesters and includes any pending changes to the configuration. Set the &lt;code&gt;Deployed&lt;/code&gt; option to &lt;code&gt;true&lt;/code&gt; to show the active configuration and exclude pending changes. For more information, see &lt;a href&#x3D;\&quot;http://docs.aws.amazon.com/cloudsearch/latest/developerguide/getting-suggestions.html\&quot; target&#x3D;\&quot;_blank\&quot;&gt;Getting Search Suggestions&lt;/a&gt; in the &lt;i&gt;Amazon CloudSearch Developer Guide&lt;/i&gt;.

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param body: 
    :type body: dict | bytes

    """
    body = DescribeSuggestersRequest.from_dict(body)
    return web.Response(status=200)


async def p_ost_index_documents(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_index_documents

    Tells the search domain to start indexing its documents using the latest indexing options. This operation must be invoked to activate options whose &lt;a&gt;OptionStatus&lt;/a&gt; is &lt;code&gt;RequiresIndexDocuments&lt;/code&gt;.

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param body: 
    :type body: dict | bytes

    """
    body = IndexDocumentsRequest.from_dict(body)
    return web.Response(status=200)


async def p_ost_list_domain_names(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """p_ost_list_domain_names

    Lists all search domains owned by an account.

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def p_ost_update_availability_options(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_update_availability_options

    Configures the availability options for a domain. Enabling the Multi-AZ option expands an Amazon CloudSearch domain to an additional Availability Zone in the same Region to increase fault tolerance in the event of a service disruption. Changes to the Multi-AZ option can take about half an hour to become active. For more information, see &lt;a href&#x3D;\&quot;http://docs.aws.amazon.com/cloudsearch/latest/developerguide/configuring-availability-options.html\&quot; target&#x3D;\&quot;_blank\&quot;&gt;Configuring Availability Options&lt;/a&gt; in the &lt;i&gt;Amazon CloudSearch Developer Guide&lt;/i&gt;.

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateAvailabilityOptionsRequest.from_dict(body)
    return web.Response(status=200)


async def p_ost_update_domain_endpoint_options(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_update_domain_endpoint_options

    Updates the domain&#39;s endpoint options, specifically whether all requests to the domain must arrive over HTTPS. For more information, see &lt;a href&#x3D;\&quot;http://docs.aws.amazon.com/cloudsearch/latest/developerguide/configuring-domain-endpoint-options.html\&quot; target&#x3D;\&quot;_blank\&quot;&gt;Configuring Domain Endpoint Options&lt;/a&gt; in the &lt;i&gt;Amazon CloudSearch Developer Guide&lt;/i&gt;.

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateDomainEndpointOptionsRequest.from_dict(body)
    return web.Response(status=200)


async def p_ost_update_scaling_parameters(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_update_scaling_parameters

    Configures scaling parameters for a domain. A domain&#39;s scaling parameters specify the desired search instance type and replication count. Amazon CloudSearch will still automatically scale your domain based on the volume of data and traffic, but not below the desired instance type and replication count. If the Multi-AZ option is enabled, these values control the resources used per Availability Zone. For more information, see &lt;a href&#x3D;\&quot;http://docs.aws.amazon.com/cloudsearch/latest/developerguide/configuring-scaling-options.html\&quot; target&#x3D;\&quot;_blank\&quot;&gt;Configuring Scaling Options&lt;/a&gt; in the &lt;i&gt;Amazon CloudSearch Developer Guide&lt;/i&gt;. 

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateScalingParametersRequest.from_dict(body)
    return web.Response(status=200)


async def p_ost_update_service_access_policies(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_update_service_access_policies

    Configures the access rules that control access to the domain&#39;s document and search endpoints. For more information, see &lt;a href&#x3D;\&quot;http://docs.aws.amazon.com/cloudsearch/latest/developerguide/configuring-access.html\&quot; target&#x3D;\&quot;_blank\&quot;&gt; Configuring Access for an Amazon CloudSearch Domain&lt;/a&gt;.

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateServiceAccessPoliciesRequest.from_dict(body)
    return web.Response(status=200)
