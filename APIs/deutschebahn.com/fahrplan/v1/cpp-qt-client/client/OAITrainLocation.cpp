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

#include "OAITrainLocation.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAITrainLocation::OAITrainLocation(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAITrainLocation::OAITrainLocation() {
    this->initializeModel();
}

OAITrainLocation::~OAITrainLocation() {}

void OAITrainLocation::initializeModel() {

    m_arr_time_isSet = false;
    m_arr_time_isValid = false;

    m_dep_time_isSet = false;
    m_dep_time_isValid = false;

    m_lat_isSet = false;
    m_lat_isValid = false;

    m_lon_isSet = false;
    m_lon_isValid = false;

    m_r_operator_isSet = false;
    m_r_operator_isValid = false;

    m_stop_id_isSet = false;
    m_stop_id_isValid = false;

    m_stop_name_isSet = false;
    m_stop_name_isValid = false;

    m_train_isSet = false;
    m_train_isValid = false;

    m_type_isSet = false;
    m_type_isValid = false;
}

void OAITrainLocation::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAITrainLocation::fromJsonObject(QJsonObject json) {

    m_arr_time_isValid = ::OpenAPI::fromJsonValue(m_arr_time, json[QString("arrTime")]);
    m_arr_time_isSet = !json[QString("arrTime")].isNull() && m_arr_time_isValid;

    m_dep_time_isValid = ::OpenAPI::fromJsonValue(m_dep_time, json[QString("depTime")]);
    m_dep_time_isSet = !json[QString("depTime")].isNull() && m_dep_time_isValid;

    m_lat_isValid = ::OpenAPI::fromJsonValue(m_lat, json[QString("lat")]);
    m_lat_isSet = !json[QString("lat")].isNull() && m_lat_isValid;

    m_lon_isValid = ::OpenAPI::fromJsonValue(m_lon, json[QString("lon")]);
    m_lon_isSet = !json[QString("lon")].isNull() && m_lon_isValid;

    m_r_operator_isValid = ::OpenAPI::fromJsonValue(m_r_operator, json[QString("operator")]);
    m_r_operator_isSet = !json[QString("operator")].isNull() && m_r_operator_isValid;

    m_stop_id_isValid = ::OpenAPI::fromJsonValue(m_stop_id, json[QString("stopId")]);
    m_stop_id_isSet = !json[QString("stopId")].isNull() && m_stop_id_isValid;

    m_stop_name_isValid = ::OpenAPI::fromJsonValue(m_stop_name, json[QString("stopName")]);
    m_stop_name_isSet = !json[QString("stopName")].isNull() && m_stop_name_isValid;

    m_train_isValid = ::OpenAPI::fromJsonValue(m_train, json[QString("train")]);
    m_train_isSet = !json[QString("train")].isNull() && m_train_isValid;

    m_type_isValid = ::OpenAPI::fromJsonValue(m_type, json[QString("type")]);
    m_type_isSet = !json[QString("type")].isNull() && m_type_isValid;
}

QString OAITrainLocation::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAITrainLocation::asJsonObject() const {
    QJsonObject obj;
    if (m_arr_time_isSet) {
        obj.insert(QString("arrTime"), ::OpenAPI::toJsonValue(m_arr_time));
    }
    if (m_dep_time_isSet) {
        obj.insert(QString("depTime"), ::OpenAPI::toJsonValue(m_dep_time));
    }
    if (m_lat_isSet) {
        obj.insert(QString("lat"), ::OpenAPI::toJsonValue(m_lat));
    }
    if (m_lon_isSet) {
        obj.insert(QString("lon"), ::OpenAPI::toJsonValue(m_lon));
    }
    if (m_r_operator_isSet) {
        obj.insert(QString("operator"), ::OpenAPI::toJsonValue(m_r_operator));
    }
    if (m_stop_id_isSet) {
        obj.insert(QString("stopId"), ::OpenAPI::toJsonValue(m_stop_id));
    }
    if (m_stop_name_isSet) {
        obj.insert(QString("stopName"), ::OpenAPI::toJsonValue(m_stop_name));
    }
    if (m_train_isSet) {
        obj.insert(QString("train"), ::OpenAPI::toJsonValue(m_train));
    }
    if (m_type_isSet) {
        obj.insert(QString("type"), ::OpenAPI::toJsonValue(m_type));
    }
    return obj;
}

