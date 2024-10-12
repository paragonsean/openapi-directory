/**
 * Fahrplan-Free
 * A RESTful webservice to request a railway journey - FREE plan with restricted access (max. 10 requests per minute). Please ignore the message in the API Console about the access token.  Register to use an less restricted version, which requires an access token.
 *
 * The version of the OpenAPI document: v1
 * Contact: DBOpenData@deutschebahn.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIBoard.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIBoard::OAIBoard(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIBoard::OAIBoard() {
    this->initializeModel();
}

OAIBoard::~OAIBoard() {}

void OAIBoard::initializeModel() {

    m_board_id_isSet = false;
    m_board_id_isValid = false;

    m_date_time_isSet = false;
    m_date_time_isValid = false;

    m_details_id_isSet = false;
    m_details_id_isValid = false;

    m_name_isSet = false;
    m_name_isValid = false;

    m_origin_isSet = false;
    m_origin_isValid = false;

    m_stop_id_isSet = false;
    m_stop_id_isValid = false;

    m_stop_name_isSet = false;
    m_stop_name_isValid = false;

    m_track_isSet = false;
    m_track_isValid = false;

    m_type_isSet = false;
    m_type_isValid = false;
}

void OAIBoard::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIBoard::fromJsonObject(QJsonObject json) {

    m_board_id_isValid = ::OpenAPI::fromJsonValue(m_board_id, json[QString("boardId")]);
    m_board_id_isSet = !json[QString("boardId")].isNull() && m_board_id_isValid;

    m_date_time_isValid = ::OpenAPI::fromJsonValue(m_date_time, json[QString("dateTime")]);
    m_date_time_isSet = !json[QString("dateTime")].isNull() && m_date_time_isValid;

    m_details_id_isValid = ::OpenAPI::fromJsonValue(m_details_id, json[QString("detailsId")]);
    m_details_id_isSet = !json[QString("detailsId")].isNull() && m_details_id_isValid;

    m_name_isValid = ::OpenAPI::fromJsonValue(m_name, json[QString("name")]);
    m_name_isSet = !json[QString("name")].isNull() && m_name_isValid;

    m_origin_isValid = ::OpenAPI::fromJsonValue(m_origin, json[QString("origin")]);
    m_origin_isSet = !json[QString("origin")].isNull() && m_origin_isValid;

    m_stop_id_isValid = ::OpenAPI::fromJsonValue(m_stop_id, json[QString("stopId")]);
    m_stop_id_isSet = !json[QString("stopId")].isNull() && m_stop_id_isValid;

    m_stop_name_isValid = ::OpenAPI::fromJsonValue(m_stop_name, json[QString("stopName")]);
    m_stop_name_isSet = !json[QString("stopName")].isNull() && m_stop_name_isValid;

    m_track_isValid = ::OpenAPI::fromJsonValue(m_track, json[QString("track")]);
    m_track_isSet = !json[QString("track")].isNull() && m_track_isValid;

    m_type_isValid = ::OpenAPI::fromJsonValue(m_type, json[QString("type")]);
    m_type_isSet = !json[QString("type")].isNull() && m_type_isValid;
}

QString OAIBoard::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIBoard::asJsonObject() const {
    QJsonObject obj;
    if (m_board_id_isSet) {
        obj.insert(QString("boardId"), ::OpenAPI::toJsonValue(m_board_id));
    }
    if (m_date_time_isSet) {
        obj.insert(QString("dateTime"), ::OpenAPI::toJsonValue(m_date_time));
    }
    if (m_details_id_isSet) {
        obj.insert(QString("detailsId"), ::OpenAPI::toJsonValue(m_details_id));
    }
    if (m_name_isSet) {
        obj.insert(QString("name"), ::OpenAPI::toJsonValue(m_name));
    }
    if (m_origin_isSet) {
        obj.insert(QString("origin"), ::OpenAPI::toJsonValue(m_origin));
    }
    if (m_stop_id_isSet) {
        obj.insert(QString("stopId"), ::OpenAPI::toJsonValue(m_stop_id));
    }
    if (m_stop_name_isSet) {
        obj.insert(QString("stopName"), ::OpenAPI::toJsonValue(m_stop_name));
    }
    if (m_track_isSet) {
        obj.insert(QString("track"), ::OpenAPI::toJsonValue(m_track));
    }
    if (m_type_isSet) {
        obj.insert(QString("type"), ::OpenAPI::toJsonValue(m_type));
    }
    return obj;
}

QString OAIBoard::getBoardId() const {
    return m_board_id;
}
void OAIBoard::setBoardId(const QString &board_id) {
    m_board_id = board_id;
    m_board_id_isSet = true;
}

bool OAIBoard::is_board_id_Set() const{
    return m_board_id_isSet;
}

bool OAIBoard::is_board_id_Valid() const{
    return m_board_id_isValid;
}

QString OAIBoard::getDateTime() const {
    return m_date_time;
}
void OAIBoard::setDateTime(const QString &date_time) {
    m_date_time = date_time;
    m_date_time_isSet = true;
}

bool OAIBoard::is_date_time_Set() const{
    return m_date_time_isSet;
}

bool OAIBoard::is_date_time_Valid() const{
    return m_date_time_isValid;
}

QString OAIBoard::getDetailsId() const {
    return m_details_id;
}
void OAIBoard::setDetailsId(const QString &details_id) {
    m_details_id = details_id;
    m_details_id_isSet = true;
}

bool OAIBoard::is_details_id_Set() const{
    return m_details_id_isSet;
}

bool OAIBoard::is_details_id_Valid() const{
    return m_details_id_isValid;
}

QString OAIBoard::getName() const {
    return m_name;
}
void OAIBoard::setName(const QString &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAIBoard::is_name_Set() const{
    return m_name_isSet;
}

bool OAIBoard::is_name_Valid() const{
    return m_name_isValid;
}

QString OAIBoard::getOrigin() const {
    return m_origin;
}
void OAIBoard::setOrigin(const QString &origin) {
    m_origin = origin;
    m_origin_isSet = true;
}

bool OAIBoard::is_origin_Set() const{
    return m_origin_isSet;
}

bool OAIBoard::is_origin_Valid() const{
    return m_origin_isValid;
}

QString OAIBoard::getStopId() const {
    return m_stop_id;
}
void OAIBoard::setStopId(const QString &stop_id) {
    m_stop_id = stop_id;
    m_stop_id_isSet = true;
}

bool OAIBoard::is_stop_id_Set() const{
    return m_stop_id_isSet;
}

bool OAIBoard::is_stop_id_Valid() const{
    return m_stop_id_isValid;
}

QString OAIBoard::getStopName() const {
    return m_stop_name;
}
void OAIBoard::setStopName(const QString &stop_name) {
    m_stop_name = stop_name;
    m_stop_name_isSet = true;
}

bool OAIBoard::is_stop_name_Set() const{
    return m_stop_name_isSet;
}

bool OAIBoard::is_stop_name_Valid() const{
    return m_stop_name_isValid;
}

QString OAIBoard::getTrack() const {
    return m_track;
}
void OAIBoard::setTrack(const QString &track) {
    m_track = track;
    m_track_isSet = true;
}

bool OAIBoard::is_track_Set() const{
    return m_track_isSet;
}

bool OAIBoard::is_track_Valid() const{
    return m_track_isValid;
}

QString OAIBoard::getType() const {
    return m_type;
}
void OAIBoard::setType(const QString &type) {
    m_type = type;
    m_type_isSet = true;
}

bool OAIBoard::is_type_Set() const{
    return m_type_isSet;
}

bool OAIBoard::is_type_Valid() const{
    return m_type_isValid;
}

bool OAIBoard::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_board_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_date_time_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_details_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_origin_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_stop_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_stop_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_track_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_type_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIBoard::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_board_id_isValid && m_date_time_isValid && m_details_id_isValid && m_name_isValid && m_origin_isValid && m_stop_id_isValid && m_stop_name_isValid && m_track_isValid && m_type_isValid && true;
}

} // namespace OpenAPI
