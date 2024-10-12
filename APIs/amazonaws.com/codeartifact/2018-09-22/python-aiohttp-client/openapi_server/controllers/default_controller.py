from typing import List, Dict
from aiohttp import web

from openapi_server.models.associate_external_connection_result import AssociateExternalConnectionResult
from openapi_server.models.copy_package_versions_request import CopyPackageVersionsRequest
from openapi_server.models.copy_package_versions_result import CopyPackageVersionsResult
from openapi_server.models.create_domain_request import CreateDomainRequest
from openapi_server.models.create_domain_result import CreateDomainResult
from openapi_server.models.create_repository_request import CreateRepositoryRequest
from openapi_server.models.create_repository_result import CreateRepositoryResult
from openapi_server.models.delete_domain_permissions_policy_result import DeleteDomainPermissionsPolicyResult
from openapi_server.models.delete_domain_result import DeleteDomainResult
from openapi_server.models.delete_package_result import DeletePackageResult
from openapi_server.models.delete_package_versions_request import DeletePackageVersionsRequest
from openapi_server.models.delete_package_versions_result import DeletePackageVersionsResult
from openapi_server.models.delete_repository_permissions_policy_result import DeleteRepositoryPermissionsPolicyResult
from openapi_server.models.delete_repository_result import DeleteRepositoryResult
from openapi_server.models.describe_domain_result import DescribeDomainResult
from openapi_server.models.describe_package_result import DescribePackageResult
from openapi_server.models.describe_package_version_result import DescribePackageVersionResult
from openapi_server.models.describe_repository_result import DescribeRepositoryResult
from openapi_server.models.disassociate_external_connection_result import DisassociateExternalConnectionResult
from openapi_server.models.dispose_package_versions_request import DisposePackageVersionsRequest
from openapi_server.models.dispose_package_versions_result import DisposePackageVersionsResult
from openapi_server.models.get_authorization_token_result import GetAuthorizationTokenResult
from openapi_server.models.get_domain_permissions_policy_result import GetDomainPermissionsPolicyResult
from openapi_server.models.get_package_version_asset_result import GetPackageVersionAssetResult
from openapi_server.models.get_package_version_readme_result import GetPackageVersionReadmeResult
from openapi_server.models.get_repository_endpoint_result import GetRepositoryEndpointResult
from openapi_server.models.get_repository_permissions_policy_result import GetRepositoryPermissionsPolicyResult
from openapi_server.models.list_domains_request import ListDomainsRequest
from openapi_server.models.list_domains_result import ListDomainsResult
from openapi_server.models.list_package_version_assets_result import ListPackageVersionAssetsResult
from openapi_server.models.list_package_version_dependencies_result import ListPackageVersionDependenciesResult
from openapi_server.models.list_package_versions_result import ListPackageVersionsResult
from openapi_server.models.list_packages_result import ListPackagesResult
from openapi_server.models.list_repositories_in_domain_result import ListRepositoriesInDomainResult
from openapi_server.models.list_repositories_result import ListRepositoriesResult
from openapi_server.models.list_tags_for_resource_result import ListTagsForResourceResult
from openapi_server.models.publish_package_version_request import PublishPackageVersionRequest
from openapi_server.models.publish_package_version_result import PublishPackageVersionResult
from openapi_server.models.put_domain_permissions_policy_request import PutDomainPermissionsPolicyRequest
from openapi_server.models.put_domain_permissions_policy_result import PutDomainPermissionsPolicyResult
from openapi_server.models.put_package_origin_configuration_request import PutPackageOriginConfigurationRequest
from openapi_server.models.put_package_origin_configuration_result import PutPackageOriginConfigurationResult
from openapi_server.models.put_repository_permissions_policy_request import PutRepositoryPermissionsPolicyRequest
from openapi_server.models.put_repository_permissions_policy_result import PutRepositoryPermissionsPolicyResult
from openapi_server.models.tag_resource_request import TagResourceRequest
from openapi_server.models.untag_resource_request import UntagResourceRequest
from openapi_server.models.update_package_versions_status_request import UpdatePackageVersionsStatusRequest
from openapi_server.models.update_package_versions_status_result import UpdatePackageVersionsStatusResult
from openapi_server.models.update_repository_request import UpdateRepositoryRequest
from openapi_server.models.update_repository_result import UpdateRepositoryResult
from openapi_server import util


async def associate_external_connection(request: web.Request, domain, repository, external_connection, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, domain_owner=None) -> web.Response:
    """associate_external_connection

    &lt;p&gt;Adds an existing external connection to a repository. One external connection is allowed per repository.&lt;/p&gt; &lt;note&gt; &lt;p&gt;A repository can have one or more upstream repositories, or an external connection.&lt;/p&gt; &lt;/note&gt;

    :param domain: The name of the domain that contains the repository.
    :type domain: str
    :param repository:  The name of the repository to which the external connection is added. 
    :type repository: str
    :param external_connection: &lt;p&gt; The name of the external connection to add to the repository. The following values are supported: &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;public:npmjs&lt;/code&gt; - for the npm public repository. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;public:nuget-org&lt;/code&gt; - for the NuGet Gallery. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;public:pypi&lt;/code&gt; - for the Python Package Index. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;public:maven-central&lt;/code&gt; - for Maven Central. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;public:maven-googleandroid&lt;/code&gt; - for the Google Android repository. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;public:maven-gradleplugins&lt;/code&gt; - for the Gradle plugins repository. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;public:maven-commonsware&lt;/code&gt; - for the CommonsWare Android repository. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;public:maven-clojars&lt;/code&gt; - for the Clojars repository. &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;
    :type external_connection: str
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
    :param domain_owner:  The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces. 
    :type domain_owner: str

    """
    return web.Response(status=200)


