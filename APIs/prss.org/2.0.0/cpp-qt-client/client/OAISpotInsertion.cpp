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

#include "OAISpotInsertion.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAISpotInsertion::OAISpotInsertion(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAISpotInsertion::OAISpotInsertion() {
    this->initializeModel();
}

OAISpotInsertion::~OAISpotInsertion() {}

void OAISpotInsertion::initializeModel() {

    m_broadcast_service_id_isSet = false;
    m_broadcast_service_id_isValid = false;

    m_created_date_isSet = false;
    m_created_date_isValid = false;

    m_cue_isSet = false;
    m_cue_isValid = false;

    m_customer_id_isSet = false;
    m_customer_id_isValid = false;

    m_duration_isSet = false;
    m_duration_isValid = false;

    m_end_date_isSet = false;
    m_end_date_isValid = false;

    m_id_isSet = false;
    m_id_isValid = false;

    m_program_id_isSet = false;
    m_program_id_isValid = false;

    m_spots_isSet = false;
    m_spots_isValid = false;

    m_start_date_isSet = false;
    m_start_date_isValid = false;
}

void OAISpotInsertion::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAISpotInsertion::fromJsonObject(QJsonObject json) {

    m_broadcast_service_id_isValid = ::OpenAPI::fromJsonValue(m_broadcast_service_id, json[QString("broadcastServiceId")]);
    m_broadcast_service_id_isSet = !json[QString("broadcastServiceId")].isNull() && m_broadcast_service_id_isValid;

    m_created_date_isValid = ::OpenAPI::fromJsonValue(m_created_date, json[QString("createdDate")]);
    m_created_date_isSet = !json[QString("createdDate")].isNull() && m_created_date_isValid;

    m_cue_isValid = ::OpenAPI::fromJsonValue(m_cue, json[QString("cue")]);
    m_cue_isSet = !json[QString("cue")].isNull() && m_cue_isValid;

    m_customer_id_isValid = ::OpenAPI::fromJsonValue(m_customer_id, json[QString("customerId")]);
    m_customer_id_isSet = !json[QString("customerId")].isNull() && m_customer_id_isValid;

    m_duration_isValid = ::OpenAPI::fromJsonValue(m_duration, json[QString("duration")]);
    m_duration_isSet = !json[QString("duration")].isNull() && m_duration_isValid;

    m_end_date_isValid = ::OpenAPI::fromJsonValue(m_end_date, json[QString("endDate")]);
    m_end_date_isSet = !json[QString("endDate")].isNull() && m_end_date_isValid;

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;

    m_program_id_isValid = ::OpenAPI::fromJsonValue(m_program_id, json[QString("programId")]);
    m_program_id_isSet = !json[QString("programId")].isNull() && m_program_id_isValid;

    m_spots_isValid = ::OpenAPI::fromJsonValue(m_spots, json[QString("spots")]);
    m_spots_isSet = !json[QString("spots")].isNull() && m_spots_isValid;

    m_start_date_isValid = ::OpenAPI::fromJsonValue(m_start_date, json[QString("startDate")]);
    m_start_date_isSet = !json[QString("startDate")].isNull() && m_start_date_isValid;
}

QString OAISpotInsertion::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAISpotInsertion::asJsonObject() const {
    QJsonObject obj;
    if (m_broadcast_service_id_isSet) {
        obj.insert(QString("broadcastServiceId"), ::OpenAPI::toJsonValue(m_broadcast_service_id));
    }
    if (m_created_date_isSet) {
        obj.insert(QString("createdDate"), ::OpenAPI::toJsonValue(m_created_date));
    }
    if (m_cue_isSet) {
        obj.insert(QString("cue"), ::OpenAPI::toJsonValue(m_cue));
    }
    if (m_customer_id_isSet) {
        obj.insert(QString("customerId"), ::OpenAPI::toJsonValue(m_customer_id));
    }
    if (m_duration_isSet) {
        obj.insert(QString("duration"), ::OpenAPI::toJsonValue(m_duration));
    }
    if (m_end_date_isSet) {
        obj.insert(QString("endDate"), ::OpenAPI::toJsonValue(m_end_date));
    }
    if (m_id_isSet) {
        obj.insert(QString("id"), ::OpenAPI::toJsonValue(m_id));
    }
    if (m_program_id_isSet) {
        obj.insert(QString("programId"), ::OpenAPI::toJsonValue(m_program_id));
    }
    if (m_spots.size() > 0) {
        obj.insert(QString("spots"), ::OpenAPI::toJsonValue(m_spots));
    }
    if (m_start_date_isSet) {
        obj.insert(QString("startDate"), ::OpenAPI::toJsonValue(m_start_date));
    }
    return obj;
}

