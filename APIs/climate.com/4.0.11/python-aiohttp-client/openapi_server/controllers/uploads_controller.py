from typing import List, Dict
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.upload import Upload
from openapi_server.models.upload_status import UploadStatus
from openapi_server.models.upload_status_query import UploadStatusQuery
from openapi_server.models.upload_statuses import UploadStatuses
from openapi_server import util


async def chunked_upload(request: web.Request, content_range, upload_id, content_type) -> web.Response:
    """Chunked upload of data

    Send chunked data for an **Upload**.

    :param content_range: Byte range &#x60;bytes start-end/total&#x60; (https://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.16). e.g. bytes 0-5242880/10242880. Downloads larger than 5MiB (5242880 bytes) in size must be downloaded in chunks no larger than 5MiB (5242880 bytes) and no smaller than 1MiB (1048576 bytes). The last chunk could be less than 1MiB (1048576 bytes).
    :type content_range: str
    :param upload_id: Unique identifier of an Upload.
    :type upload_id: str
    :type upload_id: str
    :param content_type: Must be &#x60;application/octet-stream&#x60;
    :type content_type: str

    """
    return web.Response(status=200)


async def fetch_upload_status_by_id(request: web.Request, upload_id) -> web.Response:
    """Retrieve Upload status

    Check the status of an **Upload** by ID.

    :param upload_id: Unique identifier of an Upload.
    :type upload_id: str
    :type upload_id: str

    """
    return web.Response(status=200)


async def fetch_upload_statuses(request: web.Request, body=None) -> web.Response:
    """Retrieve Upload statuses in batch

    Check the status of multiple **Uploads** (up to 100 per request).

    :param body: 
    :type body: dict | bytes

    """
    body = UploadStatusQuery.from_dict(body)
    return web.Response(status=200)