async def copy_package_versions(request: web.Request, domain, source_repository, destination_repository, format, package, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, domain_owner=None, namespace=None) -> web.Response:
    """copy_package_versions

    &lt;p&gt; Copies package versions from one repository to another repository in the same domain. &lt;/p&gt; &lt;note&gt; &lt;p&gt; You must specify &lt;code&gt;versions&lt;/code&gt; or &lt;code&gt;versionRevisions&lt;/code&gt;. You cannot specify both. &lt;/p&gt; &lt;/note&gt;

    :param domain:  The name of the domain that contains the source and destination repositories. 
    :type domain: str
    :param source_repository:  The name of the repository that contains the package versions to be copied. 
    :type source_repository: str
    :param destination_repository:  The name of the repository into which package versions are copied. 
    :type destination_repository: str
    :param format:  The format of the package versions to be copied. 
    :type format: str
    :param package:  The name of the package that contains the versions to be copied. 
    :type package: str
    :param body: 
    :type body: dict | bytes
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
    :param domain_owner:  The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces. 
    :type domain_owner: str
    :param namespace: &lt;p&gt;The namespace of the package versions to be copied. The package version component that specifies its namespace depends on its type. For example:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; The namespace of a Maven package version is its &lt;code&gt;groupId&lt;/code&gt;. The namespace is required when copying Maven package versions. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; The namespace of an npm package version is its &lt;code&gt;scope&lt;/code&gt;. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; Python and NuGet package versions do not contain a corresponding component, package versions of those formats do not have a namespace. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; The namespace of a generic package is its &lt;code&gt;namespace&lt;/code&gt;. &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;
    :type namespace: str

    """
    body = CopyPackageVersionsRequest.from_dict(body)
    return web.Response(status=200)


