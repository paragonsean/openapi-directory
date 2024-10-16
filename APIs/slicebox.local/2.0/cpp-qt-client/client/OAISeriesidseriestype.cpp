/**
 * Slicebox API
 * Slicebox - safe sharing of medical images
 *
 * The version of the OpenAPI document: 2.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAISeriesidseriestype.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAISeriesidseriestype::OAISeriesidseriestype(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAISeriesidseriestype::OAISeriesidseriestype() {
    this->initializeModel();
}

OAISeriesidseriestype::~OAISeriesidseriestype() {}

void OAISeriesidseriestype::initializeModel() {

    m_seriesid_isSet = false;
    m_seriesid_isValid = false;

    m_seriestype_isSet = false;
    m_seriestype_isValid = false;
}

void OAISeriesidseriestype::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAISeriesidseriestype::fromJsonObject(QJsonObject json) {

    m_seriesid_isValid = ::OpenAPI::fromJsonValue(m_seriesid, json[QString("seriesid")]);
    m_seriesid_isSet = !json[QString("seriesid")].isNull() && m_seriesid_isValid;

    m_seriestype_isValid = ::OpenAPI::fromJsonValue(m_seriestype, json[QString("seriestype")]);
    m_seriestype_isSet = !json[QString("seriestype")].isNull() && m_seriestype_isValid;
}

QString OAISeriesidseriestype::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAISeriesidseriestype::asJsonObject() const {
    QJsonObject obj;
    if (m_seriesid_isSet) {
        obj.insert(QString("seriesid"), ::OpenAPI::toJsonValue(m_seriesid));
    }
    if (m_seriestype.isSet()) {
        obj.insert(QString("seriestype"), ::OpenAPI::toJsonValue(m_seriestype));
    }
    return obj;
}

qint64 OAISeriesidseriestype::getSeriesid() const {
    return m_seriesid;
}
void OAISeriesidseriestype::setSeriesid(const qint64 &seriesid) {
    m_seriesid = seriesid;
    m_seriesid_isSet = true;
}

bool OAISeriesidseriestype::is_seriesid_Set() const{
    return m_seriesid_isSet;
}

bool OAISeriesidseriestype::is_seriesid_Valid() const{
    return m_seriesid_isValid;
}

OAISeriestype OAISeriesidseriestype::getSeriestype() const {
    return m_seriestype;
}
void OAISeriesidseriestype::setSeriestype(const OAISeriestype &seriestype) {
    m_seriestype = seriestype;
    m_seriestype_isSet = true;
}

bool OAISeriesidseriestype::is_seriestype_Set() const{
    return m_seriestype_isSet;
}

bool OAISeriesidseriestype::is_seriestype_Valid() const{
    return m_seriestype_isValid;
}

bool OAISeriesidseriestype::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_seriesid_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_seriestype.isSet()) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAISeriesidseriestype::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
