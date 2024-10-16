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

#include "OAIBroadcastService.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIBroadcastService::OAIBroadcastService(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIBroadcastService::OAIBroadcastService() {
    this->initializeModel();
}

OAIBroadcastService::~OAIBroadcastService() {}

void OAIBroadcastService::initializeModel() {

    m_created_date_isSet = false;
    m_created_date_isValid = false;

    m_description_isSet = false;
    m_description_isValid = false;

    m_id_isSet = false;
    m_id_isValid = false;

    m_last_modified_date_isSet = false;
    m_last_modified_date_isValid = false;

    m_name_isSet = false;
    m_name_isValid = false;
}

void OAIBroadcastService::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIBroadcastService::fromJsonObject(QJsonObject json) {

    m_created_date_isValid = ::OpenAPI::fromJsonValue(m_created_date, json[QString("createdDate")]);
    m_created_date_isSet = !json[QString("createdDate")].isNull() && m_created_date_isValid;

    m_description_isValid = ::OpenAPI::fromJsonValue(m_description, json[QString("description")]);
    m_description_isSet = !json[QString("description")].isNull() && m_description_isValid;

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;

    m_last_modified_date_isValid = ::OpenAPI::fromJsonValue(m_last_modified_date, json[QString("lastModifiedDate")]);
    m_last_modified_date_isSet = !json[QString("lastModifiedDate")].isNull() && m_last_modified_date_isValid;

    m_name_isValid = ::OpenAPI::fromJsonValue(m_name, json[QString("name")]);
    m_name_isSet = !json[QString("name")].isNull() && m_name_isValid;
}

QString OAIBroadcastService::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIBroadcastService::asJsonObject() const {
    QJsonObject obj;
    if (m_created_date_isSet) {
        obj.insert(QString("createdDate"), ::OpenAPI::toJsonValue(m_created_date));
    }
    if (m_description_isSet) {
        obj.insert(QString("description"), ::OpenAPI::toJsonValue(m_description));
    }
    if (m_id_isSet) {
        obj.insert(QString("id"), ::OpenAPI::toJsonValue(m_id));
    }
    if (m_last_modified_date_isSet) {
        obj.insert(QString("lastModifiedDate"), ::OpenAPI::toJsonValue(m_last_modified_date));
    }
    if (m_name_isSet) {
        obj.insert(QString("name"), ::OpenAPI::toJsonValue(m_name));
    }
    return obj;
}

QDateTime OAIBroadcastService::getCreatedDate() const {
    return m_created_date;
}
void OAIBroadcastService::setCreatedDate(const QDateTime &created_date) {
    m_created_date = created_date;
    m_created_date_isSet = true;
}

bool OAIBroadcastService::is_created_date_Set() const{
    return m_created_date_isSet;
}

bool OAIBroadcastService::is_created_date_Valid() const{
    return m_created_date_isValid;
}

QString OAIBroadcastService::getDescription() const {
    return m_description;
}
void OAIBroadcastService::setDescription(const QString &description) {
    m_description = description;
    m_description_isSet = true;
}

bool OAIBroadcastService::is_description_Set() const{
    return m_description_isSet;
}

bool OAIBroadcastService::is_description_Valid() const{
    return m_description_isValid;
}

qint64 OAIBroadcastService::getId() const {
    return m_id;
}
void OAIBroadcastService::setId(const qint64 &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAIBroadcastService::is_id_Set() const{
    return m_id_isSet;
}

bool OAIBroadcastService::is_id_Valid() const{
    return m_id_isValid;
}

QDateTime OAIBroadcastService::getLastModifiedDate() const {
    return m_last_modified_date;
}
void OAIBroadcastService::setLastModifiedDate(const QDateTime &last_modified_date) {
    m_last_modified_date = last_modified_date;
    m_last_modified_date_isSet = true;
}

bool OAIBroadcastService::is_last_modified_date_Set() const{
    return m_last_modified_date_isSet;
}

bool OAIBroadcastService::is_last_modified_date_Valid() const{
    return m_last_modified_date_isValid;
}

QString OAIBroadcastService::getName() const {
    return m_name;
}
void OAIBroadcastService::setName(const QString &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAIBroadcastService::is_name_Set() const{
    return m_name_isSet;
}

bool OAIBroadcastService::is_name_Valid() const{
    return m_name_isValid;
}

bool OAIBroadcastService::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_created_date_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_description_isSet) {
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

        if (m_name_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIBroadcastService::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_created_date_isValid && m_id_isValid && m_last_modified_date_isValid && m_name_isValid && true;
}

} // namespace OpenAPI
