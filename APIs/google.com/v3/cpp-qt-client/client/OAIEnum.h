/**
 * Travel Partner API
 * The Travel Partner API provides you with a RESTful interface to the Google Hotel Center platform. It enables an app to efficiently retrieve and change Hotel Center data, and is thus suitable for managing large or complex accounts.
 *
 * The version of the OpenAPI document: v3
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#ifndef OAI_ENUM_H
#define OAI_ENUM_H

#include <QJsonValue>
#include <QMetaType>
#include <QString>

namespace OpenAPI {

class OAIEnum {
public:
    OAIEnum() {}

    OAIEnum(QString jsonString) {
        fromJson(jsonString);
    }

    virtual ~OAIEnum() {}

    virtual QJsonValue asJsonValue() const {
        return QJsonValue(jstr);
    }

    virtual QString asJson() const {
        return jstr;
    }

    virtual void fromJson(QString jsonString) {
        jstr = jsonString;
    }

    virtual void fromJsonValue(QJsonValue jval) {
        jstr = jval.toString();
    }

    virtual bool isSet() const {
        return false;
    }

    virtual bool isValid() const {
        return true;
    }

private:
    QString jstr;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIEnum)

#endif // OAI_ENUM_H