async def post_upload(request: web.Request, x_recipient_email=None, body=None) -> web.Response:
    """Initiate a new upload

    Step one in uploading a data product. The method will return an **Upload** ID which the caller will use in subsequent &#x60;PUT&#x60; requests. The following &#x60;contentTypes&#x60; may be uploaded:     &lt;details&gt;&lt;summary&gt;__image/vnd.climate.thermal.geotiff__&lt;/summary&gt;      Allows for the upload of a thermal image. The image is a single band geotiff with 64 bit signed floating point values in degrees Celsius. The Coordinate Reference System (CRS) must be UTM with WGS84 datum.      The following metadata entries are required to be embedded in the geotiff:       * acquisitionStartDate - ISO8601 date       * acquisitionEndDate - ISO8601 date       * isCalibrated - boolean      The following metadata entries are optional:       * sourceId - uuid referencing the asset in the partner&#39;s system       * fieldId - uuid referencing a field in the Climate system       * boundaryId - uuid referencing a boundary in the Climate system       * brandId - uuid referencing a partner&#39;s branding in the Climate system       * name - name of the layer. The maximum number of characters that will be accepted as input is 20.      Requires either imagery:write or platform scope.   &lt;/details&gt;   &lt;details&gt;&lt;summary&gt;__image/vnd.climate.ndvi.geotiff__&lt;/summary&gt;      Allows for the upload of a NDVI image. The image is a single band geotiff with 64 bit signed floating point values in the range of -1 to 1 inclusive. The Coordinate Reference System (CRS) must be UTM with WGS84 datum.      The following metadata entries are required to be embedded in the geotiff:       * acquisitionStartDate - ISO8601 date       * acquisitionEndDate - ISO8601 date      The following metadata entries are optional:       * sourceId - uuid referencing the asset in the partner&#39;s system       * fieldId - uuid referencing a field in the Climate system       * boundaryId - uuid referencing a boundary in the Climate system       * brandId - uuid referencing a partner&#39;s branding in the Climate system       * name - name of the layer. The maximum number of characters that will be accepted as input is 20.      Requires either imagery:write or platform scope.   &lt;/details&gt;   &lt;details&gt;&lt;summary&gt; __image/vnd.climate.rgb.geotiff__&lt;/summary&gt;      Allows for the upload of a true color image. The image is a multi band geotiff with 24-bit composite values. Each band is 8 bits with values in the range of 0 to 255. The Coordinate Reference System (CRS) must be UTM with WGS84 datum. The geotiff must contain 3 bands in the order Red, Green, Blue.      The following metadata entries are required to be embedded in the geotiff:       * acquisitionStartDate - ISO8601 date       * acquisitionEndDate - ISO8601 date       * isCalibrated - boolean      The following metadata entries are optional:       * sourceId - uuid referencing the asset in the partner&#39;s system       * fieldId - uuid referencing a field in the Climate system       * boundaryId - uuid referencing a boundary in the Climate system       * brandId - uuid referencing a partner&#39;s branding in the Climate system       * reflectanceComputeMethod - either TOA or GROUND       * name - name of the layer. The maximum number of characters that will be accepted as input is 20.      Requires either imagery:write or platform scope.   &lt;/details&gt;   &lt;details&gt;&lt;summary&gt; __image/vnd.climate.rgb-nir.geotiff__&lt;/summary&gt;      Allows for the upload of a Near Infrared (NIR) image. The Coordinate Reference System (CRS) must be UTM with WGS84 datum.      The following metadata entries are required to be embedded in the geotiff:       * acquisitionStartDate - ISO8601 date       * acquisitionEndDate - ISO8601 date       * isCalibrated - boolean      The following metadata entries are optional:       * sourceId - uuid referencing the asset in the partner&#39;s system       * fieldId - uuid referencing a field in the Climate system       * boundaryId - uuid referencing a boundary in the Climate system       * brandId - uuid referencing a partner&#39;s branding in the Climate system       * reflectanceComputeMethod - either TOA or GROUND       * name - name of the layer. The maximum number of characters that will be accepted as input is 20.      Requires either imagery:write or platform scope.   &lt;/details&gt;   &lt;details&gt;&lt;summary&gt;__image/vnd.climate.rgb-cir.geotiff__&lt;/summary&gt;      Allows for the upload of a Color Infrared (CIR) image. The Coordinate Reference System (CRS) must be UTM with WGS84 datum.      The following metadata entries are required to be embedded in the geotiff:       * acquisitionStartDate - ISO8601 date       * acquisitionEndDate - ISO8601 date       * isCalibrated - boolean      The following metadata entries are optional:       * sourceId - uuid referencing the asset in the partner&#39;s system       * fieldId - uuid referencing a field in the Climate system       * boundaryId - uuid referencing a boundary in the Climate system       * brandId - uuid referencing a partner&#39;s branding in the Climate system       * reflectanceComputeMethod - either TOA or GROUND       * name - name of the layer. The maximum number of characters that will be accepted as input is 20.      Requires either imagery:write or platform scope.   &lt;/details&gt;   &lt;details&gt;&lt;summary&gt; __application/vnd.climate.rx.planting.shp__&lt;/summary&gt;      Allows for the upload of a planting prescription in shapefile format.  The upload must be an archive in the zip format.  It should contain one and only one of each of the following file types:       * .shp       * .shx       * .dbf      All files with the above suffixes must have the same prefix, ie Back40.shp, Back40.shx and Back40.dbf.      Requires either rx:write or platform scope.   &lt;/details&gt;   &lt;details&gt;&lt;summary&gt; __application/vnd.climate.prescription.zones.shp__&lt;/summary&gt;      Allows for the upload of a zones prescription in shapefile format.  The upload must be an archive in the zip format.  It should contain one and only one of each of the following file types:       * .shp       * .shx       * .dbf      All files with the above suffixes must have the same prefix, ie Back40.shp, Back40.shx and Back40.dbf.      The following metadata entries are required:       * fieldId - field identifier for prescription zones.          Requires either rxZones:write or platform scope.   &lt;/details&gt;   &lt;details&gt;&lt;summary&gt; __application/vnd.climate.modus.xml__&lt;/summary&gt;      Allows for the upload of a soil sampling file in the modus 1.0 format with some restrictions.  The upload must be a single xml file.      The following elements are required to be present in the modus file.       * EventCode - Max length of 64 bytes       * EventDate - Must be in ISO8601       * SoilSample - Has a maxOccurs of 20k       * Depth - Has a maxOccurs of 50       * LabName - Must be non-empty.       * StartingDepth - 0 to 36 inclusive, default 0       * EndingDepth - 1 - 36 inclusive, default 1       * ColumnDepth       * DepthUnit - must be inches       * Geometry - point in wgs84          Requires the soil:write scope.    &lt;/details&gt;    &lt;details&gt;&lt;summary&gt; __application/vnd.climate.stand-count.geojson__&lt;/summary&gt;      Allows for the upload of a valid [geojson feature collection](https://tools.ietf.org/html/rfc7946#section-3.3).      Each feature in the collection must contain the following entry in its properties section:       * StandPPA - A count of the number of plants per acre:      Additionally, the type field of each feature&#39;s geometry field must be:       * Point      Requires &#x60;imagery:write&#x60; scope.    &lt;/details&gt;    &lt;details&gt;&lt;summary&gt; __application/vnd.climate.weed-count.geojson__&lt;/summary&gt;      Allows for the upload of a valid [geojson feature collection](https://tools.ietf.org/html/rfc7946#section-3.3).      Each feature in the collection must contain the following entry in its properties section:       * StandPPA - A count of the number of plants per acre:      Additionally, the type field of each feature&#39;s geometry field must be:       * Point      Requires &#x60;imagery:write&#x60; scope.    &lt;/details&gt;    &lt;details&gt;&lt;summary&gt; __application/vnd.climate.as-applied.zip__&lt;/summary&gt;      Allows for the upload of a valid application data [supported formats](https://support.climate.com/kt#/kA02A000000DjvOSAS/en_US).      The following metadata entries are required:       * fileName - name of the file being uploaded.      The following metadata entries are optional:       * resourceOwner - the grower&#39;s account email, where dealer/partner wants to upload data. As a prerequisite the grower must share their operation with the dealer/partner.      Requires &#x60;asApplied:write&#x60; scope.    &lt;/details&gt;    &lt;details&gt;&lt;summary&gt; __application/vnd.climate.as-planted.zip__&lt;/summary&gt;      Allows for the upload of a valid planting data [supported formats](https://support.climate.com/kt#/kA02A000000DjvOSAS/en_US).      The following metadata entries are required:       * fileName - name of the file being uploaded.      The following metadata entries are optional:       * resourceOwner - the grower&#39;s account email, where dealer/partner wants to upload data. As a prerequisite the grower must share their operation with the dealer/partner.      Requires &#x60;asPlanted:write&#x60; scope.    &lt;/details&gt;    &lt;details&gt;&lt;summary&gt; __application/vnd.climate.as-harvested.zip__&lt;/summary&gt;      Allows for the upload of a valid harvest data [supported formats](https://support.climate.com/kt#/kA02A000000DjvOSAS/en_US).      The following metadata entries are required:       * fileName - name of the file being uploaded.      The following metadata entries are optional:       * resourceOwner - the grower&#39;s account email, where dealer/partner wants to upload data. As a prerequisite the grower must share their operation with the dealer/partner.      Requires &#x60;asHarvested:write&#x60; scope.    &lt;/details&gt;

    :param x_recipient_email: Email address associated with a Climate account, used when to sending to another user.
    :type x_recipient_email: str
    :param body: 
    :type body: dict | bytes

    """
    body = Upload.from_dict(body)
    return web.Response(status=200)
