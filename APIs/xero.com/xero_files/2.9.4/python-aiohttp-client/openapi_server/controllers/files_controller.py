from typing import List, Dict
from aiohttp import web

from openapi_server.models.association import Association
from openapi_server.models.file_object import FileObject
from openapi_server.models.files import Files
from openapi_server.models.folder import Folder
from openapi_server import util


async def create_file_association(request: web.Request, xero_tenant_id, file_id, body=None) -> web.Response:
    """Creates a new file association

    By passing in the appropriate options, you can create a new folder

    :param xero_tenant_id: Xero identifier for Tenant
    :type xero_tenant_id: str
    :param file_id: File id for single object
    :type file_id: str
    :type file_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = Association.from_dict(body)
    return web.Response(status=200)


async def create_folder(request: web.Request, xero_tenant_id, body=None) -> web.Response:
    """Creates a new folder

    By passing in the appropriate properties, you can create a new folder

    :param xero_tenant_id: Xero identifier for Tenant
    :type xero_tenant_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = Folder.from_dict(body)
    return web.Response(status=200)


async def delete_file(request: web.Request, xero_tenant_id, file_id) -> web.Response:
    """Deletes a specific file

    Delete a specific file

    :param xero_tenant_id: Xero identifier for Tenant
    :type xero_tenant_id: str
    :param file_id: File id for single object
    :type file_id: str
    :type file_id: str

    """
    return web.Response(status=200)


async def delete_file_association(request: web.Request, xero_tenant_id, file_id, object_id) -> web.Response:
    """Deletes an existing file association

    By passing in the appropriate options, you can create a new folder

    :param xero_tenant_id: Xero identifier for Tenant
    :type xero_tenant_id: str
    :param file_id: File id for single object
    :type file_id: str
    :type file_id: str
    :param object_id: Object id for single object
    :type object_id: str
    :type object_id: str

    """
    return web.Response(status=200)


async def delete_folder(request: web.Request, xero_tenant_id, folder_id) -> web.Response:
    """Deletes a folder

    By passing in the appropriate ID, you can delete a folder

    :param xero_tenant_id: Xero identifier for Tenant
    :type xero_tenant_id: str
    :param folder_id: Folder id for single object
    :type folder_id: str
    :type folder_id: str

    """
    return web.Response(status=200)


async def get_associations_by_object(request: web.Request, xero_tenant_id, object_id) -> web.Response:
    """Retrieves an association object using a unique object ID

    By passing in the appropriate options,

    :param xero_tenant_id: Xero identifier for Tenant
    :type xero_tenant_id: str
    :param object_id: Object id for single object
    :type object_id: str
    :type object_id: str

    """
    return web.Response(status=200)


async def get_file(request: web.Request, xero_tenant_id, file_id) -> web.Response:
    """Retrieves a file by a unique file ID

    

    :param xero_tenant_id: Xero identifier for Tenant
    :type xero_tenant_id: str
    :param file_id: File id for single object
    :type file_id: str
    :type file_id: str

    """
    return web.Response(status=200)


async def get_file_associations(request: web.Request, xero_tenant_id, file_id) -> web.Response:
    """Retrieves a specific file associations

    By passing in the appropriate options,  

    :param xero_tenant_id: Xero identifier for Tenant
    :type xero_tenant_id: str
    :param file_id: File id for single object
    :type file_id: str
    :type file_id: str

    """
    return web.Response(status=200)


async def get_file_content(request: web.Request, xero_tenant_id, file_id) -> web.Response:
    """Retrieves the content of a specific file

    By passing in the appropriate options, retrieve data for specific file

    :param xero_tenant_id: Xero identifier for Tenant
    :type xero_tenant_id: str
    :param file_id: File id for single object
    :type file_id: str
    :type file_id: str

    """
    return web.Response(status=200)


async def get_files(request: web.Request, xero_tenant_id, pagesize=None, page=None, sort=None) -> web.Response:
    """Retrieves files

    

    :param xero_tenant_id: Xero identifier for Tenant
    :type xero_tenant_id: str
    :param pagesize: pass an optional page size value
    :type pagesize: int
    :param page: number of records to skip for pagination
    :type page: int
    :param sort: values to sort by
    :type sort: str

    """
    return web.Response(status=200)


async def get_folder(request: web.Request, xero_tenant_id, folder_id) -> web.Response:
    """Retrieves specific folder by using a unique folder ID

    By passing in the appropriate ID, you can search for specific folder

    :param xero_tenant_id: Xero identifier for Tenant
    :type xero_tenant_id: str
    :param folder_id: Folder id for single object
    :type folder_id: str
    :type folder_id: str

    """
    return web.Response(status=200)


async def get_folders(request: web.Request, xero_tenant_id, sort=None) -> web.Response:
    """Retrieves folders

    By passing in the appropriate options, you can search for available folders

    :param xero_tenant_id: Xero identifier for Tenant
    :type xero_tenant_id: str
    :param sort: values to sort by
    :type sort: str

    """
    return web.Response(status=200)


async def get_inbox(request: web.Request, xero_tenant_id) -> web.Response:
    """Retrieves inbox folder

    Search for the user inbox

    :param xero_tenant_id: Xero identifier for Tenant
    :type xero_tenant_id: str

    """
    return web.Response(status=200)


async def update_file(request: web.Request, xero_tenant_id, file_id, body=None) -> web.Response:
    """Update a file

    Updates file properties of a single file

    :param xero_tenant_id: Xero identifier for Tenant
    :type xero_tenant_id: str
    :param file_id: File id for single object
    :type file_id: str
    :type file_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = FileObject.from_dict(body)
    return web.Response(status=200)


async def update_folder(request: web.Request, xero_tenant_id, folder_id, body) -> web.Response:
    """Updates an existing folder

    By passing in the appropriate ID and properties, you can update a folder

    :param xero_tenant_id: Xero identifier for Tenant
    :type xero_tenant_id: str
    :param folder_id: Folder id for single object
    :type folder_id: str
    :type folder_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = Folder.from_dict(body)
    return web.Response(status=200)


async def upload_file(request: web.Request, xero_tenant_id, folder_id=None, body=None, filename=None, mime_type=None, name=None) -> web.Response:
    """Uploads a File

    

    :param xero_tenant_id: Xero identifier for Tenant
    :type xero_tenant_id: str
    :param folder_id: pass an optional folder id to save file to specific folder
    :type folder_id: str
    :type folder_id: str
    :param body: 
    :type body: str
    :param filename: 
    :type filename: str
    :param mime_type: 
    :type mime_type: str
    :param name: exact name of the file you are uploading
    :type name: str

    """
    return web.Response(status=200)