qint64 OAISpotInsertion::getBroadcastServiceId() const {
    return m_broadcast_service_id;
}
void OAISpotInsertion::setBroadcastServiceId(const qint64 &broadcast_service_id) {
    m_broadcast_service_id = broadcast_service_id;
    m_broadcast_service_id_isSet = true;
}

bool OAISpotInsertion::is_broadcast_service_id_Set() const{
    return m_broadcast_service_id_isSet;
}

bool OAISpotInsertion::is_broadcast_service_id_Valid() const{
    return m_broadcast_service_id_isValid;
}

QDateTime OAISpotInsertion::getCreatedDate() const {
    return m_created_date;
}
void OAISpotInsertion::setCreatedDate(const QDateTime &created_date) {
    m_created_date = created_date;
    m_created_date_isSet = true;
}

bool OAISpotInsertion::is_created_date_Set() const{
    return m_created_date_isSet;
}

bool OAISpotInsertion::is_created_date_Valid() const{
    return m_created_date_isValid;
}

QString OAISpotInsertion::getCue() const {
    return m_cue;
}
void OAISpotInsertion::setCue(const QString &cue) {
    m_cue = cue;
    m_cue_isSet = true;
}

bool OAISpotInsertion::is_cue_Set() const{
    return m_cue_isSet;
}

bool OAISpotInsertion::is_cue_Valid() const{
    return m_cue_isValid;
}

qint64 OAISpotInsertion::getCustomerId() const {
    return m_customer_id;
}
void OAISpotInsertion::setCustomerId(const qint64 &customer_id) {
    m_customer_id = customer_id;
    m_customer_id_isSet = true;
}

bool OAISpotInsertion::is_customer_id_Set() const{
    return m_customer_id_isSet;
}

bool OAISpotInsertion::is_customer_id_Valid() const{
    return m_customer_id_isValid;
}

qint32 OAISpotInsertion::getDuration() const {
    return m_duration;
}
void OAISpotInsertion::setDuration(const qint32 &duration) {
    m_duration = duration;
    m_duration_isSet = true;
}

bool OAISpotInsertion::is_duration_Set() const{
    return m_duration_isSet;
}

bool OAISpotInsertion::is_duration_Valid() const{
    return m_duration_isValid;
}

QDate OAISpotInsertion::getEndDate() const {
    return m_end_date;
}
void OAISpotInsertion::setEndDate(const QDate &end_date) {
    m_end_date = end_date;
    m_end_date_isSet = true;
}

bool OAISpotInsertion::is_end_date_Set() const{
    return m_end_date_isSet;
}

bool OAISpotInsertion::is_end_date_Valid() const{
    return m_end_date_isValid;
}

qint64 OAISpotInsertion::getId() const {
    return m_id;
}
void OAISpotInsertion::setId(const qint64 &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAISpotInsertion::is_id_Set() const{
    return m_id_isSet;
}

bool OAISpotInsertion::is_id_Valid() const{
    return m_id_isValid;
}

qint64 OAISpotInsertion::getProgramId() const {
    return m_program_id;
}
void OAISpotInsertion::setProgramId(const qint64 &program_id) {
    m_program_id = program_id;
    m_program_id_isSet = true;
}

bool OAISpotInsertion::is_program_id_Set() const{
    return m_program_id_isSet;
}

bool OAISpotInsertion::is_program_id_Valid() const{
    return m_program_id_isValid;
}

QList<qint64> OAISpotInsertion::getSpots() const {
    return m_spots;
}
void OAISpotInsertion::setSpots(const QList<qint64> &spots) {
    m_spots = spots;
    m_spots_isSet = true;
}

bool OAISpotInsertion::is_spots_Set() const{
    return m_spots_isSet;
}

bool OAISpotInsertion::is_spots_Valid() const{
    return m_spots_isValid;
}

QDate OAISpotInsertion::getStartDate() const {
    return m_start_date;
}
void OAISpotInsertion::setStartDate(const QDate &start_date) {
    m_start_date = start_date;
    m_start_date_isSet = true;
}

bool OAISpotInsertion::is_start_date_Set() const{
    return m_start_date_isSet;
}

bool OAISpotInsertion::is_start_date_Valid() const{
    return m_start_date_isValid;
}

bool OAISpotInsertion::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_broadcast_service_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_created_date_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_cue_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_customer_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_duration_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_end_date_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_program_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_spots.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_start_date_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAISpotInsertion::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_broadcast_service_id_isValid && m_cue_isValid && m_duration_isValid && m_end_date_isValid && m_program_id_isValid && m_spots_isValid && m_start_date_isValid && true;
}

} // namespace OpenAPI
