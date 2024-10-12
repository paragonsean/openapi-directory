/**
 * ContentDepot
 * ContentDepot hosts a range of API’s that allow clients to manage, discover, and obtain content. The API spans many parts of the ContentDepot functionality including MetaPub (a.k.a. metadata distribution) and content management.  ## MetaPub  MetaPub collects, normalizes and distributes publicly available program, episode, and piece metadata through the public radio system. Backed by ContentDepot and its data model, MetaPub allows producers to supply metadata through various methods:  1. MetaPub Agents that collect producer metadata by \"crawling\" existing public feeds (e.g. C24, BBC) or the producer's production system (e.g. ATC, ME, TED Radio Hour). 2. Manually enter metadata in the ContentDepot Portal on each program and episode. 3. Publish/push the metadata to the MetaPub upload API and execute an ingest job.  MetaPub then distributes this data to stations through an electronic program guide (EPG model) for display on various listener devices such as smart phones, tablets, web streams, HD radios, RDBS enabled FM radios, and more. The EPG format is based on the RadioDNS specifications.  ### RadioDNS  The RadioDNS Service and Programme Information Specification ([ETSI TS 102 818 v3.4.1](https://www.etsi.org/deliver/etsi_ts/102800_102899/102818/03.04.01_60/ts_102818v030401p.pdf)) defines three primary documents: Service Information, Program Information, and Group Information. These documents, along with the core RadioDNS Hybrid Lookup for Radio Services Specification ([ETSI TS 103 270 v1.4.1](https://www.etsi.org/deliver/etsi_ts/103200_103299/103270/01.04.01_60/ts_103270v010401p.pdf)), define a system where an end listener device can dynamically discover program metadata and fetch the metadata via Internet Protocol (IP) requests. MetaPub's use of RadioDNS differs slightly in that MetaPub (a.k.a PRSS) acts as the \"service provider\" while the stations and related middleware act as the end devices. While this is not the primary use case of RadioDNS, the flexibility in the specification, service definitions, and DNS resolution allows this model to be easily represented. MetaPub provides both _National Metadata_ and _Station Metadata_.  It is strongly recommended that the related [RadioDNS specifications](https://radiodns.org/developers/documentation/) be read for implementation details, definitions, and required XML schemas.  ## ContentDepot Drive  ContentDepot Drive (CD Drive) provides a private, per customer file storage solution similar to other cloud storage solutions such as Google Drive, Box, and Dropbox. The CD Drive is used to stage content uploads such as metadata files, images, or segment audio before associating the content with specific programs or episodes.  CD Drive content can be referenced using a URI by some operations such as synchronizing metadata. There are two possible CD Drive URI formats supported: ID and hierarchical path. The ID reference takes the form ```cddrive:id:{value}``` where value is the integer ID of the file or folder being referenced. The hierarchical path reference takes the form ```cddrive://{path}``` where path is the full, UNIX style path to the file or folder starting with '/'. For example, two CD Drive URIs pointing to the same file may be ```cddrive:id:12345``` and ```cddrive:///show1/episode2/metadata.xml```. More information about URIs can be found at [Wikipedia](https://en.wikipedia.org/wiki/Uniform_Resource_Identifier).  ## Authentication  The API currently uses OAuth 2.0.  All operations require ```cd:full``` access where the client access is only limited by the permissions of the ContentDepot user after authentication. Limiting access scope per client is not currently supported. 
 *
 * The version of the OpenAPI document: 2.0.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAISpot.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAISpot::OAISpot(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAISpot::OAISpot() {
    this->initializeModel();
}

OAISpot::~OAISpot() {}

void OAISpot::initializeModel() {

    m_created_date_isSet = false;
    m_created_date_isValid = false;

    m_duration_isSet = false;
    m_duration_isValid = false;

    m_file_name_isSet = false;
    m_file_name_isValid = false;

    m_file_size_isSet = false;
    m_file_size_isValid = false;

    m_id_isSet = false;
    m_id_isValid = false;

    m_last_modified_date_isSet = false;
    m_last_modified_date_isValid = false;

    m_last_uploaded_date_isSet = false;
    m_last_uploaded_date_isValid = false;

    m_name_isSet = false;
    m_name_isValid = false;

    m_notes_isSet = false;
    m_notes_isValid = false;

    m_original_file_name_isSet = false;
    m_original_file_name_isValid = false;
}

void OAISpot::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAISpot::fromJsonObject(QJsonObject json) {

    m_created_date_isValid = ::OpenAPI::fromJsonValue(m_created_date, json[QString("createdDate")]);
    m_created_date_isSet = !json[QString("createdDate")].isNull() && m_created_date_isValid;

    m_duration_isValid = ::OpenAPI::fromJsonValue(m_duration, json[QString("duration")]);
    m_duration_isSet = !json[QString("duration")].isNull() && m_duration_isValid;

    m_file_name_isValid = ::OpenAPI::fromJsonValue(m_file_name, json[QString("fileName")]);
    m_file_name_isSet = !json[QString("fileName")].isNull() && m_file_name_isValid;

    m_file_size_isValid = ::OpenAPI::fromJsonValue(m_file_size, json[QString("fileSize")]);
    m_file_size_isSet = !json[QString("fileSize")].isNull() && m_file_size_isValid;

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;

    m_last_modified_date_isValid = ::OpenAPI::fromJsonValue(m_last_modified_date, json[QString("lastModifiedDate")]);
    m_last_modified_date_isSet = !json[QString("lastModifiedDate")].isNull() && m_last_modified_date_isValid;

    m_last_uploaded_date_isValid = ::OpenAPI::fromJsonValue(m_last_uploaded_date, json[QString("lastUploadedDate")]);
    m_last_uploaded_date_isSet = !json[QString("lastUploadedDate")].isNull() && m_last_uploaded_date_isValid;

    m_name_isValid = ::OpenAPI::fromJsonValue(m_name, json[QString("name")]);
    m_name_isSet = !json[QString("name")].isNull() && m_name_isValid;

    m_notes_isValid = ::OpenAPI::fromJsonValue(m_notes, json[QString("notes")]);
    m_notes_isSet = !json[QString("notes")].isNull() && m_notes_isValid;

    m_original_file_name_isValid = ::OpenAPI::fromJsonValue(m_original_file_name, json[QString("originalFileName")]);
    m_original_file_name_isSet = !json[QString("originalFileName")].isNull() && m_original_file_name_isValid;
}

QString OAISpot::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAISpot::asJsonObject() const {
    QJsonObject obj;
    if (m_created_date_isSet) {
        obj.insert(QString("createdDate"), ::OpenAPI::toJsonValue(m_created_date));
    }
    if (m_duration_isSet) {
        obj.insert(QString("duration"), ::OpenAPI::toJsonValue(m_duration));
    }
    if (m_file_name_isSet) {
        obj.insert(QString("fileName"), ::OpenAPI::toJsonValue(m_file_name));
    }
    if (m_file_size_isSet) {
        obj.insert(QString("fileSize"), ::OpenAPI::toJsonValue(m_file_size));
    }
    if (m_id_isSet) {
        obj.insert(QString("id"), ::OpenAPI::toJsonValue(m_id));
    }
    if (m_last_modified_date_isSet) {
        obj.insert(QString("lastModifiedDate"), ::OpenAPI::toJsonValue(m_last_modified_date));
    }
    if (m_last_uploaded_date_isSet) {
        obj.insert(QString("lastUploadedDate"), ::OpenAPI::toJsonValue(m_last_uploaded_date));
    }
    if (m_name_isSet) {
        obj.insert(QString("name"), ::OpenAPI::toJsonValue(m_name));
    }
    if (m_notes_isSet) {
        obj.insert(QString("notes"), ::OpenAPI::toJsonValue(m_notes));
    }
    if (m_original_file_name_isSet) {
        obj.insert(QString("originalFileName"), ::OpenAPI::toJsonValue(m_original_file_name));
    }
    return obj;
}

QDateTime OAISpot::getCreatedDate() const {
    return m_created_date;
}
void OAISpot::setCreatedDate(const QDateTime &created_date) {
    m_created_date = created_date;
    m_created_date_isSet = true;
}

bool OAISpot::is_created_date_Set() const{
    return m_created_date_isSet;
}

bool OAISpot::is_created_date_Valid() const{
    return m_created_date_isValid;
}

qint32 OAISpot::getDuration() const {
    return m_duration;
}
void OAISpot::setDuration(const qint32 &duration) {
    m_duration = duration;
    m_duration_isSet = true;
}

bool OAISpot::is_duration_Set() const{
    return m_duration_isSet;
}

bool OAISpot::is_duration_Valid() const{
    return m_duration_isValid;
}

QString OAISpot::getFileName() const {
    return m_file_name;
}
void OAISpot::setFileName(const QString &file_name) {
    m_file_name = file_name;
    m_file_name_isSet = true;
}

bool OAISpot::is_file_name_Set() const{
    return m_file_name_isSet;
}

bool OAISpot::is_file_name_Valid() const{
    return m_file_name_isValid;
}

qint64 OAISpot::getFileSize() const {
    return m_file_size;
}
void OAISpot::setFileSize(const qint64 &file_size) {
    m_file_size = file_size;
    m_file_size_isSet = true;
}

bool OAISpot::is_file_size_Set() const{
    return m_file_size_isSet;
}

bool OAISpot::is_file_size_Valid() const{
    return m_file_size_isValid;
}

qint64 OAISpot::getId() const {
    return m_id;
}
void OAISpot::setId(const qint64 &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAISpot::is_id_Set() const{
    return m_id_isSet;
}

bool OAISpot::is_id_Valid() const{
    return m_id_isValid;
}

QDateTime OAISpot::getLastModifiedDate() const {
    return m_last_modified_date;
}
void OAISpot::setLastModifiedDate(const QDateTime &last_modified_date) {
    m_last_modified_date = last_modified_date;
    m_last_modified_date_isSet = true;
}

bool OAISpot::is_last_modified_date_Set() const{
    return m_last_modified_date_isSet;
}

bool OAISpot::is_last_modified_date_Valid() const{
    return m_last_modified_date_isValid;
}

QDateTime OAISpot::getLastUploadedDate() const {
    return m_last_uploaded_date;
}
void OAISpot::setLastUploadedDate(const QDateTime &last_uploaded_date) {
    m_last_uploaded_date = last_uploaded_date;
    m_last_uploaded_date_isSet = true;
}

bool OAISpot::is_last_uploaded_date_Set() const{
    return m_last_uploaded_date_isSet;
}

bool OAISpot::is_last_uploaded_date_Valid() const{
    return m_last_uploaded_date_isValid;
}

QString OAISpot::getName() const {
    return m_name;
}
void OAISpot::setName(const QString &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAISpot::is_name_Set() const{
    return m_name_isSet;
}

bool OAISpot::is_name_Valid() const{
    return m_name_isValid;
}

QString OAISpot::getNotes() const {
    return m_notes;
}
void OAISpot::setNotes(const QString &notes) {
    m_notes = notes;
    m_notes_isSet = true;
}

bool OAISpot::is_notes_Set() const{
    return m_notes_isSet;
}

bool OAISpot::is_notes_Valid() const{
    return m_notes_isValid;
}

QString OAISpot::getOriginalFileName() const {
    return m_original_file_name;
}
void OAISpot::setOriginalFileName(const QString &original_file_name) {
    m_original_file_name = original_file_name;
    m_original_file_name_isSet = true;
}

bool OAISpot::is_original_file_name_Set() const{
    return m_original_file_name_isSet;
}

bool OAISpot::is_original_file_name_Valid() const{
    return m_original_file_name_isValid;
}

bool OAISpot::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_created_date_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_duration_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_file_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_file_size_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_last_modified_date_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_last_uploaded_date_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_notes_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_original_file_name_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAISpot::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
