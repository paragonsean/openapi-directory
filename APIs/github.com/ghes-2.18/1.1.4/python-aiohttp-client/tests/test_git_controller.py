# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.basic_error import BasicError
from openapi_server.models.blob import Blob
from openapi_server.models.git_commit import GitCommit
from openapi_server.models.git_create_blob_request import GitCreateBlobRequest
from openapi_server.models.git_create_commit_request import GitCreateCommitRequest
from openapi_server.models.git_create_ref_request import GitCreateRefRequest
from openapi_server.models.git_create_tag_request import GitCreateTagRequest
from openapi_server.models.git_create_tree_request import GitCreateTreeRequest
from openapi_server.models.git_ref import GitRef
from openapi_server.models.git_tag import GitTag
from openapi_server.models.git_tree import GitTree
from openapi_server.models.git_update_ref_request import GitUpdateRefRequest
from openapi_server.models.short_blob import ShortBlob
from openapi_server.models.validation_error import ValidationError


pytestmark = pytest.mark.asyncio

async def test_git_create_blob(client):
    """Test case for git_create_blob

    Create a blob
    """
    body = {"content":"Content of the blob","encoding":"utf-8"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/repos/{owner}/{repo}/git/blobs'.format(owner='owner_example', repo='repo_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_git_create_commit(client):
    """Test case for git_create_commit

    Create a commit
    """
    body = {"author":{"date":"2008-07-09T16:13:30+12:00","email":"octocat@github.com","name":"Mona Octocat"},"message":"my commit message","parents":["7d1b31e74ee336d15cbd21741bc88a537ed063a0"],"signature":"-----BEGIN PGP SIGNATURE-----\n\niQIzBAABAQAdFiEESn/54jMNIrGSE6Tp6cQjvhfv7nAFAlnT71cACgkQ6cQjvhfv\n7nCWwA//XVqBKWO0zF+bZl6pggvky3Oc2j1pNFuRWZ29LXpNuD5WUGXGG209B0hI\nDkmcGk19ZKUTnEUJV2Xd0R7AW01S/YSub7OYcgBkI7qUE13FVHN5ln1KvH2all2n\n2+JCV1HcJLEoTjqIFZSSu/sMdhkLQ9/NsmMAzpf/iIM0nQOyU4YRex9eD1bYj6nA\nOQPIDdAuaTQj1gFPHYLzM4zJnCqGdRlg0sOM/zC5apBNzIwlgREatOYQSCfCKV7k\nnrU34X8b9BzQaUx48Qa+Dmfn5KQ8dl27RNeWAqlkuWyv3pUauH9UeYW+KyuJeMkU\n+NyHgAsWFaCFl23kCHThbLStMZOYEnGagrd0hnm1TPS4GJkV4wfYMwnI4KuSlHKB\njHl3Js9vNzEUQipQJbgCgTiWvRJoK3ENwBTMVkKHaqT4x9U4Jk/XZB6Q8MA09ezJ\n3QgiTjTAGcum9E9QiJqMYdWQPWkaBIRRz5cET6HPB48YNXAAUsfmuYsGrnVLYbG+\nUpC6I97VybYHTy2O9XSGoaLeMI9CsFn38ycAxxbWagk5mhclNTP5mezIq6wKSwmr\nX11FW3n1J23fWZn5HJMBsRnUCgzqzX3871IqLYHqRJ/bpZ4h20RhTyPj5c/z7QXp\neSakNQMfbbMcljkha+ZMuVQX1K9aRlVqbmv3ZMWh+OijLYVU2bc=\n=5Io4\n-----END PGP SIGNATURE-----\n","tree":"827efc6d56897b048c772eb4087f854f46256132"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/repos/{owner}/{repo}/git/commits'.format(owner='owner_example', repo='repo_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_git_create_ref(client):
    """Test case for git_create_ref

    Create a reference
    """
    body = {"ref":"refs/heads/featureA","sha":"aa218f56b14c9653891f9e74264a383fa43fefbd"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/repos/{owner}/{repo}/git/refs'.format(owner='owner_example', repo='repo_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_git_create_tag(client):
    """Test case for git_create_tag

    Create a tag object
    """
    body = {"message":"initial version","object":"c3d0be41ecbe669545ee3e94d31ed9a4bc91ee3c","tag":"v0.0.1","tagger":{"date":"2011-06-17T14:53:35-07:00","email":"octocat@github.com","name":"Monalisa Octocat"},"type":"commit"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/repos/{owner}/{repo}/git/tags'.format(owner='owner_example', repo='repo_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_git_create_tree(client):
    """Test case for git_create_tree

    Create a tree
    """
    body = {"base_tree":"9fb037999f264ba9a7fc6274d15fa3ae2ab98312","tree":[{"mode":"100644","path":"file.rb","sha":"44b4fc6d56897b048c772eb4087f854f46256132","type":"blob"}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/repos/{owner}/{repo}/git/trees'.format(owner='owner_example', repo='repo_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_git_delete_ref(client):
    """Test case for git_delete_ref

    Delete a reference
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v3/repos/{owner}/{repo}/git/refs/{ref}'.format(owner='owner_example', repo='repo_example', ref='ref_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_git_get_all_refs(client):
    """Test case for git_get_all_refs

    Get all references
    """
    params = [('per_page', 30),
                    ('page', 1)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/repos/{owner}/{repo}/git/refs/{namespace}'.format(owner='owner_example', repo='repo_example', namespace='namespace_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_git_get_blob(client):
    """Test case for git_get_blob

    Get a blob
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/repos/{owner}/{repo}/git/blobs/{file_sha}'.format(owner='owner_example', repo='repo_example', file_sha='file_sha_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_git_get_commit(client):
    """Test case for git_get_commit

    Get a commit
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/repos/{owner}/{repo}/git/commits/{commit_sha}'.format(owner='owner_example', repo='repo_example', commit_sha='commit_sha_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_git_get_tag(client):
    """Test case for git_get_tag

    Get a tag
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/repos/{owner}/{repo}/git/tags/{tag_sha}'.format(owner='owner_example', repo='repo_example', tag_sha='tag_sha_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_git_get_tree(client):
    """Test case for git_get_tree

    Get a tree
    """
    params = [('recursive', 'recursive_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/repos/{owner}/{repo}/git/trees/{tree_sha}'.format(owner='owner_example', repo='repo_example', tree_sha='tree_sha_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_git_update_ref(client):
    """Test case for git_update_ref

    Update a reference
    """
    body = {"force":true,"sha":"aa218f56b14c9653891f9e74264a383fa43fefbd"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v3/repos/{owner}/{repo}/git/refs/{ref}'.format(owner='owner_example', repo='repo_example', ref='ref_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