QString OAITrainLocation::getArrTime() const {
    return m_arr_time;
}
void OAITrainLocation::setArrTime(const QString &arr_time) {
    m_arr_time = arr_time;
    m_arr_time_isSet = true;
}

bool OAITrainLocation::is_arr_time_Set() const{
    return m_arr_time_isSet;
}

bool OAITrainLocation::is_arr_time_Valid() const{
    return m_arr_time_isValid;
}

QString OAITrainLocation::getDepTime() const {
    return m_dep_time;
}
void OAITrainLocation::setDepTime(const QString &dep_time) {
    m_dep_time = dep_time;
    m_dep_time_isSet = true;
}

bool OAITrainLocation::is_dep_time_Set() const{
    return m_dep_time_isSet;
}

bool OAITrainLocation::is_dep_time_Valid() const{
    return m_dep_time_isValid;
}

double OAITrainLocation::getLat() const {
    return m_lat;
}
void OAITrainLocation::setLat(const double &lat) {
    m_lat = lat;
    m_lat_isSet = true;
}

bool OAITrainLocation::is_lat_Set() const{
    return m_lat_isSet;
}

bool OAITrainLocation::is_lat_Valid() const{
    return m_lat_isValid;
}

double OAITrainLocation::getLon() const {
    return m_lon;
}
void OAITrainLocation::setLon(const double &lon) {
    m_lon = lon;
    m_lon_isSet = true;
}

bool OAITrainLocation::is_lon_Set() const{
    return m_lon_isSet;
}

bool OAITrainLocation::is_lon_Valid() const{
    return m_lon_isValid;
}

QString OAITrainLocation::getROperator() const {
    return m_r_operator;
}
void OAITrainLocation::setROperator(const QString &r_operator) {
    m_r_operator = r_operator;
    m_r_operator_isSet = true;
}

bool OAITrainLocation::is_r_operator_Set() const{
    return m_r_operator_isSet;
}

bool OAITrainLocation::is_r_operator_Valid() const{
    return m_r_operator_isValid;
}

QString OAITrainLocation::getStopId() const {
    return m_stop_id;
}
void OAITrainLocation::setStopId(const QString &stop_id) {
    m_stop_id = stop_id;
    m_stop_id_isSet = true;
}

bool OAITrainLocation::is_stop_id_Set() const{
    return m_stop_id_isSet;
}

bool OAITrainLocation::is_stop_id_Valid() const{
    return m_stop_id_isValid;
}

QString OAITrainLocation::getStopName() const {
    return m_stop_name;
}
void OAITrainLocation::setStopName(const QString &stop_name) {
    m_stop_name = stop_name;
    m_stop_name_isSet = true;
}

bool OAITrainLocation::is_stop_name_Set() const{
    return m_stop_name_isSet;
}

bool OAITrainLocation::is_stop_name_Valid() const{
    return m_stop_name_isValid;
}

QString OAITrainLocation::getTrain() const {
    return m_train;
}
void OAITrainLocation::setTrain(const QString &train) {
    m_train = train;
    m_train_isSet = true;
}

bool OAITrainLocation::is_train_Set() const{
    return m_train_isSet;
}

bool OAITrainLocation::is_train_Valid() const{
    return m_train_isValid;
}

QString OAITrainLocation::getType() const {
    return m_type;
}
void OAITrainLocation::setType(const QString &type) {
    m_type = type;
    m_type_isSet = true;
}

bool OAITrainLocation::is_type_Set() const{
    return m_type_isSet;
}

bool OAITrainLocation::is_type_Valid() const{
    return m_type_isValid;
}

bool OAITrainLocation::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_arr_time_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_dep_time_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_lat_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_lon_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_r_operator_isSet) {
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

        if (m_train_isSet) {
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

bool OAITrainLocation::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_arr_time_isValid && m_dep_time_isValid && m_lat_isValid && m_lon_isValid && m_r_operator_isValid && m_stop_id_isValid && m_stop_name_isValid && m_train_isValid && m_type_isValid && true;
}

} // namespace OpenAPI
