from typing import List, Dict
from aiohttp import web

from openapi_server.models.test_composer_json_composer_lock_file_request import TestComposerJsonComposerLockFileRequest
from openapi_server.models.test_dep_graph_request import TestDepGraphRequest
from openapi_server.models.test_gemfile_lock_file_request import TestGemfileLockFileRequest
from openapi_server.models.test_gopkg_toml_gopkg_lock_file_request import TestGopkgTomlGopkgLockFileRequest
from openapi_server.models.test_gradle_file_request import TestGradleFileRequest
from openapi_server.models.test_maven_file_request import TestMavenFileRequest
from openapi_server.models.test_package_json_package_lock_json_file_request import TestPackageJsonPackageLockJsonFileRequest
from openapi_server.models.test_package_json_yarn_lock_file_request import TestPackageJsonYarnLockFileRequest
from openapi_server.models.test_requirements_txt_file_request import TestRequirementsTxtFileRequest
from openapi_server.models.test_sbt_file_request import TestSbtFileRequest
from openapi_server.models.test_vendor_json_file_request import TestVendorJsonFileRequest
from openapi_server import util


async def test_composer_json_composer_lock_file(request: web.Request, body=None) -> web.Response:
    """Test composer.json &amp; composer.lock file

    You can test your Composer packages for issues according to their manifest file &amp; lockfile using this action. It takes a JSON object containing a \&quot;target\&quot; &#x60;composer.json&#x60; and a &#x60;composer.lock&#x60;.

    :param body: 
    :type body: dict | bytes

    """
    body = TestComposerJsonComposerLockFileRequest.from_dict(body)
    return web.Response(status=200)


async def test_dep_graph(request: web.Request, org=None, body=None) -> web.Response:
    """Test Dep Graph

    Use this endpoint to find issues in a [DepGraph data object](https://github.com/snyk/dep-graph#depgraphdata).

    :param org: The organization to test the package with. See \&quot;The Snyk organization for a request\&quot; above.
    :type org: str
    :param body: 
    :type body: dict | bytes

    """
    body = TestDepGraphRequest.from_dict(body)
    return web.Response(status=200)


async def test_for_issues_in_a_public_gem_by_name_and_version(request: web.Request, gem_name, version, org=None) -> web.Response:
    """Test for issues in a public gem by name and version

    You can test &#x60;rubygems&#x60; packages for issues according to their name and version.

    :param gem_name: The gem name.
    :type gem_name: str
    :param version: The gem version to test.
    :type version: str
    :param org: The organization to test the package with. See \&quot;The Snyk organization for a request\&quot; above.
    :type org: str

    """
    return web.Response(status=200)


async def test_for_issues_in_a_public_package_by_group_id_artifact_id_and_version(request: web.Request, group_id, artifact_id, version, org=None, repository=None) -> web.Response:
    """Test for issues in a public package by group id, artifact id and version

    You can test &#x60;maven&#x60; packages for issues according to their [coordinates](https://maven.apache.org/pom.html#Maven_Coordinates): group ID, artifact ID and version. The repository hosting the package may also be customized (see the &#x60;repository&#x60; query parameter).

    :param group_id: The package&#39;s group ID.
    :type group_id: str
    :param artifact_id: The package&#39;s artifact ID.
    :type artifact_id: str
    :param version: The package version to test.
    :type version: str
    :param org: The organization to test the package with. See \&quot;The Snyk organization for a request\&quot; above.
    :type org: str
    :param repository: The Maven repository hosting this package. The default value is Maven Central. More than one value is supported, in order.
    :type repository: str

    """
    return web.Response(status=200)


async def test_for_issues_in_a_public_package_by_group_name_and_version(request: web.Request, group, name, version, org=None, repository=None) -> web.Response:
    """Test for issues in a public package by group, name and version

    You can test &#x60;gradle&#x60; packages for issues according to their group, name and version. This is done via the maven endpoint (for Java), since the packages are hosted on maven central or a compatible repository. See \&quot;Maven\&quot; above for details.

    :param group: The package&#39;s group ID.
    :type group: str
    :param name: The package&#39;s artifact ID.
    :type name: str
    :param version: The package version to test.
    :type version: str
    :param org: The organization to test the package with. See \&quot;The Snyk organization for a request\&quot; above.
    :type org: str
    :param repository: The repository hosting this package. The default value is Maven Central. More than one value is supported, in order.
    :type repository: str

    """
    return web.Response(status=200)


async def test_for_issues_in_a_public_package_by_name_and_version(request: web.Request, package_name, version, org=None) -> web.Response:
    """Test for issues in a public package by name and version

    You can test &#x60;npm&#x60; packages for issues according to their name and version.

    :param package_name: The package name. For scoped packages, **must** be url-encoded, so to test \&quot;@angular/core\&quot; version 4.3.2, one should &#x60;GET /test/npm/%40angular%2Fcore/4.3.2&#x60;.
    :type package_name: str
    :param version: The Package version to test.
    :type version: str
    :param org: The organization to test the package with. See \&quot;The Snyk organization for a request\&quot; above.
    :type org: str

    """
    return web.Response(status=200)


async def test_gemfile_lock_file(request: web.Request, body=None) -> web.Response:
    """Test gemfile.lock file

    You can test your rubygems applications for issues according to their lockfile using this action. It takes a JSON object containing a the \&quot;target\&quot; &#x60;Gemfile.lock&#x60;.

    :param body: 
    :type body: dict | bytes

    """
    body = TestGemfileLockFileRequest.from_dict(body)
    return web.Response(status=200)


