from typing import List, Dict
from aiohttp import web

from openapi_server.models.cluster import Cluster
from openapi_server.models.cluster_create import ClusterCreate
from openapi_server.models.cluster_result import ClusterResult
from openapi_server.models.error import Error
from openapi_server.models.instance import Instance
from openapi_server.models.instance_result import InstanceResult
from openapi_server.models.multi_cluster_result import MultiClusterResult
from openapi_server import util


async def cluster_cluster_key_delete(request: web.Request, cluster_key, checksum) -> web.Response:
    """delete cluster

    Delete an existing cluster

    :param cluster_key: the cluster key
    :type cluster_key: str
    :param checksum: the current checksum of the cluster to be deleted
    :type checksum: str

    """
    return web.Response(status=200)


async def cluster_cluster_key_get(request: web.Request, cluster_key) -> web.Response:
    """get cluster

    Get details for an existing cluster

    :param cluster_key: the cluster key
    :type cluster_key: str

    """
    return web.Response(status=200)


async def cluster_cluster_key_instances_instance_identifier_delete(request: web.Request, checksum, cluster_key, instance_identifier) -> web.Response:
    """remove instance

    Remove an instance from a cluster

    :param checksum: the current checksum of the instance to be deleted
    :type checksum: str
    :param cluster_key: the cluster to remove an instance from
    :type cluster_key: str
    :param instance_identifier: the instance to remove, identified as &lt;host&gt;:&lt;port&gt;
    :type instance_identifier: str

    """
    return web.Response(status=200)


async def cluster_cluster_key_instances_post(request: web.Request, cluster_key, instance) -> web.Response:
    """add instance

    Add a new instance to a cluster

    :param cluster_key: the cluster to add the instance to
    :type cluster_key: str
    :param instance: the instance to add
    :type instance: dict | bytes

    """
    instance = Instance.from_dict(instance)
    return web.Response(status=200)


async def cluster_cluster_key_put(request: web.Request, cluster_key, cluster) -> web.Response:
    """modify cluster

    Modify an existing cluster

    :param cluster_key: the cluster key
    :type cluster_key: str
    :param cluster: the cluster to modify
    :type cluster: dict | bytes

    """
    cluster = Cluster.from_dict(cluster)
    return web.Response(status=200)


async def cluster_get(request: web.Request, filters=None) -> web.Response:
    """get clusters

    Get a list of clusters

    :param filters: A JSON encoded array of ClusterFilter objects. The filter is taken as a union of intersections. In other words an object that matches every constraint in any ClusterFilter will be included. 
    :type filters: str

    """
    return web.Response(status=200)


async def cluster_post(request: web.Request, cluster) -> web.Response:
    """create cluster

    Create a new cluster

    :param cluster: the cluster to create
    :type cluster: dict | bytes

    """
    cluster = ClusterCreate.from_dict(cluster)
    return web.Response(status=200)
