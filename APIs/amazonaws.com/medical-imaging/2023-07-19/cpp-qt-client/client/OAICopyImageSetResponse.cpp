/**
 * AWS Health Imaging
 * <p>This is the <i>AWS HealthImaging API Reference</i>. AWS HealthImaging is an AWS service for storing, accessing, and analyzing medical images. For an introduction to the service, see the <a href=\"https://docs.aws.amazon.com/medical-imaging/latest/devguide\"> <i>AWS HealthImaging Developer Guide</i> </a>.</p> <note> <p>We recommend using one of the AWS Software Development Kits (SDKs) for your programming language, as they take care of request authentication, serialization, and connection management. For more information, see <a href=\"http://aws.amazon.com/developer/tools\">Tools to build on AWS</a>.</p> <p>For information about using AWS HealthImaging API actions in one of the language-specific AWS SDKs, refer to the <i>See Also</i> link at the end of each section that describes an API action or data type.</p> </note> <p>The following sections list AWS HealthImaging API actions categorized according to functionality. Links are provided to actions within this Reference, along with links back to corresponding sections in the <i>AWS HealthImaging Developer Guide</i> so you can view console procedures and CLI/SDK code examples.</p> <p class=\"title\"> <b>Data store actions</b> </p> <ul> <li> <p> <a href=\"https://docs.aws.amazon.com/medical-imaging/latest/APIReference/API_CreateDatastore.html\">CreateDatastore</a> – See <a href=\"https://docs.aws.amazon.com/medical-imaging/latest/devguide/create-data-store.html\">Creating a data store</a>.</p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/medical-imaging/latest/APIReference/API_GetDatastore.html\">GetDatastore</a> – See <a href=\"https://docs.aws.amazon.com/medical-imaging/latest/devguide/get-data-store.html\">Getting data store properties</a>.</p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/medical-imaging/latest/APIReference/API_ListDatastores.html\">ListDatastores</a> – See <a href=\"https://docs.aws.amazon.com/medical-imaging/latest/devguide/list-data-stores.html\">Listing data stores</a>.</p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/medical-imaging/latest/APIReference/API_DeleteDatastore.html\">DeleteDatastore</a> – See <a href=\"https://docs.aws.amazon.com/medical-imaging/latest/devguide/delete-data-store.html\">Deleting a data store</a>.</p> </li> </ul> <p class=\"title\"> <b>Import job actions</b> </p> <ul> <li> <p> <a href=\"https://docs.aws.amazon.com/medical-imaging/latest/APIReference/API_StartDICOMImportJob.html\">StartDICOMImportJob</a> – See <a href=\"https://docs.aws.amazon.com/medical-imaging/latest/devguide/start-dicom-import-job.html\">Starting an import job</a>.</p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/medical-imaging/latest/APIReference/API_GetDICOMImportJob.html\">GetDICOMImportJob</a> – See <a href=\"https://docs.aws.amazon.com/medical-imaging/latest/devguide/get-dicom-import-job.html\">Getting import job properties</a>.</p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/medical-imaging/latest/APIReference/API_ListDICOMImportJobs.html\">ListDICOMImportJobs</a> – See <a href=\"https://docs.aws.amazon.com/medical-imaging/latest/devguide/list-dicom-import-jobs.html\">Listing import jobs</a>.</p> </li> </ul> <p class=\"title\"> <b>Image set access actions</b> </p> <ul> <li> <p> <a href=\"https://docs.aws.amazon.com/medical-imaging/latest/APIReference/API_SearchImageSets.html\">SearchImageSets</a> – See <a href=\"https://docs.aws.amazon.com/medical-imaging/latest/devguide/search-image-sets.html\">Searching image sets</a>.</p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/medical-imaging/latest/APIReference/API_GetImageSet.html\">GetImageSet</a> – See <a href=\"https://docs.aws.amazon.com/medical-imaging/latest/devguide/get-image-set-properties.html\">Getting image set properties</a>.</p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/medical-imaging/latest/APIReference/API_GetImageSetMetadata.html\">GetImageSetMetadata</a> – See <a href=\"https://docs.aws.amazon.com/medical-imaging/latest/devguide/get-image-set-metadata.html\">Getting image set metadata</a>.</p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/medical-imaging/latest/APIReference/API_GetImageFrame.html\">GetImageFrame</a> – See <a href=\"https://docs.aws.amazon.com/medical-imaging/latest/devguide/get-image-frame.html\">Getting image set pixel data</a>.</p> </li> </ul> <p class=\"title\"> <b>Image set modification actions</b> </p> <ul> <li> <p> <a href=\"https://docs.aws.amazon.com/medical-imaging/latest/APIReference/API_ListImageSetVersions.html\">ListImageSetVersions</a> – See <a href=\"https://docs.aws.amazon.com/medical-imaging/latest/devguide/list-image-set-versions.html\">Listing image set versions</a>.</p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/medical-imaging/latest/APIReference/API_UpdateImageSetMetadata.html\">UpdateImageSetMetadata</a> – See <a href=\"https://docs.aws.amazon.com/medical-imaging/latest/devguide/update-image-set-metadata.html\">Updating image set metadata</a>.</p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/medical-imaging/latest/APIReference/API_CopyImageSet.html\">CopyImageSet</a> – See <a href=\"https://docs.aws.amazon.com/medical-imaging/latest/devguide/copy-image-set.html\">Copying an image set</a>.</p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/medical-imaging/latest/APIReference/API_DeleteImageSet.html\">DeleteImageSet</a> – See <a href=\"https://docs.aws.amazon.com/medical-imaging/latest/devguide/delete-image-set.html\">Deleting an image set</a>.</p> </li> </ul> <p class=\"title\"> <b>Tagging actions</b> </p> <ul> <li> <p> <a href=\"https://docs.aws.amazon.com/medical-imaging/latest/APIReference/API_TagResource.html\">TagResource</a> – See <a href=\"https://docs.aws.amazon.com/medical-imaging/latest/devguide/tag-list-untag-data-store.html\">Tagging a data store</a> and <a href=\"https://docs.aws.amazon.com/medical-imaging/latest/devguide/tag-list-untag-image-set.html\">Tagging an image set</a>.</p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/medical-imaging/latest/APIReference/API_ListTagsForResource.html\">ListTagsForResource</a> – See <a href=\"https://docs.aws.amazon.com/medical-imaging/latest/devguide/tag-list-untag-data-store.html\">Tagging a data store</a> and <a href=\"https://docs.aws.amazon.com/medical-imaging/latest/devguide/tag-list-untag-image-set.html\">Tagging an image set</a>.</p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/medical-imaging/latest/APIReference/API_UntagResource.html\">UntagResource</a> – See <a href=\"https://docs.aws.amazon.com/medical-imaging/latest/devguide/tag-list-untag-data-store.html\">Tagging a data store</a> and <a href=\"https://docs.aws.amazon.com/medical-imaging/latest/devguide/tag-list-untag-image-set.html\">Tagging an image set</a>.</p> </li> </ul>
 *
 * The version of the OpenAPI document: 2023-07-19
 * Contact: mike.ralphson@gmail.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAICopyImageSetResponse.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAICopyImageSetResponse::OAICopyImageSetResponse(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAICopyImageSetResponse::OAICopyImageSetResponse() {
    this->initializeModel();
}

OAICopyImageSetResponse::~OAICopyImageSetResponse() {}

void OAICopyImageSetResponse::initializeModel() {

    m_datastore_id_isSet = false;
    m_datastore_id_isValid = false;

    m_source_image_set_properties_isSet = false;
    m_source_image_set_properties_isValid = false;

    m_destination_image_set_properties_isSet = false;
    m_destination_image_set_properties_isValid = false;
}

void OAICopyImageSetResponse::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAICopyImageSetResponse::fromJsonObject(QJsonObject json) {

    m_datastore_id_isValid = ::OpenAPI::fromJsonValue(m_datastore_id, json[QString("datastoreId")]);
    m_datastore_id_isSet = !json[QString("datastoreId")].isNull() && m_datastore_id_isValid;

    m_source_image_set_properties_isValid = ::OpenAPI::fromJsonValue(m_source_image_set_properties, json[QString("sourceImageSetProperties")]);
    m_source_image_set_properties_isSet = !json[QString("sourceImageSetProperties")].isNull() && m_source_image_set_properties_isValid;

    m_destination_image_set_properties_isValid = ::OpenAPI::fromJsonValue(m_destination_image_set_properties, json[QString("destinationImageSetProperties")]);
    m_destination_image_set_properties_isSet = !json[QString("destinationImageSetProperties")].isNull() && m_destination_image_set_properties_isValid;
}

QString OAICopyImageSetResponse::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAICopyImageSetResponse::asJsonObject() const {
    QJsonObject obj;
    if (m_datastore_id_isSet) {
        obj.insert(QString("datastoreId"), ::OpenAPI::toJsonValue(m_datastore_id));
    }
    if (m_source_image_set_properties.isSet()) {
        obj.insert(QString("sourceImageSetProperties"), ::OpenAPI::toJsonValue(m_source_image_set_properties));
    }
    if (m_destination_image_set_properties.isSet()) {
        obj.insert(QString("destinationImageSetProperties"), ::OpenAPI::toJsonValue(m_destination_image_set_properties));
    }
    return obj;
}

QString OAICopyImageSetResponse::getDatastoreId() const {
    return m_datastore_id;
}
void OAICopyImageSetResponse::setDatastoreId(const QString &datastore_id) {
    m_datastore_id = datastore_id;
    m_datastore_id_isSet = true;
}

bool OAICopyImageSetResponse::is_datastore_id_Set() const{
    return m_datastore_id_isSet;
}

bool OAICopyImageSetResponse::is_datastore_id_Valid() const{
    return m_datastore_id_isValid;
}

OAICopyImageSetResponse_sourceImageSetProperties OAICopyImageSetResponse::getSourceImageSetProperties() const {
    return m_source_image_set_properties;
}
void OAICopyImageSetResponse::setSourceImageSetProperties(const OAICopyImageSetResponse_sourceImageSetProperties &source_image_set_properties) {
    m_source_image_set_properties = source_image_set_properties;
    m_source_image_set_properties_isSet = true;
}

bool OAICopyImageSetResponse::is_source_image_set_properties_Set() const{
    return m_source_image_set_properties_isSet;
}

bool OAICopyImageSetResponse::is_source_image_set_properties_Valid() const{
    return m_source_image_set_properties_isValid;
}

OAICopyImageSetResponse_destinationImageSetProperties OAICopyImageSetResponse::getDestinationImageSetProperties() const {
    return m_destination_image_set_properties;
}
void OAICopyImageSetResponse::setDestinationImageSetProperties(const OAICopyImageSetResponse_destinationImageSetProperties &destination_image_set_properties) {
    m_destination_image_set_properties = destination_image_set_properties;
    m_destination_image_set_properties_isSet = true;
}

bool OAICopyImageSetResponse::is_destination_image_set_properties_Set() const{
    return m_destination_image_set_properties_isSet;
}

bool OAICopyImageSetResponse::is_destination_image_set_properties_Valid() const{
    return m_destination_image_set_properties_isValid;
}

bool OAICopyImageSetResponse::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_datastore_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_source_image_set_properties.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_destination_image_set_properties.isSet()) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAICopyImageSetResponse::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_datastore_id_isValid && m_source_image_set_properties_isValid && m_destination_image_set_properties_isValid && true;
}

} // namespace OpenAPI
