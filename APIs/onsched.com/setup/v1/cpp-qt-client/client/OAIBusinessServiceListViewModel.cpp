/**
 * OnSched Setup API
 * Build secure and scalable custom apps for onboarding and setup. Our flexible API provides many options for configuration.  <br><br>  Take the API for a test drive. Just click on the Authorize button below and authenticate.   You can access our demo company profile if you are not a customer, or your own profile by using your assigned ClientId and Secret.  <br><br>  The API has two interfaces, consumer and setup.   <ul>  <li>  The consumer interface provides all the endpoints required for implementing consumer booking flows.  </li>  <li>  The setup interface provides endpoints for profile configuration and setup.  </li>  </ul>  Toggle freely between the two interfaces using the swagger tool bar option labelled 'Select a definition'.  
 *
 * The version of the OpenAPI document: v1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIBusinessServiceListViewModel.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIBusinessServiceListViewModel::OAIBusinessServiceListViewModel(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIBusinessServiceListViewModel::OAIBusinessServiceListViewModel() {
    this->initializeModel();
}

OAIBusinessServiceListViewModel::~OAIBusinessServiceListViewModel() {}

void OAIBusinessServiceListViewModel::initializeModel() {

    m_count_isSet = false;
    m_count_isValid = false;

    m_data_isSet = false;
    m_data_isValid = false;

    m_has_more_isSet = false;
    m_has_more_isValid = false;

    m_object_isSet = false;
    m_object_isValid = false;

    m_total_isSet = false;
    m_total_isValid = false;

    m_url_isSet = false;
    m_url_isValid = false;
}

void OAIBusinessServiceListViewModel::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIBusinessServiceListViewModel::fromJsonObject(QJsonObject json) {

    m_count_isValid = ::OpenAPI::fromJsonValue(m_count, json[QString("count")]);
    m_count_isSet = !json[QString("count")].isNull() && m_count_isValid;

    m_data_isValid = ::OpenAPI::fromJsonValue(m_data, json[QString("data")]);
    m_data_isSet = !json[QString("data")].isNull() && m_data_isValid;

    m_has_more_isValid = ::OpenAPI::fromJsonValue(m_has_more, json[QString("hasMore")]);
    m_has_more_isSet = !json[QString("hasMore")].isNull() && m_has_more_isValid;

    m_object_isValid = ::OpenAPI::fromJsonValue(m_object, json[QString("object")]);
    m_object_isSet = !json[QString("object")].isNull() && m_object_isValid;

    m_total_isValid = ::OpenAPI::fromJsonValue(m_total, json[QString("total")]);
    m_total_isSet = !json[QString("total")].isNull() && m_total_isValid;

    m_url_isValid = ::OpenAPI::fromJsonValue(m_url, json[QString("url")]);
    m_url_isSet = !json[QString("url")].isNull() && m_url_isValid;
}

QString OAIBusinessServiceListViewModel::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIBusinessServiceListViewModel::asJsonObject() const {
    QJsonObject obj;
    if (m_count_isSet) {
        obj.insert(QString("count"), ::OpenAPI::toJsonValue(m_count));
    }
    if (m_data.size() > 0) {
        obj.insert(QString("data"), ::OpenAPI::toJsonValue(m_data));
    }
    if (m_has_more_isSet) {
        obj.insert(QString("hasMore"), ::OpenAPI::toJsonValue(m_has_more));
    }
    if (m_object_isSet) {
        obj.insert(QString("object"), ::OpenAPI::toJsonValue(m_object));
    }
    if (m_total_isSet) {
        obj.insert(QString("total"), ::OpenAPI::toJsonValue(m_total));
    }
    if (m_url_isSet) {
        obj.insert(QString("url"), ::OpenAPI::toJsonValue(m_url));
    }
    return obj;
}

qint32 OAIBusinessServiceListViewModel::getCount() const {
    return m_count;
}
void OAIBusinessServiceListViewModel::setCount(const qint32 &count) {
    m_count = count;
    m_count_isSet = true;
}

bool OAIBusinessServiceListViewModel::is_count_Set() const{
    return m_count_isSet;
}

bool OAIBusinessServiceListViewModel::is_count_Valid() const{
    return m_count_isValid;
}

QList<OAIBusinessServiceViewModel> OAIBusinessServiceListViewModel::getData() const {
    return m_data;
}
void OAIBusinessServiceListViewModel::setData(const QList<OAIBusinessServiceViewModel> &data) {
    m_data = data;
    m_data_isSet = true;
}

bool OAIBusinessServiceListViewModel::is_data_Set() const{
    return m_data_isSet;
}

bool OAIBusinessServiceListViewModel::is_data_Valid() const{
    return m_data_isValid;
}

bool OAIBusinessServiceListViewModel::isHasMore() const {
    return m_has_more;
}
void OAIBusinessServiceListViewModel::setHasMore(const bool &has_more) {
    m_has_more = has_more;
    m_has_more_isSet = true;
}

bool OAIBusinessServiceListViewModel::is_has_more_Set() const{
    return m_has_more_isSet;
}

bool OAIBusinessServiceListViewModel::is_has_more_Valid() const{
    return m_has_more_isValid;
}

QString OAIBusinessServiceListViewModel::getObject() const {
    return m_object;
}
void OAIBusinessServiceListViewModel::setObject(const QString &object) {
    m_object = object;
    m_object_isSet = true;
}

bool OAIBusinessServiceListViewModel::is_object_Set() const{
    return m_object_isSet;
}

bool OAIBusinessServiceListViewModel::is_object_Valid() const{
    return m_object_isValid;
}

qint32 OAIBusinessServiceListViewModel::getTotal() const {
    return m_total;
}
void OAIBusinessServiceListViewModel::setTotal(const qint32 &total) {
    m_total = total;
    m_total_isSet = true;
}

bool OAIBusinessServiceListViewModel::is_total_Set() const{
    return m_total_isSet;
}

bool OAIBusinessServiceListViewModel::is_total_Valid() const{
    return m_total_isValid;
}

QString OAIBusinessServiceListViewModel::getUrl() const {
    return m_url;
}
void OAIBusinessServiceListViewModel::setUrl(const QString &url) {
    m_url = url;
    m_url_isSet = true;
}

bool OAIBusinessServiceListViewModel::is_url_Set() const{
    return m_url_isSet;
}

bool OAIBusinessServiceListViewModel::is_url_Valid() const{
    return m_url_isValid;
}

bool OAIBusinessServiceListViewModel::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_count_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_data.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_has_more_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_object_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_total_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_url_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIBusinessServiceListViewModel::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