async def test_gopkg_toml_gopkg_lock_file(request: web.Request, org=None, body=None) -> web.Response:
    """Test Gopkg.toml &amp; Gopkg.lock File

    You can test your Go dep packages for issues according to their manifest file &amp; lockfile using this action. It takes a JSON object containing a \&quot;target\&quot; &#x60;Gopkg.toml&#x60; and a &#x60;Gopkg.lock&#x60;.

    :param org: The organization to test the package with. See \&quot;The Snyk organization for a request\&quot; above.
    :type org: str
    :param body: 
    :type body: dict | bytes

    """
    body = TestGopkgTomlGopkgLockFileRequest.from_dict(body)
    return web.Response(status=200)


async def test_gradle_file(request: web.Request, body=None) -> web.Response:
    """Test gradle file

    You can test your Gradle packages for issues according to their manifest file using this action. It takes a JSON object containing the \&quot;target\&quot; &#x60;build.gradle&#x60;.

    :param body: 
    :type body: dict | bytes

    """
    body = TestGradleFileRequest.from_dict(body)
    return web.Response(status=200)


async def test_maven_file(request: web.Request, org=None, repository=None, body=None) -> web.Response:
    """Test maven file

    You can test your Maven packages for issues according to their manifest file using this action. It takes a JSON object containing a the \&quot;target\&quot; &#x60;pom.xml&#x60;.  Additional manifest files, if they are needed, like parent &#x60;pom.xml&#x60; files, child poms, etc., according the the definitions in the target &#x60;pom.xml&#x60; file, should be supplied in the &#x60;additional&#x60; body parameter.

    :param org: The organization to test the package with. See \&quot;The Snyk organization for a request\&quot; above.
    :type org: str
    :param repository: The Maven repository hosting this package. The default value is Maven Central. More than one value is supported, in order.
    :type repository: str
    :param body: 
    :type body: dict | bytes

    """
    body = TestMavenFileRequest.from_dict(body)
    return web.Response(status=200)


async def test_package_json_package_lock_json_file(request: web.Request, body=None) -> web.Response:
    """Test package.json &amp; package-lock.json File

    You can test your npm packages for issues according to their manifest file &amp; optional lockfile using this action. It takes a JSON object containing a \&quot;target\&quot; &#x60;package.json&#x60; and optionally a &#x60;package-lock.json&#x60;.

    :param body: 
    :type body: dict | bytes

    """
    body = TestPackageJsonPackageLockJsonFileRequest.from_dict(body)
    return web.Response(status=200)


async def test_package_json_yarn_lock_file(request: web.Request, body=None) -> web.Response:
    """Test package.json &amp; yarn.lock File

    You can test your yarn packages for issues according to their manifest file &amp; lockfile using this action. It takes a JSON object containing a \&quot;target\&quot; &#x60;package.json&#x60; and a &#x60;yarn.lock&#x60;.

    :param body: 
    :type body: dict | bytes

    """
    body = TestPackageJsonYarnLockFileRequest.from_dict(body)
    return web.Response(status=200)


async def test_pip_package_name_version_get(request: web.Request, package_name, version, org=None) -> web.Response:
    """Test for issues in a public package by name and version

    You can test &#x60;pip&#x60; packages for issues according to their name and version.

    :param package_name: The package name.
    :type package_name: str
    :param version: The Package version to test.
    :type version: str
    :param org: The organization to test the package with. See \&quot;The Snyk organization for a request\&quot; above.
    :type org: str

    """
    return web.Response(status=200)


async def test_requirements_txt_file(request: web.Request, body=None) -> web.Response:
    """Test requirements.txt file

    You can test your pip packages for issues according to their manifest file using this action. It takes a JSON object containing a the \&quot;target\&quot; &#x60;requirements.txt&#x60;.

    :param body: 
    :type body: dict | bytes

    """
    body = TestRequirementsTxtFileRequest.from_dict(body)
    return web.Response(status=200)


async def test_sbt_file(request: web.Request, body=None) -> web.Response:
    """Test sbt file

    You can test your &#x60;sbt&#x60; packages for issues according to their manifest file using this action. It takes a JSON object containing a the \&quot;target\&quot; &#x60;build.sbt&#x60;.

    :param body: 
    :type body: dict | bytes

    """
    body = TestSbtFileRequest.from_dict(body)
    return web.Response(status=200)


async def test_sbt_group_id_artifact_id_version_get(request: web.Request, group_id, artifact_id, version, org=None, repository=None) -> web.Response:
    """Test for issues in a public package by group id, artifact id and version

    You can test &#x60;sbt&#x60; packages for issues according to their group ID, artifact ID and version. This is done via the maven endpoint (for Java), since the packages are hosted on maven central or a compatible repository. See \&quot;Maven\&quot; above for details.

    :param group_id: The package&#39;s group ID.
    :type group_id: str
    :param artifact_id: The package&#39;s artifact ID.
    :type artifact_id: str
    :param version: The package version to test.
    :type version: str
    :param org: The organization to test the package with. See \&quot;The Snyk organization for a request\&quot; above.
    :type org: str
    :param repository: The repository hosting this package. The default value is Maven Central. More than one value is supported, in order.
    :type repository: str

    """
    return web.Response(status=200)


async def test_vendor_json_file(request: web.Request, body=None) -> web.Response:
    """Test vendor.json File

    You can test your Go vendor packages for issues according to their manifest file using this action. It takes a JSON object containing a \&quot;target\&quot; &#x60;vendor.json&#x60;.

    :param body: 
    :type body: dict | bytes

    """
    body = TestVendorJsonFileRequest.from_dict(body)
    return web.Response(status=200)