async def create_domain(request: web.Request, domain, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_domain

    &lt;p&gt; Creates a domain. CodeArtifact &lt;i&gt;domains&lt;/i&gt; make it easier to manage multiple repositories across an organization. You can use a domain to apply permissions across many repositories owned by different Amazon Web Services accounts. An asset is stored only once in a domain, even if it&#39;s in multiple repositories. &lt;/p&gt; &lt;p&gt;Although you can have multiple domains, we recommend a single production domain that contains all published artifacts so that your development teams can find and share packages. You can use a second pre-production domain to test changes to the production domain configuration. &lt;/p&gt;

    :param domain:  The name of the domain to create. All domain names in an Amazon Web Services Region that are in the same Amazon Web Services account must be unique. The domain name is used as the prefix in DNS hostnames. Do not use sensitive information in a domain name because it is publicly discoverable. 
    :type domain: str
    :param body: 
    :type body: dict | bytes
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
    body = CreateDomainRequest.from_dict(body)
    return web.Response(status=200)


async def create_repository(request: web.Request, domain, repository, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, domain_owner=None) -> web.Response:
    """create_repository

     Creates a repository. 

    :param domain:  The name of the domain that contains the created repository. 
    :type domain: str
    :param repository:  The name of the repository to create. 
    :type repository: str
    :param body: 
    :type body: dict | bytes
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
    :param domain_owner:  The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces. 
    :type domain_owner: str

    """
    body = CreateRepositoryRequest.from_dict(body)
    return web.Response(status=200)


async def delete_domain(request: web.Request, domain, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, domain_owner=None) -> web.Response:
    """delete_domain

     Deletes a domain. You cannot delete a domain that contains repositories. If you want to delete a domain with repositories, first delete its repositories. 

    :param domain:  The name of the domain to delete. 
    :type domain: str
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
    :param domain_owner:  The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces. 
    :type domain_owner: str

    """
    return web.Response(status=200)


async def delete_domain_permissions_policy(request: web.Request, domain, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, domain_owner=None, policy_revision=None) -> web.Response:
    """delete_domain_permissions_policy

     Deletes the resource policy set on a domain. 

    :param domain:  The name of the domain associated with the resource policy to be deleted. 
    :type domain: str
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
    :param domain_owner:  The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces. 
    :type domain_owner: str
    :param policy_revision:  The current revision of the resource policy to be deleted. This revision is used for optimistic locking, which prevents others from overwriting your changes to the domain&#39;s resource policy. 
    :type policy_revision: str

    """
    return web.Response(status=200)


async def delete_package(request: web.Request, domain, repository, format, package, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, domain_owner=None, namespace=None) -> web.Response:
    """delete_package

    Deletes a package and all associated package versions. A deleted package cannot be restored. To delete one or more package versions, use the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_DeletePackageVersions.html\&quot;&gt;DeletePackageVersions&lt;/a&gt; API.

    :param domain: The name of the domain that contains the package to delete.
    :type domain: str
    :param repository: The name of the repository that contains the package to delete.
    :type repository: str
    :param format: The format of the requested package to delete.
    :type format: str
    :param package: The name of the package to delete.
    :type package: str
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
    :param domain_owner:  The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces. 
    :type domain_owner: str
    :param namespace: &lt;p&gt;The namespace of the package to delete. The package component that specifies its namespace depends on its type. For example:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; The namespace of a Maven package is its &lt;code&gt;groupId&lt;/code&gt;. The namespace is required when deleting Maven package versions. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; The namespace of an npm package is its &lt;code&gt;scope&lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; Python and NuGet packages do not contain corresponding components, packages of those formats do not have a namespace. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; The namespace of a generic package is its &lt;code&gt;namespace&lt;/code&gt;. &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;
    :type namespace: str

    """
    return web.Response(status=200)


async def delete_package_versions(request: web.Request, domain, repository, format, package, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, domain_owner=None, namespace=None) -> web.Response:
    """delete_package_versions

     Deletes one or more versions of a package. A deleted package version cannot be restored in your repository. If you want to remove a package version from your repository and be able to restore it later, set its status to &lt;code&gt;Archived&lt;/code&gt;. Archived packages cannot be downloaded from a repository and don&#39;t show up with list package APIs (for example, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_ListPackageVersions.html\&quot;&gt;ListPackageVersions&lt;/a&gt;), but you can restore them using &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_UpdatePackageVersionsStatus.html\&quot;&gt;UpdatePackageVersionsStatus&lt;/a&gt;. 

    :param domain:  The name of the domain that contains the package to delete. 
    :type domain: str
    :param repository:  The name of the repository that contains the package versions to delete. 
    :type repository: str
    :param format:  The format of the package versions to delete. 
    :type format: str
    :param package:  The name of the package with the versions to delete. 
    :type package: str
    :param body: 
    :type body: dict | bytes
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
    :param domain_owner:  The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces. 
    :type domain_owner: str
    :param namespace: &lt;p&gt;The namespace of the package versions to be deleted. The package version component that specifies its namespace depends on its type. For example:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; The namespace of a Maven package version is its &lt;code&gt;groupId&lt;/code&gt;. The namespace is required when deleting Maven package versions. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; The namespace of an npm package version is its &lt;code&gt;scope&lt;/code&gt;. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; Python and NuGet package versions do not contain a corresponding component, package versions of those formats do not have a namespace. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; The namespace of a generic package is its &lt;code&gt;namespace&lt;/code&gt;. &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;
    :type namespace: str

    """
    body = DeletePackageVersionsRequest.from_dict(body)
    return web.Response(status=200)


async def delete_repository(request: web.Request, domain, repository, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, domain_owner=None) -> web.Response:
    """delete_repository

     Deletes a repository. 

    :param domain:  The name of the domain that contains the repository to delete. 
    :type domain: str
    :param repository:  The name of the repository to delete. 
    :type repository: str
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
    :param domain_owner:  The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces. 
    :type domain_owner: str

    """
    return web.Response(status=200)


async def delete_repository_permissions_policy(request: web.Request, domain, repository, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, domain_owner=None, policy_revision=None) -> web.Response:
    """delete_repository_permissions_policy

    &lt;p&gt; Deletes the resource policy that is set on a repository. After a resource policy is deleted, the permissions allowed and denied by the deleted policy are removed. The effect of deleting a resource policy might not be immediate. &lt;/p&gt; &lt;important&gt; &lt;p&gt; Use &lt;code&gt;DeleteRepositoryPermissionsPolicy&lt;/code&gt; with caution. After a policy is deleted, Amazon Web Services users, roles, and accounts lose permissions to perform the repository actions granted by the deleted policy. &lt;/p&gt; &lt;/important&gt;

    :param domain:  The name of the domain that contains the repository associated with the resource policy to be deleted. 
    :type domain: str
    :param repository:  The name of the repository that is associated with the resource policy to be deleted 
    :type repository: str
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
    :param domain_owner:  The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces. 
    :type domain_owner: str
    :param policy_revision:  The revision of the repository&#39;s resource policy to be deleted. This revision is used for optimistic locking, which prevents others from accidentally overwriting your changes to the repository&#39;s resource policy. 
    :type policy_revision: str

    """
    return web.Response(status=200)


async def describe_domain(request: web.Request, domain, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, domain_owner=None) -> web.Response:
    """describe_domain

     Returns a &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_DomainDescription.html\&quot;&gt;DomainDescription&lt;/a&gt; object that contains information about the requested domain. 

    :param domain:  A string that specifies the name of the requested domain. 
    :type domain: str
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
    :param domain_owner:  The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces. 
    :type domain_owner: str

    """
    return web.Response(status=200)


async def describe_package(request: web.Request, domain, repository, format, package, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, domain_owner=None, namespace=None) -> web.Response:
    """describe_package

     Returns a &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_PackageDescription.html\&quot;&gt;PackageDescription&lt;/a&gt; object that contains information about the requested package.

    :param domain: The name of the domain that contains the repository that contains the package.
    :type domain: str
    :param repository: The name of the repository that contains the requested package. 
    :type repository: str
    :param format: A format that specifies the type of the requested package.
    :type format: str
    :param package: The name of the requested package.
    :type package: str
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
    :param domain_owner:  The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces. 
    :type domain_owner: str
    :param namespace: &lt;p&gt;The namespace of the requested package. The package component that specifies its namespace depends on its type. For example:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; The namespace of a Maven package is its &lt;code&gt;groupId&lt;/code&gt;. The namespace is required when requesting Maven packages. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; The namespace of an npm package is its &lt;code&gt;scope&lt;/code&gt;. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; Python and NuGet packages do not contain a corresponding component, packages of those formats do not have a namespace. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; The namespace of a generic package is its &lt;code&gt;namespace&lt;/code&gt;. &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;
    :type namespace: str

    """
    return web.Response(status=200)


async def describe_package_version(request: web.Request, domain, repository, format, package, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, domain_owner=None, namespace=None) -> web.Response:
    """describe_package_version

     Returns a &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_PackageVersionDescription.html\&quot;&gt;PackageVersionDescription&lt;/a&gt; object that contains information about the requested package version. 

    :param domain:  The name of the domain that contains the repository that contains the package version. 
    :type domain: str
    :param repository:  The name of the repository that contains the package version. 
    :type repository: str
    :param format:  A format that specifies the type of the requested package version. 
    :type format: str
    :param package:  The name of the requested package version. 
    :type package: str
    :param version:  A string that contains the package version (for example, &lt;code&gt;3.5.2&lt;/code&gt;). 
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
    :param domain_owner:  The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces. 
    :type domain_owner: str
    :param namespace: &lt;p&gt;The namespace of the requested package version. The package version component that specifies its namespace depends on its type. For example:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; The namespace of a Maven package version is its &lt;code&gt;groupId&lt;/code&gt;. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; The namespace of an npm package version is its &lt;code&gt;scope&lt;/code&gt;. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; Python and NuGet package versions do not contain a corresponding component, package versions of those formats do not have a namespace. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; The namespace of a generic package is its &lt;code&gt;namespace&lt;/code&gt;. &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;
    :type namespace: str

    """
    return web.Response(status=200)


async def describe_repository(request: web.Request, domain, repository, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, domain_owner=None) -> web.Response:
    """describe_repository

     Returns a &lt;code&gt;RepositoryDescription&lt;/code&gt; object that contains detailed information about the requested repository. 

    :param domain:  The name of the domain that contains the repository to describe. 
    :type domain: str
    :param repository:  A string that specifies the name of the requested repository. 
    :type repository: str
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
    :param domain_owner:  The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces. 
    :type domain_owner: str

    """
    return web.Response(status=200)


async def disassociate_external_connection(request: web.Request, domain, repository, external_connection, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, domain_owner=None) -> web.Response:
    """disassociate_external_connection

     Removes an existing external connection from a repository. 

    :param domain: The name of the domain that contains the repository from which to remove the external repository. 
    :type domain: str
    :param repository: The name of the repository from which the external connection will be removed. 
    :type repository: str
    :param external_connection: The name of the external connection to be removed from the repository. 
    :type external_connection: str
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
    :param domain_owner:  The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces. 
    :type domain_owner: str

    """
    return web.Response(status=200)


async def dispose_package_versions(request: web.Request, domain, repository, format, package, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, domain_owner=None, namespace=None) -> web.Response:
    """dispose_package_versions

    &lt;p&gt; Deletes the assets in package versions and sets the package versions&#39; status to &lt;code&gt;Disposed&lt;/code&gt;. A disposed package version cannot be restored in your repository because its assets are deleted. &lt;/p&gt; &lt;p&gt; To view all disposed package versions in a repository, use &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_ListPackageVersions.html\&quot;&gt;ListPackageVersions&lt;/a&gt; and set the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_ListPackageVersions.html#API_ListPackageVersions_RequestSyntax\&quot;&gt;status&lt;/a&gt; parameter to &lt;code&gt;Disposed&lt;/code&gt;. &lt;/p&gt; &lt;p&gt; To view information about a disposed package version, use &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_DescribePackageVersion.html\&quot;&gt;DescribePackageVersion&lt;/a&gt;. &lt;/p&gt;

    :param domain:  The name of the domain that contains the repository you want to dispose. 
    :type domain: str
    :param repository:  The name of the repository that contains the package versions you want to dispose. 
    :type repository: str
    :param format:  A format that specifies the type of package versions you want to dispose. 
    :type format: str
    :param package:  The name of the package with the versions you want to dispose. 
    :type package: str
    :param body: 
    :type body: dict | bytes
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
    :param domain_owner:  The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces. 
    :type domain_owner: str
    :param namespace: &lt;p&gt;The namespace of the package versions to be disposed. The package version component that specifies its namespace depends on its type. For example:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; The namespace of a Maven package version is its &lt;code&gt;groupId&lt;/code&gt;. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; The namespace of an npm package version is its &lt;code&gt;scope&lt;/code&gt;. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; Python and NuGet package versions do not contain a corresponding component, package versions of those formats do not have a namespace. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; The namespace of a generic package is its &lt;code&gt;namespace&lt;/code&gt;. &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;
    :type namespace: str

    """
    body = DisposePackageVersionsRequest.from_dict(body)
    return web.Response(status=200)


async def get_authorization_token(request: web.Request, domain, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, domain_owner=None, duration=None) -> web.Response:
    """get_authorization_token

    &lt;p&gt; Generates a temporary authorization token for accessing repositories in the domain. This API requires the &lt;code&gt;codeartifact:GetAuthorizationToken&lt;/code&gt; and &lt;code&gt;sts:GetServiceBearerToken&lt;/code&gt; permissions. For more information about authorization tokens, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/codeartifact/latest/ug/tokens-authentication.html\&quot;&gt;CodeArtifact authentication and tokens&lt;/a&gt;. &lt;/p&gt; &lt;note&gt; &lt;p&gt;CodeArtifact authorization tokens are valid for a period of 12 hours when created with the &lt;code&gt;login&lt;/code&gt; command. You can call &lt;code&gt;login&lt;/code&gt; periodically to refresh the token. When you create an authorization token with the &lt;code&gt;GetAuthorizationToken&lt;/code&gt; API, you can set a custom authorization period, up to a maximum of 12 hours, with the &lt;code&gt;durationSeconds&lt;/code&gt; parameter.&lt;/p&gt; &lt;p&gt;The authorization period begins after &lt;code&gt;login&lt;/code&gt; or &lt;code&gt;GetAuthorizationToken&lt;/code&gt; is called. If &lt;code&gt;login&lt;/code&gt; or &lt;code&gt;GetAuthorizationToken&lt;/code&gt; is called while assuming a role, the token lifetime is independent of the maximum session duration of the role. For example, if you call &lt;code&gt;sts assume-role&lt;/code&gt; and specify a session duration of 15 minutes, then generate a CodeArtifact authorization token, the token will be valid for the full authorization period even though this is longer than the 15-minute session duration.&lt;/p&gt; &lt;p&gt;See &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use.html\&quot;&gt;Using IAM Roles&lt;/a&gt; for more information on controlling session duration. &lt;/p&gt; &lt;/note&gt;

    :param domain:  The name of the domain that is in scope for the generated authorization token. 
    :type domain: str
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
    :param domain_owner:  The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces. 
    :type domain_owner: str
    :param duration: The time, in seconds, that the generated authorization token is valid. Valid values are &lt;code&gt;0&lt;/code&gt; and any number between &lt;code&gt;900&lt;/code&gt; (15 minutes) and &lt;code&gt;43200&lt;/code&gt; (12 hours). A value of &lt;code&gt;0&lt;/code&gt; will set the expiration of the authorization token to the same expiration of the user&#39;s role&#39;s temporary credentials.
    :type duration: int

    """
    return web.Response(status=200)


async def get_domain_permissions_policy(request: web.Request, domain, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, domain_owner=None) -> web.Response:
    """get_domain_permissions_policy

    &lt;p&gt; Returns the resource policy attached to the specified domain. &lt;/p&gt; &lt;note&gt; &lt;p&gt; The policy is a resource-based policy, not an identity-based policy. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_identity-vs-resource.html\&quot;&gt;Identity-based policies and resource-based policies &lt;/a&gt; in the &lt;i&gt;IAM User Guide&lt;/i&gt;. &lt;/p&gt; &lt;/note&gt;

    :param domain:  The name of the domain to which the resource policy is attached. 
    :type domain: str
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
    :param domain_owner:  The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces. 
    :type domain_owner: str

    """
    return web.Response(status=200)


async def get_package_version_asset(request: web.Request, domain, repository, format, package, version, asset, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, domain_owner=None, namespace=None, revision=None) -> web.Response:
    """get_package_version_asset

     Returns an asset (or file) that is in a package. For example, for a Maven package version, use &lt;code&gt;GetPackageVersionAsset&lt;/code&gt; to download a &lt;code&gt;JAR&lt;/code&gt; file, a &lt;code&gt;POM&lt;/code&gt; file, or any other assets in the package version. 

    :param domain:  The name of the domain that contains the repository that contains the package version with the requested asset. 
    :type domain: str
    :param repository:  The repository that contains the package version with the requested asset. 
    :type repository: str
    :param format:  A format that specifies the type of the package version with the requested asset file. 
    :type format: str
    :param package:  The name of the package that contains the requested asset. 
    :type package: str
    :param version:  A string that contains the package version (for example, &lt;code&gt;3.5.2&lt;/code&gt;). 
    :type version: str
    :param asset:  The name of the requested asset. 
    :type asset: str
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
    :param domain_owner:  The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces. 
    :type domain_owner: str
    :param namespace: &lt;p&gt;The namespace of the package version with the requested asset file. The package version component that specifies its namespace depends on its type. For example:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; The namespace of a Maven package version is its &lt;code&gt;groupId&lt;/code&gt;. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; The namespace of an npm package version is its &lt;code&gt;scope&lt;/code&gt;. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; Python and NuGet package versions do not contain a corresponding component, package versions of those formats do not have a namespace. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; The namespace of a generic package is its &lt;code&gt;namespace&lt;/code&gt;. &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;
    :type namespace: str
    :param revision:  The name of the package version revision that contains the requested asset. 
    :type revision: str

    """
    return web.Response(status=200)


async def get_package_version_readme(request: web.Request, domain, repository, format, package, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, domain_owner=None, namespace=None) -> web.Response:
    """get_package_version_readme

    &lt;p&gt; Gets the readme file or descriptive text for a package version. &lt;/p&gt; &lt;p&gt; The returned text might contain formatting. For example, it might contain formatting for Markdown or reStructuredText. &lt;/p&gt;

    :param domain:  The name of the domain that contains the repository that contains the package version with the requested readme file. 
    :type domain: str
    :param repository:  The repository that contains the package with the requested readme file. 
    :type repository: str
    :param format:  A format that specifies the type of the package version with the requested readme file. 
    :type format: str
    :param package:  The name of the package version that contains the requested readme file. 
    :type package: str
    :param version:  A string that contains the package version (for example, &lt;code&gt;3.5.2&lt;/code&gt;). 
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
    :param domain_owner:  The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces. 
    :type domain_owner: str
    :param namespace: &lt;p&gt;The namespace of the package version with the requested readme file. The package version component that specifies its namespace depends on its type. For example:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; The namespace of an npm package version is its &lt;code&gt;scope&lt;/code&gt;. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; Python and NuGet package versions do not contain a corresponding component, package versions of those formats do not have a namespace. &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;
    :type namespace: str

    """
    return web.Response(status=200)


async def get_repository_endpoint(request: web.Request, domain, repository, format, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, domain_owner=None) -> web.Response:
    """get_repository_endpoint

    &lt;p&gt; Returns the endpoint of a repository for a specific package format. A repository has one endpoint for each package format: &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;maven&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;npm&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;nuget&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;pypi&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

    :param domain:  The name of the domain that contains the repository. 
    :type domain: str
    :param repository:  The name of the repository. 
    :type repository: str
    :param format:  Returns which endpoint of a repository to return. A repository has one endpoint for each package format. 
    :type format: str
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
    :param domain_owner:  The 12-digit account number of the Amazon Web Services account that owns the domain that contains the repository. It does not include dashes or spaces. 
    :type domain_owner: str

    """
    return web.Response(status=200)


async def get_repository_permissions_policy(request: web.Request, domain, repository, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, domain_owner=None) -> web.Response:
    """get_repository_permissions_policy

     Returns the resource policy that is set on a repository. 

    :param domain:  The name of the domain containing the repository whose associated resource policy is to be retrieved. 
    :type domain: str
    :param repository:  The name of the repository whose associated resource policy is to be retrieved. 
    :type repository: str
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
    :param domain_owner:  The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces. 
    :type domain_owner: str

    """
    return web.Response(status=200)


async def list_domains(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_domains

     Returns a list of &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_PackageVersionDescription.html\&quot;&gt;DomainSummary&lt;/a&gt; objects for all domains owned by the Amazon Web Services account that makes this call. Each returned &lt;code&gt;DomainSummary&lt;/code&gt; object contains information about a domain. 

    :param body: 
    :type body: dict | bytes
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
    :param max_results: Pagination limit
    :type max_results: str
    :param next_token: Pagination token
    :type next_token: str

    """
    body = ListDomainsRequest.from_dict(body)
    return web.Response(status=200)


async def list_package_version_assets(request: web.Request, domain, repository, format, package, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, domain_owner=None, namespace=None, max_results=None, next_token=None, max_results2=None, next_token2=None) -> web.Response:
    """list_package_version_assets

     Returns a list of &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_AssetSummary.html\&quot;&gt;AssetSummary&lt;/a&gt; objects for assets in a package version. 

    :param domain:  The name of the domain that contains the repository associated with the package version assets. 
    :type domain: str
    :param repository:  The name of the repository that contains the package that contains the requested package version assets. 
    :type repository: str
    :param format:  The format of the package that contains the requested package version assets. 
    :type format: str
    :param package:  The name of the package that contains the requested package version assets. 
    :type package: str
    :param version:  A string that contains the package version (for example, &lt;code&gt;3.5.2&lt;/code&gt;). 
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
    :param domain_owner:  The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces. 
    :type domain_owner: str
    :param namespace: &lt;p&gt;The namespace of the package version that contains the requested package version assets. The package version component that specifies its namespace depends on its type. For example:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; The namespace of a Maven package version is its &lt;code&gt;groupId&lt;/code&gt;. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; The namespace of an npm package version is its &lt;code&gt;scope&lt;/code&gt;. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; Python and NuGet package versions do not contain a corresponding component, package versions of those formats do not have a namespace. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; The namespace of a generic package is its &lt;code&gt;namespace&lt;/code&gt;. &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;
    :type namespace: str
    :param max_results:  The maximum number of results to return per page. 
    :type max_results: int
    :param next_token:  The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results. 
    :type next_token: str
    :param max_results2: Pagination limit
    :type max_results2: str
    :param next_token2: Pagination token
    :type next_token2: str

    """
    return web.Response(status=200)


async def list_package_version_dependencies(request: web.Request, domain, repository, format, package, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, domain_owner=None, namespace=None, next_token=None) -> web.Response:
    """list_package_version_dependencies

     Returns the direct dependencies for a package version. The dependencies are returned as &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_PackageDependency.html\&quot;&gt;PackageDependency&lt;/a&gt; objects. CodeArtifact extracts the dependencies for a package version from the metadata file for the package format (for example, the &lt;code&gt;package.json&lt;/code&gt; file for npm packages and the &lt;code&gt;pom.xml&lt;/code&gt; file for Maven). Any package version dependencies that are not listed in the configuration file are not returned. 

    :param domain:  The name of the domain that contains the repository that contains the requested package version dependencies. 
    :type domain: str
    :param repository:  The name of the repository that contains the requested package version. 
    :type repository: str
    :param format:  The format of the package with the requested dependencies. 
    :type format: str
    :param package:  The name of the package versions&#39; package. 
    :type package: str
    :param version:  A string that contains the package version (for example, &lt;code&gt;3.5.2&lt;/code&gt;). 
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
    :param domain_owner:  The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces. 
    :type domain_owner: str
    :param namespace: &lt;p&gt;The namespace of the package version with the requested dependencies. The package version component that specifies its namespace depends on its type. For example:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; The namespace of a Maven package version is its &lt;code&gt;groupId&lt;/code&gt;. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; The namespace of an npm package version is its &lt;code&gt;scope&lt;/code&gt;. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; Python and NuGet package versions do not contain a corresponding component, package versions of those formats do not have a namespace. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; The namespace of a generic package is its &lt;code&gt;namespace&lt;/code&gt;. &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;
    :type namespace: str
    :param next_token:  The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results. 
    :type next_token: str

    """
    return web.Response(status=200)


async def list_package_versions(request: web.Request, domain, repository, format, package, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, domain_owner=None, namespace=None, status=None, sort_by=None, max_results=None, next_token=None, origin_type=None, max_results2=None, next_token2=None) -> web.Response:
    """list_package_versions

     Returns a list of &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_PackageVersionSummary.html\&quot;&gt;PackageVersionSummary&lt;/a&gt; objects for package versions in a repository that match the request parameters. Package versions of all statuses will be returned by default when calling &lt;code&gt;list-package-versions&lt;/code&gt; with no &lt;code&gt;--status&lt;/code&gt; parameter. 

    :param domain:  The name of the domain that contains the repository that contains the requested package versions. 
    :type domain: str
    :param repository:  The name of the repository that contains the requested package versions. 
    :type repository: str
    :param format:  The format of the package versions you want to list. 
    :type format: str
    :param package:  The name of the package for which you want to request package versions. 
    :type package: str
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
    :param domain_owner:  The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces. 
    :type domain_owner: str
    :param namespace: &lt;p&gt;The namespace of the package that contains the requested package versions. The package component that specifies its namespace depends on its type. For example:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; The namespace of a Maven package is its &lt;code&gt;groupId&lt;/code&gt;. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; The namespace of an npm package is its &lt;code&gt;scope&lt;/code&gt;. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; Python and NuGet packages do not contain a corresponding component, packages of those formats do not have a namespace. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; The namespace of a generic package is its &lt;code&gt;namespace&lt;/code&gt;. &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;
    :type namespace: str
    :param status:  A string that filters the requested package versions by status. 
    :type status: str
    :param sort_by:  How to sort the requested list of package versions. 
    :type sort_by: str
    :param max_results:  The maximum number of results to return per page. 
    :type max_results: int
    :param next_token:  The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results. 
    :type next_token: str
    :param origin_type: The &lt;code&gt;originType&lt;/code&gt; used to filter package versions. Only package versions with the provided &lt;code&gt;originType&lt;/code&gt; will be returned.
    :type origin_type: str
    :param max_results2: Pagination limit
    :type max_results2: str
    :param next_token2: Pagination token
    :type next_token2: str

    """
    return web.Response(status=200)


async def list_packages(request: web.Request, domain, repository, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, domain_owner=None, format=None, namespace=None, package_prefix=None, max_results=None, next_token=None, publish=None, upstream=None, max_results2=None, next_token2=None) -> web.Response:
    """list_packages

     Returns a list of &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_PackageSummary.html\&quot;&gt;PackageSummary&lt;/a&gt; objects for packages in a repository that match the request parameters. 

    :param domain:  The name of the domain that contains the repository that contains the requested packages. 
    :type domain: str
    :param repository:  The name of the repository that contains the requested packages. 
    :type repository: str
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
    :param domain_owner:  The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces. 
    :type domain_owner: str
    :param format: The format used to filter requested packages. Only packages from the provided format will be returned.
    :type format: str
    :param namespace: &lt;p&gt;The namespace prefix used to filter requested packages. Only packages with a namespace that starts with the provided string value are returned. Note that although this option is called &lt;code&gt;--namespace&lt;/code&gt; and not &lt;code&gt;--namespace-prefix&lt;/code&gt;, it has prefix-matching behavior.&lt;/p&gt; &lt;p&gt;Each package format uses namespace as follows:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; The namespace of a Maven package is its &lt;code&gt;groupId&lt;/code&gt;. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; The namespace of an npm package is its &lt;code&gt;scope&lt;/code&gt;. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; Python and NuGet packages do not contain a corresponding component, packages of those formats do not have a namespace. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; The namespace of a generic package is its &lt;code&gt;namespace&lt;/code&gt;. &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;
    :type namespace: str
    :param package_prefix:  A prefix used to filter requested packages. Only packages with names that start with &lt;code&gt;packagePrefix&lt;/code&gt; are returned. 
    :type package_prefix: str
    :param max_results:  The maximum number of results to return per page. 
    :type max_results: int
    :param next_token:  The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results. 
    :type next_token: str
    :param publish: The value of the &lt;code&gt;Publish&lt;/code&gt; package origin control restriction used to filter requested packages. Only packages with the provided restriction are returned. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_PackageOriginRestrictions.html\&quot;&gt;PackageOriginRestrictions&lt;/a&gt;.
    :type publish: str
    :param upstream: The value of the &lt;code&gt;Upstream&lt;/code&gt; package origin control restriction used to filter requested packages. Only packages with the provided restriction are returned. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_PackageOriginRestrictions.html\&quot;&gt;PackageOriginRestrictions&lt;/a&gt;.
    :type upstream: str
    :param max_results2: Pagination limit
    :type max_results2: str
    :param next_token2: Pagination token
    :type next_token2: str

    """
    return web.Response(status=200)


async def list_repositories(request: web.Request, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, repository_prefix=None, max_results=None, next_token=None, max_results2=None, next_token2=None) -> web.Response:
    """list_repositories

     Returns a list of &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_RepositorySummary.html\&quot;&gt;RepositorySummary&lt;/a&gt; objects. Each &lt;code&gt;RepositorySummary&lt;/code&gt; contains information about a repository in the specified Amazon Web Services account and that matches the input parameters. 

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
    :param repository_prefix:  A prefix used to filter returned repositories. Only repositories with names that start with &lt;code&gt;repositoryPrefix&lt;/code&gt; are returned.
    :type repository_prefix: str
    :param max_results:  The maximum number of results to return per page. 
    :type max_results: int
    :param next_token:  The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results. 
    :type next_token: str
    :param max_results2: Pagination limit
    :type max_results2: str
    :param next_token2: Pagination token
    :type next_token2: str

    """
    return web.Response(status=200)


async def list_repositories_in_domain(request: web.Request, domain, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, domain_owner=None, administrator_account=None, repository_prefix=None, max_results=None, next_token=None, max_results2=None, next_token2=None) -> web.Response:
    """list_repositories_in_domain

     Returns a list of &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_RepositorySummary.html\&quot;&gt;RepositorySummary&lt;/a&gt; objects. Each &lt;code&gt;RepositorySummary&lt;/code&gt; contains information about a repository in the specified domain and that matches the input parameters. 

    :param domain:  The name of the domain that contains the returned list of repositories. 
    :type domain: str
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
    :param domain_owner:  The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces. 
    :type domain_owner: str
    :param administrator_account:  Filter the list of repositories to only include those that are managed by the Amazon Web Services account ID. 
    :type administrator_account: str
    :param repository_prefix:  A prefix used to filter returned repositories. Only repositories with names that start with &lt;code&gt;repositoryPrefix&lt;/code&gt; are returned. 
    :type repository_prefix: str
    :param max_results:  The maximum number of results to return per page. 
    :type max_results: int
    :param next_token:  The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results. 
    :type next_token: str
    :param max_results2: Pagination limit
    :type max_results2: str
    :param next_token2: Pagination token
    :type next_token2: str

    """
    return web.Response(status=200)


async def list_tags_for_resource(request: web.Request, resource_arn, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """list_tags_for_resource

    Gets information about Amazon Web Services tags for a specified Amazon Resource Name (ARN) in CodeArtifact.

    :param resource_arn: The Amazon Resource Name (ARN) of the resource to get tags for.
    :type resource_arn: str
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


async def publish_package_version(request: web.Request, domain, repository, format, package, version, asset, x_amz_content_sha257, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, domain_owner=None, namespace=None, unfinished=None) -> web.Response:
    """publish_package_version

    &lt;p&gt;Creates a new package version containing one or more assets (or files).&lt;/p&gt; &lt;p&gt;The &lt;code&gt;unfinished&lt;/code&gt; flag can be used to keep the package version in the &lt;code&gt;Unfinished&lt;/code&gt; state until all of its assets have been uploaded (see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/codeartifact/latest/ug/packages-overview.html#package-version-status.html#package-version-status\&quot;&gt;Package version status&lt;/a&gt; in the &lt;i&gt;CodeArtifact user guide&lt;/i&gt;). To set the package version’s status to &lt;code&gt;Published&lt;/code&gt;, omit the &lt;code&gt;unfinished&lt;/code&gt; flag when uploading the final asset, or set the status using &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_UpdatePackageVersionsStatus.html\&quot;&gt;UpdatePackageVersionStatus&lt;/a&gt;. Once a package version’s status is set to &lt;code&gt;Published&lt;/code&gt;, it cannot change back to &lt;code&gt;Unfinished&lt;/code&gt;.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Only generic packages can be published using this API. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/codeartifact/latest/ug/using-generic.html\&quot;&gt;Using generic packages&lt;/a&gt; in the &lt;i&gt;CodeArtifact User Guide&lt;/i&gt;.&lt;/p&gt; &lt;/note&gt;

    :param domain: The name of the domain that contains the repository that contains the package version to publish.
    :type domain: str
    :param repository: The name of the repository that the package version will be published to.
    :type repository: str
    :param format: &lt;p&gt;A format that specifies the type of the package version with the requested asset file.&lt;/p&gt; &lt;p&gt;The only supported value is &lt;code&gt;generic&lt;/code&gt;.&lt;/p&gt;
    :type format: str
    :param package: The name of the package version to publish.
    :type package: str
    :param version: The package version to publish (for example, &lt;code&gt;3.5.2&lt;/code&gt;).
    :type version: str
    :param asset: The name of the asset to publish. Asset names can include Unicode letters and numbers, and the following special characters: &lt;code&gt;~ ! @ ^ &amp;amp; ( ) - &#x60; _ + [ ] { } ; , . &#x60;&lt;/code&gt; 
    :type asset: str
    :param x_amz_content_sha257: &lt;p&gt;The SHA256 hash of the &lt;code&gt;assetContent&lt;/code&gt; to publish. This value must be calculated by the caller and provided with the request (see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/codeartifact/latest/ug/using-generic.html#publishing-generic-packages\&quot;&gt;Publishing a generic package&lt;/a&gt; in the &lt;i&gt;CodeArtifact User Guide&lt;/i&gt;).&lt;/p&gt; &lt;p&gt;This value is used as an integrity check to verify that the &lt;code&gt;assetContent&lt;/code&gt; has not changed after it was originally sent.&lt;/p&gt;
    :type x_amz_content_sha257: str
    :param body: 
    :type body: dict | bytes
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
    :param domain_owner: The 12-digit account number of the AWS account that owns the domain. It does not include dashes or spaces.
    :type domain_owner: str
    :param namespace: The namespace of the package version to publish.
    :type namespace: str
    :param unfinished: &lt;p&gt;Specifies whether the package version should remain in the &lt;code&gt;unfinished&lt;/code&gt; state. If omitted, the package version status will be set to &lt;code&gt;Published&lt;/code&gt; (see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/codeartifact/latest/ug/packages-overview.html#package-version-status\&quot;&gt;Package version status&lt;/a&gt; in the &lt;i&gt;CodeArtifact User Guide&lt;/i&gt;).&lt;/p&gt; &lt;p&gt;Valid values: &lt;code&gt;unfinished&lt;/code&gt; &lt;/p&gt;
    :type unfinished: bool

    """
    body = PublishPackageVersionRequest.from_dict(body)
    return web.Response(status=200)


async def put_domain_permissions_policy(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """put_domain_permissions_policy

    &lt;p&gt; Sets a resource policy on a domain that specifies permissions to access it. &lt;/p&gt; &lt;p&gt; When you call &lt;code&gt;PutDomainPermissionsPolicy&lt;/code&gt;, the resource policy on the domain is ignored when evaluting permissions. This ensures that the owner of a domain cannot lock themselves out of the domain, which would prevent them from being able to update the resource policy. &lt;/p&gt;

    :param body: 
    :type body: dict | bytes
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
    body = PutDomainPermissionsPolicyRequest.from_dict(body)
    return web.Response(status=200)


async def put_package_origin_configuration(request: web.Request, domain, repository, format, package, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, domain_owner=None, namespace=None) -> web.Response:
    """put_package_origin_configuration

    &lt;p&gt;Sets the package origin configuration for a package.&lt;/p&gt; &lt;p&gt;The package origin configuration determines how new versions of a package can be added to a repository. You can allow or block direct publishing of new package versions, or ingestion and retaining of new package versions from an external connection or upstream source. For more information about package origin controls and configuration, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/codeartifact/latest/ug/package-origin-controls.html\&quot;&gt;Editing package origin controls&lt;/a&gt; in the &lt;i&gt;CodeArtifact User Guide&lt;/i&gt;.&lt;/p&gt; &lt;p&gt; &lt;code&gt;PutPackageOriginConfiguration&lt;/code&gt; can be called on a package that doesn&#39;t yet exist in the repository. When called on a package that does not exist, a package is created in the repository with no versions and the requested restrictions are set on the package. This can be used to preemptively block ingesting or retaining any versions from external connections or upstream repositories, or to block publishing any versions of the package into the repository before connecting any package managers or publishers to the repository.&lt;/p&gt;

    :param domain: The name of the domain that contains the repository that contains the package.
    :type domain: str
    :param repository: The name of the repository that contains the package.
    :type repository: str
    :param format: A format that specifies the type of the package to be updated.
    :type format: str
    :param package: The name of the package to be updated.
    :type package: str
    :param body: 
    :type body: dict | bytes
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
    :param domain_owner:  The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces. 
    :type domain_owner: str
    :param namespace: &lt;p&gt;The namespace of the package to be updated. The package component that specifies its namespace depends on its type. For example:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; The namespace of a Maven package is its &lt;code&gt;groupId&lt;/code&gt;. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; The namespace of an npm package is its &lt;code&gt;scope&lt;/code&gt;. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; Python and NuGet packages do not contain a corresponding component, packages of those formats do not have a namespace. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; The namespace of a generic package is its &lt;code&gt;namespace&lt;/code&gt;. &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;
    :type namespace: str

    """
    body = PutPackageOriginConfigurationRequest.from_dict(body)
    return web.Response(status=200)


async def put_repository_permissions_policy(request: web.Request, domain, repository, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, domain_owner=None) -> web.Response:
    """put_repository_permissions_policy

    &lt;p&gt; Sets the resource policy on a repository that specifies permissions to access it. &lt;/p&gt; &lt;p&gt; When you call &lt;code&gt;PutRepositoryPermissionsPolicy&lt;/code&gt;, the resource policy on the repository is ignored when evaluting permissions. This ensures that the owner of a repository cannot lock themselves out of the repository, which would prevent them from being able to update the resource policy. &lt;/p&gt;

    :param domain:  The name of the domain containing the repository to set the resource policy on. 
    :type domain: str
    :param repository:  The name of the repository to set the resource policy on. 
    :type repository: str
    :param body: 
    :type body: dict | bytes
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
    :param domain_owner:  The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces. 
    :type domain_owner: str

    """
    body = PutRepositoryPermissionsPolicyRequest.from_dict(body)
    return web.Response(status=200)


async def tag_resource(request: web.Request, resource_arn, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """tag_resource

    Adds or updates tags for a resource in CodeArtifact.

    :param resource_arn: The Amazon Resource Name (ARN) of the resource that you want to add or update tags for.
    :type resource_arn: str
    :param body: 
    :type body: dict | bytes
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
    body = TagResourceRequest.from_dict(body)
    return web.Response(status=200)


async def untag_resource(request: web.Request, resource_arn, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """untag_resource

    Removes tags from a resource in CodeArtifact.

    :param resource_arn: The Amazon Resource Name (ARN) of the resource that you want to remove tags from.
    :type resource_arn: str
    :param body: 
    :type body: dict | bytes
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
    body = UntagResourceRequest.from_dict(body)
    return web.Response(status=200)


async def update_package_versions_status(request: web.Request, domain, repository, format, package, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, domain_owner=None, namespace=None) -> web.Response:
    """update_package_versions_status

     Updates the status of one or more versions of a package. Using &lt;code&gt;UpdatePackageVersionsStatus&lt;/code&gt;, you can update the status of package versions to &lt;code&gt;Archived&lt;/code&gt;, &lt;code&gt;Published&lt;/code&gt;, or &lt;code&gt;Unlisted&lt;/code&gt;. To set the status of a package version to &lt;code&gt;Disposed&lt;/code&gt;, use &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_DisposePackageVersions.html\&quot;&gt;DisposePackageVersions&lt;/a&gt;. 

    :param domain:  The name of the domain that contains the repository that contains the package versions with a status to be updated. 
    :type domain: str
    :param repository:  The repository that contains the package versions with the status you want to update. 
    :type repository: str
    :param format:  A format that specifies the type of the package with the statuses to update. 
    :type format: str
    :param package:  The name of the package with the version statuses to update. 
    :type package: str
    :param body: 
    :type body: dict | bytes
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
    :param domain_owner:  The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces. 
    :type domain_owner: str
    :param namespace: &lt;p&gt;The namespace of the package version to be updated. The package version component that specifies its namespace depends on its type. For example:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; The namespace of a Maven package version is its &lt;code&gt;groupId&lt;/code&gt;. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; The namespace of an npm package version is its &lt;code&gt;scope&lt;/code&gt;. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; Python and NuGet package versions do not contain a corresponding component, package versions of those formats do not have a namespace. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; The namespace of a generic package is its &lt;code&gt;namespace&lt;/code&gt;. &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;
    :type namespace: str

    """
    body = UpdatePackageVersionsStatusRequest.from_dict(body)
    return web.Response(status=200)


async def update_repository(request: web.Request, domain, repository, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, domain_owner=None) -> web.Response:
    """update_repository

     Update the properties of a repository. 

    :param domain:  The name of the domain associated with the repository to update. 
    :type domain: str
    :param repository:  The name of the repository to update. 
    :type repository: str
    :param body: 
    :type body: dict | bytes
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
    :param domain_owner:  The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces. 
    :type domain_owner: str

    """
    body = UpdateRepositoryRequest.from_dict(body)
    return web.Response(status=200)
